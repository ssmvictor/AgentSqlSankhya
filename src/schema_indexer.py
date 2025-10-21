# schema_indexer.py
"""
Sistema de Indexação e Busca para o Dicionário de Dados Sankhya
Otimizado para reduzir tokens e melhorar performance
"""

import re
import json
import pickle
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path
import hashlib

from src.constants import (
    CACHE_HASH_FILE,
    CACHE_INDEX_FILE,
    MAPEAMENTO_CONTEXTO,
    STOPWORDS_PT,
    TIPOS_DADOS,
)
from config.settings import get_cache_dir, get_schema_path

@dataclass
class Campo:
    """Representa um campo de uma tabela"""
    nome: str
    descricao: str
    tipo: str
    observacoes: str = ""
    opcoes: List[Dict[str, str]] = None
    
    def __post_init__(self):
        if self.opcoes is None:
            self.opcoes = []

@dataclass
class Tabela:
    """Representa uma tabela do banco"""
    nome: str
    descricao: str
    campos: List[Campo]
    
    def to_compact_dict(self) -> dict:
        """Retorna versão compacta para economizar tokens"""
        return {
            "nome": self.nome,
            "desc": self.descricao,
            "campos": [
                {
                    "n": c.nome,
                    "d": c.descricao,
                    "t": c.tipo,
                    "o": c.opcoes if c.opcoes else None
                }
                for c in self.campos
            ]
        }

class SchemaIndexer:
    """Indexador e buscador do schema Sankhya"""
    
    def __init__(self, schema_path: str = None, cache_dir: str = None):
        self.schema_path = Path(schema_path) if schema_path else get_schema_path()
        self.cache_dir = Path(cache_dir) if cache_dir else get_cache_dir()
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        self.tabelas: Dict[str, Tabela] = {}
        self.indice_campos: Dict[str, List[Tuple[str, str]]] = {}  # campo -> [(tabela, descricao)]
        self.indice_descricoes: Dict[str, Set[str]] = {}  # palavra -> tabelas
        self.tipos_dados = TIPOS_DADOS
        
        # Carregar ou criar índice
        if not self._load_cache():
            self.parse_schema()
            self._save_cache()
    
    def _get_cache_hash(self) -> str:
        """Gera hash do arquivo para verificar mudanças"""
        with open(self.schema_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    
    def _load_cache(self) -> bool:
        """Carrega índice do cache se existir e estiver atualizado"""
        cache_file = self.cache_dir / CACHE_INDEX_FILE
        hash_file = self.cache_dir / CACHE_HASH_FILE
        
        if cache_file.exists() and hash_file.exists():
            try:
                current_hash = self._get_cache_hash()
                with open(hash_file, 'r') as f:
                    cached_hash = f.read().strip()
                
                if current_hash == cached_hash:
                    with open(cache_file, 'rb') as f:
                        cache_data = pickle.load(f)
                        self.tabelas = cache_data['tabelas']
                        self.indice_campos = cache_data['indice_campos']
                        self.indice_descricoes = cache_data['indice_descricoes']
                        print("✓ Cache carregado com sucesso!")
                        return True
            except (pickle.UnpicklingError, AttributeError, KeyError, EOFError) as e:
                print(f"⚠️ Cache incompatível ou corrompido: {type(e).__name__}")
                print("🔄 Recriando índices...")
                # Limpar cache corrompido
                try:
                    cache_file.unlink()
                    hash_file.unlink()
                except:
                    pass
                return False
        
        return False
    
    def _save_cache(self):
        """Salva índice em cache"""
        cache_file = self.cache_dir / CACHE_INDEX_FILE
        hash_file = self.cache_dir / CACHE_HASH_FILE
        
        cache_data = {
            'tabelas': self.tabelas,
            'indice_campos': self.indice_campos,
            'indice_descricoes': self.indice_descricoes
        }
        
        with open(cache_file, 'wb') as f:
            pickle.dump(cache_data, f)
        
        with open(hash_file, 'w') as f:
            f.write(self._get_cache_hash())
        
        print("✓ Cache salvo com sucesso!")
    
    def parse_schema(self):
        """Parse do arquivo markdown para estruturas indexadas"""
        print("Indexando schema...")
        
        with open(self.schema_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Dividir por tabelas
        tabelas_raw = re.split(r'^## Tabela:', content, flags=re.MULTILINE)[1:]
        
        for tabela_raw in tabelas_raw:
            self._parse_tabela(tabela_raw)
        
        # Criar índices
        self._criar_indices()
        
        print(f"✓ {len(self.tabelas)} tabelas indexadas")
        print(f"✓ {len(self.indice_campos)} campos únicos encontrados")
    
    def _parse_tabela(self, tabela_raw: str):
        """Parse de uma tabela individual"""
        lines = tabela_raw.strip().split('\n')
        
        # Nome da tabela
        nome_tabela = lines[0].strip()
        
        # Descrição
        descricao = ""
        for i, line in enumerate(lines[1:], 1):
            if line.startswith('### Descrição:'):
                descricao = line.replace('### Descrição:', '').strip()
                break
        
        # Campos
        campos = []
        in_table = False
        opcoes_campos = {}
        
        for line in lines:
            if '| Campo | Descrição | Tipo |' in line:
                in_table = True
                continue
            
            if in_table and line.startswith('|') and not '|----' in line:
                parts = [p.strip() for p in line.split('|')[1:-1]]
                if len(parts) >= 3:
                    campo_nome = parts[0].replace('`', '')
                    campo_desc = parts[1]
                    campo_tipo = parts[2]
                    campo_obs = parts[3] if len(parts) > 3 else ""
                    
                    # Verificar se tem opções
                    if 'Veja opções' in campo_obs:
                        opcoes_campos[campo_nome] = []
                    
                    campos.append(Campo(
                        nome=campo_nome,
                        descricao=campo_desc,
                        tipo=campo_tipo,
                        observacoes=campo_obs
                    ))
        
        # Parse das opções de campos
        self._parse_opcoes(tabela_raw, nome_tabela, opcoes_campos)
        
        # Adicionar opções aos campos
        for campo in campos:
            if campo.nome in opcoes_campos:
                campo.opcoes = opcoes_campos[campo.nome]
        
        if campos:
            self.tabelas[nome_tabela] = Tabela(
                nome=nome_tabela,
                descricao=descricao,
                campos=campos
            )
    
    def _parse_opcoes(self, tabela_raw: str, nome_tabela: str, opcoes_campos: dict):
        """Parse das opções de campos"""
        # Buscar seção de opções
        if '## OPÇÕES DE CAMPOS' in tabela_raw:
            opcoes_section = tabela_raw.split('## OPÇÕES DE CAMPOS')[1]
            
            # Parse cada tabela de opções
            opcoes_tables = re.findall(
                r'### Opções para campo (\w+).*?\n((?:\|.*?\n)+)', 
                opcoes_section, 
                re.DOTALL
            )
            
            for campo_nome, opcoes_table in opcoes_tables:
                opcoes = []
                for line in opcoes_table.split('\n'):
                    if '|' in line and not '|----' in line and not '| Valor |' in line:
                        parts = [p.strip() for p in line.split('|')[1:-1]]
                        if len(parts) >= 2:
                            opcoes.append({
                                'valor': parts[0],
                                'descricao': parts[1]
                            })
                
                if campo_nome in opcoes_campos:
                    opcoes_campos[campo_nome] = opcoes
    
    def _criar_indices(self):
        """Cria índices para busca rápida"""
        for nome_tabela, tabela in self.tabelas.items():
            # Indexar palavras da descrição da tabela
            palavras = self._tokenize(tabela.descricao)
            for palavra in palavras:
                if palavra not in self.indice_descricoes:
                    self.indice_descricoes[palavra] = set()
                self.indice_descricoes[palavra].add(nome_tabela)
            
            # Indexar campos
            for campo in tabela.campos:
                campo_lower = campo.nome.lower()
                if campo_lower not in self.indice_campos:
                    self.indice_campos[campo_lower] = []
                self.indice_campos[campo_lower].append((nome_tabela, campo.descricao))
    
    def _tokenize(self, text: str) -> Set[str]:
        """Tokeniza texto para indexação"""
        # Remove pontuação e converte para lowercase
        text = re.sub(r'[^\w\s]', ' ', text.lower())
        # Remove stopwords básicas em português
        stopwords = STOPWORDS_PT
        return set(word for word in text.split() if word and word not in stopwords)
    
    def buscar_tabela(self, nome: str) -> Optional[Tabela]:
        """Busca tabela por nome exato"""
        return self.tabelas.get(nome.upper())
    
    def buscar_tabelas_por_palavra(self, palavra: str) -> List[str]:
        """Busca tabelas que contêm palavra na descrição"""
        palavra_lower = palavra.lower()
        tabelas_encontradas = set()
        
        # Busca no índice de descrições
        if palavra_lower in self.indice_descricoes:
            tabelas_encontradas.update(self.indice_descricoes[palavra_lower])
        
        # Busca parcial em nomes de tabelas
        for nome_tabela in self.tabelas.keys():
            if palavra_lower in nome_tabela.lower():
                tabelas_encontradas.add(nome_tabela)
        
        return sorted(list(tabelas_encontradas))
    
    def buscar_campo(self, nome_campo: str) -> List[Dict[str, any]]:
        """Busca campo em todas as tabelas"""
        nome_campo_lower = nome_campo.lower()
        resultados = []
        
        # Busca exata
        if nome_campo_lower in self.indice_campos:
            for tabela_nome, descricao in self.indice_campos[nome_campo_lower]:
                tabela = self.tabelas[tabela_nome]
                campo = next((c for c in tabela.campos if c.nome.lower() == nome_campo_lower), None)
                if campo:
                    resultados.append({
                        'tabela': tabela_nome,
                        'tabela_desc': tabela.descricao,
                        'campo': campo.nome,
                        'campo_desc': campo.descricao,
                        'tipo': campo.tipo,
                        'opcoes': campo.opcoes
                    })
        
        # Busca parcial se não encontrar exata
        if not resultados:
            for tabela_nome, tabela in self.tabelas.items():
                for campo in tabela.campos:
                    if nome_campo_lower in campo.nome.lower():
                        resultados.append({
                            'tabela': tabela_nome,
                            'tabela_desc': tabela.descricao,
                            'campo': campo.nome,
                            'campo_desc': campo.descricao,
                            'tipo': campo.tipo,
                            'opcoes': campo.opcoes
                        })
        
        return resultados
    
    def get_contexto_minimo(self, tabelas: List[str], campos_especificos: List[str] = None) -> str:
        """
        Retorna contexto mínimo para enviar à API
        Otimizado para usar menos tokens
        """
        contexto = []
        
        for nome_tabela in tabelas:
            if nome_tabela in self.tabelas:
                tabela = self.tabelas[nome_tabela]
                
                # Header da tabela
                contexto.append(f"## {tabela.nome}: {tabela.descricao}")
                
                # Campos
                campos_para_incluir = tabela.campos
                if campos_especificos:
                    campos_para_incluir = [
                        c for c in tabela.campos 
                        if c.nome in campos_especificos or any(ce.lower() in c.nome.lower() for ce in campos_especificos)
                    ]
                
                for campo in campos_para_incluir:
                    tipo_desc = self.tipos_dados.get(campo.tipo, campo.tipo)
                    campo_str = f"- {campo.nome} ({tipo_desc}): {campo.descricao}"
                    
                    if campo.opcoes:
                        opcoes_str = ", ".join([f"{o['valor']}={o['descricao']}" for o in campo.opcoes[:5]])
                        if len(campo.opcoes) > 5:
                            opcoes_str += f"... (+{len(campo.opcoes)-5})"
                        campo_str += f" [Opções: {opcoes_str}]"
                    
                    contexto.append(campo_str)
                
                contexto.append("")  # Linha em branco entre tabelas
        
        return "\n".join(contexto)
    
    def identificar_tabelas_relevantes(self, query: str) -> List[str]:
        """
        Identifica tabelas relevantes para uma query
        usando análise de palavras-chave
        """
        palavras = self._tokenize(query)
        tabelas_score = {}
        
        # Palavras-chave específicas do domínio
        mapeamento_contexto = MAPEAMENTO_CONTEXTO
        
        # Buscar por mapeamento direto
        for palavra in palavras:
            if palavra in mapeamento_contexto:
                for tabela in mapeamento_contexto[palavra]:
                    if tabela in self.tabelas:
                        tabelas_score[tabela] = tabelas_score.get(tabela, 0) + 2
        
        # Buscar por nome de tabela mencionado
        for nome_tabela in self.tabelas.keys():
            if nome_tabela.lower() in query.lower():
                tabelas_score[nome_tabela] = tabelas_score.get(nome_tabela, 0) + 3
        
        # Buscar por campos mencionados
        for palavra in palavras:
            if palavra in self.indice_campos:
                for tabela_nome, _ in self.indice_campos[palavra]:
                    tabelas_score[tabela_nome] = tabelas_score.get(tabela_nome, 0) + 1
        
        # Ordenar por score e retornar top 5
        tabelas_ordenadas = sorted(tabelas_score.items(), key=lambda x: x[1], reverse=True)
        return [t[0] for t in tabelas_ordenadas[:5]]
    
    def get_estatisticas(self) -> Dict[str, any]:
        """Retorna estatísticas do schema"""
        total_campos = sum(len(t.campos) for t in self.tabelas.values())
        campos_com_opcoes = sum(
            1 for t in self.tabelas.values() 
            for c in t.campos if c.opcoes
        )
        
        return {
            'total_tabelas': len(self.tabelas),
            'total_campos': total_campos,
            'campos_com_opcoes': campos_com_opcoes,
            'media_campos_por_tabela': total_campos / len(self.tabelas) if self.tabelas else 0,
            'tabelas_mais_campos': sorted(
                [(t.nome, len(t.campos)) for t in self.tabelas.values()],
                key=lambda x: x[1],
                reverse=True
            )[:5]
        }


# Exemplo de uso
if __name__ == "__main__":
    # Inicializar indexador
    indexer = SchemaIndexer()
    
    # Estatísticas
    stats = indexer.get_estatisticas()
    print("\n📊 Estatísticas do Schema:")
    print(f"  - Total de tabelas: {stats['total_tabelas']}")
    print(f"  - Total de campos: {stats['total_campos']}")
    print(f"  - Campos com opções: {stats['campos_com_opcoes']}")
    print(f"  - Média campos/tabela: {stats['media_campos_por_tabela']:.1f}")
    
    print("\n🔍 Top 5 tabelas com mais campos:")
    for tabela, qtd in stats['tabelas_mais_campos']:
        print(f"  - {tabela}: {qtd} campos")
    
    # Teste de busca
    print("\n🔎 Teste de Busca:")
    
    # Buscar tabela específica
    tabela = indexer.buscar_tabela("TGFCAB")
    if tabela:
        print(f"\n✓ Tabela TGFCAB encontrada: {tabela.descricao}")
        print(f"  Total de campos: {len(tabela.campos)}")
    
    # Buscar campo
    print("\n🔍 Buscando campo 'NUNOTA':")
    resultados = indexer.buscar_campo("NUNOTA")
    for r in resultados[:3]:
        print(f"  - {r['tabela']}: {r['campo_desc']}")
    
    # Identificar tabelas relevantes
    query = "preciso de um relatório de vendas com parceiros"
    print(f"\n🎯 Query: '{query}'")
    tabelas_relevantes = indexer.identificar_tabelas_relevantes(query)
    print(f"Tabelas relevantes: {tabelas_relevantes}")
    
    # Gerar contexto mínimo
    print("\n📝 Contexto mínimo para API:")
    contexto = indexer.get_contexto_minimo(tabelas_relevantes[:2])
    print(contexto[:500] + "..." if len(contexto) > 500 else contexto)
    print(f"\n📏 Tamanho do contexto: {len(contexto)} caracteres")

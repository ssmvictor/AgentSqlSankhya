# schema_optimizer.py
"""
Otimizador de contexto para reduzir tokens na API
Trabalha em conjunto com o SchemaIndexer
"""

from typing import Dict, List
import json
from src.schema_indexer import SchemaIndexer, Tabela
from src.constants import CAMPOS_CHAVE, TIPOS_DADOS
from config.settings import MAX_TOKENS_DEFAULT

class SchemaOptimizer:
    """
    Otimiza o contexto do schema para uso eficiente com APIs de LLM
    """
    
    def __init__(self, indexer: SchemaIndexer, max_tokens: int = None):
        self.indexer = indexer
        self.max_tokens = max_tokens if max_tokens is not None else MAX_TOKENS_DEFAULT
        
        # Estratégias de compressão
        self.estrategias = {
            'full': self._estrategia_completa,
            'compact': self._estrategia_compacta,
            'minimal': self._estrategia_minima,
            'smart': self._estrategia_inteligente
        }
        
        # Cache de queries frequentes
        self.cache_queries = {}
        
    def contar_tokens(self, texto: str, modelo: str = "gpt-3.5-turbo") -> int:
        """Conta tokens aproximados para o texto"""
        try:
            import tiktoken
            encoding = tiktoken.encoding_for_model(modelo)
            return len(encoding.encode(texto))
        except:
            # Fallback: estimativa simples (1 token ≈ 4 caracteres)
            return len(texto) // 4
    
    def otimizar_para_query(self, query: str, estrategia: str = 'smart') -> Dict[str, any]:
        """
        Otimiza o contexto do schema baseado na query do usuário
        
        Retorna:
            Dict com:
            - contexto: str com o schema otimizado
            - tabelas_incluidas: list de tabelas incluídas
            - campos_totais: int número de campos
            - tokens_estimados: int tokens estimados
            - estrategia_usada: str estratégia aplicada
        """
        
        # Verificar cache
        cache_key = f"{query}:{estrategia}"
        if cache_key in self.cache_queries:
            return self.cache_queries[cache_key]
        
        # Identificar tabelas relevantes
        tabelas_relevantes = self.indexer.identificar_tabelas_relevantes(query)
        
        # Aplicar estratégia
        if estrategia in self.estrategias:
            resultado = self.estrategias[estrategia](query, tabelas_relevantes)
        else:
            resultado = self._estrategia_inteligente(query, tabelas_relevantes)
        
        # Adicionar ao cache
        self.cache_queries[cache_key] = resultado
        
        return resultado
    
    def _estrategia_completa(self, query: str, tabelas: List[str]) -> Dict:
        """Estratégia completa: inclui todos os detalhes"""
        contexto_parts = []
        campos_total = 0
        
        for nome_tabela in tabelas[:3]:  # Limitar a 3 tabelas
            if nome_tabela not in self.indexer.tabelas:
                continue
                
            tabela = self.indexer.tabelas[nome_tabela]
            contexto_parts.append(f"## Tabela: {tabela.nome}")
            contexto_parts.append(f"### Descrição: {tabela.descricao}")
            contexto_parts.append("| Campo | Descrição | Tipo |")
            contexto_parts.append("|-------|-----------|------|")
            
            for campo in tabela.campos:
                tipo_desc = TIPOS_DADOS.get(campo.tipo, campo.tipo)
                contexto_parts.append(f"| {campo.nome} | {campo.descricao} | {tipo_desc} |")
                campos_total += 1
                
                if campo.opcoes:
                    contexto_parts.append(f"\nOpções para {campo.nome}:")
                    for opcao in campo.opcoes[:5]:
                        contexto_parts.append(f"  - {opcao['valor']}: {opcao['descricao']}")
            
            contexto_parts.append("")
        
        contexto = "\n".join(contexto_parts)
        
        return {
            'contexto': contexto,
            'tabelas_incluidas': tabelas[:3],
            'campos_totais': campos_total,
            'tokens_estimados': self.contar_tokens(contexto),
            'estrategia_usada': 'completa'
        }
    
    def _estrategia_compacta(self, query: str, tabelas: List[str]) -> Dict:
        """Estratégia compacta: formato resumido"""
        contexto_parts = []
        campos_total = 0
        
        for nome_tabela in tabelas[:5]:  # Pode incluir mais tabelas
            if nome_tabela not in self.indexer.tabelas:
                continue
                
            tabela = self.indexer.tabelas[nome_tabela]
            
            # Formato compacto
            campos_str = []
            for campo in tabela.campos[:20]:  # Limitar campos
                tipo = TIPOS_DADOS.get(campo.tipo, campo.tipo)
                campo_info = f"{campo.nome}({tipo})"
                if campo.opcoes:
                    campo_info += "*"  # Indicador de que tem opções
                campos_str.append(campo_info)
                campos_total += 1
            
            contexto_parts.append(f"{tabela.nome} ({tabela.descricao}):")
            contexto_parts.append(f"Campos: {', '.join(campos_str)}")
            contexto_parts.append("")
        
        contexto = "\n".join(contexto_parts)
        
        return {
            'contexto': contexto,
            'tabelas_incluidas': tabelas[:5],
            'campos_totais': campos_total,
            'tokens_estimados': self.contar_tokens(contexto),
            'estrategia_usada': 'compacta'
        }
    
    def _estrategia_minima(self, query: str, tabelas: List[str]) -> Dict:
        """Estratégia mínima: apenas o essencial"""
        contexto_parts = []
        campos_total = 0
        
        # Incluir apenas campos-chave
        campos_chave = CAMPOS_CHAVE
        
        for nome_tabela in tabelas[:3]:
            if nome_tabela not in self.indexer.tabelas:
                continue
                
            tabela = self.indexer.tabelas[nome_tabela]
            campos_relevantes = [
                c for c in tabela.campos 
                if c.nome in campos_chave or any(k in c.nome for k in ['COD', 'ID', 'NU'])
            ][:10]
            
            if campos_relevantes:
                contexto_parts.append(f"{tabela.nome}: {', '.join([c.nome for c in campos_relevantes])}")
                campos_total += len(campos_relevantes)
        
        contexto = "\n".join(contexto_parts)
        
        return {
            'contexto': contexto,
            'tabelas_incluidas': tabelas[:3],
            'campos_totais': campos_total,
            'tokens_estimados': self.contar_tokens(contexto),
            'estrategia_usada': 'minima'
        }
    
    def _estrategia_inteligente(self, query: str, tabelas: List[str]) -> Dict:
        """
        Estratégia inteligente: ajusta baseado na complexidade da query
        """
        query_lower = query.lower()
        
        # Detectar tipo de operação
        operacao_complexa = any(word in query_lower for word in [
            'join', 'inner', 'left', 'group by', 'having', 'union',
            'relacionar', 'cruzar', 'agrupar', 'somar', 'contar'
        ])
        
        # Detectar necessidade de opções
        precisa_opcoes = any(word in query_lower for word in [
            'status', 'tipo', 'opção', 'opcao', 'valor', 'código'
        ])
        
        # Identificar campos mencionados
        campos_mencionados = []
        for campo_nome in self.indexer.indice_campos.keys():
            if campo_nome in query_lower:
                campos_mencionados.append(campo_nome)
        
        # Construir contexto baseado na análise
        contexto_parts = []
        campos_total = 0
        tabelas_incluidas = []
        
        for nome_tabela in tabelas:
            if nome_tabela not in self.indexer.tabelas:
                continue
                
            tabela = self.indexer.tabelas[nome_tabela]
            tabelas_incluidas.append(nome_tabela)
            
            # Header
            contexto_parts.append(f"### {tabela.nome}: {tabela.descricao}")
            
            # Selecionar campos relevantes
            campos_para_incluir = []
            
            # Sempre incluir chaves primárias e estrangeiras
            for campo in tabela.campos:
                nome_upper = campo.nome.upper()
                if any(k in nome_upper for k in ['NUNOTA', 'CODPARC', 'CODPROD', 'NUFIN', 'CODEMP']):
                    campos_para_incluir.append(campo)
                elif campo.nome.lower() in campos_mencionados:
                    campos_para_incluir.append(campo)
                elif operacao_complexa and any(k in nome_upper for k in ['COD', 'NU', 'ID']):
                    campos_para_incluir.append(campo)
            
            # Se poucos campos foram selecionados, adicionar os principais
            if len(campos_para_incluir) < 5:
                for campo in tabela.campos[:10]:
                    if campo not in campos_para_incluir:
                        campos_para_incluir.append(campo)
            
            # Formatar campos
            for campo in campos_para_incluir[:15]:  # Limite de campos
                tipo = TIPOS_DADOS.get(campo.tipo, campo.tipo)
                campo_str = f"- {campo.nome} ({tipo}): {campo.descricao}"
                
                # Adicionar opções se necessário
                if precisa_opcoes and campo.opcoes:
                    opcoes_resumo = []
                    for opcao in campo.opcoes[:3]:
                        opcoes_resumo.append(f"{opcao['valor']}={opcao['descricao']}")
                    campo_str += f" [{', '.join(opcoes_resumo)}]"
                
                contexto_parts.append(campo_str)
                campos_total += 1
            
            contexto_parts.append("")
            
            # Verificar tamanho do contexto
            contexto_atual = "\n".join(contexto_parts)
            if self.contar_tokens(contexto_atual) > self.max_tokens * 0.8:
                break
        
        contexto = "\n".join(contexto_parts)
        
        return {
            'contexto': contexto,
            'tabelas_incluidas': tabelas_incluidas,
            'campos_totais': campos_total,
            'tokens_estimados': self.contar_tokens(contexto),
            'estrategia_usada': 'inteligente',
            'analise': {
                'operacao_complexa': operacao_complexa,
                'precisa_opcoes': precisa_opcoes,
                'campos_mencionados': campos_mencionados
            }
        }
    
    def gerar_contexto_com_exemplos(self, query: str, incluir_exemplos: bool = True) -> str:
        """
        Gera contexto completo incluindo exemplos de SQL quando relevante
        """
        # Otimizar schema
        resultado = self.otimizar_para_query(query)
        
        contexto_final = [
            "## Contexto do Banco de Dados Sankhya",
            "",
            resultado['contexto']
        ]
        
        if incluir_exemplos:
            # Adicionar exemplos relevantes
            exemplos = self._buscar_exemplos_relevantes(query)
            if exemplos:
                contexto_final.append("\n## Exemplos Relevantes:")
                contexto_final.extend(exemplos)
        
        return "\n".join(contexto_final)
    
    def _buscar_exemplos_relevantes(self, query: str) -> List[str]:
        """Busca exemplos relevantes baseados na query"""
        exemplos = []
        query_lower = query.lower()
        
        # Mapeamento de padrões para exemplos
        if 'pedido' in query_lower and 'aberto' in query_lower:
            exemplos.append("""
```sql
-- Pedidos em aberto
SELECT * FROM TGFCAB 
WHERE TIPMOV = 'P' AND STATUSNOTA = 'L' AND PENDENTE = 'S'
```""")
        
        if 'venda' in query_lower and 'devolução' in query_lower:
            exemplos.append("""
```sql
-- Vendas com devolução
SELECT v.NUNOTA, d.NUNOTA AS NUNOTA_DEVOL
FROM TGFCAB v
INNER JOIN TGFVAR vr ON vr.NUNOTAORIG = v.NUNOTA
INNER JOIN TGFCAB d ON d.NUNOTA = vr.NUNOTA
WHERE v.TIPMOV = 'V'
```""")
        
        return exemplos[:2]  # Limitar exemplos
    
    def salvar_estatisticas(self, filepath: str = "schema_stats.json"):
        """Salva estatísticas de uso para análise"""
        stats = {
            'total_queries_cached': len(self.cache_queries),
            'estatisticas_schema': self.indexer.get_estatisticas(),
            'queries_processadas': list(self.cache_queries.keys())[:10]
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Estatísticas salvas em {filepath}")


# Exemplo de uso prático
def exemplo_uso_completo():
    """Demonstra o uso completo do sistema de indexação e otimização"""
    
    print("🚀 Iniciando Sistema de Indexação e Otimização\n")
    
    # Inicializar
    indexer = SchemaIndexer()
    optimizer = SchemaOptimizer(indexer)
    
    # Queries de teste
    queries_teste = [
        "listar todos os pedidos de venda em aberto",
        "relatorio de vendas com parceiros e produtos",
        "qual o status da nota fiscal TGFCAB",
        "buscar notas com impostos ICMS e IPI"
    ]
    
    print("📝 Testando otimização para diferentes queries:\n")
    
    for i, query in enumerate(queries_teste, 1):
        print(f"{i}. Query: '{query}'")
        print("-" * 50)
        
        # Testar diferentes estratégias
        for estrategia in ['minimal', 'compact', 'smart']:
            resultado = optimizer.otimizar_para_query(query, estrategia)
            
            print(f"  📊 Estratégia '{estrategia}':")
            print(f"     - Tabelas: {', '.join(resultado['tabelas_incluidas'])}")
            print(f"     - Campos: {resultado['campos_totais']}")
            print(f"     - Tokens: ~{resultado['tokens_estimados']}")
            
            if estrategia == 'smart' and 'analise' in resultado:
                print(f"     - Análise: Complexa={resultado['analise']['operacao_complexa']}, "
                      f"Opções={resultado['analise']['precisa_opcoes']}")
        
        print()
    
    # Salvar estatísticas
    optimizer.salvar_estatisticas()
    
    # Exemplo de contexto final para API
    print("\n📤 Exemplo de Contexto para API:")
    print("=" * 50)
    query_exemplo = "criar relatório de vendas do mês com rentabilidade"
    contexto = optimizer.gerar_contexto_com_exemplos(query_exemplo)
    
    # Mostrar primeiras linhas
    linhas = contexto.split('\n')[:20]
    for linha in linhas:
        print(linha)
    print("...")
    print(f"\n📏 Total: {len(contexto)} caracteres, ~{optimizer.contar_tokens(contexto)} tokens")


if __name__ == "__main__":
    exemplo_uso_completo()

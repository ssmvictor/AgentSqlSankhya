# agno_sankhya_agent_corrected.py
"""
Agente Agno integrado com o sistema de indexação do Schema Sankhya.
Versão corrigida conforme a documentação oficial do Agno e alinhada com a
nova estrutura de pacotes (src/, config/).
"""

import os
from typing import Dict, Optional, Any, List
from dotenv import load_dotenv

# Carregar variaveis de ambiente o mais cedo possivel
load_dotenv()

from agno.agent import Agent
from agno.team.team import Team
from agno.tools import tool
from agno.models.xai import xAI  # Para usar o Grok
# from agno.models.openai import OpenAIChat  # Alternativa
from config.settings import (
    BASE_DIR,
    EXEMPLOS_USO_FILE,
    GROK_MODEL,
    INSTRUCOES_IA_FILE,
    get_schema_path,
)
from src.schema_indexer import SchemaIndexer
from src.schema_optimizer import SchemaOptimizer
import json
from datetime import datetime

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar componentes globais
INDEXER = SchemaIndexer(get_schema_path())
OPTIMIZER = SchemaOptimizer(INDEXER, max_tokens=1500)

# ---------- Utilidades de credenciais ----------

def _validar_credenciais_modelo(required_vars: Optional[List[str]] = None) -> None:
    """
    Garante que as variáveis de ambiente necessárias para os modelos estejam definidas.

    Args:
        required_vars: Lista explícita de variáveis a validar. Se None, usa padrão do xAI.

    Raises:
        RuntimeError: Se uma ou mais variáveis obrigatórias estiverem ausentes.
    """
    variaveis = required_vars or ["XAI_API_KEY"]
    ausentes = [var for var in variaveis if not os.getenv(var)]

    if ausentes:
        lista = ", ".join(ausentes)
        raise RuntimeError(
            "Credenciais do modelo ausentes. Defina as variáveis de ambiente "
            f"{lista} no sistema ou arquivo .env antes de usar o assistente."
        )


def _criar_modelo_xai(**kwargs) -> xAI:
    """
    Helper para instanciar o modelo xAI garantindo credenciais.
    """
    _validar_credenciais_modelo(["XAI_API_KEY"])
    return xAI(**kwargs)

# ============= FERRAMENTAS (TOOLS) =============

@tool
def schema_lookup(query: str) -> Dict[str, Any]:
    """
    Busca informações otimizadas no dicionário de dados Sankhya.
    
    Args:
        query: Pergunta ou solicitação do usuário
        
    Returns:
        Dict com contexto otimizado e metadados
    """
    # Otimizar contexto
    resultado = OPTIMIZER.otimizar_para_query(query, estrategia='smart')
    
    # Buscar exemplos relevantes
    exemplos_relevantes = _filtrar_exemplos_relevantes(query)
    
    return {
        'contexto_schema': resultado['contexto'],
        'tabelas_identificadas': resultado['tabelas_incluidas'],
        'exemplos_sql': exemplos_relevantes,
        'tokens_usados': resultado['tokens_estimados'],
        'metadados': {
            'campos_incluidos': resultado['campos_totais'],
            'estrategia': resultado['estrategia_usada']
        }
    }

@tool
def sql_validator(sql: str) -> Dict[str, Any]:
    """
    Valida SQL contra o schema Sankhya.
    
    Args:
        sql: Query SQL para validar
        
    Returns:
        Dict com resultado da validação
    """
    validacao = {
        'valido': True,
        'avisos': [],
        'erros': [],
        'tabelas_encontradas': [],
        'campos_encontrados': []
    }
    
    import re

    sql_upper = sql.upper()
    
    # Verificar tabelas mencionadas com correspondência exata por limites de palavra
    for nome_tabela in INDEXER.tabelas.keys():
        padrao_tabela = r'\b{}\b'.format(re.escape(nome_tabela))
        if re.search(padrao_tabela, sql, flags=re.IGNORECASE):
            validacao['tabelas_encontradas'].append(nome_tabela)
    
    # Verificar campos mencionados
    campos_no_sql = re.findall(r'\b([A-Z_]+)\b', sql_upper)
    tabelas_encontradas_set = set(validacao['tabelas_encontradas'])
    campos_vistos = set()
    
    for campo_possivel in campos_no_sql:
        if campo_possivel in campos_vistos:
            continue
        if campo_possivel in INDEXER.indice_campos:
            if (
                not tabelas_encontradas_set
                or any(
                    tabela in tabelas_encontradas_set
                    for tabela, _ in INDEXER.indice_campos[campo_possivel]
                )
            ):
                validacao['campos_encontrados'].append(campo_possivel)
            campos_vistos.add(campo_possivel)
    
    # Avisos básicos
    if 'SELECT *' in sql_upper:
        validacao['avisos'].append("Considere especificar campos ao invés de usar SELECT *")
    
    if not validacao['tabelas_encontradas']:
        validacao['avisos'].append("Nenhuma tabela do schema foi identificada no SQL")
    
    return validacao

def _filtrar_exemplos_relevantes(query: str) -> str:
    """Filtra exemplos relevantes para a query"""
    query_lower = query.lower()
    exemplos_filtrados = []
    
    # Carregar exemplos
    try:
        exemplos_path = (
            EXEMPLOS_USO_FILE
            if EXEMPLOS_USO_FILE.exists()
            else BASE_DIR / "exemplos_de_uso.md"
        )
        with open(exemplos_path, "r", encoding="utf-8") as f:
            exemplos_content = f.read()
    except:
        exemplos_content = ""
    
    # Parse básico dos exemplos
    if 'pedido' in query_lower:
        exemplos_filtrados.append("""
-- Pedidos em aberto
SELECT * FROM TGFCAB 
WHERE TIPMOV = 'P' AND STATUSNOTA = 'L' AND PENDENTE = 'S'
        """)
    
    if 'rentabilidade' in query_lower:
        exemplos_filtrados.append("""
-- Rentabilidade
SELECT 
    (SUM(VLRTOT - VLRDESC) - SUM(VLRCUS)) AS LUCRO,
    ((SUM(VLRTOT - VLRDESC) - SUM(VLRCUS)) / SUM(VLRTOT - VLRDESC)) * 100 AS RENTABILIDADE_PERC
FROM TGFITE
        """)
    
    return "\n".join(exemplos_filtrados[:2])

# ============= AGENTES =============

def criar_agente_sql() -> Agent:
    """
    Cria o agente principal para SQL Sankhya.
    """
    # Carregar instruções
    try:
        instrucoes_path = (
            INSTRUCOES_IA_FILE
            if INSTRUCOES_IA_FILE.exists()
            else BASE_DIR / "instrucoes_ia.md"
        )
        with open(instrucoes_path, "r", encoding="utf-8") as f:
            instrucoes_base = f.read()
    except:
        instrucoes_base = "Você é um especialista em SQL Sankhya."
    
    instrucoes = [
        instrucoes_base,
        "Use a ferramenta schema_lookup para buscar informações do schema",
        "Use a ferramenta sql_validator para validar SQL gerado",
        "Sempre formate SQL de forma legível",
        "Inclua comentários explicativos no SQL",
        "Para queries complexas, explique a lógica utilizada"
    ]
    
    return Agent(
        name="Assistente SQL Sankhya",
        instructions=instrucoes,
        model=_criar_modelo_xai(id=GROK_MODEL, temperature=0.3, max_tokens=2000),
        tools=[schema_lookup, sql_validator],
        markdown=True,
    )

def criar_agente_analista() -> Agent:
    """
    Cria um agente analista para revisar e otimizar SQL.
    """
    return Agent(
        name="Analista SQL",
        instructions=[
            "Analise queries SQL para possíveis otimizações",
            "Sugira índices quando apropriado",
            "Identifique potenciais problemas de performance",
            "Valide a lógica de negócio"
        ],
        model=_criar_modelo_xai(id=GROK_MODEL),
        tools=[sql_validator],
        markdown=True
    )

# ============= TIME (TEAM) =============

def criar_time_sankhya() -> Team:
    """
    Cria um time de agentes para trabalhar com SQL Sankhya.
    """
    agente_sql = criar_agente_sql()
    agente_analista = criar_agente_analista()
    
    return Team(
        name="Time SQL Sankhya",
        model=_criar_modelo_xai(id=GROK_MODEL),
        members=[agente_sql, agente_analista],
        instructions=[
            "Colabore para gerar SQL otimizado e validado",
            "O agente SQL gera a query inicial",
            "O analista revisa e sugere melhorias",
            "Apresente apenas o resultado final consolidado"
        ],
        markdown=True,
        enable_agentic_state=True,
    )

# ============= CLASSE PRINCIPAL =============

class SankhyaSQLAssistant:
    """
    Assistente completo para SQL Sankhya usando Agno (CORRIGIDO).
    """
    
    def __init__(self, usar_time: bool = False):
        """
        Inicializa o assistente.
        
        Args:
            usar_time: Se True, usa um time de agentes. Se False, usa agente único.
        """
        self.usar_time = usar_time
        
        if usar_time:
            self.executor = criar_time_sankhya()
        else:
            self.executor = criar_agente_sql()
        
        # Cache de respostas
        self.cache = {}
        self.historico = []
    
    def processar_query(self, query: str) -> Dict[str, Any]:
        """
        Processa uma query do usuário.
        
        Args:
            query: Solicitação do usuário
            
        Returns:
            Dict com resposta estruturada
        """
        # Verificar cache
        if query in self.cache:
            print("[CACHE] Resposta do cache")
            return self.cache[query]
        
        try:
            # Executar agente ou time
            print(f"[AGENTE] Processando: {query}")
            
            # Usar run() ao invés de kickoff() que não existe
            response = self.executor.run(query)
            
            # Estruturar resposta
            resposta = {
                'status': 'success',
                'query_original': query,
                'resposta': response.content if hasattr(response, 'content') else str(response),
                'sql_gerado': self._extrair_sql(response),
                'timestamp': str(datetime.now())
            }
            
            # Adicionar ao cache e histórico
            self.cache[query] = resposta
            self.historico.append({
                'query': query,
                'timestamp': resposta['timestamp']
            })
            
            return resposta
            
        except Exception as e:
            return {
                'status': 'error',
                'query_original': query,
                'erro': str(e),
                'sugestao': 'Tente reformular a pergunta ou seja mais específico'
            }
    
    def processar_interativo(self, query: str, stream: bool = True):
        """
        Processa query com resposta interativa (streaming).
        """
        try:
            print(f"[AGENTE] Processando: {query}")
            print("-" * 50)
            
            if isinstance(self.executor, Team):
                # Team ainda não expõe print_response de forma estável
                response = self.executor.run(query)
                conteudo = response.content if hasattr(response, "content") else response
                print(str(conteudo))
            else:
                # Usar print_response para streaming quando disponível
                self.executor.print_response(
                    query,
                    stream=stream,
                    show_full_reasoning=True if hasattr(self.executor, "reasoning") else False,
                )
            
            # Adicionar ao histórico
            self.historico.append({
                'query': query,
                'timestamp': str(datetime.now())
            })
            
        except Exception as e:
            print(f"[ERRO] Erro: {e}")
    
    def _extrair_sql(self, response: Any) -> Optional[str]:
        """Extrai SQL da resposta"""
        import re
        
        # Converter response para string
        text = str(response.content) if hasattr(response, 'content') else str(response)
        
        # Buscar padrão SQL
        sql_match = re.search(r'```sql\n(.*?)\n```', text, re.DOTALL)
        if sql_match:
            return sql_match.group(1).strip()
        
        return None
    
    def salvar_historico(self, filepath: str = "historico_queries.json"):
        """Salva histórico de queries para análise"""
        historico_completo = {
            'total_queries': len(self.historico),
            'queries_cacheadas': len(self.cache),
            'historico': self.historico[-50:],  # Últimas 50
            'timestamp_export': str(datetime.now())
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(historico_completo, f, indent=2, ensure_ascii=False)
        
        print(f"[INFO] Histórico salvo: {filepath}")

# ============= EXEMPLO DE USO =============

def exemplo_uso():
    """Demonstra o uso correto do assistente Sankhya com Agno"""
    
    print("Agente Assistente Sankhya SQL com Agno (VERSÃO CORRIGIDA)")
    print("=" * 50)
    
    # Testar com agente único
    print("\n### Teste com Agente Único ###\n")
    assistant_single = SankhyaSQLAssistant(usar_time=False)
    
    queries = [
        "Liste todos os pedidos de venda em aberto",
        "Qual a descrição da tabela TGFCAB?",
        "Monte um relatório de vendas com rentabilidade por produto"
    ]
    
    for query in queries:
        print(f"\n[QUERY] Query: {query}")
        print("-" * 40)
        assistant_single.processar_interativo(query, stream=True)
        print("\n")
    
    # Testar com time
    print("\n### Teste com Time de Agentes ###\n")
    assistant_team = SankhyaSQLAssistant(usar_time=True)
    
    query_complexa = "Crie uma query otimizada para análise de vendas dos últimos 6 meses com margem de lucro"
    assistant_team.processar_interativo(query_complexa, stream=True)
    
    # Salvar histórico
    assistant_single.salvar_historico("historico_agente_unico.json")
    assistant_team.salvar_historico("historico_time.json")

if __name__ == "__main__":
    exemplo_uso()

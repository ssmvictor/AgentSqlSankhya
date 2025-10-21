"""
Constantes globais do sistema de indexação Sankhya.

Este arquivo contém constantes utilizadas em todo o sistema de indexação
e otimização de schemas Sankhya, centralizando valores importantes para
manutenção e consistência.
"""

# Mapeamento de tipos de dados Sankhya
TIPOS_DADOS = {
    'I': 'Integer',
    'S': 'String', 
    'F': 'Float',
    'D': 'Date',
    'H': 'DateTime',
    'T': 'Time',
    'C': 'CLOB',
    'B': 'BLOB'
}

# Stopwords em português para processamento de texto
STOPWORDS_PT = frozenset({
    'de', 'da', 'do', 'para', 'o', 'a', 'e', 'ou',
    'em', 'com', 'por', 'dos', 'das', 'no', 'na',
    'nos', 'nas'
})

# Mapeamento de contexto para identificação de tabelas relevantes
MAPEAMENTO_CONTEXTO = {
    'pedido': ['TGFCAB', 'TGFITE'],
    'venda': ['TGFCAB', 'TGFITE', 'TGFPAR'],
    'nota': ['TGFCAB', 'TGFITE', 'TGFCAN'],
    'fiscal': ['TGFCAB', 'TGFDIN'],
    'parceiro': ['TGFPAR', 'TGFCPL', 'TGFCTT'],
    'cliente': ['TGFPAR', 'TGFCPL', 'TGFCTT'],
    'fornecedor': ['TGFPAR', 'TGFCPL'],
    'produto': ['TGFPRO', 'TGFITE', 'TGFBAR'],
    'financeiro': ['TGFFIN', 'TGFCOM'],
    'imposto': ['TGFDIN', 'TGFCFO'],
    'estoque': ['TGFEST', 'TGFCTE'],
    'custo': ['TGFCUS', 'TGFCUSITE'],
}

# Campos chave importantes para otimização
CAMPOS_CHAVE = [
    'NUNOTA', 'CODPARC', 'CODPROD', 'NUFIN', 
    'TIPMOV', 'STATUSNOTA', 'DTNEG', 'VLRNOTA', 
    'NOMEPARC'
]

# Estratégias de otimização disponíveis
ESTRATEGIAS_DISPONIVEIS = ['minimal', 'compact', 'smart', 'full']

# Configurações de cache
CACHE_DIR_DEFAULT = '.cache'
CACHE_INDEX_FILE = 'schema_index.pkl'
CACHE_HASH_FILE = 'schema_hash.txt'

## Documentação para schema-indexer.py

### Visão Geral
O `schema-indexer.py` é um sistema de indexação e busca para o dicionário de dados do Sankhya. Ele otimiza o acesso ao schema do banco de dados, permitindo buscas rápidas por tabelas e campos, além de reduzir o consumo de tokens ao trabalhar com APIs de LLM.

### Classes Principais

#### Campo
Representa um campo (coluna) de uma tabela do banco de dados.

**Atributos:**
- `nome` (str): Nome do campo
- `descricao` (str): Descrição do campo
- `tipo` (str): Tipo de dados do campo
- `observacoes` (str, opcional): Observações adicionais sobre o campo
- `opcoes` (List[Dict[str, str]], opcional): Lista de opções válidas para o campo

#### Tabela
Representa uma tabela do banco de dados Sankhya.

**Atributos:**
- `nome` (str): Nome da tabela
- `descricao` (str): Descrição da tabela
- `campos` (List[Campo]): Lista de campos da tabela

**Métodos:**
- `to_compact_dict()`: Retorna uma versão compacta da tabela para economizar tokens

#### SchemaIndexer
Indexador e buscador do schema do Sankhya.

**Atributos:**
- `schema_path` (Path): Caminho para o arquivo de schema markdown
- `cache_dir` (Path): Diretório para armazenamento de cache
- `tabelas` (Dict[str, Tabela]): Dicionário de tabelas indexadas
- `indice_campos` (Dict[str, List[Tuple[str, str]]]): Índice de campos para busca rápida
- `indice_descricoes` (Dict[str, Set[str]]]): Índice de palavras nas descrições
- `tipos_dados` (Dict[str, str]): Mapeamento de códigos de tipo para descrições

**Métodos Principais:**

1. **Inicialização e Cache**
   - `__init__(schema_path: str = "sankhya_schema.md", cache_dir: str = ".cache")`: Inicializa o indexador
   - `_get_cache_hash()`: Gera hash do arquivo para verificar mudanças
   - `_load_cache()`: Carrega índice do cache se existir e estiver atualizado
   - `_save_cache()`: Salva índice em cache

2. **Parsing do Schema**
   - `parse_schema()`: Faz o parse do arquivo markdown para estruturas indexadas
   - `_parse_tabela(tabela_raw: str)`: Faz o parse de uma tabela individual
   - `_parse_opcoes(tabela_raw: str, nome_tabela: str, opcoes_campos: dict)`: Faz o parse das opções de campos
   - `_criar_indices()`: Cria índices para busca rápida
   - `_tokenize(text: str)`: Tokeniza texto para indexação

3. **Métodos de Busca**
   - `buscar_tabela(nome: str)`: Busca tabela por nome exato
   - `buscar_tabelas_por_palavra(palavra: str)`: Busca tabelas que contêm palavra na descrição
   - `buscar_campo(nome_campo: str)`: Busca campo em todas as tabelas
   - `identificar_tabelas_relevantes(query: str)`: Identifica tabelas relevantes para uma query

4. **Geração de Contexto**
   - `get_contexto_minimo(tabelas: List[str], campos_especificos: List[str] = None)`: Retorna contexto mínimo para enviar à API

5. **Estatísticas**
   - `get_estatisticas()`: Retorna estatísticas do schema

### Funcionalidades Especiais
- **Cache Automático**: O indexador salva e carrega automaticamente o schema em cache para melhorar o desempenho em execuções subsequentes
- **Busca Inteligente**: Permite buscar tabelas e campos por nome ou palavras-chave nas descrições
- **Mapeamento de Contexto**: Possui mapeamentos pré-definidos entre palavras-chave e tabelas específicas (ex: "pedido" -> TGFCAB, TGFITE)
- **Tokenização Inteligente**: Remove stopwords em português durante a indexação para melhorar a relevância das buscas
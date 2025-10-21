## Documentação para schema-optimizer.py

### Visão Geral
O `schema-optimizer.py` é um componente que otimiza o contexto do schema do Sankhya para uso eficiente com APIs de LLM, reduzindo o número de tokens enviados. Ele trabalha em conjunto com o `SchemaIndexer` para gerar contextos relevantes e compactos com base nas queries do usuário.

### Dependências
- `tiktoken`: Biblioteca para contar tokens (instalar com `pip install tiktoken`)

### Classes Principais

#### SchemaOptimizer
Otimiza o contexto do schema para uso eficiente com APIs de LLM.

**Atributos:**
- `indexer` (SchemaIndexer): Instância do indexador de schema
- `max_tokens` (int): Número máximo de tokens permitidos (padrão: 2000)
- `estrategias` (Dict[str, function]): Estratégias de compressão disponíveis
- `cache_queries` (Dict): Cache de queries frequentes

**Métodos Principais:**

1. **Inicialização e Utilitários**
   - `__init__(indexer: SchemaIndexer, max_tokens: int = 2000)`: Inicializa o otimizador
   - `contar_tokens(texto: str, modelo: str = "gpt-3.5-turbo")`: Conta tokens aproximados para o texto

2. **Otimização de Contexto**
   - `otimizar_para_query(query: str, estrategia: str = 'smart')`: Otimiza o contexto do schema baseado na query do usuário

   **Retorna um dicionário com:**
   - `contexto`: String com o schema otimizado
   - `tabelas_incluidas`: Lista de tabelas incluídas
   - `campos_totais`: Número de campos incluídos
   - `tokens_estimados`: Tokens estimados do contexto
   - `estrategia_usada`: Estratégia aplicada

3. **Estratégias de Compressão**
   - `_estrategia_completa(query: str, tabelas: List[str])`: Inclui todos os detalhes das tabelas
   - `_estrategia_compacta(query: str, tabelas: List[str])`: Formato resumido das tabelas
   - `_estrategia_minima(query: str, tabelas: List[str])`: Apenas o essencial
   - `_estrategia_inteligente(query: str, tabelas: List[str])`: Ajusta baseado na complexidade da query

4. **Funcionalidades Adicionais**
   - `gerar_contexto_com_exemplos(query: str, incluir_exemplos: bool = True)`: Gera contexto completo incluindo exemplos de SQL
   - `_buscar_exemplos_relevantes(query: str)`: Busca exemplos relevantes baseados na query
   - `salvar_estatisticas(filepath: str = "schema_stats.json")`: Salva estatísticas de uso para análise

### Estratégias de Compressão

1. **Completa ('full')**: 
   - Inclui todos os detalhes das tabelas (descrição completa, todos os campos com tipos e descrições)
   - Limita a 3 tabelas
   - Mais verbosa mas com todas as informações

2. **Compacta ('compact')**: 
   - Formato resumido com nomes de campos e tipos
   - Pode incluir mais tabelas
   - Usa menos tokens que a estratégia completa

3. **Mínima ('minimal')**: 
   - Apenas campos-chave e essenciais
   - Foco em campos com prefixos como COD, ID, NU
   - Estratégia mais econômica em termos de tokens

4. **Inteligente ('smart')**: 
   - Analisa a query para determinar a complexidade
   - Detecta se precisa de opções de campos
   - Identifica campos mencionados na query
   - Ajusta o contexto automaticamente com base nessas análises

### Funcionalidades Especiais
- **Cache de Queries**: Armazena em cache resultados de otimização para queries repetidas
- **Detecção Inteligente**: Analisa automaticamente a complexidade da query para escolher o nível de detalhe apropriado
- **Contagem de Tokens**: Estima o número de tokens do contexto gerado usando a biblioteca tiktoken
- **Exemplos Relevantes**: Inclui exemplos de SQL relevantes com base na query do usuário
- **Limitação Automática**: Respeita o limite máximo de tokens configurado, parando de adicionar conteúdo quando próximo do limite
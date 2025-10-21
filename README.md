# 🤖 IA Agno - Assistente SQL para Sankhya

[![Status da Build](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/seu-usuario/ia-agno)
[![Versão](https://img.shields.io/badge/version-1.0.0-blue)](https://github.com/seu-usuario/ia-agno)
[![Licença](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

> Um assistente inteligente para gerar consultas SQL otimizadas para o banco de dados do ERP Sankhya usando linguagem natural.

---

## 📜 Índice

1.  [Visão Geral](#-visão-geral)
2.  [✨ Funcionalidades](#-funcionalidades)
3.  [⚙️ Instalação](#️-instalação)
4.  [🚀 Início Rápido](#-início-rápido)
5.  [📖 Documentação da API](#-documentação-da-api)
6.  [🔧 Configuração](#-configuração)
7.  [💻 Desenvolvimento](#-desenvolvimento)
8.  [🧪 Testes](#-testes)
9.  [🤝 Como Contribuir](#-como-contribuir)
10. [📄 Licença](#-licença)
11. [📞 Suporte e Contato](#-suporte-e-contato)

---

## 🎯 Visão Geral

O **IA Agno** é um toolkit em Python desenvolvido para simplificar a interação com o complexo banco de dados do ERP Sankhya. Ele processa um dicionário de dados legível por humanos, o indexa para buscas eficientes e utiliza esse conhecimento para alimentar um agente de IA. Este agente é capaz de entender perguntas em linguagem natural e convertê-las em consultas SQL precisas e otimizadas.

O principal problema que este projeto resolve é a alta barreira de entrada para consultar o banco de dados do Sankhya, que possui um esquema extenso e complexo. Ao fornecer uma interface de conversação, ele capacita desenvolvedores, analistas e até usuários de negócio a extrair dados valiosos sem a necessidade de serem especialistas em SQL ou de conhecerem a fundo a estrutura do banco.

## ✨ Funcionalidades

-   **⚡ Indexação Inteligente de Schema**: Processa um dicionário de dados em Markdown e cria um índice rápido e pesquisável de tabelas, campos e seus relacionamentos.
-   **🧠 Otimização Consciente do Contexto**: Seleciona dinamicamente as partes mais relevantes do schema com base na pergunta do usuário para criar um contexto com uso eficiente de tokens para Modelos de Linguagem (LLMs).
-   **🗣️ Linguagem Natural para SQL**: Integra-se com frameworks de agentes de IA (como o Agno) para fornecer uma interface de conversação que gera consultas SQL.
-   **📊 Análise de Estratégia**: Emprega múltiplas estratégias (`minimal`, `compact`, `smart`) para decidir o nível de detalhe a ser fornecido ao LLM, equilibrando a qualidade do contexto e o custo de tokens.
-   **🧩 Modular e Extensível**: Projetado com uma clara separação de responsabilidades, facilitando a adição de novas funcionalidades, o suporte a diferentes LLMs ou a integração com outros sistemas.

---

## ⚙️ Instalação

### Pré-requisitos

-   Python 3.10 ou superior
-   Gerenciador de pacotes `pip`
-   Um ambiente virtual (`venv`) é altamente recomendado.

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/ia-agno.git
    cd ia-agno
    ```

2.  **Crie e ative um ambiente virtual:**

    -   No Windows:
        ```bash
        python -m venv .venv
        .venv\Scripts\activate
        ```
    -   No macOS/Linux:
        ```bash
        python -m venv .venv
        source .venv/bin/activate
        ```

3.  **Instale as dependências necessárias:**
    ```bash
    pip install -r requirements.txt
    ```

### Verificação

Para garantir que os componentes principais foram instalados corretamente, execute os comandos abaixo. Eles devem finalizar sem erros de importação:

```bash
# Testa o SchemaIndexer
python -c "from src.schema_indexer import SchemaIndexer; print('SchemaIndexer OK')"

# Testa o SchemaOptimizer
python -c "from src.schema_optimizer import SchemaOptimizer; print('SchemaOptimizer OK')"
```

---

## 🚀 Início Rápido

A maneira mais rápida de ver o IA Agno em ação é executando o agente integrado. Isso iniciará uma sessão interativa onde você poderá fazer perguntas em português.

1.  **Garanta que sua configuração esteja pronta**, especialmente o arquivo `config/sankhya_schema.md`.

2.  **Execute o módulo de integração do agente:**
    *(Nota: Requer a biblioteca `agno` e uma chave de API de LLM configurada no seu arquivo `.env`)*.
    ```bash
    python -m agents.agno_integration
    ```

3.  **Interaja com o assistente.** O script apresentará uma série de prompts. Abaixo, um exemplo da interação esperada:

    ```text
    🤖 Assistente Sankhya SQL com Agno (VERSÃO CORRIGIDA)
    ==================================================

    ### Teste com Agente Único ###

    📝 Query: Liste todos os pedidos de venda em aberto
    ----------------------------------------
    🤖 Processando: Liste todos os pedidos de venda em aberto
    --------------------------------------------------
    (Raciocínio do Agente)
    O usuário está pedindo uma lista de pedidos de venda em aberto.
    Preciso encontrar as tabelas e campos relevantes no schema Sankhya.
    1.  Usarei a ferramenta `schema_lookup` para buscar informações sobre "pedidos de venda".
    2.  A ferramenta retornará o contexto para tabelas como `TGFCAB`.
    3.  Com base no schema, construirei uma consulta SQL.
        - `TGFCAB` parece ser a tabela principal para cabeçalhos de notas.
        - `TIPMOV = 'P'` deve identificar pedidos de venda.
        - `STATUSNOTA = 'L'` (Liberada) e `PENDENTE = 'S'` (Pendente) provavelmente indicam "em aberto".
    4.  Gerarei a consulta SQL final.

    (SQL Gerado)
    ```sql
    -- Consulta para listar todos os pedidos de venda que estão em aberto.
    -- Um pedido é considerado "em aberto" se seu tipo de movimento é 'Pedido de Venda' (P),
    -- seu status é 'Liberada' (L) e está marcado como 'Pendente' (S).
    SELECT
        NUNOTA,      -- Número Único da Nota
        CODPARC,     -- Código do Parceiro
        DTNEG,       -- Data de Negociação
        VLRNOTA      -- Valor Total da Nota
    FROM
        TGFCAB
    WHERE
        TIPMOV = 'P'
        AND STATUSNOTA = 'L'
        AND PENDENTE = 'S';
    ```
    ```

---

## 📖 Documentação da API

A lógica principal é exposta através de duas classes: `SchemaIndexer` e `SchemaOptimizer`.

### `SchemaIndexer(schema_path, cache_dir)`

Responsável por processar e indexar o arquivo `sankhya_schema.md`.

-   **`__init__(schema_path, cache_dir)`**:
    -   `schema_path` (str): Caminho para o arquivo Markdown do schema.
    -   `cache_dir` (str): Diretório para salvar e ler os arquivos de cache.
    -   Carrega o índice do cache automaticamente se ele existir e estiver atualizado; caso contrário, processa o schema e cria um novo cache.

-   **`buscar_tabela(nome: str)`**:
    -   Retorna um objeto `Tabela` para o nome da tabela fornecido ou `None` se não for encontrada.

-   **`identificar_tabelas_relevantes(query: str)`**:
    -   Analisa uma consulta do usuário e retorna uma lista ordenada de nomes de tabelas relevantes.

### `SchemaOptimizer(indexer, max_tokens)`

Usa o `SchemaIndexer` para gerar um contexto otimizado em tokens para um LLM.

-   **`__init__(indexer, max_tokens)`**:
    -   `indexer` (SchemaIndexer): Uma instância do indexador de schema.
    -   `max_tokens` (int): O número máximo de tokens para o contexto gerado.

-   **`otimizar_para_query(query: str, estrategia: str)`**:
    -   `query` (str): A pergunta do usuário em linguagem natural.
    -   `estrategia` (str): A estratégia de otimização a ser usada. Pode ser `full`, `compact`, `minimal` ou `smart` (padrão).
    -   Retorna um dicionário contendo o `contexto` (string), `tabelas_incluidas` (lista), `tokens_estimados` (int) e outros metadados.

---

## 🔧 Configuração

A configuração é gerenciada por uma combinação de arquivos de configuração e variáveis de ambiente.

-   **Arquivo `.env`**: Crie este arquivo na raiz do projeto para armazenar informações sensíveis e configurações de ambiente. Ele é carregado automaticamente.
    ```env
    # Exemplo de arquivo .env
    GROK_API_KEY="sua-chave-de-api-aqui"
    SANKHYA_SCHEMA_PATH="C:/caminho/para/seu/sankhya_schema.md" # Opcional
    ```

-   **`config/settings.py`**: Arquivo principal que define caminhos e valores padrão. Fornece funções auxiliares como `get_schema_path()` para localizar o arquivo de schema.

-   **`config/sankhya_schema.md`**: **Este é o arquivo mais crítico.** Deve conter o dicionário de dados completo do ERP Sankhya no formato Markdown esperado pelo sistema.

-   **`config/instrucoes_ia.md`**: Contém o prompt base, a persona e as regras de comportamento para o agente de IA.

---

## 💻 Desenvolvimento

### Ambiente de Desenvolvimento

Siga os mesmos passos da seção de [Instalação](#️-instalação). O uso do ambiente virtual é fundamental para isolar as dependências de desenvolvimento.

### Executando Testes

O projeto inclui uma suíte de testes para verificar sua funcionalidade.

-   **Execute todos os testes:**
    ```bash
    python -m tests.test_indexer
    ```

---

## 🧪 Testes

O projeto utiliza o framework `unittest` nativo do Python. Os testes estão localizados no diretório `tests/`.

-   **`tests/test_indexer.py`**: Contém testes para a classe `SchemaIndexer`, garantindo que o schema seja processado e indexado corretamente.

Para executar os testes, use o comando:
```bash
python -m tests.test_indexer
```

---

## 🤝 Como Contribuir

Contribuições são muito bem-vindas! Para contribuir, por favor, siga estes passos:

1.  Faça um *fork* do repositório.
2.  Crie uma nova *branch* (`git checkout -b feature/nome-da-sua-feature`).
3.  Faça suas alterações.
4.  Garanta que todos os testes estão passando.
5.  Envie um *Pull Request* com uma descrição clara das suas mudanças.

Para mais detalhes, por favor, leia nosso guia de contribuição (TODO: criar `CONTRIBUTING.md`).

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT**. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.

---

## 📞 Suporte e Contato

-   **Rastreador de Issues**: Se você encontrar um bug ou tiver uma sugestão de melhoria, por favor, abra uma issue na nossa página de [Issues do GitHub](https://github.com/seu-usuario/ia-agno/issues).
-   **Pull Requests**: Contribuições de código são bem-vindas através de Pull Requests.

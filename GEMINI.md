# GEMINI.md - IA Agno Project

## Project Overview

This project, **IA Agno**, is a Python-based toolkit designed to facilitate interaction with the Sankhya ERP database schema. It provides functionalities for indexing the schema, optimizing it for Large Language Models (LLMs), and integrating with an AI agent framework for natural language querying.

The core purpose is to enable developers and analysts to easily understand and query the complex Sankhya database structure using natural language, powered by LLMs.

**Main Technologies:**

*   **Python 3.10+**
*   **Agno:** An AI agent framework.
*   **tiktoken:** For token counting and context optimization.
*   **python-dotenv:** For managing environment variables.

**Architecture:**

The project follows a modular architecture:

*   `src/`: Contains the core logic for schema indexing (`schema_indexer.py`) and context optimization (`schema_optimizer.py`).
*   `config/`: Holds configuration files, including the Sankhya schema (`sankhya_schema.md`), AI instructions (`instrucoes_ia.md`), and usage examples (`exemplos_de_uso.md`).
*   `agents/`: Implements the integration with the Agno agent framework (`agno_integration.py`).
*   `scripts/`: Provides utility scripts, such as for managing the cache (`manage_cache.py`).
*   `tests/`: Contains unit and functional tests.
*   `docs/`: Stores detailed documentation.

## Building and Running

**1. Prerequisites:**

*   Python 3.10+
*   An active virtual environment is recommended.

**2. Installation:**

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

**3. Key Commands:**

*   **Index the schema:**
    ```bash
    python -m src.schema_indexer
    ```

*   **Optimize context for LLM prompts:**
    ```bash
    python -m src.schema_optimizer
    ```

*   **Run the Agno agent integration (requires the `agno` package):**
    ```bash
    python -m agents.agno_integration
    ```

*   **Run tests:**
    ```bash
    python -m tests.test_indexer
    ```

*   **Manage the cache:**
    *   Clear the cache:
        ```bash
        python -m scripts.manage_cache clear
        ```
    *   View cache statistics:
        ```bash
        python -m scripts.manage_cache info
        ```

## Development Conventions

*   **Coding Style:** The code follows standard Python conventions (PEP 8).
*   **Modularity:** The project is organized into distinct modules with clear responsibilities.
*   **Configuration:** Project settings are managed through `config/settings.py` and environment variables in a `.env` file.
*   **Testing:** The `tests/` directory suggests a practice of writing unit tests for the project's components.
*   **Documentation:** The `docs/` directory and the detailed `README.md` file indicate a commitment to clear documentation.
*   **Cache:** The project uses a caching mechanism to improve performance by storing the indexed schema. The cache is located in the `.cache/` directory.

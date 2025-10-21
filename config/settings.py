"""Configuracoes do sistema de indexacao Sankhya.

Este arquivo centraliza as configuracoes de paths e parametros do sistema,
permitindo manutencao e customizacao das configuracoes do projeto.
"""

import os
from pathlib import Path

# Diretorios base
BASE_DIR = Path(__file__).parent.parent
CONFIG_DIR = BASE_DIR / "config"
CACHE_DIR = BASE_DIR / ".cache"
SRC_DIR = BASE_DIR / "src"
TESTS_DIR = BASE_DIR / "tests"
SCRIPTS_DIR = BASE_DIR / "scripts"
DOCS_DIR = BASE_DIR / "docs"
AGENTS_DIR = BASE_DIR / "agents"

# Arquivos de configuracao
def get_schema_path() -> Path:
    """Resolve o caminho do schema com fallback temporario."""
    config_schema = CONFIG_DIR / "sankhya_schema.md"
    if config_schema.exists():
        return config_schema

    root_schema = BASE_DIR / "sankhya_schema.md"
    if root_schema.exists():
        return root_schema

    raise FileNotFoundError(
        "Arquivo sankhya_schema.md nao encontrado em config/ nem na raiz do projeto."
    )


def get_cache_dir() -> Path:
    """Retorna o diretorio de cache padrao."""
    return CACHE_DIR


SCHEMA_FILE = get_schema_path()
INSTRUCOES_IA_FILE = CONFIG_DIR / "instrucoes_ia.md"
EXEMPLOS_USO_FILE = CONFIG_DIR / "exemplos_de_uso.md"

# Configuracoes de otimizacao
MAX_TOKENS_DEFAULT = 2000
MAX_TABELAS_RESULTADO = 5
MAX_CAMPOS_POR_TABELA = 15
MAX_OPCOES_EXIBIDAS = 5

# Configuracoes de API (para uso futuro)
GROK_MODEL = os.getenv("GROK_MODEL", "grok-4-fast-reasoning")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")
XAI_API_KEY = os.getenv("XAI_API_KEY")

# IA Agno - Estrutura Organizada

## Seção 1 - Visão Geral
Este repositório consolida ferramentas para indexar, otimizar e consumir o dicionário de dados do ERP Sankhya com LLMs. A fase atual reorganizou configurações em `config/` e documentação em `docs/`, simplificando manutenção, deploy e onboarding de novas pessoas no projeto.

## Seção 2 - Estrutura do Projeto
- `src/` - Implementações centrais (`schema_indexer`, `schema_optimizer`, utilidades)
- `config/` - Arquivos de configuração e dados (`settings.py`, prompts, `sankhya_schema.md`)
- `agents/` - Integrações com agentes (ex.: `AgnoIntegration`)
- `scripts/` - Scripts de suporte (`manage_cache`)
- `tests/` - Testes unitários e funcionais
- `docs/` - Documentação detalhada e histórico (`README-original.md`, guias técnicos)
- `schema_stats.json` - Métricas pré-calculadas sobre o schema para diagnósticos rápidos

## Seção 3 - Pré-requisitos
- Python 3.10+ instalado e disponível no PATH
- Pip atualizado (`python -m pip install --upgrade pip`)
- Ambiente virtual recomendado (`python -m venv .venv && source .venv/bin/activate` no Linux/macOS ou `.venv\Scripts\activate` no Windows)

## Seção 4 - Instalação
```bash
pip install -r requirements.txt
```
O arquivo `requirements.txt` contém dependências mínimas e comentários guiando instalações opcionais (LLMs, streamlit, agno, etc.).

## Seção 5 - Configurações
- Variáveis de ambiente opcionais podem ser definidas em `.env` (lidas por `config.settings` via `python-dotenv`)
- Arquivos essenciais:
  - `config/sankhya_schema.md` - Dicionário completo do ERP (requerido)
  - `config/instrucoes_ia.md` - Persona e regras base para o agente
  - `config/exemplos_de_uso.md` - Casos de uso de referência para few-shot prompts
- A função `config.settings.get_schema_path()` gerencia fallback automático para o schema.

## Seção 6 - Como Executar
```bash
# Indexar o schema e gerar cache
python -m src.schema_indexer

# Otimizar contexto para prompts de LLM
python -m src.schema_optimizer

# Rodar integração com agente Agno (após instalar o pacote agno)
python -m agents.agno_integration

# Executar testes
python -m tests.test_indexer
```

## Seção 7 - Fluxo de Trabalho
1. O indexador lê `config/sankhya_schema.md`, normaliza as tabelas e gera o cache em disco.
2. O otimizador ajusta o contexto com base na consulta, aplicando estratégias (`full`, `compact`, `minimal`, `smart`).
3. A integração com o agente consome instruções e exemplos de uso para responder perguntas em linguagem natural.
4. Scripts auxiliares (`manage_cache`) inspecionam e limpam artefatos entre execuções.

## Seção 8 - Scripts úteis
```bash
# Limpar cache
python -m scripts.manage_cache clear

# Exibir estatísticas do cache
python -m scripts.manage_cache info
```

## Seção 8.5 - Validação da Reorganização

Após a reorganização do projeto, valide que tudo está funcionando:

```bash
# 1. Testar imports
python -c "from src.schema_indexer import SchemaIndexer; print('OK')"
python -c "from src.schema_optimizer import SchemaOptimizer; print('OK')"

# 2. Executar testes completos
python -m tests.test_indexer

# 3. Validar indexador
python -m src.schema_indexer

# 4. Validar otimizador
python -m src.schema_optimizer

# 5. Verificar cache
python -m scripts.manage_cache info
```

**Resultado esperado:** todos os comandos devem executar sem erros.

[Doc] Guia completo de validação: consulte `docs/VALIDACAO.md` para instruções detalhadas, troubleshooting e checklist completo.

## Seção 9 - Documentação Complementar
- `docs/README-original.md` - README antigo mantido como histórico
- `docs/schema-indexer-doc.md` - Referência detalhada do `SchemaIndexer`
- `docs/schema-optimizer-doc.md` - Referência detalhada do `SchemaOptimizer`
- `docs/indexacao-readme.md` - Guia completo da solução de indexação
- `docs/CLAUDE.md` - Referência do servidor MCP Byterover e workflows

## Seção 10 - Troubleshooting
```bash
# Limpar cache se houver problemas
python -m scripts.manage_cache clear

# Verificar imports
python -c "from src.schema_indexer import SchemaIndexer; print('OK')"

# Ver estatísticas do cache
python -m scripts.manage_cache info
```

## Seção 11 - Contribuindo
Pull requests são bem-vindos. Para mudanças maiores, abra uma issue descrevendo contexto, impacto esperado e testes planejados antes de iniciar o desenvolvimento.

## Seção 12 - Licença
Defina a licença apropriada para o projeto (ex.: MIT). Atualize esta seção assim que a licença oficial for determinada.

## Seção 13 - Rodapé
Desenvolvido para otimizar custos e performance com LLMs no ERP Sankhya.

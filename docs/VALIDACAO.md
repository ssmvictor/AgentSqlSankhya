**Seção 1 - Pré-requisitos:**
- Python 3.10+ instalado
- Dependências instaladas: `pip install -r requirements.txt`
- Estar no diretório raiz do projeto

**Seção 2 - Validação da Estrutura:**
Comandos para verificar que todos os arquivos estão nos lugares corretos:
```bash
# Verificar estrutura de diretórios
ls -la src/ config/ tests/ scripts/ docs/ agents/

# Verificar que não há arquivos órfãos na raiz
ls *.py  # Deve mostrar apenas __init__.py
```

**Seção 3 - Validação de Imports:**
Comandos para testar que todos os imports funcionam:
```bash
# Testar import do indexador
python -c "from src.schema_indexer import SchemaIndexer; print('OK SchemaIndexer')"

# Testar import do otimizador
python -c "from src.schema_optimizer import SchemaOptimizer; print('OK SchemaOptimizer')"

# Testar import das constantes
python -c "from src.constants import TIPOS_DADOS, MAPEAMENTO_CONTEXTO; print('OK Constants')"

# Testar import das configurações
python -c "from config.settings import get_schema_path, CACHE_DIR; print('OK Settings')"

# Testar import do agente (requer agno instalado)
python -c "from agents.agno_integration import SankhyaSQLAssistant; print('OK Agno Integration')" 2>/dev/null || echo "[WARN] Agno não instalado (opcional)"
```

**Seção 4 - Validação dos Testes:**
Executar a suíte de testes completa:
```bash
# Executar testes do indexador
python -m tests.test_indexer

# Saída esperada:
# [INFO] TESTE DO SISTEMA DE INDEXACAO SANKHYA
# [1] Testando importacao dos modulos... OK
# [2] Verificando arquivo sankhya_schema.md... OK
# [3] Inicializando indexador... OK
# [4] Estatisticas do schema: (dados do schema)
# [5] Testando busca da tabela TGFCAB... OK
# [6] Testando otimizador... OK
# [7] Verificando cache... OK
# SUCESSO! TODOS OS TESTES PASSARAM.
```

**Seção 5 - Validação do Indexador:**
Executar o indexador diretamente:
```bash
# Executar indexador
python -m src.schema_indexer

# Saída esperada:
# OK Cache carregado com sucesso (se já existe)
# OU
# Indexando schema...
# OK 100+ tabelas indexadas
# OK 1000+ campos únicos encontrados
# OK Cache salvo com sucesso
#
# [Estatisticas] Estatísticas do Schema:
#   - Total de tabelas: XXX
#   - Total de campos: XXXX
#   - Campos com opções: XXX
#   - Média campos/tabela: XX.X
```

**Seção 6 - Validação do Otimizador:**
Executar o otimizador:
```bash
# Executar otimizador
python -m src.schema_optimizer

# Saída esperada:
# [Launch] Iniciando Sistema de Indexacao e Otimizacao
# OK Cache carregado com sucesso
#
# [Estatisticas] Testando otimização para diferentes queries:
# 1. Query: 'listar todos os pedidos de venda em aberto'
#   [Estatisticas] Estratégia 'minimal': Tabelas: TGFCAB, Campos: XX, Tokens: ~XXX
#   [Estatisticas] Estratégia 'compact': Tabelas: TGFCAB, TGFITE, Campos: XX, Tokens: ~XXX
#   [Estatisticas] Estratégia 'smart': Tabelas: TGFCAB, TGFITE, Campos: XX, Tokens: ~XXX
# ...
# OK Estatísticas salvas em schema_stats.json
```

**Seção 7 - Validação do Cache Manager:**
Testar o script de gerenciamento de cache:
```bash
# Ver informações do cache
python -m scripts.manage_cache info

# Saída esperada:
# [Doc] Cache localizado em: /path/to/.cache
# - schema_index.pkl - XX.X KB - atualizado em YYYY-MM-DD HH:MM:SS
# - schema_hash.txt - 0.1 KB - atualizado em YYYY-MM-DD HH:MM:SS
# Total: 2 arquivo(s), XX.X KB

# Limpar cache (opcional)
python -m scripts.manage_cache clear

# Saída esperada:
# OK Cache limpo com sucesso. Um novo cache será criado conforme necessário.

# Executar testes via cache manager
python -m scripts.manage_cache test

# Saída esperada: (mesma saída de python -m tests.test_indexer)
```

**Seção 8 - Validação do .gitignore:**
Verificar que arquivos gerados não são rastreados:
```bash
# Criar cache se não existir
python -m src.schema_indexer

# Verificar status do git
git status

# Não deve mostrar:
# - .cache/ (ignorado)
# - __pycache__/ (ignorado)
# - *.pyc (ignorado)
# - schema_stats.json (ignorado)
```

**Seção 9 - Validação de Diagnósticos:**
Verificar que não há erros de importação ou sintaxe:
```bash
# Compilar todos os arquivos Python
python -m py_compile src/*.py
python -m py_compile tests/*.py
python -m py_compile scripts/*.py
python -m py_compile config/*.py
python -m py_compile agents/*.py

# Não deve mostrar erros de sintaxe
```

**Seção 10 - Checklist Final:**
Marcar cada item após validação:
- [ ] Estrutura de diretórios correta (src/, config/, tests/, scripts/, docs/, agents/)
- [ ] Nenhum arquivo órfão na raiz (apenas __init__.py, requirements.txt, README.md, .gitignore)
- [ ] Todos os imports funcionam sem erros
- [ ] Testes executam com sucesso (`python -m tests.test_indexer`)
- [ ] Indexador executa e gera cache (`python -m src.schema_indexer`)
- [ ] Otimizador executa e gera estatísticas (`python -m src.schema_optimizer`)
- [ ] Cache manager funciona (info, clear, test)
- [ ] .gitignore está funcionando (cache não é rastreado)
- [ ] Documentação está atualizada e acessível em `docs/`
- [ ] README.md reflete a nova estrutura

**Seção 11 - Troubleshooting:**
Problemas comuns e soluções:

**Erro: ModuleNotFoundError: No module named 'src'**
- Solução: execute os comandos a partir do diretório raiz do projeto (IA_Agno/)
- Verifique que existe `__init__.py` em src/, config/, etc.

**Erro: FileNotFoundError: sankhya_schema.md**
- Solução: verifique que o arquivo está em `config/sankhya_schema.md`
- A função `get_schema_path()` em `config/settings.py` tem fallback para a raiz

**Erro: ImportError ao importar agno**
- Solução: o framework Agno é opcional. Instale com `pip install agno` se necessário
- A integração em `agents/agno_integration.py` só funciona com Agno instalado

**Cache corrompido:**
- Solução: limpe o cache com `python -m scripts.manage_cache clear`
- Execute novamente o indexador para recriar

**Seção 12 - Métricas de Sucesso:**
Após todas as validações, você deve ter:
- OK 0 erros de importação
- OK 0 arquivos órfãos na raiz
- OK 100% dos testes passando
- OK Cache funcionando (< 0.1s para carregar)
- OK Redução de 95%+ em tokens (comparado ao schema completo)
- OK Estrutura organizada seguindo PEP 8

**Seção 13 - Próximos Passos:**
Após validação bem-sucedida:
1. Fazer commit das mudanças: `git add . && git commit -m "refactor: reorganizar projeto em estrutura modular"`
2. Atualizar documentação de onboarding para novos desenvolvedores
3. Considerar adicionar CI/CD para executar testes automaticamente
4. Explorar integração com outros frameworks de agentes além do Agno

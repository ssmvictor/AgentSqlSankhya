"""Script de teste para validar o sistema de indexacao Sankhya."""

import sys

from config.settings import get_schema_path


def test_basic() -> bool:
    """Executa uma bateria de testes rapidos no indexador e otimizador."""

    print("=" * 60)
    print("[INFO] TESTE DO SISTEMA DE INDEXACAO SANKHYA")
    print("=" * 60)

    try:
        print("\n[1] Testando importacao dos modulos...")
        from src.schema_indexer import SchemaIndexer
        print("   OK. src.schema_indexer importado com sucesso")

        from src.schema_optimizer import SchemaOptimizer
        print("   OK. src.schema_optimizer importado com sucesso")

    except ImportError as exc:
        print(f"   ERRO ao importar: {exc}")
        print("\n   ATENCAO: Certifique-se de que os arquivos estao em:")
        print("      - src/schema_indexer.py")
        print("      - src.schema_optimizer.py")
        print("      - sankhya_schema.md (raiz, fallback ate ser movido para config/)")
        return False

    try:
        print("\n[2] Verificando arquivo sankhya_schema.md...")
        try:
            schema_path = get_schema_path()
            print(f"   OK. Arquivo encontrado em {schema_path}")
        except FileNotFoundError:
            print("   ERRO: Arquivo nao encontrado!")
            print("   Coloque sankhya_schema.md em config (preferencial) ou na raiz.")
            return False

        print("\n[3] Inicializando indexador...")
        indexer = SchemaIndexer()
        print("   OK. Indexador criado com sucesso")

        print("\n[4] Estatisticas do schema:")
        stats = indexer.get_estatisticas()
        print(f"   - Total de tabelas: {stats['total_tabelas']}")
        print(f"   - Total de campos: {stats['total_campos']}")
        print(f"   - Campos com opcoes: {stats['campos_com_opcoes']}")

        print("\n[5] Testando busca da tabela TGFCAB...")
        tabela = indexer.buscar_tabela("TGFCAB")
        if tabela:
            print(f"   OK. Tabela encontrada: {tabela.descricao}")
            print(f"   - Numero de campos: {len(tabela.campos)}")
        else:
            print("   AVISO: Tabela TGFCAB nao encontrada")

        print("\n[6] Testando otimizador...")
        optimizer = SchemaOptimizer(indexer)
        query_teste = "pedidos de venda em aberto"
        resultado = optimizer.otimizar_para_query(query_teste, estrategia="minimal")

        print(f"   - Query: '{query_teste}'")
        print("   OK. Contexto gerado com sucesso")
        print(f"   - Tokens estimados: {resultado['tokens_estimados']}")
        print(f"   - Tabelas incluidas: {', '.join(resultado['tabelas_incluidas'])}")

        print("\n[7] Verificando cache...")
        cache_dir = indexer.cache_dir
        if cache_dir.exists():
            print(f"   OK. Diretorio de cache localizado em {cache_dir}")
            for file_name in sorted(cache_dir.iterdir()):
                print(f"      - {file_name.name}")
        else:
            print("   AVISO: Cache sera criado na primeira execucao")

        print("\n" + "=" * 60)
        print("SUCESSO! TODOS OS TESTES PASSARAM.")
        print("=" * 60)

        print("\nProximos passos:")
        print("1. Instale o tiktoken para contagem precisa de tokens:")
        print("   pip install tiktoken")
        print("\n2. Execute o indexador completo com a nova estrutura de pacotes:")
        print("   python -m src.schema_indexer")
        print("\n3. Execute o otimizador completo:")
        print("   python -m src.schema_optimizer")

        return True

    except Exception as exc:
        print(f"\nERRO durante os testes: {exc}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_basic()
    sys.exit(0 if success else 1)

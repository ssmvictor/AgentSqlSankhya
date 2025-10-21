#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste simples para verificar se o SchemaIndexer está funcionando corretamente
sem depender da API de IA.
"""

from config.settings import get_schema_path
from src.schema_indexer import SchemaIndexer

def test_schema_indexer():
    """Testa o SchemaIndexer"""
    print("Testando SchemaIndexer...")
    
    try:
        # Inicializar o indexador
        indexer = SchemaIndexer(get_schema_path())
        
        print(f"[OK] Indexador criado com sucesso")
        print(f"[OK] Tabelas carregadas: {len(indexer.tabelas)}")
        print(f"[OK] Campos indexados: {len(indexer.indice_campos)}")
        
        # Testar busca de uma tabela conhecida
        tabela = indexer.buscar_tabela("TGFCAB")
        if tabela:
            print(f"[OK] Tabela TGFCAB encontrada: {tabela.descricao}")
            print(f"  Campos: {len(tabela.campos)}")
        else:
            print("[AVISO] Tabela TGFCAB não encontrada")
        
        # Testar busca de campo
        resultados = indexer.buscar_campo("NUNOTA")
        if resultados:
            print(f"[OK] Campo NUNOTA encontrado em {len(resultados)} tabela(s)")
            for r in resultados[:2]:  # Mostrar os 2 primeiros
                print(f"  - {r['tabela']}: {r['campo_desc']}")
        else:
            print("[AVISO] Campo NUNOTA não encontrado")
        
        print("\n[OK] Teste do SchemaIndexer concluído com sucesso!")
        
    except Exception as e:
        print(f"✗ Erro no teste: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_schema_indexer()
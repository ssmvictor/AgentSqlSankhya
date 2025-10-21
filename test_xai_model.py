#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script de teste para verificar a configuração do modelo xAI
"""

import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

print("Verificando configurações do xAI...")
print(f"XAI_API_KEY no ambiente: {os.getenv('XAI_API_KEY')}")
print(f"GROK_MODEL no ambiente: {os.getenv('GROK_MODEL', 'grok-4-fast-reasoning')}")

# Testar a importação e configuração do modelo
try:
    from agno.models.xai import xAI
    
    print("\nTentando criar instância do modelo xAI...")
    model = xAI(id=os.getenv('GROK_MODEL', 'grok-4-fast-reasoning'))
    
    print(f"Modelo criado com sucesso: {model}")
    print(f"ID do modelo: {model.id}")
    print(f"API Key (primeiros 10 chars): {getattr(model, 'api_key', 'N/A')[:10] if getattr(model, 'api_key', 'N/A') != 'N/A' else 'N/A'}")
    
except Exception as e:
    print(f"Erro ao criar modelo xAI: {e}")
    import traceback
    traceback.print_exc()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script de teste para verificar o funcionamento do agente com xAI
"""

import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.xai import xAI

# Carregar variáveis de ambiente
load_dotenv()

print("Verificando configurações do agente xAI...")
print(f"XAI_API_KEY no ambiente: {os.getenv('XAI_API_KEY')}")
print(f"GROK_MODEL no ambiente: {os.getenv('GROK_MODEL', 'grok-4-fast-reasoning')}")

try:
    print("\nTentando criar agente com modelo xAI...")
    agent = Agent(
        model=xAI(id=os.getenv('GROK_MODEL', 'grok-4-fast-reasoning')),
        markdown=True
    )
    
    print(f"Agente criado com sucesso: {agent}")
    print(f"Modelo do agente: {agent.model}")
    
    print("\nTentando obter resposta do agente...")
    # Vamos tentar uma chamada simples para ver se a API funciona
    response = agent.run("Responda com 'API funcionando' se você receber esta mensagem", max_tokens=20)
    print(f"Resposta: {response.content}")
    
except Exception as e:
    print(f"Erro ao usar o agente xAI: {e}")
    import traceback
    traceback.print_exc()
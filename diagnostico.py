#!/usr/bin/env python3
"""
Script de diagnóstico do Projeto Sombra Roxa
"""
import os
from dotenv import load_dotenv

load_dotenv()

print("=" * 50)
print("DIAGNÓSTICO DO SISTEMA - PROJETO SOMBRA ROXA")
print("=" * 50)

# 1. Verificar .env
print("\n📁 ARQUIVO .ENV:")
secret = os.getenv('SECRET_KEY')
openai_key = os.getenv('OPENAI_API_KEY')
model = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')

print(f"   SECRET_KEY: {'✓ Configurado' if secret else '✗ Não encontrado'}")
print(f"   OPENAI_API_KEY: {'✓ Configurado' if openai_key else '✗ Não encontrado'}")
print(f"   OPENAI_MODEL: {model}")

# 2. Verificar OpenAI
print("\n🤖 OPENAI:")
try:
    import openai
    openai.api_key = openai_key
    print(f"   Import: ✓ Sucesso")
    print(f"   API Key: {'✓ Configurada (' + openai_key[:15] + '...)' if openai.api_key else '✗ Não configurada'}")
    print(f"   Modo: {'OpenAI Real' if openai.api_key else 'IA Simulada'}")
except Exception as e:
    print(f"   Import: ✗ Erro - {e}")
    print(f"   Modo: IA Simulada (fallback)")

# 3. Verificar módulos do projeto
print("\n📦 MÓDULOS DO PROJETO:")
modulos = ['entidades', 'desafios', 'enigmas', 'simulated_ai']
for modulo in modulos:
    try:
        __import__(modulo)
        print(f"   {modulo}.py: ✓ OK")
    except Exception as e:
        print(f"   {modulo}.py: ✗ Erro - {e}")

# 4. Verificar estrutura de arquivos
print("\n📂 ESTRUTURA:")
arquivos_criticos = [
    'app.py',
    'entidades.py',
    'desafios.py',
    'enigmas.py',
    'simulated_ai.py',
    'templates/index.html',
    'templates/interview.html',
    'static/js/interview.js',
    'static/css/style.css'
]

for arquivo in arquivos_criticos:
    existe = os.path.exists(arquivo)
    print(f"   {arquivo}: {'✓' if existe else '✗'}")

print("\n" + "=" * 50)
print("✅ SISTEMA PRONTO!")
print("=" * 50)
print("\n🚀 Para iniciar o servidor:")
print("   python3 app.py")
print("\n🌐 Acesse:")
print("   http://127.0.0.1:5000")
print()

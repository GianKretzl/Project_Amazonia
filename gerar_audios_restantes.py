#!/usr/bin/env python3
"""
Gera os áudios restantes (Yakamu e Venturi)
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
import time

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

AUDIOS_RESTANTES = {
    'yakamu_intro.mp3': {
        'texto': '''Sou Pajé Yakamu, guardião da memória do meu povo. 
        O Rio Dourado já não é mais dourado... está roxo. 
        É a Sombra da Montanha de Fogo, como nossos ancestrais previram. 
        Homens gananciosos feriram a terra sagrada. 
        Gian foi o primeiro homem branco que quis proteger, não roubar. 
        Por isso, fizeram mal a ele. A verdade está na Trilha dos Ancestrais.''',
        'voz': 'onyx',
        'velocidade': 0.85
    },
    
    'venturi_confissao.mp3': {
        'texto': '''Gian Kretzl... ele era bom. Quase tão bom quanto eu. 
        Achou que ia salvar o mundo com uma manchete de jornal. 
        Você sabe quanto vale Coltan de pureza noventa e nove vírgula oito por cento? 
        Não para celulares... para ARMAS. 
        A Amazônia não é o pulmão do mundo. É a BATERIA do mundo. 
        E eu sou o dono dessa bateria. 
        Gian se tornou um risco à segurança nacional. 
        Decisões difíceis, jovem. Você ainda não entende como o poder REAL funciona.''',
        'voz': 'fable',
        'velocidade': 0.9
    }
}

for arquivo, config in AUDIOS_RESTANTES.items():
    print(f"🎙️ Gerando {arquivo}...")
    
    try:
        response = client.audio.speech.create(
            model="tts-1",  # Modelo normal (mais rápido)
            voice=config['voz'],
            input=config['texto'],
            speed=config['velocidade']
        )
        
        caminho = f"static/audio/{arquivo}"
        response.stream_to_file(caminho)
        
        tamanho = os.path.getsize(caminho)
        print(f"✅ {arquivo} gerado! ({tamanho:,} bytes)\n")
        
        # Aguardar 2 segundos entre requisições
        if list(AUDIOS_RESTANTES.keys()).index(arquivo) < len(AUDIOS_RESTANTES) - 1:
            print("⏳ Aguardando 2 segundos...")
            time.sleep(2)
        
    except Exception as e:
        print(f"❌ Erro: {e}\n")

print("✅ Concluído!")

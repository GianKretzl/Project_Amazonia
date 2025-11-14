#!/usr/bin/env python3
"""
Gera os áudios de introdução que faltam: Podcaster e Coronel
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
import time

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

AUDIOS_FALTANTES = {
    'falcao_intro.mp3': {
        'texto': '''E aí, pessoal! Aqui é o Jonas "Falcão" Pereira, do podcast Verdades Ocultas! 
        Vocês não vão acreditar no que eu descobri sobre essa tal "Sombra Roxa"! 
        Esqueçam essa história de poluição química... 
        Isso é MUITO maior! Estamos falando de Ratanabá, a cidade perdida da Amazônia! 
        Pirâmides, tecnologia ancestral, portais dimensionais! 
        O governo está escondendo TUDO de vocês! 
        Gian Kretzl estava PERTO da verdade antes de sumir... ou será que ele descobriu o portal?''',
        'voz': 'nova',  # Voz animada, enérgica
        'velocidade': 1.1  # Mais rápido, empolgado
    },
    
    'coronel_intro.mp3': {
        'texto': '''Coronel Silva, Chefe de Segurança da Fazenda Nova Fronteira. 
        Ex-militar, operações especiais. 
        Estou aqui a serviço do Deputado Venturi. 
        Vejo que você tem perguntas sobre Gian Kretzl. 
        Eu posso esclarecer alguns... pontos. 
        Mas entenda: segurança nacional não é brincadeira. 
        Às vezes, decisões difíceis precisam ser tomadas. 
        O que você quer saber, exatamente?''',
        'voz': 'onyx',  # Voz séria, autoritária
        'velocidade': 0.9  # Mais devagar, calculado
    }
}

for arquivo, config in AUDIOS_FALTANTES.items():
    print(f"🎙️ Gerando {arquivo}...")
    
    try:
        response = client.audio.speech.create(
            model="tts-1",
            voice=config['voz'],
            input=config['texto'],
            speed=config['velocidade']
        )
        
        caminho = f"static/audio/{arquivo}"
        response.stream_to_file(caminho)
        
        tamanho = os.path.getsize(caminho)
        print(f"✅ {arquivo} gerado! ({tamanho:,} bytes)\n")
        
        # Aguardar 2 segundos entre requisições
        if list(AUDIOS_FALTANTES.keys()).index(arquivo) < len(AUDIOS_FALTANTES) - 1:
            print("⏳ Aguardando 2 segundos...")
            time.sleep(2)
        
    except Exception as e:
        print(f"❌ Erro: {e}\n")

print("✅ Concluído!")
print("\n📊 Verificando todos os áudios de personagens:")
print("=" * 50)

audios_personagens = [
    'arnaldo_intro.mp3',
    'valdemar_intro.mp3', 
    'yakamu_intro.mp3',
    'falcao_intro.mp3',
    'coronel_intro.mp3',
    'venturi_confissao.mp3'
]

for audio in audios_personagens:
    caminho = f"static/audio/{audio}"
    if os.path.exists(caminho):
        tamanho = os.path.getsize(caminho)
        print(f"✅ {audio} - {tamanho:,} bytes")
    else:
        print(f"❌ {audio} - NÃO ENCONTRADO")

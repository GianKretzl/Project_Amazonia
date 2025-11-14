#!/usr/bin/env python3
"""
Gera áudios de introdução para os personagens do jogo
usando OpenAI TTS (Text-to-Speech)
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Inicializar cliente OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Textos de introdução por personagem
INTRODUCOES = {
    'arnaldo_intro.mp3': {
        'texto': '''Olá... sou Dr. Arnaldo Silva, biólogo do INPA. 
        Eu trabalhava com Gian Kretzl estudando a fauna do Rio Dourado quando... 
        detectamos algo impossível. Uma mancha roxa brilhante, visível do espaço. 
        Gian ficou obcecado com isso, batizou de "Sombra Roxa". 
        Depois ele foi investigar uma fazenda suspeita rio acima e... desapareceu. 
        Estou recebendo ameaças para parar a pesquisa, mas preciso que alguém saiba a verdade.''',
        'voz': 'onyx',  # Voz masculina, séria
        'velocidade': 1.0
    },
    
    'valdemar_intro.mp3': {
        'texto': '''Ô rapaz, eu sou o Valdemar, dono da Fazenda Nova Fronteira. 
        Trabalho honesto, suor na testa, progresso! 
        Esse tal de Gian veio aqui me acusando de não sei o quê... 
        Falando de rio contaminado, de exploração... 
        Eu só quero desenvolver essa região, gerar emprego! 
        O Deputado Venturi entende isso. Ele sim é um visionário!''',
        'voz': 'echo',  # Voz masculina, mais rústica
        'velocidade': 0.95
    },
    
    'yakamu_intro.mp3': {
        'texto': '''Sou Pajé Yakamu, guardião da memória do meu povo. 
        O Rio Dourado já não é mais dourado... está roxo. 
        É a Sombra da Montanha de Fogo, como nossos ancestrais previram. 
        Homens gananciosos feriram a terra sagrada. 
        Gian foi o primeiro homem branco que quis proteger, não roubar. 
        Por isso, fizeram mal a ele. A verdade está na Trilha dos Ancestrais.''',
        'voz': 'onyx',  # Voz masculina, sábia
        'velocidade': 0.85  # Mais devagar, cadência sábia
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
        'voz': 'fable',  # Voz masculina, dramática
        'velocidade': 0.9
    }
}

def gerar_audio(arquivo, config):
    """Gera um arquivo de áudio usando OpenAI TTS"""
    print(f"🎙️ Gerando {arquivo}...")
    
    try:
        response = client.audio.speech.create(
            model="tts-1-hd",  # Modelo HD para melhor qualidade
            voice=config['voz'],
            input=config['texto'],
            speed=config['velocidade']
        )
        
        # Salvar arquivo
        caminho = f"static/audio/{arquivo}"
        response.stream_to_file(caminho)
        
        # Verificar tamanho
        tamanho = os.path.getsize(caminho)
        print(f"✅ {arquivo} gerado! ({tamanho:,} bytes)")
        
    except Exception as e:
        print(f"❌ Erro ao gerar {arquivo}: {e}")

def main():
    print("=" * 60)
    print("🎬 GERANDO ÁUDIOS DE INTRODUÇÃO DOS PERSONAGENS")
    print("=" * 60)
    print()
    
    # Verificar se pasta existe
    if not os.path.exists('static/audio'):
        os.makedirs('static/audio')
        print("📁 Pasta static/audio criada")
    
    # Gerar cada áudio
    for arquivo, config in INTRODUCOES.items():
        gerar_audio(arquivo, config)
        print()
    
    print("=" * 60)
    print("🎉 PROCESSO CONCLUÍDO!")
    print("=" * 60)
    print()
    print("📊 Arquivos gerados:")
    for arquivo in INTRODUCOES.keys():
        caminho = f"static/audio/{arquivo}"
        if os.path.exists(caminho):
            tamanho = os.path.getsize(caminho)
            print(f"  ✅ {arquivo} - {tamanho:,} bytes")
        else:
            print(f"  ❌ {arquivo} - NÃO ENCONTRADO")

if __name__ == '__main__':
    main()

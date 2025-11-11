#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎬 GERADOR DE ÁUDIOS - PROJETO SOMBRA ROXA
Gera arquivos de áudio MP3 em português usando OpenAI TTS (Text-to-Speech)
VOZES REALISTAS E NATURAIS - Sem robótica!
"""

import os
import sys
from pathlib import Path

# Carregar variáveis de ambiente do arquivo .env
try:
    from dotenv import load_dotenv
    load_dotenv()
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False

# Verificar se OpenAI está instalado
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("⚠️  OpenAI não instalado. Execute: pip install openai")

# Carregar chave da API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Criar diretório de áudios se não existir
AUDIO_DIR = "static/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

# Vozes OpenAI TTS disponíveis:
# - alloy: Voz neutra e equilibrada
# - echo: Voz masculina e clara
# - fable: Voz expressiva e dramática
# - onyx: Voz masculina grave e autoritária
# - nova: Voz feminina jovem e energética
# - shimmer: Voz feminina suave e calorosa

# Scripts dos áudios - VERSÃO REALISTA COM VOZES DIFERENTES
SCRIPTS = {
    "final_entry": {
        "filename": "final_entry.mp3",
        "voice": "echo",  # Voz masculina clara para Gian (repórter)
        "speed": 0.9,  # Mais lento para dramaticidade
        "text": """Eu estava errado. Completamente errado.

Achei que descobriria uma história sobre crimes ambientais, mas isso é muito, muito maior.

A Sombra Roxa não é apenas poluição. É o rastro de algo que está sendo extraído das profundezas da terra.

Coltan. O mineral mais valioso do mundo. O que move toda a tecnologia moderna. E está aqui, escondido sob a Amazônia.

O fazendeiro, o cientista, até o pajé, todos sabem de algo. Mas ninguém, NINGUÉM fala abertamente. Eles têm medo.

Venturi. Esse nome aparece em tudo que investigo. Deputado. Empresário. Controlador da região. Ele é a chave.

Se você está ouvindo isso, é porque eu não consegui sair daqui. Eles me encontraram.

Por favor, encontre as pistas. Complete o que comecei. Descubra a verdade sobre a Sombra Roxa antes que seja tarde demais.

Meu nome é Gian Kretzl. Repórter investigativo. E essa pode ser minha última investigação."""
    },
    
    "arnaldo_intro": {
        "filename": "arnaldo_intro.mp3",
        "voice": "alloy",  # Voz neutra e profissional para cientista
        "speed": 1.0,
        "text": """Olá. Você deve ser o investigador que anda fazendo perguntas por aqui.

Meu nome é Doutor Arnaldo Ferreira. Sou químico ambiental há mais de vinte anos.

Há anos monitoro os rios desta região. E posso afirmar: há uma anomalia química gravíssima acontecendo.

A Sombra Roxa não é apenas poluição comum. É algo muito mais específico. Um resíduo do processamento de um mineral extremamente raro. Coltan.

Eu tentei alertar as autoridades. Mas ninguém quis ouvir. Ou melhor, alguém não quis que ouvissem.

Se quer respostas, faça as perguntas certas. Mas cuidado. Há gente muito poderosa vigiando cada movimento nesta região.

E não confie em políticos. Especialmente não confie em Venturi."""
    },
    
    "valdemar_intro": {
        "filename": "valdemar_intro.mp3",
        "voice": "onyx",  # Voz grave e autoritária para fazendeiro agressivo
        "speed": 1.1,  # Mais rápido para tom nervoso/defensivo
        "text": """Fazenda Nova Fronteira. Soja e gado. Tudo legal, tudo certificado pelo IBAMA.

Essas acusações contra mim são pura difamação! Vocês jornalistas só querem destruir o agronegócio brasileiro!

Eu sou um trabalhador honesto! Gero empregos, produzo alimentos!

A Sombra Roxa? Isso é problema dos garimpos ilegais lá no rio! Não tem NADA a ver com minha propriedade!

Agora, se me dá licença, tenho trabalho a fazer. E sugiro que você também vá cuidar da sua vida, antes que se meta em problemas sérios.

Por aqui, a gente não gosta de gente bisbilhoteira."""
    },
    
    "yakamu_intro": {
        "filename": "yakamu_intro.mp3",
        "voice": "fable",  # Voz expressiva e sábia para o pajé ancião
        "speed": 0.95,  # Levemente mais lento para sabedoria ancestral
        "text": """O rio chorava lágrimas roxas. 

Nossos avós nadavam nessas águas. Pescavam pirarucus grandes como canoas. Agora, até o gado se recusa a beber.

A Montanha de Fogo sempre foi sagrada para nosso povo. Ela guarda segredos ancestrais.

Mas vocês, homens brancos, chamam de progresso. Vocês arrancam as pedras brilhantes da montanha e deixam a morte escorrer no rio.

Meus jovens guerreiros estão com raiva. Eles querem lutar. Mas eu sou velho. Vi muitas batalhas. Sei que algumas guerras não se vencem com lanças.

O homem de terno que vem aqui, Venturi, ele promete coisas. Mas suas promessas são como fumaça. Desaparecem no vento.

Se você quer encontrar a verdade, precisa seguir o caminho dos ancestrais. O mapa está na terra. Nas pedras. Na história que o rio conta."""
    },
    
    "venturi_confissao": {
        "filename": "venturi_confissao.mp3",
        "voice": "onyx",  # Voz grave e autoritária para vilão arrogante
        "speed": 1.0,
        "text": """Parabéns. Você conseguiu chegar até aqui. Impressionante.

Gian também chegou. Ele era bom. Muito bom. Quase tão bom quanto eu.

Sabe o que é engraçado? Ele achou que eu queria o coltan para vender. Para ficar rico. Que tolo.

Eu JÁ sou rico. O que eu quero é PODER. Controle.

Quem controla essa montanha, controla o coltan. Quem controla o coltan, controla a tecnologia do mundo inteiro.

A Amazônia não é o pulmão do mundo, meu jovem. A Amazônia é a BATERIA do mundo.

E eu sou o dono da bateria.

Todos esses hippies ambientalistas chorando pelas árvores, eles nem imaginam o que realmente está em jogo aqui.

Enquanto eles abraçam árvores, eu controlo o futuro da humanidade.

Você acha que pode me parar? Com suas pistinhas? Com seu dossiê?

Vá em frente. Tente. Mas lembre-se: eu tenho juízes, policiais, políticos, empresários. Eu tenho todos no bolso.

E você? Você tem o quê exatamente?"""
    }
}

def limpar_audios_antigos():
    """Remove todos os arquivos MP3 antigos do diretório de áudio"""
    if not os.path.exists(AUDIO_DIR):
        return 0
    
    arquivos_removidos = 0
    for arquivo in os.listdir(AUDIO_DIR):
        if arquivo.endswith('.mp3'):
            filepath = os.path.join(AUDIO_DIR, arquivo)
            try:
                os.remove(filepath)
                print(f"🗑️  Removido: {arquivo}")
                arquivos_removidos += 1
            except Exception as e:
                print(f"⚠️  Erro ao remover {arquivo}: {e}")
    
    return arquivos_removidos

def gerar_audio(script_name, script_info, client):
    """Gera um arquivo de áudio usando OpenAI TTS"""
    try:
        print(f"🎙️  Gerando {script_name} com voz '{script_info['voice']}'...")
        
        # Criar áudio com OpenAI TTS
        response = client.audio.speech.create(
            model="tts-1-hd",  # Modelo HD para melhor qualidade
            voice=script_info["voice"],
            input=script_info["text"],
            speed=script_info.get("speed", 1.0)
        )
        
        # Salvar arquivo
        filepath = os.path.join(AUDIO_DIR, script_info["filename"])
        response.stream_to_file(filepath)
        
        print(f"✅ {script_name} salvo em: {filepath}")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao gerar {script_name}: {str(e)}")
        return False

def main():
    """Função principal"""
    print("=" * 60)
    print("🎬 GERADOR DE ÁUDIOS - PROJETO SOMBRA ROXA")
    print("=" * 60)
    print()
    
    if not OPENAI_AVAILABLE:
        print("❌ Erro: OpenAI não está instalado!")
        print("   Execute: pip install openai python-dotenv")
        sys.exit(1)
    
    if not OPENAI_API_KEY:
        print("❌ Erro: Chave da API OpenAI não configurada!")
        print()
        print("📝 Siga estes passos:")
        print("1. Obtenha sua chave em: https://platform.openai.com/api-keys")
        print("2. Crie um arquivo .env na raiz do projeto")
        print("3. Adicione a linha: OPENAI_API_KEY=sua-chave-aqui")
        print()
        print("� Veja o arquivo OPENAI_SETUP.md para mais detalhes")
        sys.exit(1)
    
    # Limpar áudios antigos
    print("🧹 Limpando áudios antigos...")
    removidos = limpar_audios_antigos()
    if removidos > 0:
        print(f"✅ {removidos} arquivo(s) antigo(s) removido(s)\n")
    else:
        print("✅ Nenhum arquivo antigo encontrado\n")
    
    # Inicializar cliente OpenAI
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    print("🔑 API Key configurada!")
    print("📋 Modelo: tts-1-hd (Alta Qualidade)")
    print()
    print("🎭 Vozes por personagem:")
    print("   • Gian Kretzl: 'echo' - masculina clara")
    print("   • Dr. Arnaldo: 'alloy' - neutra profissional")
    print("   • Valdemar: 'onyx' - grave autoritária")
    print("   • Pajé Yakamu: 'fable' - expressiva e sábia")
    print("   • Deputado Venturi: 'onyx' - grave arrogante")
    print()
    print("=" * 60)
    print()
    
    # Gerar todos os áudios
    sucessos = 0
    total = len(SCRIPTS)
    
    for script_name, script_info in SCRIPTS.items():
        if gerar_audio(script_name, script_info, client):
            sucessos += 1
        print()
    
    # Resultado final
    print("=" * 60)
    print(f"✨ Concluído! {sucessos}/{total} áudios gerados")
    print(f"📁 Localização: {os.path.abspath(AUDIO_DIR)}")
    print("=" * 60)
    print()
    print("💡 Áudios com OpenAI TTS - Vozes REALISTAS!")
    print("🎧 Teste em: http://localhost:5000/test-audio")
    print()
    print("💰 Custo estimado: ~$0.15 USD")
    print("=" * 60)

if __name__ == "__main__":
    main()

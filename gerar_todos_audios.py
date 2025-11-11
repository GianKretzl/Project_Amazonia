#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔊 GERADOR COMPLETO DE ÁUDIOS - PROJETO SOMBRA ROXA
Gera TODOS os áudios necessários usando apenas Python
- Narração: OpenAI TTS
- Efeitos Sonoros: Síntese de áudio com pydub + numpy
"""

import os
import sys
import numpy as np
from pathlib import Path

# Carregar variáveis de ambiente
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Verificar OpenAI
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

# Verificar pydub para efeitos sonoros
try:
    from pydub import AudioSegment
    from pydub.generators import Sine, WhiteNoise, Square
    PYDUB_AVAILABLE = True
except ImportError:
    PYDUB_AVAILABLE = False
    print("⚠️  pydub não instalado. Execute: pip install pydub")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AUDIO_DIR = "static/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

# ============================================
# ÁUDIOS DE NARRAÇÃO (OpenAI TTS)
# ============================================

SCRIPTS_NARRACAO = {
    "final_entry": {
        "filename": "final_entry.mp3",
        "voice": "echo",
        "speed": 0.9,
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
        "voice": "alloy",
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
        "voice": "onyx",
        "speed": 1.1,
        "text": """Fazenda Nova Fronteira. Soja e gado. Tudo legal, tudo certificado pelo IBAMA.

Essas acusações contra mim são pura difamação! Vocês jornalistas só querem destruir o agronegócio brasileiro!

Eu sou um trabalhador honesto! Gero empregos, produzo alimentos!

A Sombra Roxa? Isso é problema dos garimpos ilegais lá no rio! Não tem NADA a ver com minha propriedade!

Agora, se me dá licença, tenho trabalho a fazer. E sugiro que você também vá cuidar da sua vida, antes que se meta em problemas sérios.

Por aqui, a gente não gosta de gente bisbilhoteira."""
    },
    
    "yakamu_intro": {
        "filename": "yakamu_intro.mp3",
        "voice": "fable",
        "speed": 0.95,
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
        "voice": "onyx",
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

# ============================================
# EFEITOS SONOROS (Síntese com pydub)
# ============================================

def criar_sino_conquista():
    """Cria som de sino/conquista para pista coletada"""
    # Frequências harmônicas de sino
    freq1 = Sine(800).to_audio_segment(duration=1000).fade_out(800)
    freq2 = Sine(1200).to_audio_segment(duration=800).fade_out(600)
    freq3 = Sine(1600).to_audio_segment(duration=600).fade_out(400)
    
    # Mixar frequências
    sino = freq1.overlay(freq2).overlay(freq3)
    
    # Reduzir volume e adicionar fade
    sino = sino - 10
    sino = sino.fade_in(50).fade_out(300)
    
    return sino

def criar_alerta_urgente():
    """Cria som de alerta para momentos críticos"""
    # Pulso grave
    pulso = Square(220).to_audio_segment(duration=200)
    silencio = AudioSegment.silent(duration=100)
    
    # Repetir 3 vezes
    alerta = pulso + silencio + pulso + silencio + pulso
    
    # Adicionar harmônico tenso
    harmonico = Sine(440).to_audio_segment(duration=len(alerta))
    alerta = alerta.overlay(harmonico - 15)
    
    # Fade out
    alerta = alerta.fade_out(500)
    
    return alerta

def criar_ruido_branco_curto():
    """Cria estática de rádio"""
    estatica = WhiteNoise().to_audio_segment(duration=3000)
    
    # Reduzir volume drasticamente
    estatica = estatica - 25
    
    # Adicionar fade in/out
    estatica = estatica.fade_in(200).fade_out(800)
    
    return estatica

def criar_tom_revelacao():
    """Cria crescendo dramático para revelação final"""
    # Começar com tom grave
    tom1 = Sine(220).to_audio_segment(duration=2000)
    tom2 = Sine(330).to_audio_segment(duration=2000)
    tom3 = Sine(440).to_audio_segment(duration=2000)
    tom4 = Sine(550).to_audio_segment(duration=2000)
    
    # Concatenar para crescendo
    crescendo = tom1 + tom2 + tom3 + tom4
    
    # Aplicar fade in progressivo
    crescendo = crescendo.fade_in(1000).fade_out(1000)
    
    # Aumentar volume progressivamente
    crescendo = crescendo.apply_gain_stereo(2, 6)
    
    return crescendo

def criar_floresta_ambiente():
    """Cria ambiente básico de floresta usando ruído filtrado"""
    # Usar ruído branco filtrado para simular ambiente
    base = WhiteNoise().to_audio_segment(duration=30000)
    
    # Reduzir volume muito
    base = base - 30
    
    # Aplicar fade suave para loop
    base = base.fade_in(2000).fade_out(2000)
    
    return base

# ============================================
# FUNÇÕES PRINCIPAIS
# ============================================

def gerar_narracao(script_name, script_info, client):
    """Gera áudio de narração com OpenAI TTS"""
    try:
        print(f"🎙️  Gerando {script_name} com voz '{script_info['voice']}'...")
        
        response = client.audio.speech.create(
            model="tts-1-hd",
            voice=script_info["voice"],
            input=script_info["text"],
            speed=script_info.get("speed", 1.0)
        )
        
        filepath = os.path.join(AUDIO_DIR, script_info["filename"])
        response.stream_to_file(filepath)
        
        print(f"✅ {script_name} salvo")
        return True
        
    except Exception as e:
        print(f"❌ Erro: {str(e)}")
        return False

def gerar_efeito_sonoro(nome, funcao_geradora):
    """Gera efeito sonoro usando pydub"""
    try:
        print(f"🔊 Gerando {nome}...")
        
        audio = funcao_geradora()
        filepath = os.path.join(AUDIO_DIR, nome)
        audio.export(filepath, format="mp3")
        
        print(f"✅ {nome} salvo")
        return True
        
    except Exception as e:
        print(f"❌ Erro: {str(e)}")
        return False

def limpar_audios_antigos():
    """Remove arquivos MP3 antigos"""
    if not os.path.exists(AUDIO_DIR):
        return 0
    
    removidos = 0
    for arquivo in os.listdir(AUDIO_DIR):
        if arquivo.endswith('.mp3'):
            try:
                os.remove(os.path.join(AUDIO_DIR, arquivo))
                print(f"🗑️  Removido: {arquivo}")
                removidos += 1
            except:
                pass
    
    return removidos

def main():
    print("=" * 70)
    print("🎬 GERADOR COMPLETO DE ÁUDIOS - PROJETO SOMBRA ROXA")
    print("=" * 70)
    print()
    
    # Verificar dependências
    if not OPENAI_AVAILABLE:
        print("❌ OpenAI não instalado: pip install openai")
        sys.exit(1)
    
    if not OPENAI_API_KEY:
        print("❌ OPENAI_API_KEY não configurada no .env")
        sys.exit(1)
    
    if not PYDUB_AVAILABLE:
        print("⚠️  pydub não instalado - efeitos sonoros não serão gerados")
        print("   Para instalar: pip install pydub")
        print()
    
    # Limpar áudios antigos
    print("🧹 Limpando áudios antigos...")
    removidos = limpar_audios_antigos()
    if removidos > 0:
        print(f"✅ {removidos} arquivo(s) removido(s)\n")
    else:
        print("✅ Nenhum arquivo antigo\n")
    
    # Inicializar OpenAI
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    print("📋 GERANDO ÁUDIOS DE NARRAÇÃO (OpenAI TTS)")
    print("=" * 70)
    print()
    
    sucessos_narracao = 0
    for nome, info in SCRIPTS_NARRACAO.items():
        if gerar_narracao(nome, info, client):
            sucessos_narracao += 1
        print()
    
    # Gerar efeitos sonoros se pydub estiver disponível
    sucessos_efeitos = 0
    if PYDUB_AVAILABLE:
        print("=" * 70)
        print("📋 GERANDO EFEITOS SONOROS (Síntese Python)")
        print("=" * 70)
        print()
        
        efeitos = {
            "pista_coletada.mp3": criar_sino_conquista,
            "alerta_critico.mp3": criar_alerta_urgente,
            "estatica_radio.mp3": criar_ruido_branco_curto,
            "revelacao_final.mp3": criar_tom_revelacao,
            "ambiente_floresta.mp3": criar_floresta_ambiente
        }
        
        for nome, funcao in efeitos.items():
            if gerar_efeito_sonoro(nome, funcao):
                sucessos_efeitos += 1
            print()
    
    # Resultado final
    print("=" * 70)
    print(f"✨ CONCLUÍDO!")
    print("=" * 70)
    print()
    print(f"🎙️  Narração: {sucessos_narracao}/5 áudios gerados")
    if PYDUB_AVAILABLE:
        print(f"🔊 Efeitos: {sucessos_efeitos}/5 áudios gerados")
    else:
        print(f"⚠️  Efeitos: Não gerados (instale pydub)")
    print()
    print(f"📁 Localização: {os.path.abspath(AUDIO_DIR)}")
    print()
    print("🎧 Teste em: http://localhost:5000/test-audio")
    print()
    print("💰 Custo OpenAI: ~$0.15 USD")
    print("🆓 Efeitos sonoros: Gratuito (gerados localmente)")
    print("=" * 70)

if __name__ == "__main__":
    main()

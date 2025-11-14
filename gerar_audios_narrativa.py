"""
Script para gerar todos os áudios necessários para o Projeto Encruzilhada
Usa ElevenLabs API para gerar vozes realistas
"""

import os
import requests
from pathlib import Path

# Configurar sua chave da API ElevenLabs
# Obtenha em: https://elevenlabs.io/
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "")

# IDs de vozes (você pode escolher outras em: https://elevenlabs.io/voice-library)
VOZES = {
    "gian": "21m00Tcm4TlvDq8ikWAM",  # Voz masculina madura (Josh)
    "arnaldo": "AZnzlk1XvdvUeBnXmlld",  # Voz masculina nervosa (Domi)
    "valdemar": "TxGEqnHWrfWFTfGW9XjX",  # Voz masculina grave (Josh)
    "pajé": "pNInz6obpgDQGcFmaJgB",  # Voz masculina calma (Adam)
    "falcao": "yoZ06aMxZJJ28mfd3POQ",  # Voz masculina energética (Sam)
    "coronel": "VR6AewLTigWG4xSOukaG",  # Voz masculina séria (Arnold)
    "venturi": "ODq5zmih8GrVes37Dizd",  # Voz masculina suave/calculista (Patrick)
}

# Diretório de saída
OUTPUT_DIR = Path("static/audio")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Textos para gerar
AUDIOS = {
    # PRÓLOGO - A última transmissão de Gian
    "FINAL_ENTRY.wav": {
        "voz": "gian",
        "texto": """
        [Sussurrando, ofegante, com medo]
        
        Eu... eu estava errado. Não é só desmatamento. 
        
        A Fazenda Nova Fronteira é um... um portão.
        
        [Som de galho quebrando ao fundo - pausa nervosa]
        
        O Dr. Arnaldo estava certo sobre o rio... a 'Sombra Roxa'...
        
        [Mais urgente]
        
        O Pajé tentou me avisar. A 'Trilha' é o mapa. Eles sabem que eu sei.
        
        [Voz apressada, quase em pânico]
        
        Eles estão vindo. Se alguém achar isso... o sistema está online. 
        As personas... elas sabem. Conecte as...
        
        [CORTE ABRUPTO - estática]
        """,
        "stability": 0.3,  # Mais instável/nervoso
        "similarity_boost": 0.7
    },
    
    # Sons ambiente não precisam de voz - usar geradores de som ou biblioteca
}

def gerar_audio_elevenlabs(texto, voz_id, output_file, stability=0.5, similarity_boost=0.75):
    """
    Gera áudio usando ElevenLabs API
    """
    if not ELEVENLABS_API_KEY:
        print("⚠️  ELEVENLABS_API_KEY não configurada!")
        print("   Defina a variável de ambiente ou edite o script.")
        return False
    
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voz_id}"
    
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVENLABS_API_KEY
    }
    
    data = {
        "text": texto.strip(),
        "model_id": "eleven_multilingual_v2",  # Suporta português
        "voice_settings": {
            "stability": stability,
            "similarity_boost": similarity_boost
        }
    }
    
    print(f"🎙️  Gerando: {output_file}...")
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        output_path = OUTPUT_DIR / output_file
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"✅ Gerado: {output_path}")
        return True
    else:
        print(f"❌ Erro ao gerar {output_file}: {response.status_code}")
        print(f"   {response.text}")
        return False

def gerar_sons_ambiente():
    """
    Sons ambiente podem ser gerados com bibliotecas Python ou baixados de bibliotecas livres
    """
    print("\n🎵 Sons Ambiente:")
    print("   Para sons ambiente (laboratório, fazenda, aldeia, etc.),")
    print("   recomendamos usar bibliotecas gratuitas como:")
    print("   - Freesound.org")
    print("   - Zapsplat.com")
    print("   - ou gerar com ferramentas como Audacity")
    print()
    print("   Sons necessários:")
    sons_necessarios = [
        "lab_ambiente.mp3 - Bipes de equipamentos, ventilação",
        "fazenda_ambiente.mp3 - Gado ao longe, trator, cigarras",
        "aldeia_ambiente.mp3 - Fogo crepitando, floresta noturna, sapos",
        "podcast_ambiente.mp3 - Música dramática de fundo",
        "seguranca_ambiente.mp3 - Rádio estático, passos pesados",
        "sala_situacao.mp3 - Tensão, silêncio pesado",
        "",
        "clue_collected.mp3 - Som de 'item coletado' (tipo RPG)",
        "enigma_unlocked.mp3 - Som de 'desbloqueio'",
        "character_unlocked.mp3 - Som de 'novo personagem'",
        "final_victory.mp3 - Som de 'missão cumprida'"
    ]
    for som in sons_necessarios:
        print(f"   • {som}")

def main():
    print("=" * 60)
    print("🎬 GERADOR DE ÁUDIOS - PROJETO ENCRUZILHADA")
    print("=" * 60)
    print()
    
    # Gerar áudio do prólogo
    for filename, config in AUDIOS.items():
        voz_id = VOZES.get(config["voz"])
        if voz_id:
            gerar_audio_elevenlabs(
                config["texto"],
                voz_id,
                filename,
                config.get("stability", 0.5),
                config.get("similarity_boost", 0.75)
            )
        else:
            print(f"⚠️  Voz '{config['voz']}' não encontrada para {filename}")
    
    # Instruções para sons ambiente
    gerar_sons_ambiente()
    
    print()
    print("=" * 60)
    print("✅ PROCESSO CONCLUÍDO!")
    print("=" * 60)
    print()
    print("📝 PRÓXIMOS PASSOS:")
    print("   1. Baixe os sons ambiente dos sites recomendados")
    print("   2. Coloque todos em static/audio/")
    print("   3. Teste os áudios no jogo")
    print()

if __name__ == "__main__":
    # Verificar se tem a chave da API
    if not ELEVENLABS_API_KEY:
        print("=" * 60)
        print("⚠️  CONFIGURAÇÃO NECESSÁRIA")
        print("=" * 60)
        print()
        print("Para gerar áudios com ElevenLabs:")
        print("1. Crie conta gratuita em: https://elevenlabs.io/")
        print("2. Obtenha sua API Key")
        print("3. Defina a variável de ambiente:")
        print("   export ELEVENLABS_API_KEY='sua_chave_aqui'")
        print()
        print("Ou edite este script e cole a chave diretamente.")
        print()
        print("=" * 60)
    else:
        main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎬 GERADOR COMPLETO DE ÁUDIOS - PROJETO SOMBRA ROXA
Gera TODOS os áudios necessários:
- Narrações: OpenAI TTS (voz realista)
- Efeitos Sonoros: Freesound.org (sons profissionais)
- Sons Ambiente: Freesound.org (loops de alta qualidade)
"""

import os
import sys
import requests
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
FREESOUND_API_KEY = os.getenv("FREESOUND_API_KEY")
AUDIO_DIR = Path("static/audio")
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

# ============================================
# NARRAÇÕES (OpenAI TTS)
# ============================================

NARRACOES = {
    "final_entry.mp3": {
        "voice": "echo",  # Voz masculina, dramática
        "speed": 0.9,
        "text": """Eu estava errado. Completamente errado.

Achei que descobriria uma história sobre crimes ambientais, mas isso é muito, muito maior.

A Sombra Roxa não é apenas poluição. É o rastro de algo que está sendo extraído das profundezas da terra.

Coltan. O mineral mais valioso do mundo. O que move toda a tecnologia moderna. E está aqui, escondido sob a Amazônia.

O fazendeiro, o cientista, até o pajé... todos sabem de algo. Mas ninguém, NINGUÉM fala abertamente. Eles têm medo.

Venturi. Esse nome aparece em tudo que investigo. Deputado. Empresário. Controlador da região. Ele é a chave.

Se você está ouvindo isso, é porque eu não consegui sair daqui. Eles me encontraram.

Por favor... encontre as pistas. Complete o que comecei. Descubra a verdade sobre a Sombra Roxa... antes que seja tarde demais."""
    }
}

# ============================================
# SONS AMBIENTE (Freesound.org - LOOPS)
# ============================================

SONS_AMBIENTE = {
    'lab_ambiente.mp3': {
        'id': 558842,
        'name': 'Laboratory Ambience',
        'descricao': 'Ambiente de laboratório com bipes e máquinas'
    },
    'fazenda_ambiente.mp3': {
        'id': 268903,  # ID alternativo - Rural ambience
        'name': 'Farm Rural Ambience',
        'descricao': 'Ambiente rural com animais'
    },
    'aldeia_ambiente.mp3': {
        'id': 449953,
        'name': 'Jungle Night Ambience',
        'descricao': 'Floresta noturna com insetos e fogo'
    },
    'podcast_ambiente.mp3': {
        'id': 527604,
        'name': 'Dramatic Background',
        'descricao': 'Música dramática de fundo'
    },
    'seguranca_ambiente.mp3': {
        'id': 341695,
        'name': 'Military Radio Ambience',
        'descricao': 'Rádio militar com estática'
    },
    'sala_situacao.mp3': {
        'id': 196372,  # ID alternativo - Office room tone
        'name': 'Office Room Tone',
        'descricao': 'Tom de sala de escritório'
    }
}

# ============================================
# EFEITOS SONOROS (Freesound.org - SEM LOOP)
# ============================================

EFEITOS_SONOROS = {
    'clue_collected.mp3': {
        'id': 274947,  # ID alternativo - Collect item
        'name': 'Collect Item Sound',
        'descricao': 'Som de item coletado'
    },
    'enigma_unlocked.mp3': {
        'id': 270303,
        'name': 'Unlock Achievement',
        'descricao': 'Som de desbloqueio'
    },
    'character_unlocked.mp3': {
        'id': 270333,  # ID alternativo - Success jingle
        'name': 'Success Jingle',
        'descricao': 'Jingle de sucesso para personagem'
    },
    'final_victory.mp3': {
        'id': 270402,  # ID alternativo - Epic victory
        'name': 'Epic Victory Sound',
        'descricao': 'Som épico de vitória'
    }
}

# ============================================
# FUNÇÕES
# ============================================

def gerar_narracao_openai(filename, config):
    """Gera narração usando OpenAI TTS"""
    if not OPENAI_API_KEY:
        print(f"❌ OPENAI_API_KEY não configurada!")
        return False
    
    try:
        from openai import OpenAI
        client = OpenAI(api_key=OPENAI_API_KEY)
        
        print(f"🎙️  Gerando {filename} com voz '{config['voice']}'...")
        
        response = client.audio.speech.create(
            model="tts-1-hd",
            voice=config["voice"],
            input=config["text"],
            speed=config.get("speed", 1.0)
        )
        
        filepath = AUDIO_DIR / filename
        response.stream_to_file(str(filepath))
        
        print(f"✅ {filename} gerado com sucesso!")
        return True
        
    except ImportError:
        print(f"❌ OpenAI não instalado. Execute: pip install openai")
        return False
    except Exception as e:
        print(f"❌ Erro ao gerar {filename}: {e}")
        return False

def baixar_freesound(filename, config):
    """Baixa som do Freesound.org"""
    if not FREESOUND_API_KEY:
        print(f"❌ FREESOUND_API_KEY não configurada!")
        print(f"   Configure em: https://freesound.org/apiv2/apply")
        return False
    
    try:
        sound_id = config['id']
        print(f"🔊 Baixando {filename}: {config['name']}...")
        
        # Buscar informações do som
        info_url = f"https://freesound.org/apiv2/sounds/{sound_id}/"
        headers = {'Authorization': f'Token {FREESOUND_API_KEY}'}
        
        response = requests.get(info_url, headers=headers, timeout=30)
        response.raise_for_status()
        sound_data = response.json()
        
        # Obter URL de download (preview HQ)
        download_url = sound_data.get('previews', {}).get('preview-hq-mp3')
        
        if not download_url:
            print(f"⚠️  URL de download não encontrada para {filename}")
            return False
        
        # Baixar arquivo
        audio_response = requests.get(download_url, timeout=60)
        audio_response.raise_for_status()
        
        # Salvar
        filepath = AUDIO_DIR / filename
        with open(filepath, 'wb') as f:
            f.write(audio_response.content)
        
        size_kb = len(audio_response.content) / 1024
        print(f"✅ {filename} baixado! ({size_kb:.1f} KB)")
        print(f"   Autor: {sound_data.get('username', 'Desconhecido')}")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao baixar {filename}: {e}")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False

def verificar_apis():
    """Verifica se as APIs estão configuradas"""
    problemas = []
    
    if not OPENAI_API_KEY:
        problemas.append("❌ OPENAI_API_KEY não configurada")
    else:
        print("✅ OPENAI_API_KEY encontrada")
    
    if not FREESOUND_API_KEY:
        problemas.append("❌ FREESOUND_API_KEY não configurada")
    else:
        print("✅ FREESOUND_API_KEY encontrada")
    
    return problemas

def main():
    print("=" * 70)
    print("🎬 GERADOR COMPLETO DE ÁUDIOS - PROJETO SOMBRA ROXA")
    print("=" * 70)
    print()
    
    # Verificar APIs
    print("🔑 Verificando APIs...")
    problemas = verificar_apis()
    
    if problemas:
        print("\n" + "=" * 70)
        print("⚠️  CONFIGURAÇÃO NECESSÁRIA:")
        print("=" * 70)
        for problema in problemas:
            print(f"  {problema}")
        print()
        print("📝 Como configurar:")
        print("  1. Crie um arquivo .env na raiz do projeto")
        print("  2. Adicione as chaves:")
        print()
        print("     OPENAI_API_KEY=sk-...")
        print("     FREESOUND_API_KEY=...")
        print()
        print("  3. Execute novamente este script")
        print("=" * 70)
        sys.exit(1)
    
    print()
    
    # Limpar áudios antigos
    print("🧹 Limpando áudios antigos...")
    removidos = 0
    for arquivo in AUDIO_DIR.glob("*.mp3"):
        arquivo.unlink()
        removidos += 1
    
    if removidos > 0:
        print(f"✅ {removidos} arquivo(s) removido(s)")
    else:
        print("✅ Nenhum arquivo antigo")
    
    print()
    print("=" * 70)
    print("📋 FASE 1: NARRAÇÕES (OpenAI TTS)")
    print("=" * 70)
    print()
    
    narracoes_ok = 0
    narracoes_total = len(NARRACOES)
    
    for filename, config in NARRACOES.items():
        if gerar_narracao_openai(filename, config):
            narracoes_ok += 1
        print()
    
    print("=" * 70)
    print("📋 FASE 2: SONS AMBIENTE (Freesound.org)")
    print("=" * 70)
    print()
    
    ambiente_ok = 0
    ambiente_total = len(SONS_AMBIENTE)
    
    for filename, config in SONS_AMBIENTE.items():
        if baixar_freesound(filename, config):
            ambiente_ok += 1
        print()
    
    print("=" * 70)
    print("📋 FASE 3: EFEITOS SONOROS (Freesound.org)")
    print("=" * 70)
    print()
    
    efeitos_ok = 0
    efeitos_total = len(EFEITOS_SONOROS)
    
    for filename, config in EFEITOS_SONOROS.items():
        if baixar_freesound(filename, config):
            efeitos_ok += 1
        print()
    
    # Resumo final
    print("=" * 70)
    print("✨ RESUMO FINAL")
    print("=" * 70)
    print()
    print(f"🎙️  Narrações: {narracoes_ok}/{narracoes_total} geradas")
    print(f"🌳 Sons Ambiente: {ambiente_ok}/{ambiente_total} baixados")
    print(f"🔊 Efeitos Sonoros: {efeitos_ok}/{efeitos_total} baixados")
    print()
    
    total_ok = narracoes_ok + ambiente_ok + efeitos_ok
    total_arquivos = narracoes_total + ambiente_total + efeitos_total
    
    print(f"📊 Total: {total_ok}/{total_arquivos} áudios prontos")
    print(f"📁 Pasta: {AUDIO_DIR.absolute()}")
    print()
    
    if total_ok == total_arquivos:
        print("🎉 SUCESSO! Todos os áudios foram gerados!")
        print()
        print("🎮 Próximos passos:")
        print("  1. Reinicie o servidor Flask (Ctrl+C e python app.py)")
        print("  2. Recarregue a página no navegador (F5)")
        print("  3. Os áudios serão carregados automaticamente")
    else:
        print("⚠️  Alguns áudios falharam. Verifique os erros acima.")
    
    print("=" * 70)

if __name__ == "__main__":
    # Verificar dependências
    try:
        import requests
    except ImportError:
        print("❌ requests não instalado. Execute: pip install requests")
        sys.exit(1)
    
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("❌ python-dotenv não instalado. Execute: pip install python-dotenv")
        sys.exit(1)
    
    main()

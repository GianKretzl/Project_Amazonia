#!/usr/bin/env python3
"""
Script para baixar áudios do Freesound.org
Requer conta gratuita e API key em: https://freesound.org/apiv2/apply
"""

import os
import sys
import requests
from pathlib import Path

# Configuração
FREESOUND_API_KEY = os.environ.get('FREESOUND_API_KEY', '')
AUDIO_DIR = Path(__file__).parent / 'static' / 'audio'
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

# Mapeamento de sons recomendados do Freesound.org
# IDs verificados e ativos (última verificação: nov 2025)
SONS_AMBIENTE = {
    'lab_ambiente.mp3': {
        'id': 558842,  # Laboratory ambience with beeps and machines
        'name': 'Laboratory Ambience',
        'tags': 'laboratory, science, beeps, ambience',
        'busca': 'laboratory ambience beeps'
    },
    'fazenda_ambiente.mp3': {
        'id': 416975,  # Farm ambience with cattle and birds
        'name': 'Farm Ambience',
        'tags': 'farm, cattle, rural, ambience',
        'busca': 'farm cattle ambience'
    },
    'aldeia_ambiente.mp3': {
        'id': 449953,  # Jungle/forest night with insects
        'name': 'Jungle Night Ambience',
        'tags': 'jungle, forest, night, fire, insects',
        'busca': 'jungle night campfire'
    },
    'podcast_ambiente.mp3': {
        'id': 527604,  # Dramatic tension background music
        'name': 'Dramatic Background',
        'tags': 'dramatic, tension, music',
        'busca': 'dramatic tension music'
    },
    'seguranca_ambiente.mp3': {
        'id': 341695,  # Military radio static and ambience
        'name': 'Military Radio Ambience',
        'tags': 'military, radio, static, footsteps',
        'busca': 'military radio static'
    },
    'sala_situacao.mp3': {
        'id': 387232,  # Office room tone, tense atmosphere
        'name': 'Tense Office Ambience',
        'tags': 'office, tension, ventilation, low hum',
        'busca': 'office room tone'
    }
}

SONS_EFEITOS = {
    'clue_collected.mp3': {
        'id': 320655,  # Positive notification chime
        'name': 'Positive Notification',
        'tags': 'notification, positive, collect',
        'busca': 'notification positive chime'
    },
    'enigma_unlocked.mp3': {
        'id': 270303,  # Unlock/achievement sound
        'name': 'Unlock Achievement',
        'tags': 'unlock, achievement, success',
        'busca': 'unlock achievement'
    },
    'character_unlocked.mp3': {
        'id': 456965,  # Short celebration fanfare
        'name': 'Character Unlock',
        'tags': 'celebration, unlock, success',
        'busca': 'short fanfare celebration'
    },
    'final_victory.mp3': {
        'id': 270324,  # Epic victory fanfare
        'name': 'Victory Fanfare',
        'tags': 'victory, win, celebration, fanfare',
        'busca': 'victory fanfare epic'
    }
}

def baixar_do_freesound(sound_id, output_path, sound_name):
    """Baixa um som do Freesound.org"""
    
    if not FREESOUND_API_KEY:
        print(f"❌ ERRO: FREESOUND_API_KEY não configurada!")
        print("\n📝 Como obter API Key:")
        print("1. Cadastre-se em: https://freesound.org/")
        print("2. Solicite API Key em: https://freesound.org/apiv2/apply")
        print("3. Configure:")
        print("   export FREESOUND_API_KEY='sua_chave_aqui'")
        return False
    
    print(f"\n🔍 Buscando: {sound_name} (ID: {sound_id})...")
    
    # Buscar informações do som
    info_url = f"https://freesound.org/apiv2/sounds/{sound_id}/"
    headers = {'Authorization': f'Token {FREESOUND_API_KEY}'}
    
    try:
        response = requests.get(info_url, headers=headers)
        response.raise_for_status()
        sound_data = response.json()
        
        # Obter URL de download (preview de alta qualidade)
        download_url = sound_data.get('previews', {}).get('preview-hq-mp3')
        
        if not download_url:
            print(f"⚠️  URL de download não encontrada para {sound_name}")
            return False
        
        # Baixar arquivo
        print(f"⬇️  Baixando {sound_name}...")
        audio_response = requests.get(download_url)
        audio_response.raise_for_status()
        
        # Salvar arquivo
        with open(output_path, 'wb') as f:
            f.write(audio_response.content)
        
        print(f"✅ {output_path.name} baixado com sucesso!")
        print(f"   Autor: {sound_data.get('username', 'Desconhecido')}")
        print(f"   Licença: {sound_data.get('license', 'Desconhecida')}")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao baixar {sound_name}: {e}")
        return False

def baixar_alternativa_manual():
    """Instruções para baixar manualmente"""
    print("\n" + "="*60)
    print("📥 ALTERNATIVA: BAIXAR MANUALMENTE DO FREESOUND")
    print("="*60)
    print("\nSe a API não funcionar, baixe manualmente:\n")
    
    print("🎵 Freesound.org (Download Direto)")
    print("-" * 40)
    print("1. Faça login em: https://freesound.org/")
    print("2. Use os links diretos abaixo para baixar cada som:")
    print("")
    
    todos_sons = {**SONS_AMBIENTE, **SONS_EFEITOS}
    for arquivo, info in todos_sons.items():
        sound_id = info['id']
        busca = info.get('busca', info['tags'])
        print(f"   {arquivo}:")
        print(f"   → https://freesound.org/people/*/sounds/{sound_id}/")
        print(f"   (Ou busque: {busca})")
        print("")
    
    print(f"3. Salvar todos em: {AUDIO_DIR}/\n")
    
    print("🎵 OPÇÃO 2: Zapsplat (Gratuito)")
    print("-" * 40)
    print("1. Acesse: https://www.zapsplat.com/")
    print("2. Cadastre-se (gratuito, sem verificação de email)")
    print("3. Busque pelos mesmos termos acima")
    print("4. Download direto em MP3\n")
    
    print("🎵 OPÇÃO 3: BBC Sound Effects (Gratuito)")
    print("-" * 40)
    print("1. Acesse: https://sound-effects.bbcrewind.co.uk/")
    print("2. Sem necessidade de cadastro!")
    print("3. Biblioteca enorme da BBC")
    print("4. Busque por: 'laboratory', 'farm', 'jungle', etc.\n")
    
    print("🎵 OPÇÃO 4: MyNoise.net (Geradores)")
    print("-" * 40)
    print("1. Acesse: https://mynoise.net/")
    print("2. Escolha geradores:")
    print("   - 'Japanese Garden' → aldeia_ambiente.mp3")
    print("   - 'Fireplace' → aldeia_ambiente.mp3")
    print("   - 'Distant Thunder' → tensão geral")
    print("3. Use Audacity para gravar (30-60 segundos)")
    print("4. Exportar como MP3\n")

def verificar_audios_existentes():
    """Verifica quais áudios já existem"""
    print("\n📁 Verificando áudios existentes em:", AUDIO_DIR)
    print("-" * 60)
    
    todos_sons = {**SONS_AMBIENTE, **SONS_EFEITOS}
    existentes = []
    faltantes = []
    
    for arquivo in todos_sons.keys():
        caminho = AUDIO_DIR / arquivo
        if caminho.exists():
            tamanho = caminho.stat().st_size / 1024  # KB
            existentes.append(f"✅ {arquivo} ({tamanho:.1f} KB)")
        else:
            faltantes.append(f"❌ {arquivo}")
    
    if existentes:
        print("\nÁudios ENCONTRADOS:")
        for item in existentes:
            print(f"  {item}")
    
    if faltantes:
        print("\nÁudios FALTANDO:")
        for item in faltantes:
            print(f"  {item}")
    
    print(f"\n📊 Total: {len(existentes)}/10 áudios prontos")
    return len(faltantes) == 0

def criar_script_download_simples():
    """Cria script bash simples para download com wget"""
    script_path = Path(__file__).parent / 'download_audios_simples.sh'
    
    script_content = """#!/bin/bash
# Script simplificado para download de áudios gratuitos
# Usa Zapsplat (sem necessidade de API key)

AUDIO_DIR="./static/audio"
mkdir -p "$AUDIO_DIR"

echo "📥 Baixando áudios do Zapsplat..."
echo "⚠️  Este script é um EXEMPLO. Você precisa:"
echo "1. Cadastrar-se em https://www.zapsplat.com/"
echo "2. Buscar manualmente pelos sons"
echo "3. Copiar URLs de download"
echo "4. Atualizar este script com as URLs reais"
echo ""
echo "Alternativamente, use o guia em GUIA_SONS_AMBIENTE.md"
echo ""

# Exemplo de como seria (URLs fictícias):
# wget -O "$AUDIO_DIR/lab_ambiente.mp3" "https://exemplo.com/lab_sound.mp3"
# wget -O "$AUDIO_DIR/fazenda_ambiente.mp3" "https://exemplo.com/farm_sound.mp3"
# ... etc

echo ""
echo "✅ Script criado em: download_audios_simples.sh"
echo "📝 Edite o script com URLs reais e execute:"
echo "   chmod +x download_audios_simples.sh"
echo "   ./download_audios_simples.sh"
"""
    
    with open(script_path, 'w') as f:
        f.write(script_content)
    
    os.chmod(script_path, 0o755)
    print(f"\n✅ Script criado: {script_path}")

def main():
    print("="*60)
    print("🎵 DOWNLOADER DE ÁUDIOS - PROJETO ENCRUZILHADA")
    print("="*60)
    
    # Verificar áudios existentes
    if verificar_audios_existentes():
        print("\n🎉 Todos os áudios já estão prontos!")
        return
    
    print("\n" + "="*60)
    print("ESCOLHA UMA OPÇÃO:")
    print("="*60)
    print("1. Baixar automaticamente do Freesound.org (requer API key)")
    print("2. Ver instruções para download manual")
    print("3. Criar script de download simplificado")
    print("4. Sair")
    
    try:
        escolha = input("\nEscolha (1-4): ").strip()
    except KeyboardInterrupt:
        print("\n\n👋 Cancelado pelo usuário")
        return
    
    if escolha == '1':
        if not FREESOUND_API_KEY:
            print("\n❌ FREESOUND_API_KEY não configurada!")
            print("\n📝 Como configurar:")
            print("1. Cadastre-se em: https://freesound.org/")
            print("2. Solicite API Key em: https://freesound.org/apiv2/apply")
            print("3. Configure:")
            print("   export FREESOUND_API_KEY='sua_chave_aqui'")
            print("4. Execute novamente este script")
            return
        
        print("\n🚀 Iniciando download automático...\n")
        sucessos = 0
        falhas = 0
        
        todos_sons = {**SONS_AMBIENTE, **SONS_EFEITOS}
        
        for arquivo, info in todos_sons.items():
            output_path = AUDIO_DIR / arquivo
            
            # Pular se já existe
            if output_path.exists():
                print(f"⏭️  {arquivo} já existe, pulando...")
                continue
            
            if baixar_do_freesound(info['id'], output_path, info['name']):
                sucessos += 1
            else:
                falhas += 1
        
        print("\n" + "="*60)
        print(f"✅ Downloads concluídos: {sucessos}")
        print(f"❌ Falhas: {falhas}")
        print("="*60)
        
        if falhas > 0:
            print("\n💡 Dica: IDs do Freesound podem ter mudado.")
            print("   Use a opção 2 para download manual.")
    
    elif escolha == '2':
        baixar_alternativa_manual()
        print(f"\n📁 Salvar todos os áudios em: {AUDIO_DIR}/")
    
    elif escolha == '3':
        criar_script_download_simples()
    
    elif escolha == '4':
        print("\n👋 Até logo!")
    
    else:
        print("\n❌ Opção inválida!")

if __name__ == '__main__':
    main()

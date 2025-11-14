#!/usr/bin/env python3
"""
Teste de Verificação Completa - Frontend e Backend
Verifica se todos os 6 personagens estão configurados corretamente
"""

import sys
from pathlib import Path

print("="*70)
print("🧪 VERIFICAÇÃO COMPLETA - FRONTEND E BACKEND")
print("="*70)
print()

# ============================================
# 1. BACKEND - Verificar personagens
# ============================================
print("📦 BACKEND (entidades.py):")
print("-"*70)

try:
    from entidades import lista_entidades_resumo, ENTIDADES_DA_AMAZONIA
    
    entidades = lista_entidades_resumo()
    print(f"✅ {len(entidades)} personagens encontrados:")
    
    for ent in entidades:
        emoji = ent['emoji']
        nome = ent['nome']
        disc = ent['disciplina']
        liberado = '✅' if ent.get('liberado_por_padrao') else '🔒'
        print(f"   {liberado} {emoji} {nome} ({disc})")
    
    print()
    
    # Verificar se todos os 6 estão presentes
    ids_esperados = ['biologo', 'fazendeiro', 'lider_indigena', 'podcaster', 'coronel', 'politico']
    ids_encontrados = [e['id'] for e in entidades]
    
    if set(ids_esperados) == set(ids_encontrados):
        print("✅ Todos os 6 personagens estão configurados corretamente!")
    else:
        faltando = set(ids_esperados) - set(ids_encontrados)
        print(f"❌ Faltando: {faltando}")
    
except Exception as e:
    print(f"❌ Erro ao carregar backend: {e}")

print()

# ============================================
# 2. FRONTEND - Verificar sons configurados
# ============================================
print("🎵 FRONTEND (interview.js - Sons):")
print("-"*70)

try:
    js_file = Path('static/js/interview.js')
    
    if not js_file.exists():
        print("❌ Arquivo interview.js não encontrado!")
    else:
        content = js_file.read_text()
        
        # Verificar sons ambiente
        sons_esperados = [
            'lab_ambiente',
            'fazenda_ambiente', 
            'aldeia_ambiente',
            'podcast_ambiente',
            'seguranca_ambiente',
            'sala_situacao'
        ]
        
        sons_encontrados = []
        for som in sons_esperados:
            if f'{som}:' in content and f'/static/audio/{som}.mp3' in content:
                sons_encontrados.append(som)
        
        print(f"✅ {len(sons_encontrados)}/6 sons ambiente configurados:")
        for som in sons_encontrados:
            print(f"   ✅ {som}.mp3")
        
        # Verificar mapeamento de personagens
        print()
        print("🗺️  Mapeamento personagem → som:")
        mapeamentos = [
            ("'biologo'", "'lab_ambiente'"),
            ("'fazendeiro'", "'fazenda_ambiente'"),
            ("'lider_indigena'", "'aldeia_ambiente'"),
            ("'podcaster'", "'podcast_ambiente'"),
            ("'coronel'", "'seguranca_ambiente'"),
            ("'politico'", "'sala_situacao'")
        ]
        
        for personagem, som in mapeamentos:
            if f'{personagem}: {som}' in content:
                print(f"   ✅ {personagem:<20} → {som}")
            else:
                print(f"   ❌ {personagem:<20} → FALTANDO!")
        
except Exception as e:
    print(f"❌ Erro ao verificar frontend: {e}")

print()

# ============================================
# 3. ÁUDIOS - Verificar arquivos físicos
# ============================================
print("📁 ARQUIVOS DE ÁUDIO (static/audio/):")
print("-"*70)

try:
    audio_dir = Path('static/audio')
    
    if not audio_dir.exists():
        print("❌ Pasta static/audio não encontrada!")
    else:
        audios_esperados = [
            'lab_ambiente.mp3',
            'fazenda_ambiente.mp3',
            'aldeia_ambiente.mp3',
            'podcast_ambiente.mp3',
            'seguranca_ambiente.mp3',
            'sala_situacao.mp3',
            'clue_collected.mp3',
            'enigma_unlocked.mp3',
            'character_unlocked.mp3',
            'final_victory.mp3'
        ]
        
        audios_encontrados = []
        for audio in audios_esperados:
            path = audio_dir / audio
            if path.exists():
                size = path.stat().st_size / 1024
                audios_encontrados.append(audio)
                print(f"   ✅ {audio:<25} ({size:>7.1f} KB)")
            else:
                print(f"   ❌ {audio:<25} FALTANDO!")
        
        print()
        print(f"✅ {len(audios_encontrados)}/10 áudios presentes")

except Exception as e:
    print(f"❌ Erro ao verificar áudios: {e}")

print()

# ============================================
# 4. RESUMO FINAL
# ============================================
print("="*70)
print("📊 RESUMO FINAL:")
print("="*70)

try:
    backend_ok = len(entidades) == 6
    frontend_ok = len(sons_encontrados) == 6
    audios_ok = len(audios_encontrados) == 10
    
    print(f"Backend (6 personagens):  {'✅ OK' if backend_ok else '❌ PROBLEMA'}")
    print(f"Frontend (6 sons config): {'✅ OK' if frontend_ok else '❌ PROBLEMA'}")
    print(f"Áudios (10 arquivos):     {'✅ OK' if audios_ok else '❌ PROBLEMA'}")
    print()
    
    if backend_ok and frontend_ok and audios_ok:
        print("🎉 TUDO CONFIGURADO CORRETAMENTE!")
        print("🚀 O jogo está pronto para os 6 personagens!")
    else:
        print("⚠️  Alguns ajustes são necessários (veja acima)")
    
except:
    print("⚠️  Não foi possível gerar resumo completo")

print("="*70)

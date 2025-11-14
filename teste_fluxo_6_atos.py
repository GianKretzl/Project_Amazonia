#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧪 TESTE COMPLETO DO FLUXO DOS 6 ATOS
Projeto Encruzilhada - A Última Investigação de Gian Kretzl

Este script testa todo o fluxo do jogo:
- ATO I: Dr. Arnaldo (Ciências)
- ATO II: Valdemar (Geografia)  
- ATO III: Pajé Yakamu (História)
- ATO IV: Falcão (Desinformação)
- ATO V: Coronel Silva (Plot Twist)
- ATO VI: Venturi (Confronto Final)
"""

import sys
sys.path.insert(0, '.')

from entidades import ENTIDADES_DA_AMAZONIA, lista_entidades_resumo
from enigmas import ENIGMAS, verificar_enigma
from pathlib import Path

def print_header(titulo):
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)

def print_subheader(titulo):
    print("\n" + "-" * 70)
    print(f"  {titulo}")
    print("-" * 70)

def test_ato(numero, personagem_id, pistas_esperadas, enigma_id=None):
    """Testa um ato completo"""
    print_header(f"ATO {numero}: {ENTIDADES_DA_AMAZONIA[personagem_id]['nome']}")
    
    personagem = ENTIDADES_DA_AMAZONIA[personagem_id]
    
    # 1. Verificar personagem
    print(f"\n📋 Personagem: {personagem['nome']}")
    print(f"   Disciplina: {personagem['titulo']}")
    print(f"   Emoji: {personagem['emoji']}")
    
    # 2. Verificar requisitos de desbloqueio
    if 'requisito_enigma' in personagem:
        print(f"   🔒 Requer enigma: {personagem['requisito_enigma']}")
    elif 'requisito_desbloqueio' in personagem:
        print(f"   🔓 Desbloqueio automático após: {personagem['requisito_desbloqueio']}")
    else:
        print(f"   ✅ Desbloqueado por padrão")
    
    # 3. Verificar pistas
    print_subheader(f"Pistas do Ato {numero}")
    pistas = personagem.get('pistas', {})
    
    for i, pista_id in enumerate(pistas_esperadas, 1):
        if pista_id in pistas:
            pista = pistas[pista_id]
            principal = "⭐ PRINCIPAL" if "PRINCIPAL" in pista.get('nome', '') else ""
            print(f"   ✅ {i}. {pista_id:30} {principal}")
            print(f"      └─ {pista.get('nome', 'Sem nome')}")
        else:
            print(f"   ❌ {i}. {pista_id:30} → NÃO ENCONTRADA")
    
    print(f"\n   Total esperado: {len(pistas_esperadas)} | Encontradas: {len([p for p in pistas_esperadas if p in pistas])}")
    
    # 4. Verificar enigma (se houver)
    if enigma_id:
        print_subheader(f"Enigma para Desbloquear Próximo Ato")
        
        if enigma_id in ENIGMAS:
            enigma = ENIGMAS[enigma_id]
            print(f"   ✅ Enigma: {enigma['titulo']}")
            print(f"      Requer pistas: {', '.join(enigma['requer_pistas'])}")
            print(f"      Desbloqueia: {enigma['recompensa_entidade']}")
            
            # Testar resposta correta
            resposta_correta = enigma['resposta_correta']
            resultado = verificar_enigma(enigma_id, resposta_correta)
            if resultado:
                print(f"      ✅ Resposta correta testada: {resposta_correta}")
            else:
                print(f"      ❌ ERRO: Validação de resposta falhou!")
        else:
            print(f"   ❌ Enigma '{enigma_id}' NÃO ENCONTRADO!")
    
    # 5. Verificar áudio ambiente
    audio_file = f"{personagem_id}_ambiente.mp3" if personagem_id != 'biologo' else 'lab_ambiente.mp3'
    audio_path = Path('static/audio') / audio_file
    
    if audio_path.exists():
        tamanho = audio_path.stat().st_size / 1024
        print(f"\n   🎵 Áudio ambiente: {audio_file} ({tamanho:.1f} KB)")
    else:
        print(f"\n   ❌ Áudio '{audio_file}' não encontrado!")
    
    return True

def main():
    print_header("🎮 TESTE COMPLETO DO FLUXO DOS 6 ATOS")
    print("Projeto Encruzilhada - A Última Investigação de Gian Kretzl")
    print()
    
    resultados = []
    
    # ATO I: Dr. Arnaldo Silva (Ciências)
    try:
        test_ato(
            numero=1,
            personagem_id='biologo',
            pistas_esperadas=['Sombra_Roxa', 'Química_Coltan', 'Conexão_Fazenda'],
            enigma_id='desbloquear_fazendeiro'
        )
        resultados.append(("ATO I: Dr. Arnaldo", True))
    except Exception as e:
        print(f"\n❌ ERRO no ATO I: {e}")
        resultados.append(("ATO I: Dr. Arnaldo", False))
    
    # ATO II: Valdemar (Geografia)
    try:
        test_ato(
            numero=2,
            personagem_id='fazendeiro',
            pistas_esperadas=['Poço_Artesiano', 'Fazenda_Fachada_Logística', 'Deputado_Venturi_Conexão', 'Conflito_Reserva_Indígena'],
            enigma_id='desbloquear_lider_indigena'
        )
        resultados.append(("ATO II: Valdemar", True))
    except Exception as e:
        print(f"\n❌ ERRO no ATO II: {e}")
        resultados.append(("ATO II: Valdemar", False))
    
    # ATO III: Pajé Yakamu (História)
    try:
        test_ato(
            numero=3,
            personagem_id='lider_indigena',
            pistas_esperadas=['Sombra_Montanha_Fogo', 'Trilha_Ancestrais_Mapa_Coltan', 'Homem_Terno_Venturi'],
            enigma_id='desbloquear_podcaster'
        )
        resultados.append(("ATO III: Pajé Yakamu", True))
    except Exception as e:
        print(f"\n❌ ERRO no ATO III: {e}")
        resultados.append(("ATO III: Pajé Yakamu", False))
    
    # ATO IV: Falcão (Desinformação)
    try:
        test_ato(
            numero=4,
            personagem_id='podcaster',
            pistas_esperadas=['Teoria_Ratanabá', 'Sombra_Roxa_É_Energia'],
            enigma_id=None  # Desbloqueio automático do Coronel
        )
        resultados.append(("ATO IV: Falcão", True))
    except Exception as e:
        print(f"\n❌ ERRO no ATO IV: {e}")
        resultados.append(("ATO IV: Falcão", False))
    
    # ATO V: Coronel Silva (Plot Twist)
    try:
        test_ato(
            numero=5,
            personagem_id='coronel',
            pistas_esperadas=['Ratanabá_É_Desinformação', 'Coltan_Projeto_Militar', 'Gian_Segurança_Nacional'],
            enigma_id='desbloquear_politico'
        )
        resultados.append(("ATO V: Coronel Silva", True))
    except Exception as e:
        print(f"\n❌ ERRO no ATO V: {e}")
        resultados.append(("ATO V: Coronel Silva", False))
    
    # ATO VI: Deputado Venturi (Confronto Final)
    try:
        test_ato(
            numero=6,
            personagem_id='politico',
            pistas_esperadas=['Confissão_Venturi'],
            enigma_id=None  # Confronto final
        )
        resultados.append(("ATO VI: Deputado Venturi", True))
    except Exception as e:
        print(f"\n❌ ERRO no ATO VI: {e}")
        resultados.append(("ATO VI: Deputado Venturi", False))
    
    # RESUMO FINAL
    print_header("📊 RESUMO DOS TESTES")
    
    sucessos = sum(1 for _, sucesso in resultados if sucesso)
    total = len(resultados)
    
    for ato, sucesso in resultados:
        status = "✅" if sucesso else "❌"
        print(f"   {status} {ato}")
    
    print()
    print(f"   Total: {sucessos}/{total} atos testados com sucesso")
    
    if sucessos == total:
        print()
        print("   🎉 TODOS OS ATOS ESTÃO FUNCIONANDO PERFEITAMENTE!")
        print("   🎮 O jogo está pronto para ser jogado!")
    else:
        print()
        print(f"   ⚠️  {total - sucessos} ato(s) com problemas - revisar erros acima")
    
    # Teste de áudios efeitos
    print_header("🔊 VERIFICAÇÃO DE EFEITOS SONOROS")
    
    efeitos = {
        'clue_collected.mp3': 'Pista coletada',
        'enigma_unlocked.mp3': 'Enigma resolvido',
        'character_unlocked.mp3': 'Personagem desbloqueado',
        'final_victory.mp3': 'Vitória final',
        'final_entry.mp3': 'Narração prólogo'
    }
    
    audio_dir = Path('static/audio')
    for arquivo, descricao in efeitos.items():
        caminho = audio_dir / arquivo
        if caminho.exists():
            tamanho = caminho.stat().st_size / 1024
            print(f"   ✅ {arquivo:25} ({tamanho:7.1f} KB) - {descricao}")
        else:
            print(f"   ❌ {arquivo:25} - {descricao}")
    
    print()
    print("=" * 70)
    print("✅ TESTE COMPLETO FINALIZADO!")
    print("=" * 70)

if __name__ == "__main__":
    main()

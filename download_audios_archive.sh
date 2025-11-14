#!/bin/bash
# Script MELHORADO para baixar áudios de bibliotecas públicas
# Usa Archive.org (Internet Archive) - sem necessidade de cadastro

set -e

AUDIO_DIR="./static/audio"
mkdir -p "$AUDIO_DIR"

echo "🎵 BAIXADOR DE ÁUDIOS - INTERNET ARCHIVE"
echo "========================================"
echo ""
echo "📌 Fonte: Archive.org (Domínio Público)"
echo ""

# Contadores
total=10
baixados=0

# Função para baixar com wget
baixar_arquivo() {
    local nome="$1"
    local url="$2"
    local descricao="$3"
    
    if [ -f "$AUDIO_DIR/$nome" ]; then
        echo "✅ $nome já existe ($(du -h "$AUDIO_DIR/$nome" | cut -f1))"
        baixados=$((baixados + 1))
        return 0
    fi
    
    echo "⬇️  Baixando: $descricao"
    
    if wget -q --show-progress -O "$AUDIO_DIR/$nome" "$url" 2>/dev/null; then
        echo "✅ Sucesso! ($(du -h "$AUDIO_DIR/$nome" | cut -f1))"
        baixados=$((baixados + 1))
    else
        echo "❌ Falha ao baixar"
        rm -f "$AUDIO_DIR/$nome"
    fi
    echo ""
}

echo "📥 BAIXANDO SONS AMBIENTE (6 arquivos)"
echo "======================================"
echo ""

# 1. Laboratório - Archive.org
baixar_arquivo "lab_ambiente.mp3" \
    "https://archive.org/download/freesound_laboratory/laboratory_ambience.mp3" \
    "🔬 Laboratório"

# 2. Fazenda - Archive.org
baixar_arquivo "fazenda_ambiente.mp3" \
    "https://archive.org/download/freesound_farm/farm_cattle_ambience.mp3" \
    "🐄 Fazenda"

# 3. Floresta - Archive.org
baixar_arquivo "aldeia_ambiente.mp3" \
    "https://archive.org/download/freesound_jungle/jungle_night_campfire.mp3" \
    "🌳 Floresta + Fogo"

# 4. Música Dramática - Archive.org
baixar_arquivo "podcast_ambiente.mp3" \
    "https://archive.org/download/freesound_dramatic/dramatic_tension_music.mp3" \
    "🎙️ Música Dramática"

# 5. Base Militar - Archive.org
baixar_arquivo "seguranca_ambiente.mp3" \
    "https://archive.org/download/freesound_military/military_radio_ambience.mp3" \
    "🎖️ Base Militar"

# 6. Gabinete - Archive.org
baixar_arquivo "sala_situacao.mp3" \
    "https://archive.org/download/freesound_office/office_tension_ambience.mp3" \
    "🏛️ Gabinete"

echo ""
echo "📥 BAIXANDO EFEITOS SONOROS (4 arquivos)"
echo "========================================"
echo ""

# 7. Pista coletada
baixar_arquivo "clue_collected.mp3" \
    "https://archive.org/download/freesound_notification/positive_notification.mp3" \
    "✨ Notificação"

# 8. Enigma resolvido
baixar_arquivo "enigma_unlocked.mp3" \
    "https://archive.org/download/freesound_unlock/unlock_achievement.mp3" \
    "🔓 Desbloqueio"

# 9. Personagem desbloqueado
baixar_arquivo "character_unlocked.mp3" \
    "https://archive.org/download/freesound_fanfare/short_fanfare.mp3" \
    "🎉 Fanfarra"

# 10. Vitória final
baixar_arquivo "final_victory.mp3" \
    "https://archive.org/download/freesound_victory/victory_fanfare.mp3" \
    "🏆 Vitória"

echo ""
echo "======================================"
echo "📊 RESUMO"
echo "======================================"
echo "✅ Baixados: $baixados/$total"
echo ""

if [ $baixados -eq $total ]; then
    echo "🎉 PERFEITO! Todos os áudios prontos!"
    echo ""
    echo "🚀 Próximo passo:"
    echo "   python app.py"
    echo ""
elif [ $baixados -eq 0 ]; then
    echo "❌ Nenhum áudio foi baixado."
    echo ""
    echo "💡 SOLUÇÃO ALTERNATIVA - Gerar Sons Sintéticos:"
    echo "   ./gerar_audios_sinteticos.sh"
    echo ""
    echo "💡 OU - Download Manual:"
    echo "   Leia: DOWNLOAD_AUDIOS_RAPIDO.md"
    echo ""
else
    echo "⚠️  Alguns downloads falharam ($((total - baixados)) faltando)."
    echo ""
    echo "💡 Execute novamente ou use:"
    echo "   ./gerar_audios_sinteticos.sh"
    echo ""
fi

# Listar arquivos
if [ $baixados -gt 0 ]; then
    echo "📁 Arquivos baixados:"
    ls -lh "$AUDIO_DIR"/*.mp3 2>/dev/null | awk '{print "   " $9 " (" $5 ")"}'
fi

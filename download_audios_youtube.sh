#!/bin/bash
# Script para baixar áudios de ambientes do YouTube (domínio público)
# Requer: yt-dlp (instalado automaticamente se necessário)

set -e

AUDIO_DIR="./static/audio"
mkdir -p "$AUDIO_DIR"

echo "🎵 BAIXADOR AUTOMÁTICO DE ÁUDIOS"
echo "================================"
echo ""

# Verificar/instalar yt-dlp
if ! command -v yt-dlp &> /dev/null; then
    echo "📦 Instalando yt-dlp..."
    pip install -q yt-dlp
    echo "✅ yt-dlp instalado!"
    echo ""
fi

# Verificar/instalar ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "📦 Instalando ffmpeg..."
    sudo apt-get update -qq
    sudo apt-get install -y -qq ffmpeg
    echo "✅ ffmpeg instalado!"
    echo ""
fi

echo "🔍 Verificando áudios existentes..."
echo ""

# Contadores
total=0
existentes=0

# Função para baixar áudio do YouTube
baixar_audio() {
    local nome="$1"
    local url="$2"
    local descricao="$3"
    
    total=$((total + 1))
    
    if [ -f "$AUDIO_DIR/$nome" ]; then
        echo "⏭️  $nome já existe ($(du -h "$AUDIO_DIR/$nome" | cut -f1))"
        existentes=$((existentes + 1))
        return
    fi
    
    echo "⬇️  Baixando: $descricao"
    echo "   Fonte: $url"
    
    # Baixar apenas áudio, converter para MP3, pegar 60 segundos
    yt-dlp -x --audio-format mp3 \
           --audio-quality 5 \
           --postprocessor-args "-ss 00:00:00 -t 00:01:00" \
           --output "$AUDIO_DIR/temp_$nome" \
           --quiet --no-warnings \
           "$url" 2>/dev/null || {
        echo "   ⚠️  Erro ao baixar. Tentando fonte alternativa..."
        return 1
    }
    
    # Renomear arquivo
    mv "$AUDIO_DIR/temp_$nome" "$AUDIO_DIR/$nome" 2>/dev/null || true
    
    if [ -f "$AUDIO_DIR/$nome" ]; then
        echo "   ✅ Baixado com sucesso! ($(du -h "$AUDIO_DIR/$nome" | cut -f1))"
        existentes=$((existentes + 1))
    else
        echo "   ❌ Falha no download"
    fi
    echo ""
}

# Sons Ambiente (60 segundos, em loop)
echo "📥 BAIXANDO SONS AMBIENTE (6 arquivos)"
echo "======================================"
echo ""

# 1. Laboratório
baixar_audio "lab_ambiente.mp3" \
    "https://www.youtube.com/watch?v=ezGCeKQLjnY" \
    "🔬 Laboratório (bipes, ventilação)"

# 2. Fazenda
baixar_audio "fazenda_ambiente.mp3" \
    "https://www.youtube.com/watch?v=N6L1HdR8rqU" \
    "🐄 Fazenda (gado, galos, cigarras)"

# 3. Aldeia/Floresta
baixar_audio "aldeia_ambiente.mp3" \
    "https://www.youtube.com/watch?v=eKFTSSKCzWA" \
    "🌳 Floresta Noturna (sapos, grilos, fogo)"

# 4. Podcast
baixar_audio "podcast_ambiente.mp3" \
    "https://www.youtube.com/watch?v=LNcTx8ZRHPM" \
    "🎙️ Música Dramática (suspense)"

# 5. Base Militar
baixar_audio "seguranca_ambiente.mp3" \
    "https://www.youtube.com/watch?v=fGx6K90TmCI" \
    "🎖️ Base Militar (rádio, passos)"

# 6. Gabinete
baixar_audio "sala_situacao.mp3" \
    "https://www.youtube.com/watch?v=9lOd1ljjUkY" \
    "🏛️ Gabinete (silêncio tenso, ventilação)"

echo ""
echo "📥 BAIXANDO EFEITOS SONOROS (4 arquivos)"
echo "========================================"
echo ""

# 7. Pista coletada
baixar_audio "clue_collected.mp3" \
    "https://www.youtube.com/watch?v=n3LKadmwhCU" \
    "✨ Notificação Positiva"

# 8. Enigma resolvido
baixar_audio "enigma_unlocked.mp3" \
    "https://www.youtube.com/watch?v=3R6_bjH4aRM" \
    "🔓 Desbloqueio"

# 9. Personagem desbloqueado
baixar_audio "character_unlocked.mp3" \
    "https://www.youtube.com/watch?v=8-PjPM4f5JU" \
    "🎉 Fanfarra Curta"

# 10. Vitória final
baixar_audio "final_victory.mp3" \
    "https://www.youtube.com/watch?v=hcD7u0eXUlI" \
    "🏆 Fanfarra de Vitória"

echo ""
echo "======================================"
echo "📊 RESUMO DO DOWNLOAD"
echo "======================================"
echo "✅ Áudios baixados: $existentes/$total"
echo ""

if [ $existentes -eq 10 ]; then
    echo "🎉 SUCESSO! Todos os áudios estão prontos!"
    echo ""
    echo "📁 Arquivos salvos em: $AUDIO_DIR/"
    echo ""
    echo "🚀 Próximo passo:"
    echo "   python app.py"
    echo ""
else
    echo "⚠️  Alguns downloads falharam."
    echo ""
    echo "💡 Soluções:"
    echo "1. Execute novamente este script"
    echo "2. Use o guia manual: DOWNLOAD_AUDIOS_RAPIDO.md"
    echo "3. Baixe do Zapsplat: https://www.zapsplat.com/"
    echo ""
fi

# Listar arquivos baixados
echo "📁 Arquivos em $AUDIO_DIR/:"
ls -lh "$AUDIO_DIR"/*.mp3 2>/dev/null || echo "   (nenhum arquivo MP3 encontrado)"

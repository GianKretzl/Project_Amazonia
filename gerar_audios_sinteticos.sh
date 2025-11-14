#!/bin/bash
# Gerador de áudios sintéticos usando SoX (Sound eXchange)
# Cria sons simples mas funcionais para o jogo

AUDIO_DIR="./static/audio"
mkdir -p "$AUDIO_DIR"

echo "🎵 GERADOR DE ÁUDIOS SINTÉTICOS"
echo "================================"
echo ""

# Verificar/instalar sox
if ! command -v sox &> /dev/null; then
    echo "📦 Instalando SoX (Sound eXchange)..."
    sudo apt-get update -qq
    sudo apt-get install -y -qq sox libsox-fmt-mp3
    echo "✅ SoX instalado!"
    echo ""
fi

echo "🔧 Gerando áudios..."
echo ""

# Função para gerar áudio
gerar() {
    local nome="$1"
    local descricao="$2"
    shift 2
    
    if [ -f "$AUDIO_DIR/$nome" ]; then
        echo "⏭️  $nome já existe"
        return
    fi
    
    echo "🎨 Criando: $descricao"
    
    # Executar comando sox
    "$@" "$AUDIO_DIR/$nome" 2>/dev/null
    
    if [ -f "$AUDIO_DIR/$nome" ]; then
        echo "✅ $nome criado! ($(du -h "$AUDIO_DIR/$nome" | cut -f1))"
    else
        echo "❌ Falha ao criar $nome"
    fi
    echo ""
}

echo "📥 GERANDO SONS AMBIENTE (60 segundos cada)"
echo "============================================"
echo ""

# 1. Laboratório - Bipes eletrônicos
gerar "lab_ambiente.mp3" "🔬 Laboratório (bipes eletrônicos)" \
    sox -n -r 44100 -c 2 synth 60 sine 440 sine 880 gain -20 \
    tremolo 0.3 5 reverb 20

# 2. Fazenda - Tom baixo com variações (simula vento/animais distantes)
gerar "fazenda_ambiente.mp3" "🐄 Fazenda (ambiente rural)" \
    sox -n -r 44100 -c 2 synth 60 pinknoise gain -25 \
    lowpass 1000 tremolo 0.1 2

# 3. Floresta - Ruído rosa (simula natureza)
gerar "aldeia_ambiente.mp3" "🌳 Floresta (ambiente natural)" \
    sox -n -r 44100 -c 2 synth 60 pinknoise gain -22 \
    lowpass 2000 highpass 100 reverb 30

# 4. Podcast - Tom dramático
gerar "podcast_ambiente.mp3" "🎙️ Podcast (tensão)" \
    sox -n -r 44100 -c 2 synth 60 sine 220 sine 165 gain -18 \
    tremolo 0.5 3 reverb 15

# 5. Base Militar - Ruído branco baixo (simula estática)
gerar "seguranca_ambiente.mp3" "🎖️ Base Militar (rádio)" \
    sox -n -r 44100 -c 2 synth 60 whitenoise gain -30 \
    lowpass 3000 tremolo 2 10

# 6. Gabinete - Silêncio tenso com ruído muito baixo
gerar "sala_situacao.mp3" "🏛️ Gabinete (tensão)" \
    sox -n -r 44100 -c 2 synth 60 brownnoise gain -35 \
    lowpass 500 reverb 10

echo ""
echo "📥 GERANDO EFEITOS SONOROS (curtos)"
echo "===================================="
echo ""

# 7. Pista coletada - Tom ascendente
gerar "clue_collected.mp3" "✨ Pista coletada" \
    sox -n -r 44100 -c 2 synth 0.3 sine 523 sine 659 sine 784 gain -15

# 8. Enigma resolvido - Sequência de 3 tons
gerar "enigma_unlocked.mp3" "🔓 Enigma resolvido" \
    sox -n -r 44100 -c 2 synth 0.5 sine 440 sine 554 sine 659 gain -15 \
    delay 0.1 0.2

# 9. Personagem desbloqueado - Acorde alegre
gerar "character_unlocked.mp3" "🎉 Personagem desbloqueado" \
    sox -n -r 44100 -c 2 synth 0.8 sine 523 sine 659 sine 784 sine 1047 gain -12

# 10. Vitória final - Fanfarra simples
gerar "final_victory.mp3" "🏆 Vitória final" \
    sox -n -r 44100 -c 2 synth 1.5 sine 523 sine 659 sine 784 sine 1047 sine 1319 gain -10 \
    delay 0.1 0.2 0.3 0.4

echo ""
echo "======================================"
echo "📊 RESUMO"
echo "======================================"

count=$(ls -1 "$AUDIO_DIR"/*.mp3 2>/dev/null | wc -l)
echo "✅ Áudios gerados: $count/10"
echo ""

if [ $count -eq 10 ]; then
    echo "🎉 SUCESSO! Todos os áudios prontos!"
    echo ""
    echo "⚠️  NOTA: Sons sintéticos são BÁSICOS."
    echo "   Para melhor experiência, baixe sons profissionais:"
    echo "   - Leia: DOWNLOAD_AUDIOS_RAPIDO.md"
    echo "   - Site: https://www.zapsplat.com/"
    echo ""
    echo "🚀 Mas você já pode testar o jogo:"
    echo "   python app.py"
    echo ""
else
    echo "⚠️  Alguns áudios faltaram. Execute novamente."
    echo ""
fi

# Listar arquivos
if [ $count -gt 0 ]; then
    echo "📁 Arquivos criados:"
    ls -lh "$AUDIO_DIR"/*.mp3 2>/dev/null | awk '{print "   " $9 " (" $5 ")"}'
fi

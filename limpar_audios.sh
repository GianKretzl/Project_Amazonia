#!/bin/bash
# Script para limpar todos os áudios gerados

echo "🧹 Limpando áudios antigos..."

if [ -d "static/audio" ]; then
    count=$(find static/audio -name "*.mp3" | wc -l)
    if [ $count -gt 0 ]; then
        rm -f static/audio/*.mp3
        echo "✅ $count arquivo(s) removido(s)"
    else
        echo "✅ Nenhum arquivo encontrado"
    fi
else
    echo "✅ Diretório de áudio não existe"
fi

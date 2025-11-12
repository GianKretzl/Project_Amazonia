#!/usr/bin/env bash
# Script de inicialização para Render.com

echo "🚀 Iniciando Project Amazonia no Render..."

# Verificar se DATABASE_URL existe (PostgreSQL)
if [ -z "$DATABASE_URL" ]; then
    echo "⚠️  DATABASE_URL não configurado - usando SQLite local (não recomendado para produção)"
else
    echo "✅ PostgreSQL detectado"
    
    # Render usa postgres:// mas psycopg2 precisa de postgresql://
    if [[ $DATABASE_URL == postgres://* ]]; then
        export DATABASE_URL="${DATABASE_URL/postgres:\/\//postgresql:\/\/}"
        echo "🔧 DATABASE_URL convertido para postgresql://"
    fi
fi

# Inicializar banco de dados (criar tabelas)
echo "📊 Inicializando banco de dados..."
python -c "from database import db; print('✅ Banco de dados inicializado!')"

echo "🎮 Pronto! Iniciando servidor..."

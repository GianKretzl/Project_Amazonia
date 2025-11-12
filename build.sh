#!/usr/bin/env bash
# Script de inicialização para Render.com

# ⚠️⚠️⚠️ ATENÇÃO: BANCO SERÁ ZERADO A CADA DEPLOY! ⚠️⚠️⚠️
# Para PRODUÇÃO REAL, comente a seção "ZERAR banco de dados" no final deste arquivo

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

# ZERAR banco de dados a cada deploy (remover para produção real)
echo "🗑️  ZERANDO banco de dados (todos os dados serão apagados)..."
python -c "
from database import db
import sys

try:
    conn = db.get_connection()
    cursor = db.dict_cursor(conn)
    
    # Lista de todas as tabelas
    tables = [
        'desafios_completados',
        'contra_perguntas', 
        'entity_interactions',
        'enigmas_resolvidos',
        'pistas_coletadas',
        'chat_history',
        'players',
        'usuarios'
    ]
    
    # Deletar todos os dados de todas as tabelas
    for table in tables:
        try:
            cursor.execute(f'DELETE FROM {table}')
            print(f'   ✓ Tabela {table} zerada')
        except Exception as e:
            print(f'   ⚠ Erro ao zerar {table}: {e}')
    
    conn.commit()
    conn.close()
    print('✅ Banco zerado com sucesso!')
except Exception as e:
    print(f'❌ Erro ao zerar banco: {e}')
    sys.exit(0)  # Não falhar o build por causa disso
"

echo "🎮 Pronto! Iniciando servidor..."

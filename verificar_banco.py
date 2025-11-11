#!/usr/bin/env python3
"""
Script para verificar se o banco de dados está sendo usado corretamente
"""

from database import db
import sqlite3

print('🔍 Verificando banco de dados...\n')

# Conectar ao banco
conn = db.get_connection()
cursor = conn.cursor()

# 1. Listar todas as sessões
print('1️⃣ SESSÕES REGISTRADAS:')
cursor.execute('SELECT session_id, created_at, last_activity FROM players ORDER BY last_activity DESC LIMIT 10')
players = cursor.fetchall()
if players:
    for p in players:
        print(f'  - Session: {p["session_id"][:20]}... (última atividade: {p["last_activity"]})')
else:
    print('  ❌ Nenhuma sessão encontrada')
print()

# 2. Para cada sessão, mostrar dados
for player in players[:3]:  # Apenas as 3 mais recentes
    session_id = player['session_id']
    print(f'📊 DADOS DA SESSÃO: {session_id[:20]}...')
    
    # Interações
    cursor.execute('SELECT entity_id, interaction_count FROM entity_interactions WHERE session_id = ?', (session_id,))
    interactions = cursor.fetchall()
    if interactions:
        print('  💬 Interações:')
        for i in interactions:
            print(f'    - {i["entity_id"]}: {i["interaction_count"]} mensagens')
    
    # Pistas
    cursor.execute('SELECT pista, collected_at FROM pistas_coletadas WHERE session_id = ? ORDER BY collected_at', (session_id,))
    pistas = cursor.fetchall()
    if pistas:
        print(f'  🔍 Pistas coletadas: {len(pistas)}')
        for p in pistas:
            print(f'    - {p["pista"]} (em {p["collected_at"]})')
    
    # Histórico de chat
    cursor.execute('SELECT entity_id, COUNT(*) as total FROM chat_history WHERE session_id = ? GROUP BY entity_id', (session_id,))
    chat_stats = cursor.fetchall()
    if chat_stats:
        print('  💭 Mensagens por entidade:')
        for c in chat_stats:
            print(f'    - {c["entity_id"]}: {c["total"]} mensagens')
            
            # Mostrar últimas 3 mensagens
            cursor.execute('''
                SELECT role, content, timestamp 
                FROM chat_history 
                WHERE session_id = ? AND entity_id = ? 
                ORDER BY timestamp DESC 
                LIMIT 3
            ''', (session_id, c["entity_id"]))
            recent = cursor.fetchall()
            for r in recent:
                preview = r["content"][:50].replace('\n', ' ')
                print(f'      [{r["role"]}] {preview}... ({r["timestamp"]})')
    
    # Contra-perguntas
    cursor.execute('SELECT entity_id, pergunta_tipo, resposta FROM contra_perguntas WHERE session_id = ?', (session_id,))
    cp = cursor.fetchall()
    if cp:
        print('  ❓ Contra-perguntas:')
        for c in cp:
            print(f'    - {c["entity_id"]}/{c["pergunta_tipo"]}: {c["resposta"]}')
    
    # Enigmas
    cursor.execute('SELECT enigma_id, acertou FROM enigmas_resolvidos WHERE session_id = ?', (session_id,))
    enigmas = cursor.fetchall()
    if enigmas:
        print('  🧩 Enigmas:')
        for e in enigmas:
            status = '✅ Resolvido' if e["acertou"] else '❌ Errado'
            print(f'    - {e["enigma_id"]}: {status}')
    
    print()

conn.close()

print('✅ Verificação completa!')
print('💡 Se você vê dados aqui, o banco está funcionando.')
print('💡 Se não vê dados, o sistema não está salvando no banco.')

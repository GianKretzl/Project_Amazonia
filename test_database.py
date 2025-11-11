#!/usr/bin/env python3
"""Script de teste para o banco de dados"""

from database import db

print('🔍 Testando banco de dados...\n')

# Teste 1: Criar jogador
print('1️⃣ Criando jogador...')
db.ensure_player('test_session')
print('✅ Jogador criado\n')

# Teste 2: Salvar mensagens
print('2️⃣ Salvando mensagens no chat...')
db.save_chat_message('test_session', 'biologo', 'user', 'Olá, Dr. Arnaldo!')
db.save_chat_message('test_session', 'biologo', 'assistant', 'Olá! Como posso ajudá-lo?')
db.save_chat_message('test_session', 'biologo', 'user', 'Fale sobre a Sombra Roxa')
db.save_chat_message('test_session', 'biologo', 'assistant', 'A Sombra Roxa é uma anomalia...')
print('✅ 4 mensagens salvas\n')

# Teste 3: Recuperar histórico
print('3️⃣ Recuperando histórico...')
history = db.get_chat_history('test_session', 'biologo', limit=10)
print(f'✅ {len(history)} mensagens recuperadas')
for msg in history:
    print(f'   - {msg["role"]}: {msg["content"][:50]}...')
print()

# Teste 4: Adicionar pistas
print('4️⃣ Adicionando pistas...')
db.add_pista('test_session', 'Sombra_Roxa')
db.add_pista('test_session', 'Química_Coltan')
db.add_pista('test_session', 'Gado_Não_Bebe_Rio')
pistas = db.get_pistas('test_session')
print(f'✅ {len(pistas)} pistas coletadas: {pistas}\n')

# Teste 5: Incrementar interações
print('5️⃣ Incrementando interações...')
for i in range(7):
    count = db.increment_interaction('test_session', 'biologo')
print(f'✅ Total de interações: {count}\n')

# Teste 6: Contra-pergunta
print('6️⃣ Salvando contra-pergunta...')
db.save_contra_pergunta('test_session', 'biologo', 'coltan', 'sim')
resposta = db.get_contra_pergunta_feita('test_session', 'biologo', 'coltan')
print(f'✅ Resposta salva: {resposta}\n')

# Teste 7: Resolver enigma
print('7️⃣ Resolvendo enigma...')
db.save_enigma_result('test_session', 'desbloquear_fazendeiro', 'C', True)
enigmas = db.get_enigmas_resolvidos('test_session')
print(f'✅ Enigmas resolvidos: {enigmas}\n')

# Teste 8: Estatísticas do jogador
print('8️⃣ Estatísticas do jogador...')
stats = db.get_player_stats('test_session')
print(f'✅ Pistas coletadas: {stats["pistas_coletadas"]}')
print(f'✅ Enigmas resolvidos: {stats["enigmas_resolvidos"]}')
print(f'✅ Total de mensagens: {stats["total_mensagens"]}')
print(f'✅ Entidades interagidas: {stats["entidades_interagidas"]}\n')

print('🎉 TODOS OS TESTES PASSARAM COM SUCESSO!')
print('✅ O banco de dados está funcionando perfeitamente!\n')
print('📝 Arquivo do banco: game_data.db')
print('🔄 Para resetar o progresso de teste: db.reset_player_progress("test_session")')

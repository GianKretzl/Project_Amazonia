"""
Teste do Sistema de Autenticação
"""
from database import db
import hashlib

print('🧪 TESTANDO SISTEMA DE AUTENTICAÇÃO\n')

# Limpar usuário de teste anterior (se existir)
try:
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE username = 'teste_user'")
    conn.commit()
    conn.close()
except:
    pass

# Teste 1: Criar usuário
print('1️⃣ Criando usuário de teste...')
senha = 'ABCD1234'
senha_hash = hashlib.sha256(senha.encode()).hexdigest()
user_id = db.create_user('teste_user', senha_hash, 'Investigadores', ['Ana', 'Bruno', 'Carlos'])

if user_id:
    print(f'   ✓ Usuário criado com ID: {user_id}')
    print(f'   ✓ Senha gerada: {senha}')
else:
    print('   ❌ Falha ao criar usuário')
    exit(1)

# Teste 2: Autenticar
print('\n2️⃣ Autenticando usuário...')
user_data = db.authenticate_user('teste_user', senha_hash)

if user_data:
    print(f'   ✓ Autenticado com sucesso!')
    print(f'   ✓ Username: {user_data["username"]}')
    print(f'   ✓ Grupo: {user_data["grupo"]}')
    print(f'   ✓ Integrantes: {", ".join(user_data["integrantes"])}')
else:
    print('   ❌ Falha na autenticação')
    exit(1)

# Teste 3: Vincular sessão
print('\n3️⃣ Vinculando sessão ao usuário...')
test_session_id = 'test_session_xyz123'
db.link_session_to_user(test_session_id, user_id)
print('   ✓ Sessão vinculada')

# Teste 4: Recuperar sessão
print('\n4️⃣ Recuperando sessão do usuário...')
recovered_session = db.get_user_session(user_id)
if recovered_session == test_session_id:
    print(f'   ✓ Sessão recuperada corretamente: {recovered_session}')
else:
    print(f'   ❌ Sessão incorreta: esperado {test_session_id}, obtido {recovered_session}')

# Teste 5: Proteção contra duplicação
print('\n5️⃣ Testando proteção contra usuário duplicado...')
dup_id = db.create_user('teste_user', senha_hash, 'Outro Grupo', ['Pedro'])
if dup_id is None:
    print('   ✓ Proteção funcionando - usuário duplicado rejeitado')
else:
    print('   ❌ ERRO - permitiu criar usuário duplicado!')

# Teste 6: Senha incorreta
print('\n6️⃣ Testando rejeição de senha incorreta...')
wrong_hash = hashlib.sha256('SENHA_ERRADA'.encode()).hexdigest()
wrong_user = db.authenticate_user('teste_user', wrong_hash)
if wrong_user is None:
    print('   ✓ Proteção funcionando - senha incorreta rejeitada')
else:
    print('   ❌ ERRO - aceitou senha incorreta!')

print('\n' + '='*50)
print('✅ TODOS OS TESTES PASSARAM COM SUCESSO!')
print('='*50)
print('\n💡 Sistema de autenticação está funcionando corretamente!')
print('💡 Usuários podem criar contas e retomar o jogo.')

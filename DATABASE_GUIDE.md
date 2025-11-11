# 🗄️ Sistema de Banco de Dados - Project Amazonia

## 📋 Visão Geral

O jogo agora usa **SQLite** para persistir todo o progresso do jogador, garantindo que:
- ✅ O histórico de chat é preservado mesmo após fechar o modal
- ✅ Pistas coletadas são mantidas entre sessões
- ✅ Interações com personagens são contadas corretamente
- ✅ Contra-perguntas não são esquecidas
- ✅ Enigmas resolvidos ficam registrados

## 🏗️ Estrutura do Banco

### Tabelas Criadas:

#### 1. **players** (Jogadores/Sessões)
```sql
- id: INTEGER PRIMARY KEY
- session_id: TEXT UNIQUE (UUID da sessão)
- created_at: TIMESTAMP
- last_activity: TIMESTAMP
```

#### 2. **chat_history** (Histórico de Conversas)
```sql
- id: INTEGER PRIMARY KEY
- session_id: TEXT
- entity_id: TEXT (biologo, fazendeiro, etc.)
- role: TEXT (user ou assistant)
- content: TEXT (mensagem)
- timestamp: TIMESTAMP
```

#### 3. **pistas_coletadas** (Pistas do Dossiê)
```sql
- id: INTEGER PRIMARY KEY
- session_id: TEXT
- pista: TEXT (nome da pista)
- collected_at: TIMESTAMP
```

#### 4. **enigmas_resolvidos** (Puzzles Completados)
```sql
- id: INTEGER PRIMARY KEY
- session_id: TEXT
- enigma_id: TEXT
- resposta: TEXT
- acertou: BOOLEAN
- solved_at: TIMESTAMP
```

#### 5. **entity_interactions** (Contador de Interações)
```sql
- id: INTEGER PRIMARY KEY
- session_id: TEXT
- entity_id: TEXT
- interaction_count: INTEGER
- last_interaction: TIMESTAMP
```

#### 6. **contra_perguntas** (Respostas Especiais)
```sql
- id: INTEGER PRIMARY KEY
- session_id: TEXT
- entity_id: TEXT
- pergunta_tipo: TEXT (ex: 'coltan')
- resposta: TEXT (sim/não)
- asked_at: TIMESTAMP
```

## 🔧 API do Banco de Dados

### Importação
```python
from database import db
```

### Métodos Principais

#### Histórico de Chat
```python
# Salvar mensagem
db.save_chat_message(session_id, entity_id, role, content)

# Recuperar histórico (últimas N mensagens)
history = db.get_chat_history(session_id, entity_id, limit=10)

# Limpar histórico
db.clear_chat_history(session_id, entity_id)  # Apenas uma entidade
db.clear_chat_history(session_id)  # Todas as entidades
```

#### Pistas
```python
# Adicionar pista
db.add_pista(session_id, 'Sombra_Roxa')

# Obter todas as pistas
pistas = db.get_pistas(session_id)  # Retorna lista de strings
```

#### Interações
```python
# Incrementar e retornar novo total
count = db.increment_interaction(session_id, 'biologo')

# Apenas consultar
count = db.get_interaction_count(session_id, 'biologo')
```

#### Contra-Perguntas
```python
# Salvar resposta
db.save_contra_pergunta(session_id, 'biologo', 'coltan', 'sim')

# Verificar se já foi feita
resposta = db.get_contra_pergunta_feita(session_id, 'biologo', 'coltan')
# Retorna None se não foi feita, ou a resposta (sim/não)
```

#### Enigmas
```python
# Salvar resultado
db.save_enigma_result(session_id, 'desbloquear_fazendeiro', 'C', True)

# Obter enigmas resolvidos (apenas os corretos)
enigmas = db.get_enigmas_resolvidos(session_id)  # ['desbloquear_fazendeiro', ...]
```

#### Estatísticas
```python
stats = db.get_player_stats(session_id)
# Retorna:
# {
#   'pistas_coletadas': 3,
#   'enigmas_resolvidos': 1,
#   'total_mensagens': 15,
#   'entidades_interagidas': [
#     {'entity_id': 'biologo', 'interactions': 8},
#     {'entity_id': 'fazendeiro', 'interactions': 3}
#   ]
# }
```

#### Reset
```python
# Resetar todo o progresso de um jogador
db.reset_player_progress(session_id)
```

## 🔄 Mudanças no app.py

### Before (Session)
```python
session['pistas'] = []
session['interacoes_entidade'] = {}
session['enigmas_resolvidos'] = []
```

### After (Database)
```python
pistas = db.get_pistas(session['session_id'])
count = db.increment_interaction(session['session_id'], entity_id)
enigmas = db.get_enigmas_resolvidos(session['session_id'])
```

## 🎯 Benefícios

### 1. **Persistência Entre Sessões**
- Jogador pode fechar o navegador e continuar de onde parou
- Histórico de chat preservado mesmo fechando o modal

### 2. **Contra-Pergunta Funcionando**
- Sistema agora rastreia corretamente:
  - Quantas interações o jogador teve (6+)
  - Se já coletou "Sombra_Roxa"
  - Se já fez a contra-pergunta antes
  - A resposta dada (sim/não)

### 3. **Debugging Facilitado**
```python
# Ver progresso completo
stats = db.get_player_stats(session_id)
print(stats)

# Ver histórico de chat
history = db.get_chat_history(session_id, 'biologo')
for msg in history:
    print(f"{msg['role']}: {msg['content']}")
```

### 4. **Performance**
- SQLite é extremamente rápido para operações locais
- Índices criados automaticamente em colunas-chave
- Queries otimizadas com `LIMIT` e `ORDER BY`

## 📝 Arquivo do Banco

- **Localização**: `/workspaces/Project_Amazonia/game_data.db`
- **Formato**: SQLite 3
- **Tamanho**: ~20KB (vazio) até ~5MB (com muitos dados)
- **Git**: Adicionado ao `.gitignore` (não versionar dados dos jogadores)

## 🧪 Testes

Execute o script de teste:
```bash
python3 test_database.py
```

Deve mostrar:
```
✅ Jogador criado
✅ 4 mensagens salvas
✅ 4 mensagens recuperadas
✅ 3 pistas coletadas
✅ Total de interações: 7
✅ Resposta salva: sim
✅ Enigmas resolvidos: ['desbloquear_fazendeiro']
🎉 TODOS OS TESTES PASSARAM COM SUCESSO!
```

## 🔍 Inspeção Manual do Banco

Usando SQLite CLI:
```bash
sqlite3 game_data.db

# Ver todas as tabelas
.tables

# Ver schema de uma tabela
.schema chat_history

# Query exemplo
SELECT * FROM pistas_coletadas WHERE session_id = 'xxx';

# Sair
.quit
```

Usando Python:
```python
from database import db

# Ver todas as pistas de uma sessão
pistas = db.get_pistas('sua-session-id-aqui')
print(pistas)

# Ver histórico completo
history = db.get_chat_history('sua-session-id', 'biologo', limit=100)
for msg in history:
    print(f"{msg['timestamp']}: {msg['role']} - {msg['content']}")
```

## 🚀 Próximos Passos (Opcional)

Se quiser expandir no futuro:

1. **Multi-jogador**: Cada jogador tem seu próprio `session_id`
2. **Leaderboard**: Query para ranking por pistas/enigmas
3. **Analytics**: Rastrear quais perguntas os jogadores fazem mais
4. **Backup**: Exportar/importar progresso
5. **Admin Panel**: Interface web para ver todos os jogadores

## ⚠️ Observações Importantes

1. **Session ID**: Gerado automaticamente como UUID no primeiro acesso
2. **Segurança**: Banco local (não exposto na web)
3. **Backup**: Copie `game_data.db` para fazer backup manual
4. **Reset**: Delete `game_data.db` para começar do zero (todos os jogadores)

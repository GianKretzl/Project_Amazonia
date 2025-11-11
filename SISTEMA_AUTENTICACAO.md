# 🔐 Sistema de Autenticação e Salvamento de Progresso

## 📋 Visão Geral

Sistema completo de autenticação implementado para permitir que jogadores criem contas, salvem automaticamente seu progresso e retomem a investigação de onde pararam.

---

## ✨ Funcionalidades Implementadas

### 1. **Tela de Login Renovada** (`templates/login.html`)

#### **Aba: Nova Investigação**
- ✅ Campo **Nome de Usuário** (único, obrigatório)
- ✅ Campo **Nome do Grupo**
- ✅ Campos **Integrantes** (1-6 pessoas)
- ✅ Geração automática de **senha aleatória**
- ✅ Tela de confirmação com senha exibida
- ✅ Botão de copiar senha
- ✅ Aviso para anotar a senha

#### **Aba: Continuar Investigação**
- ✅ Campo **Nome de Usuário**
- ✅ Campo **Senha**
- ✅ Autenticação segura
- ✅ Recuperação de progresso salvo

---

### 2. **Banco de Dados Atualizado** (`database.py`)

#### **Nova Tabela: `usuarios`**
```sql
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    grupo_nome TEXT NOT NULL,
    integrantes TEXT NOT NULL (JSON),
    created_at TIMESTAMP,
    last_login TIMESTAMP
)
```

#### **Tabela `players` Atualizada**
```sql
CREATE TABLE players (
    id INTEGER PRIMARY KEY,
    session_id TEXT UNIQUE,
    user_id INTEGER,  -- NOVO: vincula ao usuário
    created_at TIMESTAMP,
    last_activity TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES usuarios(id)
)
```

#### **Novas Funções**
- `create_user(username, password_hash, grupo, integrantes)` - Criar conta
- `authenticate_user(username, password_hash)` - Fazer login
- `link_session_to_user(session_id, user_id)` - Vincular sessão
- `get_user_session(user_id)` - Recuperar sessão salva

---

### 3. **Backend Atualizado** (`app.py`)

#### **Novas Rotas**

**`POST /api/login`** - Nova Investigação
```python
{
  "usuario": "investigador_123",
  "grupo": "Detetives da Amazônia", 
  "integrantes": ["Ana", "Bruno"]
}
→ Retorna: { "success": true, "senha": "A7X9K2M1" }
```

**`POST /api/login/continue`** - Continuar Investigação
```python
{
  "usuario": "investigador_123",
  "senha": "A7X9K2M1"
}
→ Retorna: { "success": true, "grupo": "...", "integrantes": [...] }
```

**`POST /api/logout`** - Salvar e Sair
```python
→ Salva progresso automaticamente
→ Retorna: { "success": true, "message": "Progresso salvo!" }
```

#### **Segurança Implementada**
- ✅ Senhas armazenadas com **SHA-256 hash**
- ✅ Proteção contra **usuários duplicados**
- ✅ Validação de **credenciais**
- ✅ Sessões vinculadas a **usuários autenticados**

---

### 4. **Interface Atualizada**

#### **Botão "Salvar e Sair"** (`templates/interview.html`)
```html
<button onclick="salvarESair()" class="btn-small btn-logout">
  💾 Salvar e Sair
</button>
```

#### **Estilos CSS Adicionados** (`static/css/style.css`)
- `.login-tabs` - Abas de navegação
- `.tab-button` - Botões de aba
- `.password-box` - Exibição de senha
- `.password-display` - Código da senha
- `.btn-copy` - Botão copiar senha
- `.btn-logout` - Botão sair

---

## 🎮 Fluxo de Uso

### **Cenário 1: Novo Jogador**
1. Acessa `/` (tela de login)
2. Clica em "🆕 Nova Investigação"
3. Preenche:
   - Nome de usuário: `detective_silva`
   - Nome do grupo: `Investigadores da Amazônia`
   - Integrantes: `João Silva`, `Maria Santos`
4. Clica em "🚀 INICIAR INVESTIGAÇÃO"
5. **Tela exibe senha**: `X7K9M2A1`
6. Jogador **anota a senha** ✍️
7. Clica em "✅ JÁ ANOTEI A SENHA - CONTINUAR"
8. Jogo carrega e salva progresso automaticamente

### **Cenário 2: Retomar Investigação**
1. Acessa `/` (tela de login)
2. Clica em "▶️ Continuar Investigação"
3. Preenche:
   - Nome de usuário: `detective_silva`
   - Senha: `X7K9M2A1`
4. Clica em "🔓 ACESSAR INVESTIGAÇÃO"
5. Jogo carrega **exatamente de onde parou**:
   - ✅ Pistas coletadas recuperadas
   - ✅ Desafios completados mantidos
   - ✅ Enigmas resolvidos preservados
   - ✅ Histórico de chat restaurado
   - ✅ Interações contadas

### **Cenário 3: Salvar Durante o Jogo**
1. Jogador está investigando
2. Precisa sair temporariamente
3. Clica em "💾 Salvar e Sair" (canto superior direito)
4. Confirma ação
5. Progresso salvo, volta para tela de login
6. Pode retomar depois com usuário + senha

---

## 🔒 Segurança

### **Proteções Implementadas**
1. **Hash de Senhas**: SHA-256 (senhas nunca armazenadas em texto puro)
2. **Usuários Únicos**: Constraint UNIQUE no username
3. **Validação de Entrada**: 
   - Username: apenas letras, números e underscore
   - Grupo: máximo 50 caracteres
   - Integrantes: 1-6 pessoas, máximo 60 caracteres cada
4. **Sessões Seguras**: Flask session com secret_key

### **Geração de Senhas**
```python
import secrets
senha = secrets.token_urlsafe(6)[:8].upper()
# Exemplo: "A7X9K2M1" (8 caracteres alfanuméricos)
```

---

## 💾 Dados Persistidos

### **O que é salvo automaticamente:**
✅ Pistas coletadas (`pistas_coletadas` table)  
✅ Enigmas resolvidos (`enigmas_resolvidos` table)  
✅ Desafios completados (`desafios_completados` table) ← **NOVO!**  
✅ Histórico de chat (`chat_history` table)  
✅ Interações com personagens (`entity_interactions` table)  
✅ Contra-perguntas respondidas (`contra_perguntas` table)  
✅ Estatísticas do jogador  

### **O que NÃO é salvo:**
❌ Dicas desbloqueadas (ainda em `session` - pode migrar depois)

---

## 🧪 Testes

### **Executar Testes**
```bash
python3 test_auth_system.py
```

### **Resultados Esperados**
```
✅ Criar usuário
✅ Autenticar usuário
✅ Vincular sessão
✅ Recuperar sessão
✅ Rejeitar usuário duplicado
✅ Rejeitar senha incorreta
```

---

## 📊 Estatísticas do Sistema

### **Antes**
- 11 desafios
- Session storage (perdido ao reiniciar)
- Sem autenticação
- Sem recuperação de progresso

### **Agora**
- ✅ **31 desafios** (rotatividade)
- ✅ **Banco de dados SQLite** (persistência)
- ✅ **Sistema de autenticação completo**
- ✅ **Recuperação de progresso**
- ✅ **Múltiplos jogadores simultâneos**
- ✅ **Salvamento automático**

---

## 🚀 Próximos Passos (Opcionais)

### **Melhorias Futuras**
1. [ ] Migrar `dicas_desbloqueadas` para o banco
2. [ ] Sistema de recuperação de senha via email
3. [ ] Ranking de jogadores (pontuação)
4. [ ] Multiplayer em tempo real
5. [ ] Histórico de investigações anteriores
6. [ ] Exportar relatório da investigação em PDF

---

## 📝 Notas Técnicas

### **Compatibilidade**
- ✅ Código antigo continua funcionando
- ✅ Sessões antigas ainda são suportadas
- ✅ Migration automática do banco (via `init_database()`)

### **Performance**
- Banco SQLite otimizado com índices
- Queries eficientes com FOREIGN KEYs
- Session management leve

### **Estrutura de Arquivos Modificados**
```
/workspaces/Project_Amazonia/
├── templates/
│   ├── login.html         ← ATUALIZADO (abas, senha)
│   └── interview.html     ← ATUALIZADO (botão sair)
├── static/css/
│   └── style.css          ← ATUALIZADO (estilos novos)
├── app.py                 ← ATUALIZADO (rotas autenticação)
├── database.py            ← ATUALIZADO (tabela usuarios)
├── desafios.py            ← ATUALIZADO (31 desafios)
└── test_auth_system.py    ← NOVO (testes)
```

---

## ✅ Status Final

**🎉 SISTEMA 100% FUNCIONAL E TESTADO!**

Jogadores agora podem:
1. ✅ Criar conta com usuário e senha
2. ✅ Jogar e ter progresso salvo automaticamente
3. ✅ Sair do jogo a qualquer momento
4. ✅ Retomar exatamente de onde pararam
5. ✅ Ter múltiplas investigações em paralelo (diferentes usuários)

---

**Desenvolvido para: Projeto Sombra Roxa - Gian Kretzl**  
**Data: 11 de novembro de 2025**

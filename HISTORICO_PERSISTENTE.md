# 🔄 CORREÇÃO: Histórico de Chat Persistente

## ✅ Problema Resolvido

**ANTES:**
- Ao fechar o modal do chat e abrir novamente, o histórico aparecia em branco
- Frontend limpava `this.chatHistory = []` ao selecionar entidade
- Histórico não era recuperado do banco de dados

**AGORA:**
- ✅ Histórico é carregado do banco ao abrir o personagem
- ✅ Mensagens anteriores aparecem automaticamente
- ✅ Contador de interações preservado
- ✅ Contra-pergunta não se repete

## 🔧 Mudanças Realizadas

### 1. Frontend (`static/js/interview.js`)

#### A) Método `selectEntity()` - Agora é async e carrega histórico
```javascript
async selectEntity(entity) {
  this.currentEntity = entity;
  
  // NOVO: Carregar histórico do banco
  await this.loadChatHistory(entity.id);
  
  // ...resto do código
  
  // Se já tem histórico, renderizar as mensagens
  if (this.chatHistory.length > 0) {
    this.renderChatHistory();
  } else {
    // Primeira vez - mostrar introdução
    this.adicionarAudioIntroducao(entity);
  }
}
```

#### B) Nova função `loadChatHistory()`
```javascript
async loadChatHistory(entityId) {
  try {
    const res = await fetch(`/api/chat/history/${entityId}`);
    const data = await res.json();
    
    if (data.history && data.history.length > 0) {
      this.chatHistory = data.history;
      console.log(`📚 Histórico carregado: ${data.history.length} mensagens`);
    } else {
      this.chatHistory = [];
      console.log('📭 Nenhum histórico - primeira conversa');
    }
  } catch (error) {
    console.error('Erro ao carregar histórico:', error);
    this.chatHistory = [];
  }
}
```

#### C) Nova função `renderChatHistory()`
```javascript
renderChatHistory() {
  console.log(`🎨 Renderizando ${this.chatHistory.length} mensagens...`);
  
  this.chatHistory.forEach((msg, index) => {
    if (msg.role === 'user') {
      this.appendUserMessage(msg.content);
    } else if (msg.role === 'assistant') {
      this.appendEntityMessage(msg.content);
    }
  });
  
  this.appendSystemMessage(`🔄 Conversa retomada com ${this.currentEntity.nome}. Continue de onde parou!`);
}
```

#### D) Removido envio de histórico nas requisições
```javascript
// ANTES:
body: JSON.stringify({
  entity_id: this.currentEntity.id,
  message: message,
  history: this.chatHistory  // ❌ Removido
})

// AGORA:
body: JSON.stringify({
  entity_id: this.currentEntity.id,
  message: message
  // Histórico vem do banco - não precisa enviar
})
```

### 2. Backend (`app.py`)

#### Nova rota GET `/api/chat/history/<entity_id>`
```python
@app.route('/api/chat/history/<entity_id>')
def api_chat_history(entity_id):
    """Retorna o histórico de chat para uma entidade específica"""
    session_id = session.get('session_id')
    if not session_id:
        return jsonify({'history': []})
    
    # Buscar histórico do banco de dados
    history = db.get_chat_history(session_id, entity_id, limit=50)
    
    return jsonify({
        'history': history,
        'entity_id': entity_id,
        'total_messages': len(history)
    })
```

## 🧪 Como Testar

### Teste 1: Verificar se histórico persiste
1. Abra o jogo e converse com Dr. Arnaldo
2. Faça 3-4 perguntas
3. **Feche o modal do chat**
4. Clique novamente em Dr. Arnaldo
5. ✅ **ESPERADO**: Todas as mensagens anteriores aparecem
6. ✅ **ESPERADO**: Mensagem "🔄 Conversa retomada com Dr. Arnaldo..."

### Teste 2: Verificar contador de interações
1. Abra o console do navegador (F12)
2. Converse com Dr. Arnaldo
3. Veja no console: `Interações com Dr. Arnaldo: X/6`
4. Feche o modal
5. Abra novamente
6. Faça outra pergunta
7. ✅ **ESPERADO**: Contador continua de onde parou (não volta para 0)

### Teste 3: Contra-pergunta após 6 interações
1. Comece uma nova sessão (limpe cookies ou use aba anônima)
2. Pergunte sobre "Sombra Roxa" → coleta pista
3. Faça mais 5 perguntas variadas
4. Na 6ª pergunta, mencione "químico" ou "coltan"
5. ✅ **ESPERADO**: Contra-pergunta aparece
6. Feche o modal e abra novamente
7. ✅ **ESPERADO**: Contra-pergunta NÃO aparece de novo

### Teste 4: Múltiplas entidades
1. Converse com Dr. Arnaldo (3 mensagens)
2. Feche e abra Valdemar
3. Converse com Valdemar (2 mensagens)
4. Volte para Dr. Arnaldo
5. ✅ **ESPERADO**: As 3 mensagens do Arnaldo aparecem
6. Volte para Valdemar
7. ✅ **ESPERADO**: As 2 mensagens do Valdemar aparecem

## 🔍 Debug

### Ver dados no banco
```bash
python3 verificar_banco.py
```

### Ver logs do navegador
Abra o console (F12) e procure por:
```
📚 Histórico carregado: 8 mensagens
🎨 Renderizando 8 mensagens do histórico...
  Mensagem 1: user - Olá, Dr. Arnaldo!...
  Mensagem 2: assistant - Olá! Meu nome é Dr. Arnaldo Silva...
```

### Testar rota manualmente
```bash
# Pegar session_id do cookie no navegador
# Depois chamar:
curl http://localhost:5000/api/chat/history/biologo \
  -H "Cookie: session=SEU_SESSION_ID"
```

## 📊 Fluxo Completo

```
1. Usuário clica em Dr. Arnaldo
   ↓
2. selectEntity('biologo') é chamado
   ↓
3. loadChatHistory('biologo') busca do banco
   ↓
4. Se tem histórico:
   - renderChatHistory() mostra mensagens antigas
   - Mensagem "🔄 Conversa retomada..."
   ↓
5. Se não tem histórico:
   - adicionarAudioIntroducao()
   - Mensagem "💬 Entrevista iniciada..."
   ↓
6. Usuário faz perguntas
   ↓
7. Cada mensagem é salva no banco (app.py)
   ↓
8. Histórico local (this.chatHistory) é atualizado
   ↓
9. Usuário fecha modal
   ↓
10. Reabre: Volta para passo 2 ✅
```

## ⚠️ Observações Importantes

1. **Session ID**: Precisa estar presente no cookie
   - Gerado automaticamente no primeiro acesso
   - Válido enquanto o navegador não fechar (ou cookie expirar)

2. **Primeira Conversa**: Se nunca conversou com uma entidade
   - `history` retorna lista vazia `[]`
   - Áudio de introdução toca
   - Mensagem de "Entrevista iniciada"

3. **Conversa Retomada**: Se já conversou antes
   - `history` retorna todas as mensagens
   - Mensagens são renderizadas em ordem
   - Mensagem de "Conversa retomada"

4. **Performance**: Limitado a 50 mensagens mais recentes
   - Definido em `limit=50` na rota
   - Pode ser aumentado se necessário

## 🎯 Resultado Final

Agora o histórico de chat funciona exatamente como em aplicativos de mensagem modernos (WhatsApp, Telegram, etc.):
- ✅ Mensagens persistem entre abrir/fechar
- ✅ Contexto da conversa preservado
- ✅ Contador de interações correto
- ✅ Contra-perguntas não se repetem
- ✅ Cada personagem tem seu próprio histórico separado

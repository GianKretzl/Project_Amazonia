# 🔧 Guia de Solução de Problemas

## Problemas Comuns e Soluções

### 1. Servidor não inicia

**Erro:** `ModuleNotFoundError: No module named 'flask'`

**Solução:**
```bash
pip install -r requirements.txt
```

---

### 2. Entidades não aparecem na tela

**Problema:** Grid de entidades vazio

**Verificações:**
1. Abra o console do navegador (F12)
2. Vá para a aba "Network"
3. Recarregue a página
4. Verifique se `/api/entities` retorna 200

**Solução:**
```bash
# Reinicie o servidor
# Ctrl+C no terminal
python app.py
```

---

### 3. Pistas não desbloqueiam entidades

**Problema:** Coletou pista mas personagem continua bloqueado

**Causa:** Sistema de sessão não está mantendo estado

**Solução:**
```python
# Verifique se SECRET_KEY está configurada no .env
SECRET_KEY=sua-chave-secreta-aleatoria
```

**Workaround temporário:**
```bash
# Limpe cookies do navegador
# Ou use modo anônimo
```

---

### 4. Excalibur.js não carrega

**Problema:** Canvas preto ou vazio

**Verificações:**
1. Console do navegador tem erro de CDN?
2. Você está offline?

**Solução 1 (CDN alternativo):**
```html
<!-- Em interview.html, troque por: -->
<script src="https://cdn.jsdelivr.net/npm/excalibur@0.29.3/dist/excalibur.min.js"></script>
```

**Solução 2 (Download local):**
```bash
cd /workspaces/Project_Amazonia/static/js
wget https://unpkg.com/excalibur@0.29.3/dist/excalibur.min.js
```

```html
<!-- Em interview.html: -->
<script src="{{ url_for('static', filename='js/excalibur.min.js') }}"></script>
```

---

### 5. IA não responde ou dá erro

**Problema:** Respostas genéricas ou erro 500

**Causa 1:** OpenAI API key não configurada
**Solução:** O jogo funciona sem! Usa respostas simuladas.

**Causa 2:** OpenAI API com problema
**Solução:**
```python
# app.py já tem fallback automático
# Verifique logs do terminal
```

**Para testar sem OpenAI:**
```bash
# Remova a chave do .env ou:
export OPENAI_API_KEY=""
python app.py
```

---

### 6. CSS não carrega / página sem estilo

**Problema:** Página aparece sem cores/formatação

**Verificação:**
```bash
# Verifique se o arquivo existe:
ls -la static/css/style.css
```

**Solução:**
```bash
# Limpe cache do navegador
# Ctrl+Shift+R (Chrome/Firefox)
# Cmd+Shift+R (Mac)

# Ou force reload no servidor
# Ctrl+C
python app.py
```

---

### 7. JavaScript não executa

**Problema:** Botões não funcionam, animações não aparecem

**Console mostra:** `Uncaught TypeError` ou similar

**Solução 1:**
```bash
# Verifique se interview.js existe:
ls -la static/js/interview.js
```

**Solução 2:**
```html
<!-- Verifique ordem dos scripts em interview.html -->
<!-- Excalibur ANTES de interview.js -->
<script src="https://unpkg.com/excalibur@0.29.3/dist/excalibur.min.js"></script>
<script src="{{ url_for('static', filename='js/interview.js') }}"></script>
```

---

### 8. Porta 5000 já em uso

**Erro:** `OSError: [Errno 48] Address already in use`

**Solução 1:**
```bash
# Mate processo na porta 5000
lsof -ti:5000 | xargs kill -9
```

**Solução 2:**
```bash
# Use porta diferente
export PORT=5001
python app.py
# Acesse: http://localhost:5001
```

---

### 9. Fonte não carrega (Google Fonts)

**Problema:** Fontes aparecem como padrão

**Causa:** Problema com CDN do Google Fonts

**Solução (Offline):**
```bash
# Baixe fontes para static/fonts/
# Atualize CSS para usar fontes locais
```

---

### 10. Mobile não funciona bem

**Problema:** Layout quebrado em smartphone

**Solução temporária:**
```css
/* Adicione em style.css */
@media (max-width: 480px) {
  .terminal-container {
    font-size: 12px;
    padding: 10px;
  }
  
  .entity-card {
    width: 100%;
  }
}
```

---

## 🔍 Debug Avançado

### Habilitar logs detalhados

```python
# Em app.py, adicione no topo:
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Testar API diretamente

```bash
# Teste endpoint de entidades
curl http://localhost:5000/api/entities

# Teste chat
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"entity_id":"biologo","message":"Olá"}'

# Teste coleta de pista
curl -X POST http://localhost:5000/api/collect \
  -H "Content-Type: application/json" \
  -d '{"pista":"Anomalia_Química_Coltan"}'
```

### Verificar estrutura de arquivos

```bash
tree -I '__pycache__|*.pyc' /workspaces/Project_Amazonia
```

Estrutura esperada:
```
Project_Amazonia/
├── app.py
├── entidades.py
├── requirements.txt
├── README.md
├── CHANGELOG.md
├── .env.example
├── templates/
│   ├── index.html
│   ├── briefing.html
│   └── interview.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        ├── main.js
        └── interview.js
```

---

## 🆘 Ainda com Problemas?

### 1. Reinstalação Limpa

```bash
# Backup do código
cd /workspaces
cp -r Project_Amazonia Project_Amazonia_backup

# Reinstale dependências
cd Project_Amazonia
pip uninstall -y flask python-dotenv openai
pip install -r requirements.txt

# Reinicie
python app.py
```

### 2. Verifique Versões

```bash
python --version  # Deve ser 3.8+
pip show flask    # Deve ser 3.0+
```

### 3. Logs Completos

```bash
# Execute com output completo
python app.py 2>&1 | tee debug.log

# Compartilhe debug.log se precisar de ajuda
```

---

## 💡 Dicas de Performance

### Se o jogo estiver lento:

1. **Reduza partículas**
```javascript
// Em interview.js, linha ~183, reduza de 20 para 10:
for (let i = 0; i < 10; i++) {
```

2. **Desabilite estrelas**
```javascript
// Em interview.js, comente linha ~67-82:
// createStarfield(scene, Ex);
```

3. **Simplifique animações**
```css
/* Em style.css, adicione: */
* {
  animation-duration: 0.1s !important;
  transition-duration: 0.1s !important;
}
```

---

## ✅ Checklist de Funcionamento

Use esta lista para verificar se tudo está ok:

- [ ] Servidor inicia sem erros
- [ ] Página inicial carrega com animações
- [ ] Briefing mostra todos os atos
- [ ] Sala de entrevistas mostra Dr. Arnaldo desbloqueado
- [ ] Canvas Excalibur renderiza (estrelas visíveis)
- [ ] Contador de pistas mostra "0"
- [ ] Pode clicar no Dr. Arnaldo
- [ ] Chat abre corretamente
- [ ] Pode enviar mensagem
- [ ] Resposta da IA aparece
- [ ] Botão de coletar pista aparece
- [ ] Coletar pista atualiza contador
- [ ] Nova entidade desbloqueia
- [ ] Animação de partículas ao desbloquear

Se todos os itens estão ✅, o jogo está funcionando perfeitamente!

---

**🎮 Boa sorte, estagiário!**

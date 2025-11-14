# Testes Visuais - Projeto Sombra Roxa

## 🤖 Teste Visual Automatizado

### Scripts Disponíveis

#### 1. `teste_visual_completo.py` - Teste Visual Interativo
**Descrição:** Abre o servidor e navegador para você testar manualmente.

**Uso:**
```bash
python teste_visual_completo.py
```

**Características:**
- ✅ Inicia servidor Flask automaticamente
- ✅ Abre navegador na URL correta
- ✅ Fornece instruções detalhadas
- ✅ Permite comandos interativos
- ✅ Você testa manualmente a interface

---

#### 2. `teste_visual_automatizado.py` - Teste Totalmente Automatizado
**Descrição:** Simula um usuário real usando Selenium WebDriver.

**Uso:**
```bash
python teste_visual_automatizado.py
```

**Características:**
- 🤖 Totalmente automatizado
- 📸 Tira screenshots de cada etapa
- ✅ Testa login, conversas, pistas
- ✅ Navega entre personagens
- ✅ Gera relatório completo
- 📊 Estatísticas de sucesso/falha

**Requisitos:**
```bash
pip install selenium
```

**WebDriver necessário:**
- ChromeDriver: https://chromedriver.chromium.org/
- Ou use Firefox (geckodriver instalado automaticamente)

---

### 📸 Screenshots

Os testes automatizados salvam screenshots em:
```
screenshots_testes/
├── 20251114_153045_01_pagina_inicial.png
├── 20251114_153045_02_formulario_preenchido.png
├── 20251114_153045_03_apos_login.png
└── ...
```

---

### 📊 Comparação

| Aspecto | Interativo | Automatizado |
|---------|-----------|--------------|
| **Automação** | Manual | Total |
| **Screenshots** | Manual | Automático |
| **Relatório** | Não | Sim |
| **Navegador** | Você controla | Script controla |
| **Tempo** | Quanto quiser | ~2-5 minutos |
| **Uso** | Exploração | Validação/CI |

---

### 🎯 Quando usar cada um?

**Teste Interativo (`teste_visual_completo.py`):**
- ✅ Explorar a interface
- ✅ Testar funcionalidades específicas
- ✅ Verificar design e UX
- ✅ Debug manual

**Teste Automatizado (`teste_visual_automatizado.py`):**
- ✅ Validação rápida após mudanças
- ✅ Testes de regressão
- ✅ CI/CD pipeline
- ✅ Documentação visual (screenshots)

---

### 🚀 Exemplo de Execução

```bash
# Teste automatizado
python teste_visual_automatizado.py

# Output:
🤖 TESTE VISUAL AUTOMATIZADO - PROJETO SOMBRA ROXA
📋 O que será testado:
   • Login e criação de conta
   • Conversas com personagens
   • Coleta de pistas
   • Navegação entre personagens

🧪 TESTE 1: Login e Criação de Conta
📝 Preenchendo formulário de login...
📸 Screenshot: 01_pagina_inicial.png
✅ Login realizado com sucesso!

🧪 TESTE 2: Conversa com Dr. Arnaldo
💬 Enviando: 'Olá Dr. Arnaldo'
📸 Screenshot: conversa_Dr_Arnaldo_01.png
✅ Mensagem 1/4 enviada

...

📊 RELATÓRIO FINAL
📈 Total de testes: 15
✅ Sucessos: 15
❌ Falhas: 0
📊 Taxa de sucesso: 100.0%
🎉 TODOS OS TESTES PASSARAM!
```

---

### 💡 Dicas

1. **ChromeDriver:**
   - Baixe em: https://chromedriver.chromium.org/
   - Adicione ao PATH do sistema
   - Ou coloque na pasta do projeto

2. **Screenshots:**
   - Use para documentação
   - Compare antes/depois de mudanças
   - Identifique bugs visuais

3. **Customização:**
   - Edite `teste_visual_automatizado.py`
   - Adicione mais testes conforme necessário
   - Ajuste timeouts se necessário

---

### 🐛 Troubleshooting

**Erro: ChromeDriver não encontrado**
```bash
# Instale o webdriver-manager
pip install webdriver-manager

# Ou baixe manualmente
# https://chromedriver.chromium.org/
```

**Erro: Servidor não responde**
```bash
# Verifique se porta 5000 está livre
# Ou inicie servidor manualmente em outra janela
python app.py
```

**Screenshots não são salvos**
```bash
# Verifique permissões da pasta
# Pasta será criada automaticamente
```

# 🤖 GUIA DE USO DA IA NO PROJETO

## ✅ A IA ESTÁ SENDO USADA? SIM!

O sistema usa **OpenAI GPT** para gerar respostas dinâmicas durante as entrevistas.

## 🔧 Como Funciona

### Sistema Híbrido (IA + Fallback)

```python
# Em app.py, linha ~50-70

# 1. Tenta usar OpenAI se configurado
if OPENAI_AVAILABLE and openai and openai.api_key:
    try:
        resp = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'system', 'content': ent['prompt_base']},
                {'role': 'user', 'content': message}
            ]
        )
        assistant_reply = resp.choices[0].message['content']
    except:
        # 2. Se falhar, usa resposta simulada
        assistant_reply = simulated_reply(ent, message)
else:
    # 3. Se não configurado, usa resposta simulada
    assistant_reply = simulated_reply(ent, message)
```

## 🎯 Quando a IA é Usada

### ✅ IA ATIVA (quando configurada)
- Respostas naturais e variadas
- Contexto completo da história
- Adaptação às perguntas do usuário
- Revelação gradual de informações
- Personalidade consistente dos personagens

### ⚠️ FALLBACK (sem configuração)
- Respostas baseadas em palavras-chave
- Funcionais mas menos naturais
- Funciona perfeitamente para protótipo
- Não requer API key

## 🔐 Como Ativar a IA (OpenAI)

### Passo 1: Obter API Key

1. Acesse: https://platform.openai.com/
2. Crie uma conta (ou faça login)
3. Vá em: **API Keys** → **Create new secret key**
4. Copie a chave (começa com `sk-...`)

### Passo 2: Configurar no Projeto

**Opção A: Arquivo `.env` (recomendado)**

```bash
# Na raiz do projeto
cd /workspaces/Project_Amazonia

# Crie o arquivo .env
cp .env.example .env

# Edite o arquivo
nano .env
```

Adicione sua chave:
```env
OPENAI_API_KEY=sk-sua-chave-aqui
OPENAI_MODEL=gpt-3.5-turbo
```

**Opção B: Variável de Ambiente**

```bash
export OPENAI_API_KEY="sk-sua-chave-aqui"
python app.py
```

### Passo 3: Reiniciar o Servidor

```bash
# Pare o servidor (Ctrl+C)
# Inicie novamente
python app.py
```

### Passo 4: Testar

Você verá no console:
```
✅ OpenAI disponível e configurado
```

Ou se não configurado:
```
⚠️ OpenAI não disponível - usando respostas simuladas
```

## 💰 Custos da API OpenAI

### GPT-3.5-turbo (Recomendado)
- **Preço**: ~$0.002 por 1.000 tokens
- **1 conversa típica**: ~500 tokens = $0.001 (muito barato!)
- **100 jogadas completas**: ~$0.50
- **Ideal para**: Educação, protótipos, uso moderado

### GPT-4 (Opcional - Melhor Qualidade)
```env
OPENAI_MODEL=gpt-4
```
- **Preço**: ~$0.03 por 1.000 tokens
- **Qualidade superior**: Respostas mais elaboradas
- **Recomendado para**: Demonstrações, versão final

### Créditos Gratuitos
- Novas contas ganham **$5 em créditos grátis**
- Suficiente para **centenas de jogadas completas**

## 🎭 Prompts dos Personagens

Cada personagem tem um **prompt base** detalhado:

### Dr. Arnaldo (Biólogo)
```python
prompt_base = """
Você é o Dr. Arnaldo Silva, biólogo do INPA.
Você está ATERRORIZADO.
Você descobriu a 'Sombra Roxa'...

[Instruções detalhadas sobre o que revelar]
"""
```

**A IA usa esse prompt para:**
- Manter personalidade consistente
- Saber o que revelar e quando
- Adaptar respostas às perguntas
- Criar diálogos naturais

## 🔍 Como Verificar se a IA Está Funcionando

### Teste 1: Logs do Servidor

```bash
# Ao iniciar app.py, você deve ver:
OPENAI_AVAILABLE = True  # ✅ Configurado
# ou
OPENAI_AVAILABLE = False # ⚠️ Não configurado
```

### Teste 2: Qualidade das Respostas

**Com IA:**
```
Você: O que é a Sombra Roxa?

Dr. Arnaldo: [respira fundo, nervoso] Olha, eu... 
eu realmente não deveria estar falando sobre isso. 
Mas você precisa entender - a "Sombra Roxa" não é 
apenas uma anomalia visual. É uma proliferação de 
algas tóxicas que descobri nas imagens de satélite...
```

**Sem IA (fallback):**
```
Você: O que é a Sombra Roxa?

Dr. Arnaldo: (Resposta de protótipo) Sobre 'Sombra Roxa', 
investigue mais com perguntas específicas.
```

### Teste 3: Console do Navegador

```javascript
// F12 → Console → Ao enviar mensagem

// Com IA:
"reply": "Resposta natural e elaborada..."

// Sem IA:
"reply": "(Resposta de protótipo)..."
```

## 🚨 Solução de Problemas

### Erro: "Invalid API Key"
```
❌ Problema: Chave incorreta
✅ Solução: Verifique se copiou a chave completa
```

### Erro: "Rate limit exceeded"
```
❌ Problema: Muitas requisições
✅ Solução: Aguarde 1 minuto ou upgrade do plano
```

### Erro: "Insufficient quota"
```
❌ Problema: Créditos esgotados
✅ Solução: Adicione créditos ou use fallback
```

### IA não responde (demora muito)
```
❌ Problema: Timeout da API
✅ Solução: Sistema usa fallback automaticamente
```

## 🎓 Para Professores: Quando Usar IA?

### ✅ Recomendado COM IA:
- Demonstrações em aula
- Apresentações públicas
- Experiência completa e imersiva
- Aulas com poucos grupos (5-10)

### ✅ Recomendado SEM IA (Fallback):
- Testes iniciais
- Turmas grandes (20+ grupos)
- Uso sem internet
- Sem orçamento para API

**Ambos funcionam perfeitamente!**

## 📊 Comparação

| Aspecto | Com IA | Sem IA (Fallback) |
|---------|--------|-------------------|
| **Respostas** | Naturais, variadas | Baseadas em keywords |
| **Imersão** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Custo** | ~$0.005/jogada | Grátis |
| **Setup** | API Key necessária | Zero config |
| **Offline** | ❌ Requer internet | ✅ Funciona offline |
| **Educacional** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ (mesmo valor!) |

## 🎮 Exemplo de Conversa Completa (COM IA)

```
👨‍🎓 Grupo: O que é a Sombra Roxa?

👨‍🔬 Dr. Arnaldo: [voz trêmula] A "Sombra Roxa"... 
eu dei esse nome. Foi o que vi nas imagens de 
satélite - uma mancha púrpura no rio, acima da 
Fazenda Nova Fronteira. No início, pensei que 
fosse apenas algas, mas quando analisamos... 
[pausa] É um coquetel químico muito específico. 
Não é mercúrio comum de garimpo. É algo industrial, 
usado para processar Coltan - aquele mineral de 
celulares. Mas não há minas oficiais ali! Eu contei 
isso à Clara e ela... ela foi investigar o Valdemar. 
[olha ao redor nervoso] Desde então, tenho recebido 
ameaças.

👨‍🎓 Grupo: Quem está ameaçando você?

👨‍🔬 Dr. Arnaldo: [sussurrando] Não sei ao certo, 
mas Clara mencionou um "Homem de Terno" que apareceu 
na fazenda. Alguém de Brasília. Olha, você precisa 
falar com o Valdemar. Ele está escondendo algo. 
Aquela fazenda não é o que parece ser...
```

## 🔧 Monitoramento de Uso

### Ver uso da API
1. Acesse: https://platform.openai.com/usage
2. Veja quanto gastou
3. Configure alertas de limite

### Limitar gastos
```python
# Em app.py, adicione:
max_tokens=400  # Limita resposta (economiza)
```

## 🎯 Conclusão

**A IA OpenAI:**
- ✅ Está implementada e funcional
- ✅ Melhora muito a experiência
- ✅ É opcional (fallback funciona bem)
- ✅ Tem custo baixíssimo para educação
- ✅ Fácil de configurar

**Recomendação:**
- 🎓 Professores: Usem IA para demonstrações
- 👨‍💻 Desenvolvedores: Testem sem IA primeiro
- 🎮 Alunos: Ambas versões são divertidas!

---

**🤖 A IA está pronta para tornar a investigação ainda mais realista!**

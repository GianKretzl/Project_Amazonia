# 🔑 GUIA RÁPIDO: API KEY FREESOUND.ORG

## 📝 Passo a Passo (5 minutos)

### 1️⃣ Criar Conta (2 minutos)

1. Acesse: **https://freesound.org/home/register/**

2. Preencha o formulário:
   - Username: (escolha um)
   - Email: seu email
   - Password: (escolha uma senha)

3. Clique em **"Sign Up"**

4. Verifique seu email e clique no link de confirmação

---

### 2️⃣ Solicitar API Key (1 minuto)

1. Faça login em: **https://freesound.org/home/login/**

2. Acesse: **https://freesound.org/apiv2/apply/**

3. Preencha o formulário:
   - **Name:** Projeto Encruzilhada (ou qualquer nome)
   - **Description:** Educational game about Amazon deforestation
   - **URL:** http://localhost:5000 (pode deixar vazio se não tiver)
   - **Accepted terms:** ✅ Marque a caixa

4. Clique em **"Apply for a key"**

---

### 3️⃣ Copiar API Key (30 segundos)

Após solicitar, você verá uma página com:

```
Client id: XXXXXXXXXXXXXXXXXXXX
Api key: YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
```

**Copie apenas o "Api key"** (a linha mais longa)

---

### 4️⃣ Configurar no Projeto (30 segundos)

Cole a API key no arquivo `.env`:

```bash
# Abrir o arquivo .env
nano .env
```

Adicione esta linha no final:

```bash
# Freesound API Key
FREESOUND_API_KEY=cole_sua_api_key_aqui
```

Salve: `Ctrl+O` → `Enter` → `Ctrl+X`

---

### 5️⃣ Executar o Download (2 minutos)

```bash
# Verificar se está configurado
python baixar_audios.py

# Selecionar opção 1 (Freesound automático)
```

---

## 🚀 ATALHO DIRETO

**Links diretos:**

1. **Cadastro:** https://freesound.org/home/register/
2. **Login:** https://freesound.org/home/login/
3. **API Key:** https://freesound.org/apiv2/apply/
4. **Minhas Credenciais:** https://freesound.org/apiv2/apply/ (após login)

---

## ⚡ COMANDO COMPLETO

Depois de configurar a API key:

```bash
# Exportar variável (temporário - só funciona nesta sessão)
export FREESOUND_API_KEY='sua_chave_aqui'

# OU adicionar no .env (permanente)
echo "FREESOUND_API_KEY=sua_chave_aqui" >> .env

# Executar download
python baixar_audios.py
```

---

## 🔍 VERIFICAR SE FUNCIONOU

```bash
# Testar se a API key está funcionando
python -c "import os; print('✅ API Key configurada!' if os.getenv('FREESOUND_API_KEY') else '❌ API Key não encontrada')"
```

---

## 💡 ALTERNATIVA MAIS RÁPIDA

Se preferir não esperar aprovação da API key, use sons do Freesound **manualmente**:

### Buscar e Baixar Direto (sem API):

1. **Laboratório:**
   - Acesse: https://freesound.org/search/?q=laboratory+ambience
   - Escolha um som
   - Clique em "Download" (precisa estar logado)
   - Renomeie para `lab_ambiente.mp3`

2. **Fazenda:**
   - Busque: https://freesound.org/search/?q=farm+cattle
   - Download → `fazenda_ambiente.mp3`

3. **Floresta:**
   - Busque: https://freesound.org/search/?q=jungle+night
   - Download → `aldeia_ambiente.mp3`

4. Continue para os outros 7 áudios...

**Salvar todos em:** `/workspaces/Project_Amazonia/static/audio/`

---

## 📋 CHECKLIST

- [ ] Criar conta no Freesound.org
- [ ] Verificar email
- [ ] Solicitar API Key
- [ ] Copiar API Key
- [ ] Adicionar no `.env`
- [ ] Executar `python baixar_audios.py`
- [ ] Testar o jogo: `python app.py`

---

## ⏱️ TEMPO TOTAL

- **Com API:** 5 min (setup) + 2 min (download) = **7 minutos**
- **Manual (sem API):** 15-20 minutos (baixar cada som)

---

**🎯 RECOMENDAÇÃO:** Use a API key! É mais rápido depois de configurar.

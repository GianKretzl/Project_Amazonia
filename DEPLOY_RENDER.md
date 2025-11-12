# 🚀 GUIA DE DEPLOY NO RENDER.COM

## Passo a Passo

### 1️⃣ Preparar Repositório GitHub
```bash
git add .
git commit -m "feat: PostgreSQL + Render deploy config"
git push origin main
```

### 2️⃣ Criar Conta no Render
- Acesse: https://render.com
- Faça login com GitHub
- Autorize acesso ao repositório

### 3️⃣ Criar Banco de Dados PostgreSQL

1. No Dashboard do Render, clique em **"New +"**
2. Escolha **"PostgreSQL"**
3. Configurações:
   - **Name**: `project-amazonia-db`
   - **Database**: `project_amazonia`
   - **User**: (gerado automaticamente)
   - **Region**: Oregon (US West)
   - **Plan**: Free
4. Clique em **"Create Database"**
5. **IMPORTANTE**: Copie o **Internal Database URL** (começa com `postgres://`)

### 4️⃣ Criar Web Service

1. No Dashboard, clique em **"New +"**
2. Escolha **"Web Service"**
3. Conecte o repositório **Project_Amazonia**
4. Configurações:
   - **Name**: `project-amazonia`
   - **Region**: Oregon (US West)
   - **Branch**: `main`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt && chmod +x build.sh && ./build.sh`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free

### 5️⃣ Configurar Variáveis de Ambiente

No painel do Web Service, vá em **"Environment"** e adicione:

```
DATABASE_URL = [cole o Internal Database URL do PostgreSQL]
SECRET_KEY = [gere uma chave aleatória forte]
FLASK_ENV = production
FLASK_DEBUG = 0
OPENAI_API_KEY = [opcional - sua chave OpenAI]
```

**Gerar SECRET_KEY** (rode no terminal):
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 6️⃣ Deploy!

Clique em **"Create Web Service"**

O Render vai:
1. ✅ Clonar o repositório
2. ✅ Instalar dependências
3. ✅ Executar build.sh (inicializar banco)
4. ✅ Iniciar servidor Gunicorn
5. ✅ Fornecer URL pública (ex: `https://project-amazonia.onrender.com`)

### 7️⃣ Monitorar Deploy

- Logs em tempo real disponíveis no painel
- Primeiro deploy leva ~5 minutos
- Free tier "dorme" após 15 min de inatividade (acorda em ~30s)

## 🔧 Atualizações Futuras

Toda vez que fizer `git push origin main`, o Render redeploy automaticamente!

## 🌐 Acessar Aplicação

Após deploy, sua URL será algo como:
```
https://project-amazonia.onrender.com
```

## 🐛 Troubleshooting

### Erro de DATABASE_URL
- Verifique se copiou o **Internal Database URL** correto
- Certifique-se que começa com `postgres://` ou `postgresql://`

### Erro 502 Bad Gateway
- Aguarde ~1 minuto (servidor iniciando)
- Verifique logs no painel do Render

### Tabelas não criadas
- Verifique logs do build.sh
- Banco é inicializado automaticamente no build

## 💰 Custos

- **Free Tier**: 750 horas/mês
- **Limitações**:
  - Dorme após 15 min inatividade
  - PostgreSQL: 90 dias (depois expira dados)
  - 512 MB RAM

## 🚀 Upgrade para Produção Real

Para uso 24/7 sem sleep:
- Upgrade para Starter Plan ($7/mês)
- PostgreSQL Starter ($7/mês)
- Total: $14/mês

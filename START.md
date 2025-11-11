# 🚀 GUIA RÁPIDO - INÍCIO IMEDIATO

## ⚡ Começar Agora (3 passos)

### 1️⃣ Inicie o Servidor
```bash
cd /workspaces/Project_Amazonia
python app.py
```

### 2️⃣ Abra o Navegador
```
http://localhost:5000
```

### 3️⃣ Faça Login
- Digite nome do grupo
- Adicione pelo menos 1 integrante
- Clique em "INICIAR INVESTIGAÇÃO"

**Pronto! Você está dentro do sistema.**

---

## 🎮 Fluxo do Jogo

```
LOGIN → INTRO → BRIEFING → ENTREVISTAS → RESOLVER O CASO
  1      2         3           4             5
```

### 1. LOGIN (Página inicial)
- Identifique seu grupo
- Máximo 6 integrantes

### 2. INTRO (Após login)
- Background da Amazônia revelando
- Áudio corrompido de Clara
- Prólogo da história

### 3. BRIEFING
- Entenda a missão
- Veja os 4 atos
- Saiba como jogar

### 4. ENTREVISTAS
- Fale com Dr. Arnaldo (desbloqueado)
- Colete pistas
- Desbloqueie novos personagens
- Conecte as informações

### 5. RESOLVER
- Confronte o vilão final
- Revele a conspiração
- Complete o dossiê

---

## 💡 Dicas Essenciais

### Perguntas que Funcionam Bem

**Dr. Arnaldo:**
- "O que é a Sombra Roxa?"
- "Que químico causa isso?"
- "Onde você viu a anomalia?"

**Seu Valdemar:**
- "Sua fazenda dá lucro?"
- "Por que quer a terra indígena?"

**Pajé Yakamu:**
- "O que é o Mapa da Montanha de Fogo?"
- "Quem é o Homem de Terno?"

**Deputado Venturi:**
- Acuse diretamente!
- Use todas as 3 pistas coletadas

### Como Coletar Pistas

1. Faça perguntas específicas
2. Quando o personagem revelar algo importante
3. Botão "🔍 Coletar pista" aparece
4. Clique para adicionar ao dossiê
5. Novas entidades desbloqueiam automaticamente

---

## 🔧 IA: Usar ou Não?

### SEM IA (Padrão)
- ✅ Funciona imediatamente
- ✅ Zero configuração
- ✅ Grátis
- ⚠️ Respostas baseadas em keywords

### COM IA (OpenAI)
- ✅ Respostas naturais e elaboradas
- ✅ Experiência mais imersiva
- ⚠️ Precisa configurar API key
- ⚠️ Custo mínimo (~$0.005/jogo)

**Como ativar IA:**
```bash
# 1. Obtenha chave em: platform.openai.com
# 2. Crie arquivo .env
cp .env.example .env

# 3. Edite e adicione:
OPENAI_API_KEY=sk-sua-chave-aqui

# 4. Reinicie servidor
```

**Recomendação:** Teste SEM IA primeiro!

---

## ⚠️ Problemas Comuns

### Página não carrega
```bash
# Verifique se servidor está rodando
# Deve mostrar: "Running on http://127.0.0.1:5000"
```

### Login não funciona
```bash
# Limpe cookies do navegador
# Ou use modo anônimo
```

### Pistas não desbloqueiam
```bash
# Certifique-se de CLICAR no botão "Coletar pista"
# Não desbloqueia automaticamente!
```

### CSS não carrega
```bash
# Force refresh: Ctrl+Shift+R (Windows/Linux)
# Ou: Cmd+Shift+R (Mac)
```

---

## 📱 Atalhos do Teclado

| Tecla | Ação |
|-------|------|
| F12 | Abrir DevTools |
| Ctrl+Shift+R | Force refresh |
| Ctrl+- | Zoom out |
| Ctrl++ | Zoom in |
| F5 | Recarregar |

---

## 🎓 Para Professores

### Antes da Aula
1. ✅ Teste o jogo você mesmo
2. ✅ Divida turma em grupos de 2-6
3. ✅ Prepare computador/projetor
4. ✅ (Opcional) Configure IA

### Durante a Aula (50 min)
- **5 min:** Introdução ao tema Amazônia
- **5 min:** Explicar o jogo e login
- **30 min:** Grupos jogam
- **10 min:** Discussão das descobertas

### Após a Aula
- Discuta: Ciências, Geografia, História
- Conecte com temas do currículo
- Reflita sobre trabalho em equipe

---

## 📊 Tempo Estimado

| Etapa | Tempo |
|-------|-------|
| Login | 2 min |
| Intro | 3 min |
| Briefing | 5 min |
| Dr. Arnaldo | 7 min |
| Valdemar | 7 min |
| Pajé | 7 min |
| Deputado | 5 min |
| **TOTAL** | **30-35 min** |

---

## 🏆 Objetivos de Aprendizagem

### Ciências
- ✅ Poluição química
- ✅ Bioacumulação
- ✅ Impactos ambientais

### Geografia
- ✅ Uso do solo
- ✅ Conflitos territoriais
- ✅ Economia vs preservação

### História
- ✅ Direitos indígenas
- ✅ Memória ancestral
- ✅ Exploração de recursos

### Habilidades
- ✅ Pensamento crítico
- ✅ Investigação
- ✅ Trabalho em equipe
- ✅ Conexão interdisciplinar

---

## 📞 Suporte

### Documentação Completa
- `README.md` - Visão geral
- `GUIA_IA.md` - Tudo sobre IA
- `NOVAS_FUNCIONALIDADES.md` - Features
- `TROUBLESHOOTING.md` - Soluções
- `IMPLEMENTACOES_CONCLUIDAS.md` - Resumo técnico

### Logs de Debug
```bash
# Veja erros no terminal onde rodou:
python app.py

# Ou no navegador (F12 → Console)
```

---

## ✅ Checklist Pré-Jogo

- [ ] Servidor rodando (localhost:5000)
- [ ] Navegador aberto
- [ ] Grupos definidos
- [ ] Nomes dos integrantes prontos
- [ ] (Opcional) IA configurada
- [ ] Projetor/tela para demonstração

**Tudo pronto? Comece a investigação! 🚀**

---

## 🎯 Meta do Jogo

**Descobrir:**
- ❓ O que é a "Sombra Roxa"?
- ❓ Quem está por trás da conspiração?
- ❓ O que aconteceu com Gian Kretzl?

**Conectar pistas de:**
- 🧪 Ciências (anomalia química)
- 🗺️ Geografia (fazenda fachada)
- 📜 História (território ancestral)

**Resultado:**
- 📂 Dossiê completo
- 🎓 Aprendizado multidisciplinar
- 🏆 Caso resolvido!

---

**🎮 Boa investigação, estagiário!**

*"Não deixe eles vencerem. Confie apenas no que você conectar..."* - Gian Kretzl

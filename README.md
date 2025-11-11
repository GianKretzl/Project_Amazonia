# 🎮 Projeto Sombra Roxa

**Um thriller investigativo interativo sobre a Amazônia**

![Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0+-green.svg)

## 📖 A História

Você é um **estagiário de jornalismo** que encontrou o notebook de **Gian Kretzl**, um jornalista investigativo desaparecido há 3 dias na Amazônia Legal.

No sistema dele, você descobre um arquivo de áudio corrompido - sua última mensagem antes de desaparecer. Ele menciona algo chamado **"Sombra Roxa"**, uma conspiração envolvendo a Fazenda Nova Fronteira, e um mapa secreto nas terras indígenas.

### 🎯 Sua Missão

- Descobrir o que é a "Sombra Roxa"
- Entrevistar as fontes do Gian usando IA
- Conectar pistas de **Ciências**, **Geografia** e **História**
- Expor a conspiração
- Descobrir o que aconteceu com o Gian

## 🎭 Personagens

### Ato I: A Pista Científica (Ciências)
**👨‍🔬 Dr. Arnaldo Silva** - Biólogo do INPA
- Desbloqueado desde o início
- Descobriu a "Sombra Roxa" - uma anomalia química no rio
- Está aterrorizado e recebendo ameaças

### Ato II: A Fachada (Geografia)
**🧑‍🌾 "Seu" Valdemar** - Dono da Fazenda Nova Fronteira
- Desbloqueado após coletar pista do Biólogo
- Arrogante e defensivo
- Esconde um segredo sobre sua fazenda

### Ato III: O Mapa (História)
**🌿 Pajé Yakamu** - Líder Indígena
- Desbloqueado após descobrir a fachada
- Guardião de conhecimento ancestral
- Possui o "Mapa da Montanha de Fogo"

### Clímax: O Dossiê Final
**🤵 Deputado Venturi** - Político
- Desbloqueado após todas as pistas
- O verdadeiro vilão da história
- Confronte-o com todas as evidências

## 🎮 Como Jogar

### Instalação

```bash
# Clone o repositório
git clone <repo-url>
cd Project_Amazonia

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente (opcional - para IA real)
cp .env.example .env
# Edite .env e adicione sua OPENAI_API_KEY (opcional)

# Execute o servidor
python app.py
```

### Acesse o jogo

Abra seu navegador em: `http://localhost:5000`

### Primeiro Acesso - Login de Grupo

1. **Tela de Login** aparecerá primeiro
2. **Digite o nome do grupo** (ex: "Investigadores da Turma A")
3. **Adicione os integrantes** (mínimo 1, máximo 6)
4. **Clique em "INICIAR INVESTIGAÇÃO"**
5. **Aguarde o loading** e redirecionamento
6. **Background da Amazônia** se revelará progressivamente
7. **Seu grupo** aparecerá no topo da tela

### Gameplay

1. **Explore o Briefing** - Entenda a missão e os objetivos
2. **Entre na Sala de Entrevistas** - Veja as fontes disponíveis
3. **Entreviste as entidades desbloqueadas** - Faça perguntas estratégicas
4. **Colete pistas** - Botões aparecem quando você descobre informações importantes
5. **Desbloqueie novos personagens** - Conecte as pistas para avançar
6. **Monte o dossiê completo** - Confronte o vilão final

## 💡 Dicas para Jogar

### Perguntas Estratégicas

**Para o Dr. Arnaldo:**
- "O que é a Sombra Roxa?"
- "Que tipo de químico causa isso?"
- "Onde você viu essa anomalia?"

**Para o Seu Valdemar:**
- "Sua fazenda dá lucro?"
- "Por que quer expandir para a reserva indígena?"
- "O que você sabe sobre Coltan?"

**Para o Pajé Yakamu:**
- "O que há em sua terra ancestral?"
- "O que é o Mapa da Montanha de Fogo?"
- "Quem é o Homem de Terno?"

**Para o Deputado Venturi:**
- Use as 3 pistas coletadas para confrontá-lo
- Acuse-o diretamente da conspiração

## 🛠️ Tecnologias

- **Backend**: Flask (Python)
- **IA**: OpenAI GPT (opcional - funciona com respostas simuladas)
- **Sessão**: Flask Sessions para persistência de dados do grupo
- **Frontend**: HTML5, CSS3, JavaScript ES6+
- **Visualização**: Excalibur.js (engine de games 2D)
- **Animações**: CSS Animations + Canvas API
- **Design**: Terminal/Cyber/Investigativo com revelação progressiva
- **Fonts**: Google Fonts (Courier Prime, Share Tech Mono)

## 🎨 Recursos Visuais

- ✨ **Tela de Login** com identificação de grupo e integrantes
- 🎭 **Animações de terminal** com efeito de digitação
- 🌟 **Visualização interativa** com Excalibur.js
- 💫 **Efeitos de partículas** ao desbloquear personagens
- � **Interface estilo investigação** policial
- 🌌 **Tema dark** com tons roxos e verdes néon
- 🌄 **Background revelador** - imagem da Amazônia aparece progressivamente
- 👥 **Banner de grupo** exibindo equipe de investigadores

## 📋 Estrutura do Projeto

```
Project_Amazonia/
├── app.py                 # Servidor Flask principal
├── entidades.py          # Definição dos personagens e prompts
├── requirements.txt      # Dependências Python
├── README.md            # Este arquivo
├── GUIA_IA.md           # Guia sobre uso da IA
├── NOVAS_FUNCIONALIDADES.md  # Documentação das features
├── templates/           # Templates HTML
│   ├── login.html       # Tela de login do grupo
│   ├── index.html       # Página inicial (prólogo)
│   ├── briefing.html    # Briefing da missão
│   └── interview.html   # Sala de entrevistas
├── static/
│   ├── css/
│   │   └── style.css    # Estilos do tema
│   ├── js/
│   │   ├── main.js      # Script da página inicial
│   │   └── interview.js # Sistema de entrevistas
│   └── img/            # Imagens (opcional)
└── .env                # Configurações (criar)
```

## 🔧 Configuração Avançada

### Com OpenAI (IA Real)

1. Crie uma conta em [OpenAI](https://platform.openai.com/)
2. Obtenha uma API Key
3. Configure no `.env`:

```env
OPENAI_API_KEY=sua-chave-aqui
OPENAI_MODEL=gpt-3.5-turbo
SECRET_KEY=sua-secret-key-aleatoria
```

### Modo Protótipo (Sem IA)

O jogo funciona perfeitamente sem OpenAI usando respostas simuladas baseadas em palavras-chave.

## 🎓 Aspectos Educacionais

Este jogo ensina:

- **Ciências**: Ecologia, contaminação química, bioacumulação
- **Geografia**: Uso do solo, conflitos territoriais, economia agrícola
- **História**: Direitos indígenas, memória ancestral, colonização
- **Pensamento Crítico**: Conectar pistas, questionar fontes
- **Jornalismo Investigativo**: Fazer perguntas estratégicas

## 🐛 Solução de Problemas

### O servidor não inicia
```bash
pip install --upgrade flask python-dotenv openai
```

### As entidades não desbloquei
- Certifique-se de clicar em "Coletar pista" quando aparecer
- Verifique o console do navegador (F12) para erros

### Excalibur.js não carrega
- Verifique sua conexão com a internet (CDN)
- Abra o console do navegador para ver erros

## 🤝 Contribuindo

Sinta-se livre para:
- Adicionar novos personagens
- Criar novos atos da história
- Melhorar os prompts da IA
- Adicionar efeitos visuais
- Traduzir para outros idiomas

## 📜 Licença

Este projeto é educacional e open-source.

## 👏 Créditos

- **História Original**: Inspirada em casos reais na Amazônia
- **Game Engine**: Excalibur.js
- **IA**: OpenAI GPT
- **Framework Web**: Flask

---

**🎮 Boa investigação, estagiário! Gian está contando com você.**

*"Não deixe eles vencerem. Confie apenas no que você conectar..."* - Gian Kretzl
# Project_Amazonia
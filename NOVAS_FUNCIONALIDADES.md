# 🎮 NOVAS FUNCIONALIDADES IMPLEMENTADAS

## ✅ Sistema de Login de Grupo

### 📋 Tela de Login (`/`)
- **Formulário de identificação do grupo**
  - Campo para nome do grupo (obrigatório)
  - Até 6 integrantes (mínimo 1)
  - Botão para adicionar/remover integrantes dinamicamente
  - Validação de dados no frontend e backend
  
- **Recursos visuais**
  - Design cyberpunk consistente com o tema
  - Animações de entrada dos campos
  - Efeitos de hover e focus
  - Loading screen após submit
  - Redirecionamento suave para /intro

### 🔐 Backend de Autenticação

#### Nova API: `/api/login` (POST)
```json
{
  "grupo": "Nome do Grupo",
  "integrantes": ["Nome 1", "Nome 2", "Nome 3"]
}
```

**Validações:**
- Grupo não pode estar vazio
- Mínimo 1, máximo 6 integrantes
- Dados salvos na sessão Flask
- Timestamp de login registrado

#### Nova API: `/api/grupo-info` (GET)
Retorna informações do grupo logado:
```json
{
  "grupo": "Nome do Grupo",
  "integrantes": ["Nome 1", "Nome 2", "Nome 3"]
}
```

### 📊 Sessão Persistente

**Dados armazenados na sessão:**
- `grupo`: Nome do grupo
- `integrantes`: Lista de nomes
- `login_timestamp`: Data/hora do login
- `pistas`: Pistas coletadas (já existente)

## 🎨 Efeito de Revelação Progressiva

### 🌄 Background Animado na Página Intro

**Como funciona:**
1. Ao entrar em `/intro` (após login), o background começa invisível
2. Após 1 segundo, inicia animação de revelação circular
3. A imagem da Amazônia vai aparecendo progressivamente
4. Transição suave de 4 segundos
5. Background fica semi-transparente (opacity: 0.3) para não atrapalhar a leitura

**Técnica CSS:**
- `clip-path: circle()` para criar efeito circular
- Transição de 0% para 150% do raio
- Background fixo com `background-attachment: fixed`
- Overlay com gradient para melhor legibilidade

### 🎯 Banner de Informação do Grupo

**Localização:** Topo da página `/intro`

**Exibe:**
- 👥 Nome do grupo
- 🎓 Lista de todos os integrantes
- Animação de slide down ao aparecer
- Design integrado ao tema do terminal

## 🔄 Fluxo do Usuário Atualizado

```
1. Acessa http://localhost:5000
   ↓
2. Vê tela de LOGIN
   ↓
3. Preenche nome do grupo
   ↓
4. Adiciona integrantes (1-6)
   ↓
5. Clica em "INICIAR INVESTIGAÇÃO"
   ↓
6. Loading screen (3 segundos)
   ↓
7. Redireciona para /intro
   ↓
8. Background da Amazônia se revela progressivamente
   ↓
9. Banner do grupo aparece no topo
   ↓
10. Vê o prólogo da história
   ↓
11. Acessa Briefing ou Entrevistas
```

## 📁 Arquivos Modificados

### Novos Arquivos
- `templates/login.html` - Tela de login do grupo

### Arquivos Modificados
- `app.py` - Rotas de login e API
- `templates/index.html` - Background revelador + banner de grupo
- `static/css/style.css` - Estilos do login e revelação

## 🎨 Elementos Visuais Adicionados

### Login Page
- ✅ Card de login com borda roxa brilhante
- ✅ Inputs com efeito focus elegante
- ✅ Botões de adicionar/remover integrantes
- ✅ Contador visual de integrantes
- ✅ Loading spinner animado
- ✅ Barra de progresso
- ✅ Validação visual em tempo real

### Intro Page
- ✅ Background da Amazônia (Unsplash)
- ✅ Efeito de revelação circular
- ✅ Overlay semi-transparente
- ✅ Terminal com backdrop blur
- ✅ Banner de grupo animado
- ✅ Status "ONLINE" (antes era "OFFLINE")

## 🔧 Configuração da Imagem de Background

**Opção 1: Usar imagem online (atual)**
```css
background-image: url('https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=1920&q=80');
```

**Opção 2: Usar imagem local**
1. Baixe uma imagem da Amazônia
2. Salve em `/static/img/amazonia-background.jpg`
3. Atualize o CSS:
```css
background-image: url('/static/img/amazonia-background.jpg');
```

**Sugestões de imagens:**
- Floresta amazônica aérea
- Rio Amazonas
- Comunidade indígena
- Garimpo ilegal (para dramaticidade)

## 🎮 Como Testar

### 1. Acesse a página de login
```
http://localhost:5000
```

### 2. Preencha o formulário
- Grupo: "Investigadores da Turma A"
- Integrantes:
  - João Silva
  - Maria Santos
  - Pedro Costa

### 3. Clique em "INICIAR INVESTIGAÇÃO"

### 4. Observe:
- ✅ Loading screen aparece
- ✅ Redirecionamento para /intro
- ✅ Background se revela aos poucos
- ✅ Banner do grupo aparece no topo
- ✅ Prólogo da história carrega

## 📊 Dados Persistentes

**Durante toda a sessão:**
- Nome do grupo é mantido
- Lista de integrantes é preservada
- Pistas coletadas são acumuladas
- Entidades desbloqueadas permanecem

**Quando a sessão expira:**
- Usuário retorna para a tela de login
- Deve preencher novamente
- Investigação recomeça do zero

## 🚀 Próximas Melhorias Sugeridas

### Curto Prazo
- [ ] Adicionar avatar/ícone do grupo
- [ ] Salvar progresso no localStorage
- [ ] Mostrar tempo de investigação
- [ ] Ranking de grupos mais rápidos

### Médio Prazo
- [ ] Banco de dados para persistência
- [ ] Sistema de salas/turmas para professores
- [ ] Exportar relatório PDF com nome do grupo
- [ ] Histórico de investigações

### Longo Prazo
- [ ] Modo competitivo entre grupos
- [ ] Certificado de conclusão personalizado
- [ ] Dashboard do professor
- [ ] Analytics de gameplay por grupo

## 🎯 Objetivo Educacional

O sistema de login em grupo:
- ✅ Incentiva trabalho colaborativo
- ✅ Identifica responsáveis pela investigação
- ✅ Permite rastreamento do progresso
- ✅ Cria senso de pertencimento
- ✅ Facilita avaliação pelo professor

## 💡 Uso em Sala de Aula

### Para Professores

**Antes da aula:**
1. Divida a turma em grupos de 2-6 alunos
2. Cada grupo escolhe um nome criativo
3. Um aluno será o "digitador" (pode revezar)

**Durante a aula:**
1. Grupos fazem login com seus nomes
2. Trabalham juntos para resolver o mistério
3. Discutem as pistas antes de coletar
4. Tomam decisões coletivas

**Após a aula:**
1. Grupos apresentam suas descobertas
2. Comparam estratégias de investigação
3. Discutem os temas multidisciplinares
4. Refletem sobre trabalho em equipe

---

**Status: ✅ SISTEMA DE LOGIN IMPLEMENTADO E FUNCIONAL!**

🎮 **Agora os grupos podem se identificar antes de iniciar a investigação!**

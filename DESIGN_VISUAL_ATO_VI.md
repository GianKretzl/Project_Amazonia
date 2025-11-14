# 🎬 DESIGN VISUAL - ATO VI: O CONFRONTO FINAL
## 🎯 A Exposição da Conspiração no Projeto Encruzilhada

---

## 📖 VISÃO GERAL

O **ATO VI** é o **clímax narrativo** onde o jogador confronta o Deputado Venturi com todas as evidências coletadas. É uma experiência **cinematográfica e interativa** que revela toda a conspiração.

---

## 🎭 FLUXO VISUAL COMPLETO

### **FASE 1: DESBLOQUEIO DRAMÁTICO** 🚨

Após conversar com o Coronel Silva e coletar as 3 pistas finais:

```
╔══════════════════════════════════════════════════════════╗
║  🎖️ Coronel Silva revelou tudo...                       ║
║                                                          ║
║  [ANIMAÇÃO: Tela treme levemente]                       ║
║  [SOM: Alerta crítico + estática de rádio]              ║
║                                                          ║
║  ⚠️  SISTEMA ATUALIZADO                                  ║
║                                                          ║
║  O VILÃO FINAL FOI IDENTIFICADO.                         ║
║                                                          ║
║  🤵 DEPUTADO VENTURI - DESBLOQUEADO                      ║
║                                                          ║
║  [Botão pulsando em vermelho]                           ║
║  ┌─────────────────────────────┐                        ║
║  │  🎯 INICIAR CONFRONTO FINAL │  ← Animação pulsante   ║
║  └─────────────────────────────┘                        ║
╚══════════════════════════════════════════════════════════╝
```

**Elementos Visuais:**
- ✅ Background escurece (overlay preto 70%)
- ✅ Modal central com borda vermelha pulsante
- ✅ Ícone de alerta girando
- ✅ Texto digitado letra por letra (efeito máquina de escrever)
- ✅ Botão com efeito glow vermelho

**Áudios:**
- 🔊 `alerta_critico.mp3` (som de alerta)
- 🔊 `estatica_radio.mp3` (interferência)
- 🔊 Música de tensão crescente (fade in)

---

### **FASE 2: INTERFACE DE CONFRONTO** 🎯

Ao clicar no botão, a tela **transforma completamente**:

```
╔═══════════════════════════════════════════════════════════════════╗
║                   🏛️ SALA DE ACUSAÇÃO                             ║
║                                                                   ║
║  ┌────────────────────────────────────────────────────────────┐  ║
║  │  [VÍDEO/IMAGEM: Sala escura, mesa de interrogatório]      │  ║
║  │  [Deputado Venturi sentado, sorriso confiante]            │  ║
║  │                                                            │  ║
║  │  💬 Venturi: "Jovem jornalista... você tem coragem       │  ║
║  │             de me acusar? Cuidado com o que diz..."      │  ║
║  └────────────────────────────────────────────────────────────┘  ║
║                                                                   ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ║
║                                                                   ║
║  📂 SEU DOSSIÊ (15/15 pistas coletadas)                         ║
║                                                                   ║
║  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐           ║
║  │ 🟣 C02  │  │ 🟢 G02  │  │ 🔵 H02  │  │ 🔴 O01  │  ...      ║
║  │ Química │  │ Fachada │  │  Mapa   │  │Ratanabá │           ║
║  │ Coltan  │  │Logística│  │ Coltan  │  │ =Falso  │           ║
║  └─────────┘  └─────────┘  └─────────┘  └─────────┘           ║
║     ↓ Arraste para acusar ↓                                     ║
║                                                                   ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ║
║                                                                   ║
║  🎯 ZONA DE ACUSAÇÃO (Arraste as pistas aqui)                   ║
║  ┌───────────────────────────────────────────────────────────┐  ║
║  │                                                            │  ║
║  │         [Área para arrastar pistas - vazia]               │  ║
║  │                                                            │  ║
║  │  💡 Dica: Conecte 3 pistas que provam a operação ilegal  │  ║
║  └───────────────────────────────────────────────────────────┘  ║
║                                                                   ║
║  [Botão ACUSAR - ainda desabilitado]                            ║
╚═══════════════════════════════════════════════════════════════════╝
```

**Mecânica Visual:**
- ✅ Cards de pistas são **arrastáveis** (drag & drop)
- ✅ Pistas corretas **brilham verde** ao passar sobre zona de acusação
- ✅ Pistas erradas **tremem** e voltam
- ✅ Cada pista tem **tooltip** com conteúdo resumido
- ✅ Contador de pistas selecionadas: `0/3 pistas`

**CSS/Animações:**
```css
.pista-card {
  cursor: grab;
  transition: transform 0.3s, box-shadow 0.3s;
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

.pista-card:hover {
  transform: translateY(-5px) scale(1.05);
  box-shadow: 0 8px 16px rgba(0,0,0,0.3);
}

.pista-card.dragging {
  opacity: 0.5;
  cursor: grabbing;
}

.zona-acusacao.valid-drop {
  border: 3px solid #00ff00;
  box-shadow: 0 0 20px rgba(0,255,0,0.5);
}

.zona-acusacao.invalid-drop {
  border: 3px solid #ff0000;
  animation: shake 0.5s;
}
```

---

### **FASE 3: ROUND 1 - A OPERAÇÃO** 🕵️

Jogador arrasta as pistas corretas:
- **PISTA-C02:** Química_Coltan
- **PISTA-G02:** Fazenda_Fachada_Logística  
- **PISTA-H02:** Trilha_Ancestrais_Mapa_Coltan

```
╔═══════════════════════════════════════════════════════════════════╗
║  🎯 ZONA DE ACUSAÇÃO - ROUND 1                                    ║
║  ┌───────────────────────────────────────────────────────────┐   ║
║  │  [PISTA ARRASTADA: 🟣 Química_Coltan]                     │   ║
║  │  [PISTA ARRASTADA: 🟢 Fazenda_Fachada_Logística]          │   ║
║  │  [PISTA ARRASTADA: 🔵 Trilha_Ancestrais_Mapa_Coltan]      │   ║
║  │                                                            │   ║
║  │  ✅ 3/3 PISTAS CONECTADAS                                 │   ║
║  └───────────────────────────────────────────────────────────┘   ║
║                                                                   ║
║  ┌──────────────────────────────────┐                            ║
║  │  ⚖️ APRESENTAR ACUSAÇÃO - ROUND 1 │ ← Botão ativado, pulsante ║
║  └──────────────────────────────────┘                            ║
╚═══════════════════════════════════════════════════════════════════╝
```

**Ao clicar em "APRESENTAR ACUSAÇÃO":**

```
╔═══════════════════════════════════════════════════════════════════╗
║  [ANIMAÇÃO: Pistas "voam" para o centro e formam conexão]        ║
║                                                                   ║
║  ┌────────────────────────────────────────────────────────────┐  ║
║  │       🟣 Química_Coltan                                    │  ║
║  │            ↘                                               │  ║
║  │              🎯 OPERAÇÃO ILEGAL                           │  ║
║  │            ↗                    ↘                          │  ║
║  │  🟢 Fazenda_Fachada         🔵 Trilha_Mapa               │  ║
║  └────────────────────────────────────────────────────────────┘  ║
║                                                                   ║
║  [SOM: Revelação dramática]                                      ║
║  [TEXTO DIGITADO:]                                               ║
║                                                                   ║
║  🎤 VOCÊ: "Deputado Venturi, as evidências provam que:          ║
║                                                                   ║
║     1️⃣ Há COLTAN sendo minerado ilegalmente (C02)              ║
║     2️⃣ Sua fazenda é uma FACHADA logística (G02)               ║
║     3️⃣ O alvo é a RESERVA INDÍGENA com o mapa (H02)            ║
║                                                                   ║
║     Você orquestrou essa operação criminosa!"                   ║
║                                                                   ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ║
║                                                                   ║
║  [Pausa de 2 segundos...]                                        ║
║                                                                   ║
║  💬 Venturi: [Ri condescendente]                                ║
║     "Teorias da conspiração, jovem... Você anda ouvindo         ║
║      demais o 'Falcão' e seus delírios sobre Ratanabá..."      ║
║                                                                   ║
║  [Expressão confiante, ainda negando]                            ║
╚═══════════════════════════════════════════════════════════════════╝
```

**Áudios:**
- 🔊 `revelacao_final.mp3` (música dramática)
- 🔊 Som de "conexão" (ping metálico)

---

### **FASE 4: ROUND 2 - A VERDADE** 💀

Interface reseta, novas pistas necessárias:

```
╔═══════════════════════════════════════════════════════════════════╗
║  🎯 ZONA DE ACUSAÇÃO - ROUND 2 (DECISIVO)                        ║
║                                                                   ║
║  💡 Ele ainda nega... Mas você tem a PROVA FINAL!                ║
║                                                                   ║
║  📂 PISTAS CRÍTICAS DISPONÍVEIS:                                 ║
║  ┌─────────┐  ┌─────────┐                                       ║
║  │ 🔴 O01  │  │ ⚔️ O02  │                                       ║
║  │Ratanabá │  │ Coltan  │                                       ║
║  │ =Falso! │  │ Militar │                                       ║
║  └─────────┘  └─────────┘                                       ║
║                                                                   ║
║  ┌───────────────────────────────────────────────────────────┐  ║
║  │  [Arraste as 2 pistas que destroem a defesa dele]         │  ║
║  └───────────────────────────────────────────────────────────┘  ║
╚═══════════════════════════════════════════════════════════════════╝
```

**Após arrastar O01 + O02:**

```
╔═══════════════════════════════════════════════════════════════════╗
║  [ANIMAÇÃO: Tela escurece, luz vermelha pulsante]                ║
║  [SOM: Batida cardíaca acelerando + estática]                    ║
║                                                                   ║
║  🎤 VOCÊ: "NÃO, DEPUTADO. EU TENHO A VERDADE:                   ║
║                                                                   ║
║     🔴 RATANABÁ É DESINFORMAÇÃO!                                 ║
║        O Coronel Silva confessou: VOCÊ pagou o Falcão           ║
║        para espalhar essa teoria! Cortina de fumaça!            ║
║                                                                   ║
║     ⚔️ COLTAN PARA PROJETO MILITAR SECRETO!                      ║
║        Não é sobre dinheiro. É sobre ARMAS. Contrabando         ║
║        para programa militar. Gian descobriu isso!              ║
║                                                                   ║
║     💀 GIAN KRETZL FOI ASSASSINADO POR VOCÊ!"                    ║
║                                                                   ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ║
║                                                                   ║
║  [Pausa tensa de 3 segundos... música para...]                  ║
║                                                                   ║
║  [MUDANÇA VISUAL: Venturi para de rir. Expressão FRIA.]         ║
║                                                                   ║
║  💬 Venturi: [Tom gelado, sem emoção]                           ║
║              "..."                                               ║
║                                                                   ║
║  [Ele levanta, caminha até a janela]                             ║
╚═══════════════════════════════════════════════════════════════════╝
```

**Elementos Visuais:**
- ✅ Background muda para vermelho escuro
- ✅ Silhueta de Venturi contra janela
- ✅ Efeito de lentidão (slow motion) por 2 segundos
- ✅ Texto aparece palavra por palavra

---

### **FASE 5: A CONFISSÃO** 🏆

```
╔═══════════════════════════════════════════════════════════════════╗
║  [CINEMÁTICA FINAL - TEXTO COMPLETO REVELADO]                    ║
║                                                                   ║
║  💬 DEPUTADO VENTURI - CONFISSÃO:                                ║
║  ┌────────────────────────────────────────────────────────────┐  ║
║  │                                                            │  ║
║  │  "O Gian... ele não entendia. Um repórter.               │  ║
║  │   Achava que ia salvar o mundo com uma manchete."        │  ║
║  │                                                            │  ║
║  │  "Você sabe quanto vale Coltan de pureza 99,8%?          │  ║
║  │   Não para celulares - para ARMAS.                       │  ║
║  │   Lasers de pulso, sistemas antimísseis."                │  ║
║  │                                                            │  ║
║  │  "Quem controla esse minério controla o futuro bélico."  │  ║
║  │                                                            │  ║
║  │  "A Amazônia? O 'pulmão do mundo'? [Ri amargo]           │  ║
║  │   A Amazônia é a BATERIA do mundo."                      │  ║
║  │                                                            │  ║
║  │  "E o Brasil PRECISA ser uma potência.                   │  ║
║  │   Soberania exige sacrifícios."                          │  ║
║  │                                                            │  ║
║  │  "Gian ia estragar anos de planejamento.                 │  ║
║  │   Mobilizar ONGs, imprensa internacional, CPI..."        │  ║
║  │                                                            │  ║
║  │  "Ele se tornou um risco à segurança nacional."          │  ║
║  │                                                            │  ║
║  │  [Pausa]                                                  │  ║
║  │                                                            │  ║
║  │  "Decisões difíceis, jovem.                              │  ║
║  │   Você ainda não entende como o poder REAL funciona."    │  ║
║  │                                                            │  ║
║  └────────────────────────────────────────────────────────────┘  ║
║                                                                   ║
║  [SOM: Música épica/triste crescendo]                            ║
║  [VISUAL: Câmera fecha no rosto de Venturi - olhar vazio]       ║
║                                                                   ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ║
║                                                                   ║
║  ✅ PISTA FINAL COLETADA:                                        ║
║  🏆 Confissão_Venturi                                            ║
║                                                                   ║
║  📊 DOSSIÊ COMPLETO: 16/16 PISTAS                                ║
╚═══════════════════════════════════════════════════════════════════╝
```

**Áudios:**
- 🔊 `final_victory.mp3` (música épica)
- 🔊 Voz narrada de Venturi (opcional - TTS ou ator)

---

### **FASE 6: MISSÃO CUMPRIDA** 📰

```
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║                    🏆 MISSÃO CUMPRIDA 🏆                          ║
║                                                                   ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ║
║                                                                   ║
║  Você completou a última investigação de Gian Kretzl.            ║
║  O dossiê está completo. A verdade foi revelada.                 ║
║                                                                   ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ║
║                                                                   ║
║  Agora você pode:                                                 ║
║                                                                   ║
║  ┌──────────────────────────────────────────┐                   ║
║  │  📰 VAZAR INVESTIGAÇÃO PARA A IMPRENSA  │ ← Botão principal  ║
║  └──────────────────────────────────────────┘                   ║
║                                                                   ║
║  ┌──────────────────────────────────────────┐                   ║
║  │  📂 VER DOSSIÊ COMPLETO (16 pistas)     │                    ║
║  └──────────────────────────────────────────┘                   ║
║                                                                   ║
║  ┌──────────────────────────────────────────┐                   ║
║  │  🔄 JOGAR NOVAMENTE                      │                    ║
║  └──────────────────────────────────────────┘                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

---

### **FASE 7: MANCHETES FINAIS** 📰

Ao clicar em "VAZAR INVESTIGAÇÃO":

```
╔═══════════════════════════════════════════════════════════════════╗
║  [ANIMAÇÃO: Manchetes aparecem uma por vez, como jornal girando] ║
║  [SOM: Máquina de escrever + flash de câmera]                    ║
║                                                                   ║
║  📰 ──────────────────────────────────────────────────────────   ║
║                                                                   ║
║  [Flash 1 - 1 segundo]                                            ║
║  ⚡ URGENTE: Áudio de repórter desaparecido vaza dossiê explosivo ║
║                                                                   ║
║  [Flash 2 - 1 segundo]                                            ║
║  ⚡ Deputado Federal afastado por envolvimento em contrabando     ║
║     militar de Coltan extraído ilegalmente da Amazônia           ║
║                                                                   ║
║  [Flash 3 - 1 segundo]                                            ║
║  ⚡ Fazenda na Amazônia era fachada para operação de mineração    ║
║     ilegal em Terra Indígena                                     ║
║                                                                   ║
║  [Flash 4 - 1 segundo]                                            ║
║  ⚡ 'Sombra Roxa' confirmada como poluição química por            ║
║     processamento de minério de Coltan                           ║
║                                                                   ║
║  [Flash 5 - 1 segundo]                                            ║
║  ⚡ Teoria de 'Ratanabá' exposta como operação de desinformação   ║
║     financiada por políticos                                     ║
║                                                                   ║
║  [Flash 6 - 1 segundo]                                            ║
║  ⚡ Terra Indígena da 'Trilha dos Ancestrais' recebe demarcação   ║
║     emergencial. Mineração suspensa                              ║
║                                                                   ║
║  [Flash 7 - 1 segundo]                                            ║
║  ⚡ Corpo de Gian Kretzl nunca foi encontrado, mas seu trabalho   ║
║     jornalístico está completo                                   ║
║                                                                   ║
║  📰 ──────────────────────────────────────────────────────────   ║
╚═══════════════════════════════════════════════════════════════════╝
```

**Animação CSS:**
```css
@keyframes manchete-entrada {
  0% {
    transform: rotateY(90deg) scale(0.5);
    opacity: 0;
  }
  50% {
    transform: rotateY(45deg) scale(0.8);
  }
  100% {
    transform: rotateY(0deg) scale(1);
    opacity: 1;
  }
}

.manchete {
  animation: manchete-entrada 1s ease-out;
  box-shadow: 0 4px 8px rgba(0,0,0,0.3);
  border-left: 5px solid #ff0000;
  padding: 15px;
  margin: 10px 0;
  background: #fff;
}
```

---

### **FASE 8: TELA FINAL** 🌟

```
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║                         [FADE TO BLACK]                           ║
║                                                                   ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ║
║                                                                   ║
║                    💻 O Notebook de Gian Kretzl                   ║
║                    cumpriu sua última missão.                     ║
║                                                                   ║
║                    A verdade foi revelada.                        ║
║                    A Amazônia foi protegida.                      ║
║                                                                   ║
║                    Gian... descanse em paz.                       ║
║                                                                   ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ║
║                                                                   ║
║                         🕊️                                        ║
║                                                                   ║
║                    [CRÉDITOS SOBEM]                               ║
║                                                                   ║
║                 PROJETO ENCRUZILHADA v3.0                         ║
║           A Última Investigação de Gian Kretzl                    ║
║                                                                   ║
║                    Desenvolvido por:                              ║
║              Sistema Educacional Amazônia                         ║
║                                                                   ║
║                 Baseado em casos reais de:                        ║
║          - Exploração ilegal de Coltan na Amazônia                ║
║          - Assassinatos de jornalistas investigativos             ║
║          - Operações de desinformação                             ║
║                                                                   ║
║              Este jogo é uma homenagem aos                        ║
║           jornalistas que arriscam suas vidas                     ║
║              pela verdade e pela Amazônia                         ║
║                                                                   ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ║
║                                                                   ║
║  [Botão: 🏠 VOLTAR AO MENU]                                      ║
║  [Botão: 📊 VER ESTATÍSTICAS]                                   ║
║  [Botão: 🔄 JOGAR NOVAMENTE]                                     ║
╚═══════════════════════════════════════════════════════════════════╝
```

**Áudio:**
- 🔊 Música melancólica/inspiradora (fade out lento)
- 🔊 Sons da floresta amazônica ao fundo

---

## 🎨 PALETA DE CORES - ATO VI

```
TENSÃO (Rounds 1-2):
- Background: #1a1a2e (azul escuro profundo)
- Acento: #ff0000 (vermelho alerta)
- Texto: #ffffff (branco)
- Pistas: #ffd700 (dourado)

CONFISSÃO:
- Background: #0f0f0f (preto quase total)
- Spotlight: #4a4a4a (cinza escuro)
- Texto Venturi: #cccccc (cinza claro)
- Destaques: #ff4444 (vermelho suave)

VITÓRIA:
- Background: #f5f5f5 (branco quente)
- Manchetes: #000000 (preto jornal)
- Acentos: #228b22 (verde floresta)
- Botões: #4169e1 (azul royal)
```

---

## 🎬 ESPECIFICAÇÕES TÉCNICAS

### **HTML Estrutura:**
```html
<div id="confronto-final" class="hidden">
  <!-- Fase 1: Desbloqueio -->
  <div class="desbloqueio-modal">...</div>
  
  <!-- Fase 2-4: Interface de Confronto -->
  <div class="sala-acusacao">
    <div class="venturi-avatar">...</div>
    <div class="dossie-pistas">...</div>
    <div class="zona-acusacao" 
         ondrop="drop(event)" 
         ondragover="allowDrop(event)">
    </div>
  </div>
  
  <!-- Fase 5: Confissão -->
  <div class="confissao-cinematica">...</div>
  
  <!-- Fase 6-8: Finais -->
  <div class="tela-vitoria">...</div>
  <div class="manchetes">...</div>
  <div class="creditos">...</div>
</div>
```

### **JavaScript Principais:**
```javascript
// Detecção de pistas corretas por round
const ROUNDS = {
  1: ['Química_Coltan', 'Fazenda_Fachada_Logística', 'Trilha_Ancestrais_Mapa_Coltan'],
  2: ['Ratanabá_É_Desinformação', 'Coltan_Projeto_Militar']
};

// Drag & Drop
function drag(ev) {
  ev.dataTransfer.setData("pista", ev.target.id);
}

function drop(ev) {
  ev.preventDefault();
  const pistaId = ev.dataTransfer.getData("pista");
  
  if (validarPista(pistaId, roundAtual)) {
    adicionarPistaZona(pistaId);
    tocarSom('acerto');
  } else {
    animarErro();
    tocarSom('erro');
  }
}

// Cinemática de confissão
function mostrarConfissao() {
  ocultarSalaAcusacao();
  mostrarCinematica();
  digitarTextoVenturi(textoConfissao, 50); // 50ms por letra
  tocarSom('final_victory');
}
```

---

## 📊 DIAGRAMA DE FLUXO VISUAL

```
INÍCIO DO ATO VI
       ↓
┌──────────────────┐
│ Alerta Crítico   │ ← Coronel revelou tudo
│ Vilão Desbloqueado│
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Sala de Acusação │ ← Interface drag & drop
│ (Venturi confiante)│
└────────┬─────────┘
         ↓
┌──────────────────┐
│ ROUND 1          │ ← Arraste 3 pistas: C02, G02, H02
│ Prova da Operação│
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Venturi Nega     │ ← "Teorias da conspiração..."
│ Menciona Falcão  │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ ROUND 2          │ ← Arraste 2 pistas: O01, O02
│ A Verdade Final  │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Venturi Para     │ ← Expressão muda (fria)
│ [Silêncio Tenso] │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ CONFISSÃO        │ ← Texto completo revelado
│ (Cinemática)     │ ← Música épica
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Dossiê Completo  │ ← 16/16 pistas
│ Missão Cumprida  │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ VAZAR INVESTIGAÇÃO│ ← Botão principal
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Manchetes Finais │ ← 7 manchetes animadas
│ (Jornal rotativo)│
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Tela Final       │ ← "Gian... descanse em paz"
│ Créditos         │
└──────────────────┘
       ↓
     FIM
```

---

## 🎯 IMPACTO EMOCIONAL DESEJADO

### **Progressão Emocional:**

1. **Alerta (Fase 1):** ⚡ Adrenalina, urgência
2. **Concentração (Fase 2-3):** 🎯 Foco, dedução
3. **Tensão (Fase 4):** 😰 Dúvida: "Será que vai funcionar?"
4. **Revelação (Fase 5):** 💀 Choque, horror moral
5. **Vitória (Fase 6):** 🏆 Catarse, satisfação
6. **Esperança (Fase 7-8):** 🌟 Reflexão, inspiração

---

## 💡 DICAS DE IMPLEMENTAÇÃO

### **Prioridade 1 (Essencial):**
- ✅ Sistema drag & drop de pistas
- ✅ Validação de pistas corretas por round
- ✅ Texto da confissão completo
- ✅ Manchetes finais

### **Prioridade 2 (Importante):**
- ✅ Animações de transição suaves
- ✅ Efeitos sonoros sincronizados
- ✅ Efeito de texto digitado

### **Prioridade 3 (Polimento):**
- ⭐ Avatar animado de Venturi
- ⭐ Partículas/efeitos visuais
- ⭐ Voz narrada (TTS ou ator)
- ⭐ Música original

---

## 📝 CHECKLIST DE DESENVOLVIMENTO

```
[ ] HTML: Estrutura do modal de confronto
[ ] CSS: Estilos de drag & drop
[ ] CSS: Animações de transição
[ ] JS: Lógica de validação de rounds
[ ] JS: Sistema drag & drop
[ ] JS: Cinemática de confissão
[ ] JS: Manchetes animadas
[ ] Áudio: final_victory.mp3 (já existe ✅)
[ ] Áudio: Som de "acerto" ao arrastar
[ ] Áudio: Som de "erro" ao arrastar errado
[ ] Texto: Confissão completa de Venturi
[ ] Teste: Fluxo completo do Ato VI
```

---

## 🎮 EXPERIÊNCIA DO JOGADOR

**Tempo estimado:** 8-12 minutos

**Emoções desejadas:**
- 😨 Tensão crescente
- 🤔 Desafio intelectual
- 😱 Choque moral
- 🏆 Satisfação da vitória
- 😢 Reflexão sobre a realidade

**Mensagem final:**
> *"A verdade sempre vence. Mas a que custo?"*

---

**🎬 Este é o momento mais impactante do jogo - a revelação completa da conspiração!**

# 🎵 GUIA DE CRIAÇÃO DE SONS AMBIENTE - PROJETO ENCRUZILHADA

Este guia mostra como criar ou baixar os sons ambiente necessários para o jogo.

---

## 📋 SONS NECESSÁRIOS

### Sons Ambiente (Loops):
1. **lab_ambiente.mp3** - Laboratório (bipes, ventilação)
2. **fazenda_ambiente.mp3** - Fazenda (gado ao longe, trator, cigarras)
3. **aldeia_ambiente.mp3** - Aldeia (fogo crepitando, floresta noturna, sapos)
4. **podcast_ambiente.mp3** - Podcast (música dramática)
5. **seguranca_ambiente.mp3** - Segurança (rádio estático, passos)
6. **sala_situacao.mp3** - Sala de situação (tensão, silêncio pesado)

### Efeitos Sonoros:
7. **clue_collected.mp3** - Som de "item coletado"
8. **enigma_unlocked.mp3** - Som de "desbloqueio"
9. **character_unlocked.mp3** - Som de "novo personagem"
10. **final_victory.mp3** - Som de "missão cumprida"

---

## 🆓 OPÇÃO 1: BAIXAR DE BIBLIOTECAS GRATUITAS

### Sites Recomendados:

#### 1. **Freesound.org** (Melhor opção - Creative Commons)
- URL: https://freesound.org/
- Requer cadastro gratuito
- Busque por: "laboratory ambience", "farm sounds", "campfire", etc.
- Filtro: Duração > 30s, Loop-able

#### 2. **Zapsplat.com**
- URL: https://www.zapsplat.com/
- Cadastro gratuito
- Boa biblioteca de efeitos sonoros e ambientes

#### 3. **BBC Sound Effects**
- URL: https://sound-effects.bbcrewind.co.uk/
- Gratuito para uso educacional
- Qualidade profissional

#### 4. **FreeSound Effects (YouTube Audio Library)**
- URL: https://studio.youtube.com/ → Biblioteca de Áudio
- Sem necessidade de atribuição
- Pode baixar em MP3

---

## 🎨 OPÇÃO 2: CRIAR COM FERRAMENTAS ONLINE

### **MyNoise.net** - Gerador de Sons Ambiente
- URL: https://mynoise.net/
- Crie ambientes personalizados
- Exportável como MP3
- Gratuito (doação opcional)

**Como usar:**
1. Acesse o site
2. Escolha um ambiente (ex: "Jungle", "Fire", "Office Noise")
3. Ajuste os sliders para personalizar
4. Grave usando software de captura de áudio (Audacity)

---

### **Audacity** - Editor de Áudio Gratuito
- URL: https://www.audacityteam.org/
- Totalmente gratuito
- Permite misturar sons

**Como criar loops:**
1. Baixe 2-3 sons relacionados do Freesound
2. Abra no Audacity
3. Sobreponha as faixas (Ctrl+Shift+P)
4. Adicione efeitos (reverb, fade)
5. Exporte como MP3

---

## 🎯 SUGESTÕES ESPECÍFICAS POR SOM

### 1. **lab_ambiente.mp3**
**Buscar no Freesound:**
- "laboratory hum"
- "computer room"
- "ventilation fan"
- "equipment beep"

**Misturar:**
- Ventilador de computador (loop)
- Bipes ocasionais de equipamento
- Zumbido elétrico leve

---

### 2. **fazenda_ambiente.mp3**
**Buscar no Freesound:**
- "farm ambience"
- "cattle distance"
- "cicadas"
- "tractor idle"

**Misturar:**
- Cigarras (base contínua)
- Mugidos distantes
- Vento leve
- Trator ocasional ao longe

---

### 3. **aldeia_ambiente.mp3**
**Buscar no Freesound:**
- "campfire crackling"
- "jungle night"
- "frogs chirping"
- "forest ambience"

**Misturar:**
- Fogo crepitando (primeiro plano)
- Sapos e grilos (segundo plano)
- Floresta noturna (fundo)

---

### 4. **podcast_ambiente.mp3**
**Buscar no YouTube Audio Library:**
- "Dramatic Background Music"
- "Suspense Loop"
- Filtro: Mood = Dark/Suspenseful

**Características:**
- Música instrumental
- Tom dramático mas não muito alto
- Loop de 30-60 segundos

---

### 5. **seguranca_ambiente.mp3**
**Buscar no Freesound:**
- "radio static"
- "footsteps concrete"
- "security room"
- "walkie talkie"

**Misturar:**
- Estática de rádio (leve, constante)
- Passos pesados ocasionais
- Som de rádio ao fundo

---

### 6. **sala_situacao.mp3**
**Buscar no Freesound:**
- "office ambience"
- "air conditioning"
- "tension drone"
- "room tone"

**Misturar:**
- Silêncio com ruído de sala leve
- Ar-condicionado distante
- Drone/tom de tensão muito baixo

---

### 7-10. **Efeitos Sonoros**

**clue_collected.mp3:**
- Buscar: "item collect", "achievement", "pickup"
- Duração: 0.5-1s
- Tom: Positivo, gratificante

**enigma_unlocked.mp3:**
- Buscar: "unlock", "door open", "chest open"
- Duração: 1-2s
- Tom: Revelador

**character_unlocked.mp3:**
- Buscar: "level up", "new character", "fanfare"
- Duração: 2-3s
- Tom: Celebrativo

**final_victory.mp3:**
- Buscar: "victory", "mission complete", "success"
- Duração: 3-5s
- Tom: Triunfante

---

## 🛠️ PASSO A PASSO: CRIAR UM SOM AMBIENTE

### Exemplo: lab_ambiente.mp3

1. **Baixar sons do Freesound:**
   - Busque "computer fan loop"
   - Busque "equipment beep"
   - Baixe 2-3 arquivos em WAV

2. **Abrir no Audacity:**
   - File → Open → Selecione o primeiro áudio
   - File → Import → Audio → Adicione os outros

3. **Ajustar volumes:**
   - Ventilador: Volume 70%
   - Bipes: Volume 30-40%

4. **Criar loop:**
   - Selecione tudo (Ctrl+A)
   - Effect → Fade In/Out nas bordas
   - Corte para duração de 30-60 segundos

5. **Exportar:**
   - File → Export → Export as MP3
   - Quality: 128kbps (suficiente)
   - Salve como "lab_ambiente.mp3"

6. **Testar loop:**
   - Abra no VLC ou Windows Media Player
   - Ative "Repetir" para ver se fica contínuo

---

## 📁 ORGANIZAÇÃO DOS ARQUIVOS

Salve todos os áudios em:
```
/workspaces/Project_Amazonia/static/audio/
```

Estrutura final:
```
static/audio/
├── lab_ambiente.mp3
├── fazenda_ambiente.mp3
├── aldeia_ambiente.mp3
├── podcast_ambiente.mp3
├── seguranca_ambiente.mp3
├── sala_situacao.mp3
├── clue_collected.mp3
├── enigma_unlocked.mp3
├── character_unlocked.mp3
├── final_victory.mp3
└── FINAL_ENTRY.wav (gerado via script Python)
```

---

## ⚙️ ESPECIFICAÇÕES TÉCNICAS

### Formato Recomendado:
- **Formato:** MP3
- **Bitrate:** 128 kbps (ambientes) / 192 kbps (efeitos)
- **Taxa de amostragem:** 44.1 kHz
- **Canais:** Estéreo

### Duração:
- **Ambientes:** 30-60 segundos (loop)
- **Efeitos:** 0.5-3 segundos

### Volume:
- Normalizar para -3dB (evita distorção)
- Ambientes mais baixos que efeitos

---

## 🎓 LICENÇAS E ATRIBUIÇÕES

Ao usar sons de terceiros:

1. **Verifique a licença:**
   - Creative Commons 0 (CC0) - Domínio público, sem atribuição
   - Creative Commons BY - Requer atribuição
   - Creative Commons BY-SA - Requer atribuição e mesma licença

2. **Crie arquivo CREDITS.txt:**
```
Som: lab_ambiente.mp3
Fonte: Computer Fan Loop by UserName (Freesound)
Licença: CC BY 3.0
URL: https://freesound.org/...
```

---

## ✅ CHECKLIST RÁPIDO

- [ ] Criar pasta `/static/audio/` (se não existir)
- [ ] Baixar/criar 6 sons ambiente
- [ ] Baixar/criar 4 efeitos sonoros
- [ ] Gerar FINAL_ENTRY.wav (script Python)
- [ ] Testar loops (devem ser contínuos)
- [ ] Verificar volumes (não muito altos)
- [ ] Criar CREDITS.txt (se usar sons de terceiros)
- [ ] Testar no jogo

---

## 🚀 ATALHO RÁPIDO (15 minutos)

### Opção Mínima Viável:

1. Acesse: https://mynoise.net/
2. Para cada ambiente, use:
   - **Lab:** "Brown Noise" (computador)
   - **Fazenda:** "Country Noise" (rural)
   - **Aldeia:** "Fire" (fogo) + "Jungle" (floresta)
   - **Podcast:** Silêncio ou música da YouTube Library
   - **Segurança:** "White Noise" (estática leve)
   - **Sala:** "Office Noise" (escritório)

3. Para efeitos, use efeitos prontos do Windows:
   - Grave sons do sistema
   - Ou use sons padrão do PowerPoint

4. Converta tudo para MP3 usando:
   - https://online-audio-converter.com/

---

**Pronto! Com esses sons, o jogo terá ambiente imersivo completo! 🎮🔊**

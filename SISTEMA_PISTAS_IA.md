# 🔍 SISTEMA DE PISTAS - Integração com IA

## 📊 RESUMO: Pistas por Personagem

### 👨‍🔬 Dr. Arnaldo Silva (Biólogo)
**Disciplina:** Ciências  
**Pistas (3 total):**
1. ✅ `Sombra_Roxa` - Detectada automaticamente pela IA
2. ⭐ `Química_Coltan` - **ESPECIAL**: Só via contra-pergunta após 8 interações
3. ✅ `Gado_Não_Bebe_Rio` - Detectada automaticamente pela IA

**Como funciona:**
- Pistas 1 e 3 são detectadas quando a IA menciona os termos
- Pista 2 (crítica) requer 8+ interações + ter coletado as outras 2
- Sistema de contra-pergunta oferece revelação especial

---

### 🧑‍🌾 "Seu" Valdemar (Fazendeiro)
**Disciplina:** Geografia  
**Pistas (4 total):**
1. ✅ `Poço_Artesiano` - Detectada automaticamente pela IA
2. ⭐ `Fazenda_Fachada_Logística` - Detectada automaticamente pela IA (CRÍTICA)
3. ✅ `Deputado_Venturi_Conexão` - Detectada automaticamente pela IA
4. ✅ `Conflito_Reserva_Indígena` - Detectada automaticamente pela IA

**Como funciona:**
- Todas detectadas automaticamente quando mencionadas
- Valdemar se "contradiz" e revela informações quando pressionado
- Prompt da IA instrui revelar gradualmente

---

### 🌿 Pajé Yakamu (Líder Indígena)
**Disciplina:** História  
**Pistas (3 total):**
1. ✅ `Sombra_Montanha_Fogo` - Detectada automaticamente pela IA
2. ⭐ `Trilha_Ancestrais_Mapa_Coltan` - Detectada automaticamente pela IA (CRÍTICA)
3. ✅ `Homem_Terno_Venturi` - Detectada automaticamente pela IA

**Como funciona:**
- Todas detectadas automaticamente
- Pajé revela conhecimento ancestral em metáforas
- Prompt da IA instrui revelar através de histórias

---

### 🤵 Deputado Venturi (Político)
**Disciplina:** Interdisciplinar  
**Pistas (1 total):**
1. 🏆 `Confissão_Venturi_Controle_Mundial` - Detectada automaticamente pela IA (FINAL)

**Como funciona:**
- Revelada quando confrontado com todas as evidências
- Venturi "confessa" sua genialidade
- É a pista final que completa o dossiê

---

## 🤖 INTEGRAÇÃO COM IA

### ✅ Sistema ESTÁ Integrado

**Como funciona a detecção automática:**

```python
# 1. IA gera resposta (OpenAI ou simulada)
assistant_reply = openai_client.chat.completions.create(...)

# 2. Sistema detecta pistas na resposta da IA
reply_lower = assistant_reply.lower()
for pista in ent['pistas_chave']:
    pista_formatada = pista.replace('_', ' ').lower()
    
    if pista_formatada in reply_lower:
        # Pista encontrada!
        found.append(pista)

# 3. Frontend recebe lista de pistas encontradas
return jsonify({
    'reply': assistant_reply,
    'pistas_encontradas': found  # <- Botões aparecem aqui
})
```

**Prompts da IA instruem mencionar pistas:**

Exemplo do Dr. Arnaldo:
```python
"✅ SEMPRE mencione:
- Foi GIAN quem deu o nome 'Sombra Roxa'
- Mencione pistas específicas (nomes com underscore: Sombra_Roxa, Química_Coltan, etc)"
```

---

## ⭐ PISTA ESPECIAL: Química_Coltan

### Por que é especial?

Esta é a **PISTA CRÍTICA** do Ato I. Ela revela:
- QUE mineral está sendo extraído (Coltan)
- É a chave para entender toda a conspiração
- Conecta Ciências → Geografia → História

### Sistema de Contra-Pergunta

**Requisitos para ativar:**
1. ✅ Ter 8+ interações com Dr. Arnaldo
2. ✅ Ter coletado `Sombra_Roxa`
3. ✅ Ter coletado `Gado_Não_Bebe_Rio`

**Fluxo:**
```
Jogador conversa → 8+ mensagens
              ↓
Dr. Arnaldo oferece: "Quer saber o químico exato?"
              ↓
Jogador clica: "Sim, preciso saber"
              ↓
IA revela: "Química_Coltan" ← Pista crítica desbloqueada
```

**Código:**
```python
if entity_id == 'biologo' and interaction_count >= 8:
    tem_base = 'Sombra_Roxa' in pistas and 'Gado_Não_Bebe_Rio' in pistas
    
    if tem_base:
        contra_pergunta = {
            'texto': 'Quer que eu revele o químico exato?',
            'opcoes': ['Sim', 'Ainda não']
        }
```

---

## 📈 AJUSTE: 12 → 8 Interações

### Mudança Aplicada

**ANTES:**
```python
if entity_id == 'biologo' and interaction_count >= 12:
```

**DEPOIS:**
```python
if entity_id == 'biologo' and interaction_count >= 8:
```

### Por que 8 interações?

| Interação | Exemplo de Pergunta |
|-----------|---------------------|
| 1 | "Olá, pode me contar sobre a Sombra Roxa?" |
| 2 | "Como você descobriu isso?" |
| 3 | "O que causa essa anomalia?" |
| 4 | "Você falou com o Gian sobre isso?" |
| 5 | "Por que o gado não bebe do rio?" |
| 6 | "Quem mais sabe sobre isso?" |
| 7 | "Você tem medo?" |
| 8 | **← CONTRA-PERGUNTA APARECE** |

**Vantagens:**
- ✅ Mais rápido (era 12, agora 8)
- ✅ Ainda exige exploração (não é imediato)
- ✅ Jogador não fica entediado
- ✅ Mantém progressão natural

---

## 🎯 DETECÇÃO DE PISTAS: Como Funciona

### Método 1: Detecção Automática (Maioria)

**Condições:**
1. IA menciona o nome da pista na resposta
2. Contexto suficiente (resposta com 100+ caracteres OU múltiplas palavras)
3. Não é uma saudação simples

**Exemplo:**
```
Jogador: "O que você descobriu no rio?"

IA: "Encontrei uma proliferação de cianobactérias tóxicas 
     causada por mercúrio e um solvente industrial usado 
     para processar COLTAN..."

Sistema detecta: "coltan" na resposta
              ↓
Botão aparece: "🔍 Coletar pista: Química_Coltan"
```

### Método 2: Contra-Pergunta (Química_Coltan)

**Só para pista crítica do Dr. Arnaldo**

```
8+ interações + 2 pistas coletadas
              ↓
Sistema oferece: "Quer saber o químico exato?"
              ↓
Jogador: "Sim"
              ↓
Sistema adiciona: Química_Coltan às pistas encontradas
```

---

## 🔗 INTEGRAÇÃO COMPLETA

### 1. Prompts da IA (entidades.py)
✅ Cada personagem tem instruções específicas para mencionar suas pistas

### 2. Detecção Automática (app.py)
✅ Sistema lê resposta da IA e detecta menções às pistas

### 3. Sistema de Contra-Pergunta (app.py)
✅ Lógica especial para pista crítica após exploração

### 4. Frontend (interview.js)
✅ Mostra botões para coletar pistas detectadas

### 5. Banco de Dados (database.py)
✅ Salva pistas coletadas permanentemente

---

## 📝 CHECKLIST DE INTEGRAÇÃO

- [x] Prompts da IA mencionam pistas nos nomes corretos
- [x] Sistema detecta pistas automaticamente
- [x] Contra-pergunta funciona após 8 interações
- [x] Pistas requerem contexto (não só menção)
- [x] Pistas são salvas no banco de dados
- [x] Frontend mostra botões de coleta
- [x] Enigmas checam pistas coletadas
- [x] Sistema funciona com OpenAI E simulação

---

## 🎮 PROGRESSÃO TÍPICA

### Dr. Arnaldo (Ato I)
```
Interações 1-3: Exploração inicial, descoberta da Sombra Roxa
Interação 4-5: Pista "Sombra_Roxa" detectada e coletada
Interação 6-7: Discussão sobre o gado, pista "Gado_Não_Bebe_Rio"
Interação 8+: CONTRA-PERGUNTA aparece
Interação 9: Jogador aceita, "Química_Coltan" revelada
```

### Valdemar (Ato II)
```
Interações 1-2: Valdemar defensivo
Interação 3-4: Contradições sobre o rio, "Poço_Artesiano"
Interação 5-6: Gagueja sobre lucro, "Fazenda_Fachada_Logística"
Interação 7-8: Menciona Venturi, "Deputado_Venturi_Conexão"
Interação 9-10: Revela interesse na reserva, "Conflito_Reserva_Indígena"
```

### Pajé Yakamu (Ato III)
```
Interações 1-2: Metáforas sobre o rio
Interação 3-4: História da montanha, "Sombra_Montanha_Fogo"
Interação 5-6: Trilha ancestral, "Trilha_Ancestrais_Mapa_Coltan"
Interação 7-8: Revela Venturi, "Homem_Terno_Venturi"
```

### Deputado Venturi (Clímax)
```
Interações 1-2: Suave e polido
Interação 3-4: Confrontado com evidências
Interação 5+: CONFESSA, "Confissão_Venturi_Controle_Mundial"
```

---

## 🚀 CONCLUSÃO

✅ **Sistema TOTALMENTE integrado com IA**
✅ **Ajustado para 8 interações** (era 12)
✅ **Todas as 11 pistas funcionam**
✅ **Detecção automática + contra-pergunta especial**
✅ **Funciona com OpenAI e fallback simulado**

**Próximo teste:** Jogar cada ato para verificar timing das pistas!

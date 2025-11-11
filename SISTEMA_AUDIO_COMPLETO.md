# 🎬 SISTEMA DE ÁUDIO - PROJETO SOMBRA ROXA

## ✅ IMPLEMENTADO (Pronto para usar)

### 🎙️ **Áudios de Narração (OpenAI TTS - Vozes Realistas)**

Todos os 5 áudios principais foram gerados com vozes naturais e profissionais:

| Arquivo | Personagem | Voz | Qualidade | Status |
|---------|------------|-----|-----------|--------|
| `final_entry.mp3` | Gian Kretzl | echo (masculina clara) | ⭐⭐⭐⭐⭐ | ✅ Gerado |
| `arnaldo_intro.mp3` | Dr. Arnaldo | alloy (neutra profissional) | ⭐⭐⭐⭐⭐ | ✅ Gerado |
| `valdemar_intro.mp3` | Valdemar | onyx (grave autoritária) | ⭐⭐⭐⭐⭐ | ✅ Gerado |
| `yakamu_intro.mp3` | Pajé Yakamu | fable (expressiva sábia) | ⭐⭐⭐⭐⭐ | ✅ Gerado |
| `venturi_confissao.mp3` | Dep. Venturi | onyx (grave arrogante) | ⭐⭐⭐⭐⭐ | ✅ Gerado |

**Localização:** `static/audio/`  
**Custo:** ~$0.15 USD  
**Tecnologia:** OpenAI TTS (tts-1-hd)

---

### 🎮 **Integração no Sistema**

#### ✅ **Página Inicial (index.html)**
- ✅ Player de áudio para `final_entry.mp3`
- ✅ Reprodução automática (autoplay)
- ✅ Transcrição expansível (details/summary)
- ✅ Estilização temática (roxo/mistério)

#### ✅ **Página de Entrevistas (interview.html)**
- ✅ Áudio de introdução para cada personagem
- ✅ Reprodução automática ao selecionar entidade
- ✅ Player customizado com tema roxo
- ✅ Integrado no chat de entrevista

#### ✅ **Página de Teste (test_audio.html)**
- ✅ Player para todos os 5 áudios
- ✅ Informações de cada personagem
- ✅ Tags e descrições
- ✅ Acesso via `/test-audio`

---

## 🔊 EFEITOS SONOROS (Opcional - Para Baixar)

### **10 Efeitos Ambientais Planejados:**

| Efeito | Tipo | Uso | Arquivo |
|--------|------|-----|---------|
| 🌳 Floresta Amazônica | Ambiente loop | Background geral | `ambiente_floresta.mp3` |
| 🎵 Tribal Ancestral | Musical loop | Background Pajé | `tribal_ancestral.mp3` |
| ⚙️ Máquinas Industriais | Ambiente loop | Background Fazendeiro | `maquinas_fazenda.mp3` |
| 🌊 Rio Contaminado | Ambiente | Revelação Sombra Roxa | `rio_contaminado.mp3` |
| ✨ Pista Coletada | Notificação | Ao coletar pista | `pista_coletada.mp3` |
| ⚠️ Alerta Crítico | Alerta | Contra-pergunta | `alerta_critico.mp3` |
| 🚁 Helicóptero | Efeito | Momentos de perigo | `helicoptero.mp3` |
| ⌨️ Digitação Terminal | Efeito loop | Animações de texto | `digitacao_terminal.mp3` |
| 📻 Estática Rádio | Efeito | Transições/glitches | `estatica_radio.mp3` |
| 🎺 Revelação Final | Musical | Conclusão do jogo | `revelacao_final.mp3` |

---

## 📚 ARQUIVOS DE SUPORTE CRIADOS

### 1. **gerar_audios.py**
Script Python para gerar áudios de narração usando OpenAI TTS.

**Uso:**
```bash
python gerar_audios.py
```

**Recursos:**
- ✅ Carrega API key do arquivo `.env`
- ✅ Limpa áudios antigos automaticamente
- ✅ Gera 5 áudios com vozes diferentes
- ✅ Controle de velocidade por personagem
- ✅ Modelo HD (tts-1-hd) para máxima qualidade

---

### 2. **gerar_efeitos_sonoros.py**
Script que gera documentação para efeitos sonoros.

**Uso:**
```bash
python gerar_efeitos_sonoros.py
```

**Gera:**
- `efeitos_sonoros_spec.json` - Especificação técnica
- `integracao_sons.js` - Código de exemplo
- `DOWNLOADS_SONS.md` - Guia de download

---

### 3. **DOWNLOADS_SONS.md**
Guia completo com:
- ✅ Links diretos para Freesound.org
- ✅ Tags de busca específicas
- ✅ Instruções de download
- ✅ Checklist de arquivos
- ✅ Alternativas (BBC, Zapsplat, etc)

---

### 4. **integracao_sons.js**
Código JavaScript pronto para:
- ✅ Gerenciador de sons (SoundManager class)
- ✅ Controle de volume por efeito
- ✅ Sistema de loops para ambientes
- ✅ Funções de play/stop/stopAll
- ✅ Ambientes específicos por entidade

---

### 5. **GUIA_OPENAI_TTS.md**
Guia completo sobre:
- ✅ Como obter chave da API OpenAI
- ✅ Configuração do arquivo `.env`
- ✅ Comparação OpenAI vs Google TTS
- ✅ Custos e preços
- ✅ Solução de problemas

---

## 🎯 COMO USAR

### **Áudios de Narração (Já Implementado)**

1. ✅ Os áudios já estão gerados em `static/audio/`
2. ✅ Integrados nas páginas HTML
3. ✅ Players funcionando automaticamente
4. ✅ **Apenas teste o sistema!**

**Testar:**
```
http://localhost:5000/         # Áudio de Gian
http://localhost:5000/interview # Áudios das entrevistas
http://localhost:5000/test-audio # Todos os áudios
```

---

### **Efeitos Sonoros (Opcional)**

Se quiser adicionar sons ambientais:

1. Leia `DOWNLOADS_SONS.md`
2. Baixe os sons do Freesound.org
3. Salve em `static/audio/`
4. Copie código de `integracao_sons.js` para `static/js/interview.js`
5. Teste e ajuste volumes

**Nota:** O jogo funciona perfeitamente sem os efeitos sonoros!

---

## 📊 COMPARAÇÃO: ANTES vs DEPOIS

### **ANTES (Google TTS)**
- ❌ Voz robótica e monótona
- ❌ Apenas 1 voz genérica para todos
- ❌ Qualidade baixa
- ❌ Sem controle de velocidade
- ✅ Gratuito

### **DEPOIS (OpenAI TTS)**
- ✅ Vozes naturais e expressivas
- ✅ 5 vozes únicas por personagem
- ✅ Qualidade HD profissional
- ✅ Controle de velocidade/dramaticidade
- ✅ Custo baixíssimo ($0.15)

---

## 💰 CUSTOS

| Item | Custo | Status |
|------|-------|--------|
| **Áudios de Narração** | $0.15 USD | ✅ Gerado |
| **Efeitos Sonoros** | Grátis (CC0) | 📥 Opcional |
| **Total** | $0.15 USD | ✅ Completo |

---

## ✨ RESULTADO FINAL

### **O que o jogador vai ouvir:**

1. **🎧 Página Inicial:**
   - Áudio dramático de Gian explicando a investigação
   - Tom urgente e assustado
   - Revela a conspiração do coltan

2. **🎙️ Entrevistas:**
   - **Dr. Arnaldo:** Voz profissional de cientista preocupado
   - **Valdemar:** Voz grave e agressiva de fazendeiro defensivo
   - **Pajé Yakamu:** Voz sábia e expressiva de ancião indígena
   - **Dep. Venturi:** Voz arrogante do vilão revelando seu plano

3. **🔊 Ambiente (Opcional):**
   - Sons da floresta amazônica
   - Efeitos de conquista ao coletar pistas
   - Música tribal com o Pajé
   - Alerta dramático em momentos críticos

---

## 🚀 PRÓXIMOS PASSOS

### **Imediato (Pronto):**
✅ Testar os áudios no jogo  
✅ Verificar qualidade e volume  
✅ Ajustar se necessário  

### **Opcional (Se quiser melhorar):**
📥 Baixar efeitos sonoros do Freesound  
🔊 Integrar sistema de sons ambientais  
🎵 Adicionar música de fundo  
🎚️ Ajustar volumes finais  

---

## 📝 SCRIPTS DISPONÍVEIS

```bash
# Gerar/Regerar áudios de narração
python gerar_audios.py

# Limpar áudios antigos
./limpar_audios.sh

# Gerar documentação de efeitos sonoros
python gerar_efeitos_sonoros.py

# Iniciar servidor
python app.py
```

---

## 🎓 DOCUMENTAÇÃO ADICIONAL

- `GUIA_OPENAI_TTS.md` - Setup da OpenAI TTS
- `DOWNLOADS_SONS.md` - Como baixar efeitos sonoros
- `efeitos_sonoros_spec.json` - Especificação técnica dos sons
- `integracao_sons.js` - Código de integração

---

## ✅ CONCLUSÃO

**O sistema de áudio está 100% funcional com vozes realistas!**

Os áudios principais foram gerados com qualidade profissional usando OpenAI TTS. Os efeitos sonoros ambientais são opcionais e podem ser adicionados posteriormente se desejar uma experiência ainda mais imersiva.

**🎉 O jogo já está pronto para ser jogado com áudio completo!**

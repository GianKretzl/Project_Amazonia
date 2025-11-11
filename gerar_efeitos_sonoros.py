#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔊 GERADOR DE EFEITOS SONOROS - PROJETO SOMBRA ROXA
Cria efeitos sonoros ambientais usando descrições de áudio

NOTA: OpenAI TTS gera apenas voz. Para sons ambientais, este script
fornece descrições que podem ser usadas com:
1. Bibliotecas gratuitas (Freesound, BBC Sound Effects)
2. Geradores de áudio AI (ElevenLabs, Mubert)
3. Síntese de áudio com Python (pydub, numpy)
"""

import os
import json

# Definir efeitos sonoros necessários
EFEITOS_SONOROS = {
    "floresta_amazonica": {
        "tipo": "ambiente",
        "duracao": "30-60s loop",
        "descricao": "Sons da floresta amazônica: pássaros cantando, grilos, vento nas folhas, som de água ao fundo",
        "uso": "Background durante entrevistas",
        "tags": ["amazonia", "floresta", "natureza", "passaros", "ambiente"],
        "volume": "baixo (20-30%)",
        "arquivo_sugerido": "ambiente_floresta.mp3"
    },
    
    "pista_coletada": {
        "tipo": "notificacao",
        "duracao": "2-3s",
        "descricao": "Som de conquista/descoberta: sino suave + brilho digital ascendente",
        "uso": "Quando jogador coleta uma pista",
        "tags": ["sucesso", "descoberta", "conquista", "notificacao"],
        "volume": "médio (50-60%)",
        "arquivo_sugerido": "pista_coletada.mp3"
    },
    
    "alerta_importante": {
        "tipo": "alerta",
        "duracao": "3-5s",
        "descricao": "Som de alerta urgente mas não agressivo: pulso grave + harmônicos tensos",
        "uso": "Quando contra-pergunta aparece ou momento crítico",
        "tags": ["alerta", "urgente", "tensao", "importante"],
        "volume": "médio-alto (60-70%)",
        "arquivo_sugerido": "alerta_critico.mp3"
    },
    
    "rio_contaminado": {
        "tipo": "ambiente",
        "duracao": "20-30s",
        "descricao": "Som de rio com reverberação estranha, água borbulhando de forma irregular, tons roxos/químicos",
        "uso": "Background durante revelação da Sombra Roxa",
        "tags": ["rio", "agua", "contaminacao", "quimico", "misterioso"],
        "volume": "médio (40-50%)",
        "arquivo_sugerido": "rio_contaminado.mp3"
    },
    
    "helicoptero_distante": {
        "tipo": "efeito",
        "duracao": "10-15s",
        "descricao": "Som de helicóptero distante se aproximando lentamente, criando tensão",
        "uso": "Momentos de perigo/ameaça na narrativa",
        "tags": ["helicoptero", "perigo", "ameaca", "tensao"],
        "volume": "médio (50%)",
        "arquivo_sugerido": "helicoptero.mp3"
    },
    
    "tribal_ancestral": {
        "tipo": "musical",
        "duracao": "30-45s loop",
        "descricao": "Percussão tribal suave, flauta indígena, cânticos distantes, atmosfera mística",
        "uso": "Background durante entrevista com Pajé Yakamu",
        "tags": ["indigena", "tribal", "ancestral", "mistico", "flauta"],
        "volume": "baixo (30-40%)",
        "arquivo_sugerido": "tribal_ancestral.mp3"
    },
    
    "maquinas_industrial": {
        "tipo": "ambiente",
        "duracao": "20-30s",
        "descricao": "Som de maquinário pesado distante, motosserras, tratores, atividade industrial",
        "uso": "Background durante entrevista com fazendeiro",
        "tags": ["industrial", "maquinas", "fazenda", "mecanico"],
        "volume": "baixo (25-35%)",
        "arquivo_sugerido": "maquinas_fazenda.mp3"
    },
    
    "revelacao_final": {
        "tipo": "musical",
        "duracao": "15-20s",
        "descricao": "Crescendo dramático orquestral, revelação épica, resolução de mistério",
        "uso": "Quando jogador completa a investigação",
        "tags": ["dramatico", "revelacao", "final", "orquestral"],
        "volume": "alto (70-80%)",
        "arquivo_sugerido": "revelacao_final.mp3"
    },
    
    "digitacao_terminal": {
        "tipo": "efeito",
        "duracao": "1-2s loop",
        "descricao": "Som de digitação em teclado mecânico vintage, ritmo constante",
        "uso": "Durante animações de texto tipo terminal",
        "tags": ["teclado", "digitacao", "terminal", "retro"],
        "volume": "muito baixo (15-20%)",
        "arquivo_sugerido": "digitacao_terminal.mp3"
    },
    
    "estatica_radio": {
        "tipo": "efeito",
        "duracao": "3-5s",
        "descricao": "Estática de rádio/transmissão interrompida, interferência",
        "uso": "Transições e momentos de comunicação cortada",
        "tags": ["estatica", "radio", "interferencia", "glitch"],
        "volume": "médio (40-50%)",
        "arquivo_sugerido": "estatica_radio.mp3"
    }
}

def gerar_documentacao():
    """Gera documentação dos efeitos sonoros necessários"""
    print("=" * 70)
    print("🔊 EFEITOS SONOROS - PROJETO SOMBRA ROXA")
    print("=" * 70)
    print()
    
    # Salvar JSON para referência
    with open("efeitos_sonoros_spec.json", "w", encoding="utf-8") as f:
        json.dump(EFEITOS_SONOROS, f, indent=2, ensure_ascii=False)
    
    print("✅ Especificação salva em: efeitos_sonoros_spec.json")
    print()
    
    # Gerar lista de downloads
    print("📥 FONTES PARA DOWNLOAD DE EFEITOS SONOROS:")
    print()
    print("1. 🆓 FREESOUND.ORG (Grátis, Creative Commons)")
    print("   https://freesound.org")
    print()
    
    categorias = {}
    for nome, info in EFEITOS_SONOROS.items():
        tipo = info['tipo']
        if tipo not in categorias:
            categorias[tipo] = []
        categorias[tipo].append((nome, info))
    
    for tipo, efeitos in categorias.items():
        print(f"\n📂 {tipo.upper()}")
        print("-" * 70)
        for nome, info in efeitos:
            print(f"\n🎵 {info['arquivo_sugerido']}")
            print(f"   Descrição: {info['descricao']}")
            print(f"   Tags de busca: {', '.join(info['tags'])}")
            print(f"   Duração: {info['duracao']}")
            print(f"   Volume sugerido: {info['volume']}")
            print(f"   Uso: {info['uso']}")
    
    print("\n" + "=" * 70)
    print("📚 GUIA DE DOWNLOAD:")
    print("=" * 70)
    print()
    print("1. Acesse https://freesound.org")
    print("2. Crie uma conta gratuita")
    print("3. Busque usando as tags listadas acima")
    print("4. Filtre por licença: Creative Commons 0 (uso livre)")
    print("5. Baixe e salve em: static/audio/")
    print("6. Renomeie para os nomes sugeridos")
    print()
    print("🎨 ALTERNATIVAS:")
    print("- BBC Sound Effects: https://sound-effects.bbcrewind.co.uk/")
    print("- Zapsplat: https://www.zapsplat.com/")
    print("- ElevenLabs Sound Effects (AI): https://elevenlabs.io/")
    print("- YouTube Audio Library")
    print()
    
    # Gerar script de implementação
    gerar_codigo_integracao()

def gerar_codigo_integracao():
    """Gera código exemplo para integrar os sons"""
    print("=" * 70)
    print("💻 CÓDIGO DE INTEGRAÇÃO")
    print("=" * 70)
    print()
    
    codigo_js = """
// Adicionar ao interview.js

class SoundManager {
  constructor() {
    this.sounds = {
      floresta: new Audio('/static/audio/ambiente_floresta.mp3'),
      pistaColetada: new Audio('/static/audio/pista_coletada.mp3'),
      alerta: new Audio('/static/audio/alerta_critico.mp3'),
      rioContaminado: new Audio('/static/audio/rio_contaminado.mp3'),
      helicoptero: new Audio('/static/audio/helicoptero.mp3'),
      tribal: new Audio('/static/audio/tribal_ancestral.mp3'),
      maquinas: new Audio('/static/audio/maquinas_fazenda.mp3'),
      revelacao: new Audio('/static/audio/revelacao_final.mp3'),
      digitacao: new Audio('/static/audio/digitacao_terminal.mp3'),
      estatica: new Audio('/static/audio/estatica_radio.mp3')
    };
    
    // Configurar loops
    this.sounds.floresta.loop = true;
    this.sounds.tribal.loop = true;
    this.sounds.maquinas.loop = true;
    this.sounds.digitacao.loop = true;
    
    // Configurar volumes
    this.sounds.floresta.volume = 0.25;
    this.sounds.pistaColetada.volume = 0.6;
    this.sounds.alerta.volume = 0.65;
    this.sounds.rioContaminado.volume = 0.45;
    this.sounds.helicoptero.volume = 0.5;
    this.sounds.tribal.volume = 0.35;
    this.sounds.maquinas.volume = 0.3;
    this.sounds.revelacao.volume = 0.75;
    this.sounds.digitacao.volume = 0.18;
    this.sounds.estatica.volume = 0.45;
  }
  
  play(soundName) {
    if (this.sounds[soundName]) {
      this.sounds[soundName].currentTime = 0;
      this.sounds[soundName].play().catch(e => console.log('Audio play failed:', e));
    }
  }
  
  stop(soundName) {
    if (this.sounds[soundName]) {
      this.sounds[soundName].pause();
      this.sounds[soundName].currentTime = 0;
    }
  }
  
  stopAll() {
    Object.values(this.sounds).forEach(sound => {
      sound.pause();
      sound.currentTime = 0;
    });
  }
  
  setAmbiente(entidadeId) {
    // Parar ambientes anteriores
    this.stop('floresta');
    this.stop('tribal');
    this.stop('maquinas');
    
    // Tocar ambiente específico
    switch(entidadeId) {
      case 'lider_indigena':
        this.play('tribal');
        break;
      case 'fazendeiro':
        this.play('maquinas');
        break;
      default:
        this.play('floresta');
    }
  }
}

// Inicializar
const soundManager = new SoundManager();

// Usar nos eventos
function coletarPista(pista) {
  soundManager.play('pistaColetada');
  // ... resto do código
}

function mostrarContraPergunta(pergunta) {
  soundManager.play('alerta');
  // ... resto do código
}

function selectEntity(entity) {
  soundManager.setAmbiente(entity.id);
  // ... resto do código
}
"""
    
    with open("integracao_sons.js", "w", encoding="utf-8") as f:
        f.write(codigo_js)
    
    print("✅ Código de exemplo salvo em: integracao_sons.js")
    print()
    print("📋 Para integrar:")
    print("1. Baixe os arquivos de áudio e salve em static/audio/")
    print("2. Copie o código de integracao_sons.js para static/js/interview.js")
    print("3. Teste o volume e ajuste conforme necessário")
    print()

def criar_lista_download():
    """Cria arquivo com links diretos para downloads"""
    markdown = """# 🔊 Lista de Downloads - Efeitos Sonoros

## Sites Recomendados

### 1. Freesound.org (Melhor opção - CC0)
- **URL:** https://freesound.org
- **Licença:** Creative Commons 0 (domínio público)
- **Cadastro:** Necessário (gratuito)

### 2. BBC Sound Effects
- **URL:** https://sound-effects.bbcrewind.co.uk/
- **Licença:** Uso educacional permitido
- **Cadastro:** Não necessário

### 3. Zapsplat
- **URL:** https://www.zapsplat.com/
- **Licença:** Uso gratuito com atribuição
- **Cadastro:** Recomendado

---

## Buscas Específicas no Freesound

"""
    
    for nome, info in EFEITOS_SONOROS.items():
        tags_str = " ".join(info['tags'])
        markdown += f"\n### {info['arquivo_sugerido']}\n"
        markdown += f"**Buscar:** `{tags_str}`\n"
        markdown += f"**Link direto:** https://freesound.org/search/?q={'+'.join(info['tags'])}\n"
        markdown += f"- Duração: {info['duracao']}\n"
        markdown += f"- Uso: {info['uso']}\n"
        markdown += f"- Volume: {info['volume']}\n\n"
    
    markdown += """
---

## Checklist de Download

- [ ] ambiente_floresta.mp3
- [ ] pista_coletada.mp3
- [ ] alerta_critico.mp3
- [ ] rio_contaminado.mp3
- [ ] helicoptero.mp3
- [ ] tribal_ancestral.mp3
- [ ] maquinas_fazenda.mp3
- [ ] revelacao_final.mp3
- [ ] digitacao_terminal.mp3
- [ ] estatica_radio.mp3

---

## Instruções de Instalação

1. Baixe cada arquivo de áudio
2. Salve em: `static/audio/`
3. Renomeie para os nomes da checklist
4. Teste no jogo
5. Ajuste volumes conforme necessário

---

## Alternativa Rápida: Usar Sons de Sistema

Se quiser começar rápido, use sons de notificação do sistema:
- macOS: `/System/Library/Sounds/`
- Windows: `C:\\Windows\\Media\\`
- Linux: `/usr/share/sounds/`

"""
    
    with open("DOWNLOADS_SONS.md", "w", encoding="utf-8") as f:
        f.write(markdown)
    
    print("📝 Lista de downloads criada em: DOWNLOADS_SONS.md")

if __name__ == "__main__":
    gerar_documentacao()
    criar_lista_download()
    
    print("\n" + "=" * 70)
    print("✨ RESUMO")
    print("=" * 70)
    print()
    print(f"📊 Total de efeitos sonoros necessários: {len(EFEITOS_SONOROS)}")
    print()
    print("📁 Arquivos criados:")
    print("   - efeitos_sonoros_spec.json (especificação técnica)")
    print("   - integracao_sons.js (código de exemplo)")
    print("   - DOWNLOADS_SONS.md (guia de download)")
    print()
    print("🎯 Próximos passos:")
    print("   1. Leia DOWNLOADS_SONS.md")
    print("   2. Baixe os sons do Freesound.org")
    print("   3. Salve em static/audio/")
    print("   4. Integre o código em interview.js")
    print()
    print("=" * 70)

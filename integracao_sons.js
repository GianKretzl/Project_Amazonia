
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

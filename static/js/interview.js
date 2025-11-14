// ============================================
// PROJETO SOMBRA ROXA - Interview System
// ============================================

// Gerenciador de Sons
class SoundManager {
  constructor() {
    this.sounds = {};
    this.initialized = false;
    this.ambientePlaying = false;
    this.audioEnabled = true;
    this.failedAudios = [];
    this.playCount = {}; // Contador de reproduções
    
    // Definir configurações de áudio
    this.audioConfig = {
      // Sons ambiente por personagem (máximo 2 vezes)
      lab_ambiente: { path: '/static/audio/lab_ambiente.mp3', volume: 0.25, maxPlays: 2 },
      fazenda_ambiente: { path: '/static/audio/fazenda_ambiente.mp3', volume: 0.25, maxPlays: 2 },
      aldeia_ambiente: { path: '/static/audio/aldeia_ambiente.mp3', volume: 0.25, maxPlays: 2 },
      podcast_ambiente: { path: '/static/audio/podcast_ambiente.mp3', volume: 0.30, maxPlays: 2 },
      seguranca_ambiente: { path: '/static/audio/seguranca_ambiente.mp3', volume: 0.25, maxPlays: 2 },
      sala_situacao: { path: '/static/audio/sala_situacao.mp3', volume: 0.20, maxPlays: 2 },
      
      // Efeitos sonoros
      floresta: { path: '/static/audio/ambiente_floresta.mp3', volume: 0.25 },
      pistaColetada: { path: '/static/audio/pista_coletada.mp3', volume: 0.6 },
      clue_collected: { path: '/static/audio/clue_collected.mp3', volume: 0.6 },
      alerta: { path: '/static/audio/alerta_critico.mp3', volume: 0.65 },
      estatica: { path: '/static/audio/estatica_radio.mp3', volume: 0.45 },
      revelacao: { path: '/static/audio/revelacao_final.mp3', volume: 0.75 },
      enigma_unlocked: { path: '/static/audio/enigma_unlocked.mp3', volume: 0.7 },
      character_unlocked: { path: '/static/audio/character_unlocked.mp3', volume: 0.7 },
      final_victory: { path: '/static/audio/final_victory.mp3', volume: 0.8 }
    };
    
    // Mapear personagens para sons ambiente
    this.ambienteMap = {
      'biologo': 'lab_ambiente',
      'fazendeiro': 'fazenda_ambiente',
      'lider_indigena': 'aldeia_ambiente',
      'podcaster': 'podcast_ambiente',
      'coronel': 'seguranca_ambiente',
      'politico': 'sala_situacao'
    };
  }
  
  // Inicializar áudios após interação do usuário
  init() {
    if (this.initialized) return;
    
    console.log('🔊 Inicializando sistema de áudio...');
    
    try {
      Object.entries(this.audioConfig).forEach(([name, config]) => {
        const audio = new Audio(config.path);
        audio.volume = config.volume;
        audio.preload = 'auto';
        
        // Adicionar event listeners para debug detalhado
        audio.addEventListener('error', (e) => {
          console.error(`❌ ERRO ao carregar áudio ${name}:`, {
            path: config.path,
            error: e.target.error,
            code: e.target.error?.code,
            message: e.target.error?.message
          });
          this.failedAudios.push(name);
        });
        
        audio.addEventListener('canplaythrough', () => {
          console.log(`✅ Áudio ${name} carregado com sucesso`);
        });
        
        audio.addEventListener('loadedmetadata', () => {
          console.log(`📊 Metadata carregada para ${name}: ${audio.duration.toFixed(2)}s`);
        });
        
        this.sounds[name] = audio;
      });
      
      this.initialized = true;
      console.log('🔊 Sistema de áudio inicializado');
      
      // Mostrar aviso se houver falhas após 3 segundos
      setTimeout(() => {
        if (this.failedAudios.length > 0) {
          console.warn(`⚠️ ${this.failedAudios.length} áudios falharam ao carregar:`, this.failedAudios);
        }
      }, 3000);
      
    } catch (error) {
      console.error('❌ Erro crítico ao inicializar áudios:', error);
      this.audioEnabled = false;
    }
  }
  
  play(soundName, loop = false) {
    // Verificar se áudio está habilitado
    if (!this.audioEnabled) {
      console.log(`🔇 Áudio desabilitado, não tocando ${soundName}`);
      return;
    }
    
    // Inicializar se necessário
    if (!this.initialized) {
      this.init();
    }
    
    if (this.sounds[soundName]) {
      // Configurar loop (apenas para sons ambiente)
      this.sounds[soundName].loop = loop;
      
      // Resetar e tocar
      this.sounds[soundName].currentTime = 0;
      
      const playPromise = this.sounds[soundName].play();
      
      if (playPromise !== undefined) {
        playPromise
          .then(() => {
            console.log(`🎵 Tocando ${soundName}`);
          })
          .catch(e => {
            console.warn(`⚠️ Não foi possível tocar ${soundName}:`, {
              error: e.name,
              message: e.message,
              reason: e.name === 'NotAllowedError' ? 'Autoplay bloqueado pelo navegador' : 'Erro desconhecido'
            });
          });
      }
    } else {
      console.warn(`⚠️ Áudio ${soundName} não encontrado nos sons carregados`);
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
    this.ambientePlaying = false;
  }
  
  startAmbiente() {
    if (!this.ambientePlaying) {
      this.play('floresta', true);
      this.ambientePlaying = true;
    }
  }
  
  startAmbientePersonagem(personagemId) {
    // Parar qualquer som ambiente tocando
    this.stopAll();
    
    // Pegar o som ambiente específico do personagem
    const ambienteSom = this.ambienteMap[personagemId];
    
    if (ambienteSom && this.sounds[ambienteSom]) {
      console.log(`🎵 Iniciando som ambiente: ${ambienteSom} para ${personagemId}`);
      
      // Inicializar contador se não existir
      if (!this.playCount[ambienteSom]) {
        this.playCount[ambienteSom] = 0;
      }
      
      const maxPlays = this.audioConfig[ambienteSom]?.maxPlays || 2;
      
      // Resetar áudio
      this.sounds[ambienteSom].currentTime = 0;
      
      // Configurar evento de término para replay limitado
      const onEnded = () => {
        this.playCount[ambienteSom]++;
        console.log(`🔁 ${ambienteSom} tocou ${this.playCount[ambienteSom]}/${maxPlays} vezes`);
        
        if (this.playCount[ambienteSom] < maxPlays) {
          // Tocar novamente
          this.sounds[ambienteSom].currentTime = 0;
          this.sounds[ambienteSom].play().catch(e => console.warn(`⚠️ Erro no replay: ${e.message}`));
        } else {
          console.log(`✅ ${ambienteSom} completou ${maxPlays} reproduções`);
          this.sounds[ambienteSom].removeEventListener('ended', onEnded);
        }
      };
      
      // Remover listener antigo se existir
      this.sounds[ambienteSom].removeEventListener('ended', onEnded);
      this.sounds[ambienteSom].addEventListener('ended', onEnded);
      
      const playPromise = this.sounds[ambienteSom].play();
      
      if (playPromise !== undefined) {
        playPromise
          .then(() => {
            this.ambientePlaying = true;
            console.log(`✅ Som ambiente ${ambienteSom} tocando (máximo ${maxPlays} vezes)`);
          })
          .catch(e => {
            console.warn(`⚠️ Não foi possível tocar ${ambienteSom}:`, e.message);
            // Fallback para som genérico de floresta
            this.startAmbiente();
          });
      }
    } else {
      console.log(`⚠️ Som ambiente não encontrado para ${personagemId}, usando genérico`);
      // Fallback para som genérico
      this.startAmbiente();
    }
  }
  
  stopAmbiente() {
    this.stop('floresta');
    this.ambientePlaying = false;
  }
}

// Instância global do gerenciador de sons
const soundManager = new SoundManager();

class InterviewSystem {
  constructor() {
    console.log('🎮 Iniciando Interview System...');
    
    this.currentEntity = null;
    this.previousEntitiesState = {};
    this.excaliburEngine = null;
    this.excaliburScene = null;
    this.entityActors = {};
    this.chatHistory = [];
    this.desafiosDisponiveis = [];
    this.desafioAtual = null;
    this.respostaSelecionada = null;
    this.audioInitialized = false;
    
    this.initElements();
    this.initExcalibur();
    this.loadEntities();
    this.setupAudioInit();
    
    console.log('✅ Interview System inicializado!');
  }
  
  // Inicializar áudio após primeira interação do usuário
  setupAudioInit() {
    const audioStatus = document.getElementById('audio-status');
    const btnTestAudio = document.getElementById('btn-test-audio');
    
    const initAudio = () => {
      if (!this.audioInitialized) {
        soundManager.init();
        this.audioInitialized = true;
        console.log('🎵 Áudio inicializado após interação do usuário');
        
        if (audioStatus) {
          audioStatus.textContent = '🔊 Áudio: Inicializado ✅';
          audioStatus.style.color = '#00ff88';
        }
      }
    };
    
    // Botão de teste de áudio
    if (btnTestAudio) {
      btnTestAudio.addEventListener('click', () => {
        initAudio();
        
        // Testar tocando som de alerta
        setTimeout(() => {
          soundManager.play('alerta');
          
          if (audioStatus) {
            audioStatus.textContent = '🔊 Áudio: Testando...';
            audioStatus.style.color = '#fbbf24';
          }
          
          // Verificar resultado após 1 segundo
          setTimeout(() => {
            if (soundManager.failedAudios.length === 0) {
              if (audioStatus) {
                audioStatus.textContent = '🔊 Áudio: Funcionando! 🎉';
                audioStatus.style.color = '#00ff88';
              }
            } else {
              if (audioStatus) {
                audioStatus.textContent = `⚠️ ${soundManager.failedAudios.length} áudios com erro`;
                audioStatus.style.color = '#ef4444';
              }
            }
          }, 1000);
        }, 100);
      });
    }
    
    // Inicializar ao clicar em qualquer lugar (exceto no botão de teste)
    document.addEventListener('click', (e) => {
      if (e.target !== btnTestAudio && !btnTestAudio?.contains(e.target)) {
        initAudio();
      }
    }, { once: true });
    
    // Inicializar ao enviar mensagem
    if (this.chatForm) {
      this.chatForm.addEventListener('submit', initAudio, { once: true });
    }
  }

  initElements() {
    console.log('🔧 Inicializando elementos do DOM...');
    
    this.entitiesGrid = document.getElementById('entities-grid');
    console.log('  Grid de entidades:', this.entitiesGrid ? '✅ Encontrado' : '❌ NÃO ENCONTRADO');
    
    this.chatArea = document.getElementById('chat-area');
    this.chatLog = document.getElementById('chat-log');
    this.entityName = document.getElementById('entity-name');
    this.entityEmoji = document.getElementById('entity-emoji');
    this.entityDiscipline = document.getElementById('entity-discipline');
    this.chatForm = document.getElementById('chat-form');
    this.chatInput = document.getElementById('chat-input');
    this.pistasCount = document.getElementById('pistas-count');
    this.pistasCountDossie = document.getElementById('pistas-count-dossie');
    this.pistasList = document.getElementById('pistas-list');
    this.closeChat = document.getElementById('close-chat');
    
    // Elementos de desafios
    this.btnDesafios = document.getElementById('btn-desafios');
    this.desafiosBadge = document.getElementById('desafios-badge');
    this.modalDesafio = document.getElementById('modal-desafio');
    this.closeModal = document.getElementById('close-modal');
    this.desafioPergunta = document.getElementById('desafio-pergunta');
    this.desafioDisciplina = document.getElementById('desafio-disciplina');
    this.desafioOpcoes = document.getElementById('desafio-opcoes');
    this.btnConfirmarResposta = document.getElementById('btn-confirmar-resposta');
    this.resultadoArea = document.getElementById('resultado-area');
    this.resultadoConteudo = document.getElementById('resultado-conteudo');
    this.btnProximoDesafio = document.getElementById('btn-proximo-desafio');
    this.dicasArea = document.getElementById('dicas-area');
    this.dicasList = document.getElementById('dicas-list');
    
    // Botão de enigmas no dossiê
    this.btnVerificarEnigmas = document.getElementById('btn-verificar-enigmas');
    if (this.btnVerificarEnigmas) {
      this.btnVerificarEnigmas.addEventListener('click', () => this.verificarEnigmasDisponiveis());
    }

    if (this.chatForm) {
      this.chatForm.addEventListener('submit', (e) => this.handleChatSubmit(e));
    }

    if (this.closeChat) {
      this.closeChat.addEventListener('click', () => this.closeChatArea());
    }
    
    if (this.btnDesafios) {
      this.btnDesafios.addEventListener('click', () => this.abrirDesafio());
    }
    
    if (this.closeModal) {
      this.closeModal.addEventListener('click', () => this.fecharModal());
    }
    
    if (this.btnConfirmarResposta) {
      this.btnConfirmarResposta.addEventListener('click', () => this.confirmarResposta());
    }
    
    if (this.btnProximoDesafio) {
      this.btnProximoDesafio.addEventListener('click', () => this.proximoDesafio());
    }
  }

  async initExcalibur() {
    try {
      if (!window.ex) {
        console.log('Excalibur não disponível');
        return;
      }

      const Ex = window.ex;
      const container = document.getElementById('excalibur-container');
      
      if (!container) return;

      const canvas = document.createElement('canvas');
      canvas.width = 1200;
      canvas.height = 280;
      canvas.style.maxWidth = '100%';
      canvas.style.maxHeight = '100%';
      
      container.innerHTML = '';
      container.appendChild(canvas);

      const engine = new Ex.Engine({
        canvasElement: canvas,
        width: canvas.width,
        height: canvas.height,
        displayMode: Ex.DisplayMode.FitScreen,
        backgroundColor: Ex.Color.fromHex('#0a0e1a')
      });

      const scene = new Ex.Scene();
      engine.addScene('main', scene);
      
      // Fundo com estrelas
      this.createStarfield(scene, Ex);
      
      this.excaliburEngine = engine;
      this.excaliburScene = scene;
      
      await engine.start();
      engine.goToScene('main');
      
      console.log('Excalibur iniciado com sucesso');
    } catch (error) {
      console.log('Erro ao iniciar Excalibur:', error);
    }
  }

  createStarfield(scene, Ex) {
    for (let i = 0; i < 50; i++) {
      const star = new Ex.Actor({
        pos: new Ex.Vector(
          Math.random() * 1200,
          Math.random() * 280
        ),
        width: 2,
        height: 2,
        color: Ex.Color.White
      });
      
      star.graphics.opacity = Math.random() * 0.7 + 0.3;
      scene.add(star);
      
      // Animação de pulsar
      star.actions.repeatForever(ctx => {
        ctx.fade(0.3, 2000).fade(1, 2000);
      });
    }
  }

  async loadEntities() {
    console.log('🔍 Carregando entidades...');
    try {
      const res = await fetch('/api/entities');
      
      if (!res.ok) {
        throw new Error(`HTTP ${res.status}: ${res.statusText}`);
      }
      
      const data = await res.json();
      console.log('✅ Entidades carregadas:', data.entities.length, 'fontes encontradas');
      console.log('📊 Detalhes:', data.entities.map(e => `${e.emoji} ${e.nome} (${e.liberado ? 'Liberado' : 'Bloqueado'})`));
      
      this.updatePistasDisplay(data.pistas || []);
      this.renderEntities(data.entities);
      this.updateExcaliburActors(data.entities);
      
      this.previousEntitiesState = {};
      data.entities.forEach(e => {
        this.previousEntitiesState[e.id] = { liberado: e.liberado };
      });
    } catch (error) {
      console.error('❌ Erro ao carregar entidades:', error);
      
      // Mostrar mensagem de erro no grid
      if (this.entitiesGrid) {
        this.entitiesGrid.innerHTML = `
          <div style="grid-column: 1/-1; text-align: center; padding: 40px; color: #ff6b6b;">
            <div style="font-size: 48px; margin-bottom: 15px;">⚠️</div>
            <p style="font-size: 18px; margin-bottom: 10px;">Erro ao carregar fontes</p>
            <p style="font-size: 14px; color: #888;">${error.message}</p>
            <button onclick="location.reload()" style="margin-top: 20px; padding: 10px 20px; background: #3b82f6; border: none; border-radius: 6px; color: white; cursor: pointer;">
              🔄 Recarregar Página
            </button>
          </div>
        `;
      }
    }
  }

  renderEntities(entities) {
    if (!this.entitiesGrid) {
      console.error('❌ Grid de entidades não encontrado!');
      return;
    }
    
    console.log(`🎨 Renderizando ${entities.length} entidades no grid...`);
    this.entitiesGrid.innerHTML = '';
    
    if (entities.length === 0) {
      this.entitiesGrid.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 40px; color: #888;">
          <div style="font-size: 48px; margin-bottom: 15px;">🔍</div>
          <p>Nenhuma fonte encontrada</p>
          <p style="font-size: 12px; margin-top: 10px;">Verifique o console (F12) para mais detalhes</p>
        </div>
      `;
      return;
    }
    
    entities.forEach((entity, index) => {
      const card = this.createEntityCard(entity);
      this.entitiesGrid.appendChild(card);
      console.log(`  ${index + 1}. ${entity.emoji} ${entity.nome} - ${entity.liberado ? '✅ Disponível' : '🔒 Bloqueado'}`);
    });
    
    console.log('✅ Entidades renderizadas com sucesso!');
  }

  createEntityCard(entity) {
    const card = document.createElement('div');
    card.className = 'entity-card';
    
    if (!entity.liberado) {
      card.classList.add('locked');
    }
    
    // Removido: não mostrar requisitos de pistas nos cards
    const lockMessage = !entity.liberado 
      ? '<p class="unlock-requirement">🔐 Complete enigmas para desbloquear</p>'
      : '';
    
    card.innerHTML = `
      <div class="entity-card-header">
        <span class="entity-emoji-large">${entity.emoji || '❓'}</span>
        <div class="entity-info">
          <h3>${entity.nome}</h3>
          <p class="discipline">${entity.disciplina}</p>
        </div>
      </div>
      ${lockMessage}
      ${!entity.liberado ? '<span class="lock-indicator">🔒</span>' : ''}
    `;
    
    if (entity.liberado) {
      card.addEventListener('click', () => this.selectEntity(entity));
    }
    
    return card;
  }

  updateExcaliburActors(entities) {
    if (!this.excaliburScene || !window.ex) return;
    
    const Ex = window.ex;
    const totalEntities = entities.length;
    const canvasWidth = 1200;
    const spacing = totalEntities > 1 ? canvasWidth / (totalEntities + 1) : canvasWidth / 2;
    
    entities.forEach((entity, index) => {
      const x = spacing * (index + 1);
      const y = 140;
      
      if (this.entityActors[entity.id]) {
        // Atualizar actor existente
        const actor = this.entityActors[entity.id];
        const prev = this.previousEntitiesState[entity.id];
        
        // Mudar cor baseado em desbloqueio
        actor.color = entity.liberado 
          ? Ex.Color.fromHex('#a855f7') 
          : Ex.Color.fromHex('#4b5563');
        
        // Animação de desbloqueio
        if (entity.liberado && prev && !prev.liberado) {
          actor.actions.scaleTo(new Ex.Vector(1.5, 1.5), new Ex.Vector(200, 200))
                      .scaleTo(new Ex.Vector(1, 1), new Ex.Vector(200, 200));
          
          // Efeito de partículas
          this.createUnlockParticles(Ex, x, y);
        }
        
        actor.pos = new Ex.Vector(x, y);
      } else {
        // Criar novo actor
        const actor = this.createEntityActor(Ex, entity, x, y);
        this.excaliburScene.add(actor);
        this.entityActors[entity.id] = actor;
      }
    });
  }

  createEntityActor(Ex, entity, x, y) {
    const actor = new Ex.Actor({
      pos: new Ex.Vector(x, y),
      width: 80,
      height: 80,
      color: entity.liberado 
        ? Ex.Color.fromHex('#a855f7') 
        : Ex.Color.fromHex('#4b5563')
    });
    
    actor.anchor = new Ex.Vector(0.5, 0.5);
    
    // Adicionar label de texto
    const label = new Ex.Label({
      text: (entity.nome || '').split(' ')[0],
      pos: new Ex.Vector(0, 60),
      font: new Ex.Font({
        size: 16,
        family: 'Arial',
        color: entity.liberado ? Ex.Color.White : Ex.Color.Gray
      })
    });
    label.anchor = new Ex.Vector(0.5, 0);
    actor.addChild(label);
    
    // Animação flutuante
    if (entity.liberado) {
      actor.actions.repeatForever(ctx => {
        ctx.moveBy(0, -10, 50)
          .moveBy(0, 10, 50);
      });
    }
    
    // Click handler
    actor.on('pointerup', () => {
      if (entity.liberado) {
        this.selectEntity(entity);
      }
    });
    
    return actor;
  }

  createUnlockParticles(Ex, x, y) {
    for (let i = 0; i < 20; i++) {
      const particle = new Ex.Actor({
        pos: new Ex.Vector(x, y),
        width: 4,
        height: 4,
        color: Ex.Color.fromHex('#a855f7')
      });
      
      const angle = (Math.PI * 2 * i) / 20;
      const speed = 100 + Math.random() * 100;
      const vx = Math.cos(angle) * speed;
      const vy = Math.sin(angle) * speed;
      
      this.excaliburScene.add(particle);
      
      particle.actions
        .moveBy(vx, vy, 500)
        .fade(0, 500)
        .die();
    }
  }

  async selectEntity(entity) {
    this.currentEntity = entity;
    
    // Carregar histórico do banco de dados
    await this.loadChatHistory(entity.id);
    
    // Iniciar som ambiente específico do personagem
    soundManager.startAmbientePersonagem(entity.id);
    
    if (this.entityName) this.entityName.textContent = entity.nome;
    if (this.entityEmoji) this.entityEmoji.textContent = entity.emoji || '❓';
    if (this.entityDiscipline) this.entityDiscipline.textContent = entity.disciplina;
    
    // Carregar desafios desta entidade
    this.carregarDesafios(entity.id);
    
    // VERIFICAR se deve mostrar contra-pergunta do Coltan (Dr. Arnaldo com >3 interações)
    if (entity.id === 'biologo' && this.chatHistory.length >= 6) {
      // 6 mensagens = 3 interações (pergunta + resposta)
      console.log('🔔 Dr. Arnaldo tem mais de 3 interações - verificando contra-pergunta...');
      await this.verificarContraPerguntaColtan();
    }
    
    if (this.chatArea) {
      this.chatArea.style.display = 'block';
      this.chatArea.scrollIntoView({ behavior: 'smooth' });
    }
    
    if (this.chatLog) {
      this.chatLog.innerHTML = '';
      
      // Se já tem histórico, renderizar as mensagens
      if (this.chatHistory.length > 0) {
        this.renderChatHistory();
      } else {
        // Primeira vez conversando - mostrar introdução
        this.adicionarAudioIntroducao(entity);
        this.appendSystemMessage(`💬 Entrevista iniciada com ${entity.nome}. Faça perguntas para descobrir pistas!`);
      }
    }
    
    if (this.chatInput) {
      this.chatInput.focus();
    }
  }

  async loadChatHistory(entityId) {
    try {
      const res = await fetch(`/api/chat/history/${entityId}`);
      const data = await res.json();
      
      if (data.history && data.history.length > 0) {
        this.chatHistory = data.history;
        console.log(`📚 Histórico carregado: ${data.history.length} mensagens`);
      } else {
        this.chatHistory = [];
        console.log('📭 Nenhum histórico encontrado - primeira conversa');
      }
    } catch (error) {
      console.error('Erro ao carregar histórico:', error);
      this.chatHistory = [];
    }
  }

  renderChatHistory() {
    console.log(`🎨 Renderizando ${this.chatHistory.length} mensagens do histórico...`);
    
    // Renderizar histórico existente
    this.chatHistory.forEach((msg, index) => {
      console.log(`  Mensagem ${index + 1}: ${msg.role} - ${msg.content.substring(0, 50)}...`);
      if (msg.role === 'user') {
        this.appendUserMessage(msg.content);
      } else if (msg.role === 'assistant') {
        this.appendEntityMessage(msg.content);
      }
    });
    
    // Adicionar mensagem de continuação
    this.appendSystemMessage(`🔄 Conversa retomada com ${this.currentEntity.nome}. Continue de onde parou!`);
  }

  adicionarAudioIntroducao(entity) {
    // Mapear entidades para arquivos de áudio
    const audioMap = {
      'biologo': 'arnaldo_intro.mp3',
      'fazendeiro': 'valdemar_intro.mp3',
      'lider_indigena': 'yakamu_intro.mp3',
      'podcaster': 'falcao_intro.mp3',
      'coronel': 'coronel_intro.mp3',
      'politico': 'venturi_confissao.mp3'
    };
    
    const audioFile = audioMap[entity.id];
    if (!audioFile) {
      console.log(`⚠️ Nenhum áudio de introdução mapeado para ${entity.id}`);
      return;
    }
    
    // Verificar se o arquivo existe antes de tentar adicionar
    const audioPath = `/static/audio/${audioFile}`;
    const testAudio = new Audio(audioPath);
    
    testAudio.addEventListener('error', () => {
      console.log(`⚠️ Áudio de introdução não disponível para ${entity.nome}`);
      // Não mostrar nada se o áudio não existir
    });
    
    testAudio.addEventListener('canplaythrough', () => {
      // Áudio existe, adicionar player ao chat
      const audioContainer = document.createElement('div');
      audioContainer.className = 'chat-message system-message audio-intro-message';
      audioContainer.innerHTML = `
        <div class="audio-intro-box">
          <div class="audio-intro-header">
            <span class="audio-icon">🎙️</span>
            <span class="audio-title">Introdução - ${entity.nome}</span>
          </div>
          <audio controls class="entity-audio">
            <source src="${audioPath}" type="audio/mpeg">
            Seu navegador não suporta o elemento de áudio.
          </audio>
        </div>
      `;
      
      this.chatLog.appendChild(audioContainer);
      console.log(`✅ Player de áudio adicionado para ${entity.nome}`);
    }, { once: true });
  }

  // Sugestões de perguntas removidas - jogador explora livremente

  closeChatArea() {
    // Tocar som de estática ao fechar
    soundManager.play('estatica');
    
    if (this.chatArea) {
      this.chatArea.style.display = 'none';
    }
    this.currentEntity = null;
  }

  async handleChatSubmit(e) {
    e.preventDefault();
    
    if (!this.currentEntity) {
      alert('Selecione uma entidade primeiro');
      return;
    }
    
    const message = this.chatInput.value.trim();
    if (!message) return;
    
    this.appendUserMessage(message);
    this.chatInput.value = '';
    
    // Mostrar indicador de digitação
    const typingIndicator = this.showTypingIndicator();
    
    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          entity_id: this.currentEntity.id,
          message: message
          // Histórico agora vem do banco de dados - não precisa enviar
        })
      });
      
      const data = await res.json();
      
      // Remover indicador de digitação
      if (typingIndicator && typingIndicator.parentNode) {
        typingIndicator.remove();
      }
      
      // Adicionar ao histórico LOCAL (para manter sincronizado)
      this.chatHistory.push({ role: 'user', content: message });
      this.chatHistory.push({ role: 'assistant', content: data.reply });
      
      this.appendEntityMessage(data.reply);
      
      // Verificar se há contra-pergunta (para Anomalia Química Coltan)
      if (data.contra_pergunta) {
        this.mostrarContraPergunta(data.contra_pergunta);
      }
      
      if (data.pistas_encontradas && data.pistas_encontradas.length > 0) {
        data.pistas_encontradas.forEach(pista => {
          this.showCollectButton(pista);
        });
      }
      
      // Mostrar contador de interações (para debug/progresso)
      if (data.interacoes && this.currentEntity.id === 'biologo') {
        const interacoes = data.interacoes;
        if (interacoes < 6) {
          console.log(`Interações com Dr. Arnaldo: ${interacoes}/6 para desbloquear pista especial`);
        }
      }
    } catch (error) {
      console.error('Erro ao enviar mensagem:', error);
      
      // Remover indicador de digitação em caso de erro
      if (typingIndicator && typingIndicator.parentNode) {
        typingIndicator.remove();
      }
      
      this.appendSystemMessage('❌ Erro ao comunicar com o servidor. Tente novamente.');
    }
  }

  showTypingIndicator() {
    const div = document.createElement('div');
    div.className = 'chat-message entity typing-indicator';
    div.innerHTML = `
      <div class="message-sender entity">${this.currentEntity.nome}</div>
      <div class="message-content">
        <span class="typing-dots">
          <span>●</span>
          <span>●</span>
          <span>●</span>
        </span>
      </div>
    `;
    this.chatLog.appendChild(div);
    this.chatLog.scrollTop = this.chatLog.scrollHeight;
    return div;
  }

  appendUserMessage(text) {
    const div = document.createElement('div');
    div.className = 'chat-message user';
    div.innerHTML = `
      <div class="message-sender user">Você</div>
      <div class="message-content">${this.escapeHtml(text)}</div>
    `;
    this.chatLog.appendChild(div);
    this.chatLog.scrollTop = this.chatLog.scrollHeight;
  }

  appendEntityMessage(text) {
    const div = document.createElement('div');
    div.className = 'chat-message entity';
    div.innerHTML = `
      <div class="message-sender entity">${this.currentEntity.nome}</div>
      <div class="message-content">${this.escapeHtml(text)}</div>
    `;
    this.chatLog.appendChild(div);
    this.chatLog.scrollTop = this.chatLog.scrollHeight;
  }

  appendSystemMessage(text) {
    const div = document.createElement('div');
    div.className = 'chat-message';
    div.innerHTML = `
      <div class="message-content" style="background: #374151; color: #d1d5db; border: none;">
        <em>💡 ${this.escapeHtml(text)}</em>
      </div>
    `;
    this.chatLog.appendChild(div);
    this.chatLog.scrollTop = this.chatLog.scrollHeight;
  }

  showCollectButton(pista) {
    // Verificar se a pista já foi coletada
    if (this.pistasColetadas.includes(pista)) {
      console.log(`⚠️ Pista "${pista}" já foi coletada anteriormente. Ignorando.`);
      return;
    }
    
    const btn = document.createElement('button');
    btn.className = 'collect-pista-btn';
    btn.textContent = `🔍 Coletar pista: ${pista}`;
    btn.dataset.pista = pista; // Adicionar identificador
    
    btn.addEventListener('click', async () => {
      btn.disabled = true;
      await this.collectPista(pista, btn);
    });
    
    this.chatLog.appendChild(btn);
    this.chatLog.scrollTop = this.chatLog.scrollHeight;
  }

  async collectPista(pista, buttonElement) {
    try {
      const res = await fetch('/api/collect', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ pista })
      });
      
      const data = await res.json();
      
      // DEBUG: Verificar resposta
      console.log('📦 Resposta /api/collect:', data);
      console.log('🔍 Enigma disponível?', data.enigma_disponivel);
      
      // Tocar som de conquista
      soundManager.play('pistaColetada');
      
      // Remover o botão após coletar
      if (buttonElement) {
        buttonElement.style.transition = 'opacity 0.5s, transform 0.5s';
        buttonElement.style.opacity = '0';
        buttonElement.style.transform = 'scale(0.8)';
        setTimeout(() => buttonElement.remove(), 500);
      }
      
      this.appendSystemMessage(`Pista "${pista}" adicionada ao dossiê!`);
      this.updatePistasDisplay(data.pistas);
      this.renderEntities(data.entities);
      this.updateExcaliburActors(data.entities);
      
      // Verificar se há enigma disponível
      if (data.enigma_disponivel) {
        console.log('🎯 Mostrando enigma:', data.enigma_disponivel.titulo);
        this.mostrarEnigma(data.enigma_disponivel);
      }
      
      // Atualizar estado anterior
      data.entities.forEach(e => {
        this.previousEntitiesState[e.id] = { liberado: e.liberado };
      });
    } catch (error) {
      console.error('Erro ao coletar pista:', error);
      this.appendSystemMessage('Erro ao coletar pista');
    }
  }

  updatePistasDisplay(pistas) {
    // Atualizar array local de pistas coletadas
    this.pistasColetadas = pistas;
    
    // Atualizar ambos os contadores
    if (this.pistasCount) {
      this.pistasCount.textContent = pistas.length;
    }
    if (this.pistasCountDossie) {
      this.pistasCountDossie.textContent = pistas.length;
    }
    
    if (this.pistasList) {
      if (pistas.length === 0) {
        this.pistasList.innerHTML = '<p class="empty-state">Nenhuma pista coletada ainda...</p>';
        // Esconder botão de enigmas se não tem pistas
        if (this.btnVerificarEnigmas) {
          this.btnVerificarEnigmas.style.display = 'none';
        }
      } else {
        this.pistasList.innerHTML = '';
        pistas.forEach(pista => {
          const badge = document.createElement('span');
          badge.className = 'pista-badge';
          badge.textContent = pista;
          badge.style.cursor = 'pointer';
          badge.title = 'Clique para ver detalhes';
          
          // Adicionar evento de clique para mostrar detalhes
          badge.addEventListener('click', () => this.mostrarDetalhesPista(pista));
          
          this.pistasList.appendChild(badge);
        });
        
        // Mostrar botão de enigmas se tem 2 ou mais pistas
        if (this.btnVerificarEnigmas && pistas.length >= 2) {
          this.btnVerificarEnigmas.style.display = 'block';
        }
      }
    }
  }
  
  async mostrarDetalhesPista(pista) {
    try {
      const res = await fetch('/api/pistas/detalhes');
      const data = await res.json();
      
      const pistaInfo = data.pistas[pista];
      if (!pistaInfo) {
        alert('Informações da pista não encontradas');
        return;
      }
      
      // Criar modal com detalhes da pista
      const modal = document.createElement('div');
      modal.className = 'modal-pista-detalhe';
      modal.innerHTML = `
        <div class="modal-pista-content">
          <div class="pista-header">
            <h2>${pistaInfo.titulo}</h2>
            <button class="close-pista-modal">×</button>
          </div>
          <div class="pista-body">
            <div class="pista-meta">
              <span class="pista-disciplina">📚 ${pistaInfo.disciplina}</span>
              <span class="pista-fonte">👤 Fonte: ${pistaInfo.fonte}</span>
            </div>
            ${pistaInfo.importancia ? `<div class="pista-importancia">${pistaInfo.importancia}</div>` : ''}
            <p class="pista-descricao">${pistaInfo.descricao}</p>
            <div class="pista-detalhes">
              <h3>🔍 Análise Detalhada:</h3>
              <p>${pistaInfo.detalhes}</p>
            </div>
            ${pistaInfo.historia ? `
              <div class="pista-historia">
                <h3>📖 Na História de Gian:</h3>
                <p>${pistaInfo.historia}</p>
              </div>
            ` : ''}
            <div class="pista-conexoes">
              <h3>🔗 Conexões com outras pistas:</h3>
              <div class="conexoes-lista">
                ${pistaInfo.conexoes.map(conexao => {
                  const pistaConectada = data.pistas[conexao];
                  const coletada = pistaConectada && pistaConectada.coletada;
                  return `<span class="conexao-badge ${coletada ? 'coletada' : 'nao-coletada'}">
                    ${coletada ? '✅' : '🔒'} ${conexao.replace(/_/g, ' ')}
                  </span>`;
                }).join('')}
              </div>
              <p class="dica-investigacao">💡 Colete todas as pistas conectadas para montar o dossiê completo de Gian!</p>
            </div>
          </div>
        </div>
      `;
      
      document.body.appendChild(modal);
      
      // Event listener para fechar
      modal.querySelector('.close-pista-modal').addEventListener('click', () => {
        modal.remove();
      });
      
      modal.addEventListener('click', (e) => {
        if (e.target === modal) {
          modal.remove();
        }
      });
      
    } catch (error) {
      console.error('Erro ao buscar detalhes da pista:', error);
      alert('Erro ao carregar detalhes da pista');
    }
  }
  
  async verificarContraPerguntaColtan() {
    // Fazer uma pergunta "dummy" para triggerar a contra-pergunta
    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          entity_id: this.currentEntity.id,
          message: '.' // Mensagem mínima apenas para triggerar verificação
        })
      });
      
      const data = await res.json();
      
      // Se retornou contra-pergunta, mostrar
      if (data.contra_pergunta) {
        console.log('✅ Contra-pergunta detectada! Mostrando agora...');
        this.mostrarContraPergunta(data.contra_pergunta);
      } else {
        console.log('❌ Contra-pergunta não retornada - pode já ter sido respondida');
      }
    } catch (error) {
      console.error('Erro ao verificar contra-pergunta:', error);
    }
  }
  
  mostrarContraPergunta(contraPergunta) {
    // Tocar som de alerta
    soundManager.play('alerta');
    
    // Criar elemento de contra-pergunta interativo
    const div = document.createElement('div');
    div.className = 'contra-pergunta-box';
    div.innerHTML = `
      <div class="contra-pergunta-header">
        <span class="emoji-pensativo">🤔</span>
        <p class="contra-pergunta-texto">${contraPergunta.texto}</p>
      </div>
      <div class="contra-pergunta-opcoes">
        <button class="btn-contra-resposta" data-resposta="sim">
          ${contraPergunta.opcoes[0]}
        </button>
        <button class="btn-contra-resposta" data-resposta="nao">
          ${contraPergunta.opcoes[1]}
        </button>
      </div>
    `;
    
    this.chatLog.appendChild(div);
    this.chatLog.scrollTop = this.chatLog.scrollHeight;
    
    // Event listeners para as respostas
    div.querySelectorAll('.btn-contra-resposta').forEach(btn => {
      btn.addEventListener('click', async () => {
        const resposta = btn.dataset.resposta;
        
        // Desabilitar botões
        div.querySelectorAll('.btn-contra-resposta').forEach(b => b.disabled = true);
        
        if (resposta === 'sim') {
          // Enviar mensagem especial para obter a pista Química_Coltan
          await this.responderContraPergunta('Sim, quero saber os detalhes técnicos da anomalia');
        } else {
          this.appendSystemMessage('Dr. Arnaldo suspira e continua a conversa...');
        }
        
        // Remover a contra-pergunta após resposta
        setTimeout(() => div.remove(), 2000);
      });
    });
  }
  
  async responderContraPergunta(mensagem) {
    this.appendUserMessage(mensagem);
    
    const typingIndicator = this.showTypingIndicator();
    
    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          entity_id: this.currentEntity.id,
          message: mensagem,
          resposta_contra_pergunta: 'sim'  // Flag especial - histórico vem do banco
        })
      });
      
      const data = await res.json();
      
      if (typingIndicator && typingIndicator.parentNode) {
        typingIndicator.remove();
      }
      
      // Resposta especial com a anomalia química
      const respostaEspecial = `*Dr. Arnaldo ajusta os óculos e mostra seus dados*

Muito bem. Vou ser específico.

Nas amostras que coletei, identifiquei uma ANOMALIA QUÍMICA muito particular: compostos de fluoreto e ácido nítrico em concentrações absurdas. Esse coquetel químico específico só tem UMA aplicação conhecida...

Processamento de COLTAN - Columbita-Tantalita.

*mostra gráficos*

É o mineral usado em todos os dispositivos eletrônicos modernos. Celulares, laptops, drones... Vale mais que ouro. E alguém está processando toneladas dele ilegalmente aqui.

*voz baixa* Por isso o Gian desapareceu. Ele descobriu a verdade.`;
      
      this.chatHistory.push({ role: 'user', content: mensagem });
      this.chatHistory.push({ role: 'assistant', content: respostaEspecial });
      
      this.appendEntityMessage(respostaEspecial);
      
      // Mostrar botão para coletar a pista especial
      if (data.pistas_encontradas && data.pistas_encontradas.includes('Química_Coltan')) {
        this.showCollectButton('Química_Coltan');
      } else {
        // Forçar aparição da pista (fallback)
        this.showCollectButton('Química_Coltan');
      }
      
    } catch (error) {
      console.error('Erro ao responder contra-pergunta:', error);
      if (typingIndicator && typingIndicator.parentNode) {
        typingIndicator.remove();
      }
    }
  }

  escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }
  
  // ============================================
  // SISTEMA DE DESAFIOS EDUCACIONAIS
  // ============================================
  
  async carregarDesafios(entityId) {
    try {
      const res = await fetch(`/api/desafios/${entityId}`);
      const data = await res.json();
      
      this.desafiosDisponiveis = data.desafios;
      
      // Atualizar badge
      if (this.desafiosBadge) {
        this.desafiosBadge.textContent = this.desafiosDisponiveis.length;
        this.desafiosBadge.style.display = this.desafiosDisponiveis.length > 0 ? 'inline' : 'none';
      }
      
      // Mostrar dicas desbloqueadas
      if (data.dicas && data.dicas.length > 0) {
        this.mostrarDicas(data.dicas);
      }
    } catch (error) {
      console.error('Erro ao carregar desafios:', error);
    }
  }
  
  mostrarDicas(dicas) {
    if (!this.dicasArea || !this.dicasList) return;
    
    this.dicasList.innerHTML = '';
    dicas.forEach(dica => {
      const div = document.createElement('div');
      div.className = 'dica-item';
      div.innerHTML = `<p>${dica.texto}</p>`;
      this.dicasList.appendChild(div);
    });
    
    this.dicasArea.style.display = dicas.length > 0 ? 'block' : 'none';
  }
  
  abrirDesafio() {
    if (this.desafiosDisponiveis.length === 0) {
      alert('🎉 Parabéns! Você completou todos os desafios desta entrevista!');
      return;
    }
    
    this.desafioAtual = this.desafiosDisponiveis[0];
    this.respostaSelecionada = null;
    
    // Preencher modal
    if (this.desafioDisciplina) {
      this.desafioDisciplina.textContent = `📚 Disciplina: ${this.desafioAtual.disciplina}`;
    }
    
    if (this.desafioPergunta) {
      this.desafioPergunta.textContent = this.desafioAtual.pergunta;
    }
    
    // Criar opções
    if (this.desafioOpcoes) {
      this.desafioOpcoes.innerHTML = '';
      this.desafioAtual.opcoes.forEach((opcao, index) => {
        const div = document.createElement('div');
        div.className = 'opcao-item';
        
        const radio = document.createElement('input');
        radio.type = 'radio';
        radio.name = 'resposta';
        radio.value = String.fromCharCode(65 + index); // A, B, C, D
        radio.id = `opcao-${index}`;
        radio.addEventListener('change', () => {
          this.respostaSelecionada = radio.value;
          if (this.btnConfirmarResposta) {
            this.btnConfirmarResposta.disabled = false;
          }
        });
        
        const label = document.createElement('label');
        label.htmlFor = `opcao-${index}`;
        label.textContent = opcao;
        
        div.appendChild(radio);
        div.appendChild(label);
        this.desafioOpcoes.appendChild(div);
      });
    }
    
    // Resetar áreas COMPLETAMENTE
    if (this.resultadoArea) {
      this.resultadoArea.style.display = 'none';
    }
    if (this.resultadoConteudo) {
      this.resultadoConteudo.innerHTML = '';
    }
    if (this.btnConfirmarResposta) {
      this.btnConfirmarResposta.disabled = true;
      this.btnConfirmarResposta.style.display = 'inline-block'; // Garantir que está visível
    }
    
    // Mostrar modal
    if (this.modalDesafio) {
      this.modalDesafio.style.display = 'flex';
    }
  }
  
  fecharModal() {
    if (this.modalDesafio) {
      this.modalDesafio.style.display = 'none';
    }
  }
  
  async confirmarResposta() {
    if (!this.respostaSelecionada || !this.desafioAtual) return;
    
    try {
      const res = await fetch('/api/desafios/responder', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          desafio_id: this.desafioAtual.id,
          resposta: this.respostaSelecionada
        })
      });
      
      const data = await res.json();
      
      // Mostrar resultado
      if (this.resultadoConteudo) {
        if (data.sucesso) {
          this.resultadoConteudo.innerHTML = `
            <div class="resultado-sucesso">
              <h3>✅ Correto!</h3>
              <p>${data.explicacao}</p>
              <div class="recompensa">
                ${data.dica_texto}
              </div>
            </div>
          `;
        } else {
          this.resultadoConteudo.innerHTML = `
            <div class="resultado-erro">
              <h3>❌ Incorreto</h3>
              <p><strong>Resposta correta:</strong> ${data.resposta_correta}</p>
              <p>${data.explicacao}</p>
              <p class="dica-erro">💡 Tente novamente! Você pode responder este desafio mais tarde.</p>
            </div>
          `;
        }
      }
      
      if (this.resultadoArea) {
        this.resultadoArea.style.display = 'block';
      }
      
      // Esconder botão de confirmar
      if (this.btnConfirmarResposta) {
        this.btnConfirmarResposta.style.display = 'none';
      }
      
      // Recarregar desafios se acertou
      if (data.sucesso && this.currentEntity) {
        await this.carregarDesafios(this.currentEntity.id);
      }
      
    } catch (error) {
      console.error('Erro ao confirmar resposta:', error);
      alert('Erro ao processar resposta. Tente novamente.');
    }
  }
  
  proximoDesafio() {
    // Resetar áreas antes de fechar
    if (this.resultadoArea) {
      this.resultadoArea.style.display = 'none';
    }
    if (this.resultadoConteudo) {
      this.resultadoConteudo.innerHTML = '';
    }
    if (this.btnConfirmarResposta) {
      this.btnConfirmarResposta.style.display = 'inline-block';
      this.btnConfirmarResposta.disabled = true;
    }
    
    // Fechar modal
    this.fecharModal();
    
    // Se ainda há desafios, abrir próximo
    if (this.desafiosDisponiveis.length > 0) {
      setTimeout(() => this.abrirDesafio(), 300);
    }
  }
  
  async verificarEnigmasDisponiveis() {
    try {
      const res = await fetch('/api/enigmas');
      const data = await res.json();
      
      if (data.enigma) {
        this.mostrarEnigma(data.enigma);
      } else {
        alert('📚 Nenhum enigma disponível no momento. Continue coletando pistas!');
      }
    } catch (error) {
      console.error('Erro ao verificar enigmas:', error);
      alert('Erro ao buscar enigmas. Tente novamente.');
    }
  }
  
  mostrarEnigma(enigma) {
    // Criar modal para enigma
    const enigmaModal = document.createElement('div');
    enigmaModal.className = 'modal-enigma';
    enigmaModal.innerHTML = `
      <div class="modal-enigma-content">
        <div class="enigma-header">
          <h2>🔐 ${enigma.titulo}</h2>
          <button class="close-enigma">×</button>
        </div>
        <div class="enigma-body">
          <p class="enigma-contexto">${enigma.contexto}</p>
          <h3 class="enigma-pergunta">${enigma.pergunta}</h3>
          <div class="enigma-opcoes">
            ${enigma.opcoes.map((opcao, idx) => `
              <label class="enigma-opcao">
                <input type="radio" name="enigma_resposta" value="${String.fromCharCode(65 + idx)}">
                <span>${opcao}</span>
              </label>
            `).join('')}
          </div>
          <button class="btn-confirmar-enigma">Confirmar Resposta</button>
        </div>
        <div class="enigma-resultado" style="display: none;"></div>
      </div>
    `;
    
    document.body.appendChild(enigmaModal);
    
    // Event listeners
    enigmaModal.querySelector('.close-enigma').addEventListener('click', () => {
      enigmaModal.remove();
    });
    
    enigmaModal.querySelector('.btn-confirmar-enigma').addEventListener('click', async () => {
      const resposta = enigmaModal.querySelector('input[name="enigma_resposta"]:checked');
      if (!resposta) {
        alert('Por favor, selecione uma resposta!');
        return;
      }
      
      await this.responderEnigma(enigma.id, resposta.value, enigmaModal);
    });
  }
  
  async responderEnigma(enigma_id, resposta, modal) {
    try {
      const res = await fetch('/api/enigmas/responder', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ enigma_id, resposta })
      });
      
      const data = await res.json();
      
      const resultadoDiv = modal.querySelector('.enigma-resultado');
      
      if (data.sucesso) {
        resultadoDiv.innerHTML = `
          <div class="enigma-sucesso">
            <h3>🎉 Correto!</h3>
            <p>${data.explicacao}</p>
            <p class="entidade-desbloqueada">✨ Desbloqueado: ${data.entidade_desbloqueada.nome}</p>
            <button class="btn-continuar">Continuar Investigação</button>
          </div>
        `;
        
        // Atualizar entidades
        if (data.entities) {
          this.renderEntities(data.entities);
          this.updateExcaliburActors(data.entities);
        }
        
        resultadoDiv.querySelector('.btn-continuar').addEventListener('click', () => {
          modal.remove();
        });
      } else {
        resultadoDiv.innerHTML = `
          <div class="enigma-erro">
            <h3>❌ Incorreto</h3>
            <p>${data.explicacao}</p>
            <button class="btn-tentar-novamente">Tentar Novamente</button>
          </div>
        `;
        
        resultadoDiv.querySelector('.btn-tentar-novamente').addEventListener('click', () => {
          resultadoDiv.style.display = 'none';
          modal.querySelector('.enigma-body').style.display = 'block';
        });
      }
      
      modal.querySelector('.enigma-body').style.display = 'none';
      resultadoDiv.style.display = 'block';
      
    } catch (error) {
      console.error('Erro ao responder enigma:', error);
      alert('Erro ao processar resposta. Tente novamente.');
    }
  }
}

// Inicializar quando a página carregar
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    new InterviewSystem();
  });
} else {
  new InterviewSystem();
}

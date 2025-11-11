// ============================================
// PROJETO SOMBRA ROXA - Interview System
// ============================================

class InterviewSystem {
  constructor() {
    this.currentEntity = null;
    this.previousEntitiesState = {};
    this.excaliburEngine = null;
    this.excaliburScene = null;
    this.entityActors = {};
    
    this.initElements();
    this.initExcalibur();
    this.loadEntities();
  }

  initElements() {
    this.entitiesGrid = document.getElementById('entities-grid');
    this.chatArea = document.getElementById('chat-area');
    this.chatLog = document.getElementById('chat-log');
    this.entityName = document.getElementById('entity-name');
    this.entityEmoji = document.getElementById('entity-emoji');
    this.entityDiscipline = document.getElementById('entity-discipline');
    this.chatForm = document.getElementById('chat-form');
    this.chatInput = document.getElementById('chat-input');
    this.pistasCount = document.getElementById('pistas-count');
    this.pistasList = document.getElementById('pistas-list');
    this.closeChat = document.getElementById('close-chat');

    if (this.chatForm) {
      this.chatForm.addEventListener('submit', (e) => this.handleChatSubmit(e));
    }

    if (this.closeChat) {
      this.closeChat.addEventListener('click', () => this.closeChatArea());
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
    try {
      const res = await fetch('/api/entities');
      const data = await res.json();
      
      this.updatePistasDisplay(data.pistas || []);
      this.renderEntities(data.entities);
      this.updateExcaliburActors(data.entities);
      
      this.previousEntitiesState = {};
      data.entities.forEach(e => {
        this.previousEntitiesState[e.id] = { liberado: e.liberado };
      });
    } catch (error) {
      console.error('Erro ao carregar entidades:', error);
    }
  }

  renderEntities(entities) {
    if (!this.entitiesGrid) return;
    
    this.entitiesGrid.innerHTML = '';
    
    entities.forEach(entity => {
      const card = this.createEntityCard(entity);
      this.entitiesGrid.appendChild(card);
    });
  }

  createEntityCard(entity) {
    const card = document.createElement('div');
    card.className = 'entity-card';
    
    if (!entity.liberado) {
      card.classList.add('locked');
    }
    
    const requirements = entity.requisito_desbloqueio || [];
    const reqText = requirements.length > 0 
      ? `<p class="unlock-requirement">🔐 Requer: ${requirements.join(', ')}</p>`
      : '';
    
    card.innerHTML = `
      <div class="entity-card-header">
        <span class="entity-emoji-large">${entity.emoji || '❓'}</span>
        <div class="entity-info">
          <h3>${entity.nome}</h3>
          <p class="discipline">${entity.disciplina}</p>
        </div>
      </div>
      ${reqText}
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

  selectEntity(entity) {
    this.currentEntity = entity;
    
    if (this.entityName) this.entityName.textContent = entity.nome;
    if (this.entityEmoji) this.entityEmoji.textContent = entity.emoji || '❓';
    if (this.entityDiscipline) this.entityDiscipline.textContent = entity.disciplina;
    
    if (this.chatArea) {
      this.chatArea.style.display = 'block';
      this.chatArea.scrollIntoView({ behavior: 'smooth' });
    }
    
    if (this.chatLog) {
      this.chatLog.innerHTML = '';
      this.appendSystemMessage(`Entrevista iniciada com ${entity.nome}`);
    }
    
    if (this.chatInput) {
      this.chatInput.focus();
    }
  }

  closeChatArea() {
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
    
    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          entity_id: this.currentEntity.id,
          message: message
        })
      });
      
      const data = await res.json();
      
      this.appendEntityMessage(data.reply);
      
      if (data.pistas_encontradas && data.pistas_encontradas.length > 0) {
        data.pistas_encontradas.forEach(pista => {
          this.showCollectButton(pista);
        });
      }
    } catch (error) {
      console.error('Erro ao enviar mensagem:', error);
      this.appendSystemMessage('Erro ao comunicar com o servidor');
    }
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
    const btn = document.createElement('button');
    btn.className = 'collect-pista-btn';
    btn.textContent = `🔍 Coletar pista: ${pista}`;
    
    btn.addEventListener('click', async () => {
      btn.disabled = true;
      await this.collectPista(pista);
    });
    
    this.chatLog.appendChild(btn);
    this.chatLog.scrollTop = this.chatLog.scrollHeight;
  }

  async collectPista(pista) {
    try {
      const res = await fetch('/api/collect', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ pista })
      });
      
      const data = await res.json();
      
      this.appendSystemMessage(`Pista "${pista}" adicionada ao dossiê!`);
      this.updatePistasDisplay(data.pistas);
      this.renderEntities(data.entities);
      this.updateExcaliburActors(data.entities);
      
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
    if (this.pistasCount) {
      this.pistasCount.textContent = pistas.length;
    }
    
    if (this.pistasList) {
      if (pistas.length === 0) {
        this.pistasList.innerHTML = '<p class="empty-state">Nenhuma pista coletada ainda...</p>';
      } else {
        this.pistasList.innerHTML = '';
        pistas.forEach(pista => {
          const badge = document.createElement('span');
          badge.className = 'pista-badge';
          badge.textContent = pista;
          this.pistasList.appendChild(badge);
        });
      }
    }
  }

  escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
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

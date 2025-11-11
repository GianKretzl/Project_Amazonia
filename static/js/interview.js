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
    this.chatHistory = [];  // Histórico de conversa
    this.desafiosDisponiveis = [];
    this.desafioAtual = null;
    this.respostaSelecionada = null;
    
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

  selectEntity(entity) {
    this.currentEntity = entity;
    this.chatHistory = [];  // Limpar histórico ao trocar de entidade
    
    if (this.entityName) this.entityName.textContent = entity.nome;
    if (this.entityEmoji) this.entityEmoji.textContent = entity.emoji || '❓';
    if (this.entityDiscipline) this.entityDiscipline.textContent = entity.disciplina;
    
    // Carregar desafios desta entidade
    this.carregarDesafios(entity.id);
    
    // Mostrar sugestões de perguntas
    this.showQuestionSuggestions(entity);
    
    if (this.chatArea) {
      this.chatArea.style.display = 'block';
      this.chatArea.scrollIntoView({ behavior: 'smooth' });
    }
    
    if (this.chatLog) {
      this.chatLog.innerHTML = '';
      this.appendSystemMessage(`💬 Entrevista iniciada com ${entity.nome}`);
    }
    
    if (this.chatInput) {
      this.chatInput.focus();
    }
  }

  showQuestionSuggestions(entity) {
    const suggestionsContainer = document.getElementById('suggestions-buttons');
    if (!suggestionsContainer) return;
    
    // Sugestões específicas por entidade
    const suggestions = {
      'biologo': [
        'O que é a sombra roxa?',
        'Você conhece a Gian Kretzl?',
        'O que é Coltan?',
        'Por que você está com medo?'
      ],
      'fazendeiro': [
        'O que você produz na fazenda?',
        'A fazenda é lucrativa?',
        'O que você sabe sobre a sombra roxa?',
        'Por que quer expandir para a reserva indígena?'
      ],
      'lider_indigena': [
        'O que aconteceu com o rio?',
        'O que é o Mapa da Montanha de Fogo?',
        'Quem é o homem de terno?',
        'O que você sabe sobre Coltan?'
      ],
      'politico': [
        'Qual é seu interesse na Amazônia?',
        'Você conhece o Valdemar?',
        'O que aconteceu com a Gian Kretzl?',
        'Qual é o verdadeiro plano?'
      ]
    };
    
    const entitySuggestions = suggestions[entity.id] || [
      'Conte-me sobre você',
      'O que você sabe sobre a investigação?',
      'Você pode me ajudar?'
    ];
    
    suggestionsContainer.innerHTML = '';
    entitySuggestions.forEach(question => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'suggestion-btn';
      btn.textContent = question;
      btn.addEventListener('click', () => {
        this.chatInput.value = question;
        this.chatInput.focus();
      });
      suggestionsContainer.appendChild(btn);
    });
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
    
    // Mostrar indicador de digitação
    const typingIndicator = this.showTypingIndicator();
    
    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          entity_id: this.currentEntity.id,
          message: message,
          history: this.chatHistory  // Enviar histórico
        })
      });
      
      const data = await res.json();
      
      // Remover indicador de digitação
      if (typingIndicator && typingIndicator.parentNode) {
        typingIndicator.remove();
      }
      
      // Adicionar ao histórico
      this.chatHistory.push({ role: 'user', content: message });
      this.chatHistory.push({ role: 'assistant', content: data.reply });
      
      this.appendEntityMessage(data.reply);
      
      if (data.pistas_encontradas && data.pistas_encontradas.length > 0) {
        data.pistas_encontradas.forEach(pista => {
          this.showCollectButton(pista);
        });
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
      
      // Verificar se há enigma disponível
      if (data.enigma_disponivel) {
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
    
    // Resetar áreas
    if (this.resultadoArea) {
      this.resultadoArea.style.display = 'none';
    }
    if (this.btnConfirmarResposta) {
      this.btnConfirmarResposta.disabled = true;
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
    this.fecharModal();
    
    // Se ainda há desafios, abrir próximo
    if (this.desafiosDisponiveis.length > 0) {
      setTimeout(() => this.abrirDesafio(), 300);
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

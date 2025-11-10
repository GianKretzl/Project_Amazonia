document.addEventListener('DOMContentLoaded', () => {
  const entitiesDiv = document.getElementById('entities');
  const chatArea = document.getElementById('chat-area');
  const chatLog = document.getElementById('chat-log');
  const entityName = document.getElementById('entity-name');
  const chatForm = document.getElementById('chat-form');
  const chatInput = document.getElementById('chat-input');

  let currentEntity = null;

  // manter último estado para detectar desbloqueios
  let previousEntitiesState = {};
  // map de imagens por id (pré-carregado)
  window.entityImages = window.entityImages || {};
  const entityImagePaths = {
    'biologo': '/static/img/biologo.svg',
    'fazendeiro': '/static/img/fazendeiro.svg',
    'lider_indigena': '/static/img/lider_indigena.svg',
    'politico': '/static/img/politico.svg'
  };
  // pré-carregar imagens
  Object.entries(entityImagePaths).forEach(([id, path]) => {
    const img = new Image();
    img.src = path;
    window.entityImages[id] = img;
  });

  async function loadEntities() {
    const res = await fetch('/api/entities');
    const data = await res.json();
    entitiesDiv.innerHTML = '';
    // posicionamento simples para a cena: espaçar actors horizontalmente
    const total = data.entities.length;
    const width = 760; // espaço dentro do container
    let idx = 0;
    data.entities.forEach(e => {
      const card = document.createElement('div');
      card.className = 'entity-card';
      card.innerHTML = `<strong>${e.nome}</strong> <em>(${e.disciplina})</em>`;
      if (!e.liberado) {
        card.classList.add('locked');
        card.innerHTML += ' <span class="lock">🔒</span>';
      } else {
        card.addEventListener('click', () => selectEntity(e));
      }
      entitiesDiv.appendChild(card);

      // atualizar/ criar actor na cena Excalibur (se disponível)
      try {
        if (window.exEngine) {
          const Ex = window.ex;
          const Actor = Ex.Actor;
          const Vector = Ex.Vector;
          const Color = Ex.Color;
          const x = 40 + Math.round((idx / Math.max(1, total - 1)) * width);
          const y = 80;
          // se já existe, atualiza cor/estado
          if (window.entityActors && window.entityActors[e.id]) {
            const actor = window.entityActors[e.id];
            // brincar com cor: desbloqueado -> verde mais vivo
            actor.color = e.liberado ? Color.fromHex('#4caf50') : Color.fromHex('#9e9e9e');
            // se acabou de ser desbloqueado -> animar
            const prev = previousEntitiesState[e.id];
            if (e.liberado && prev && !prev.liberado) {
              // pulse
              actor.actions.scaleTo(1.4, 1.4, 200).then(() => actor.actions.scaleTo(1, 1, 200));
            }
            actor.pos = new Vector(x, y);
              } else {
                const actor = new Actor({ pos: new Vector(x, y), width: 64, height: 64 });
                actor.color = e.liberado ? Color.fromHex('#4caf50') : Color.fromHex('#9e9e9e');
                actor.anchor.setTo(0.5, 0.5);
                // desenhar imagem (sprite) se carregada; fallback para label
                const ent = e; // capturar
                actor.on('postdraw', (ctx) => {
                  try {
                    const img = window.entityImages[ent.id];
                    if (img && img.complete) {
                      const w = 48, h = 48;
                      const dx = Math.round(actor.pos.x - w / 2);
                      const dy = Math.round(actor.pos.y - h / 2) - 6;
                      ctx.drawImage(img, dx, dy, w, h);
                    } else {
                      // fallback: círculo
                      ctx.save();
                      ctx.fillStyle = '#999';
                      ctx.beginPath();
                      ctx.arc(actor.pos.x, actor.pos.y, 24, 0, Math.PI * 2);
                      ctx.fill();
                      ctx.restore();
                    }
                    // label
                    ctx.save();
                    ctx.fillStyle = '#000';
                    ctx.font = '12px Arial';
                    ctx.textAlign = 'center';
                    ctx.fillText(ent.nome.split(' ')[0], actor.pos.x, actor.pos.y + 48);
                    ctx.restore();
                  } catch (err) {
                    // ignorar erros de desenho
                  }
                });
                window.scene.add(actor);
                window.entityActors = window.entityActors || {};
                window.entityActors[e.id] = actor;
              }
        }
      } catch (err) {
        // falha em animacao não é crítica
        console.log('Excalibur update ignorado:', err);
      }

      idx += 1;
    });

    // atualizar estado anterior
    previousEntitiesState = {};
    data.entities.forEach(e => previousEntitiesState[e.id] = { liberado: e.liberado });
  }

  function selectEntity(e) {
    currentEntity = e;
    entityName.textContent = e.nome + ' — ' + e.disciplina;
    chatArea.style.display = 'block';
    chatLog.innerHTML = '';
  }

  chatForm.addEventListener('submit', async (ev) => {
    ev.preventDefault();
    if (!currentEntity) return alert('Selecione uma entidade desbloqueada primeiro.');
    const message = chatInput.value.trim();
    if (!message) return;
    appendMessage('Você', message);
    chatInput.value = '';
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({entity_id: currentEntity.id, message})
    });
    const data = await res.json();
    appendMessage(currentEntity.nome, data.reply);
    if (data.pistas_encontradas && data.pistas_encontradas.length) {
      data.pistas_encontradas.forEach(p => showCollectButton(p));
    }
  });

  function appendMessage(who, text) {
    const p = document.createElement('p');
    p.innerHTML = `<strong>${who}:</strong> ${text}`;
    chatLog.appendChild(p);
    chatLog.scrollTop = chatLog.scrollHeight;
  }

  function showCollectButton(pista) {
    const btn = document.createElement('button');
    btn.textContent = `Coletar pista: ${pista}`;
    btn.addEventListener('click', async () => {
      btn.disabled = true;
      const res = await fetch('/api/collect', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({pista})
      });
      const data = await res.json();
      appendMessage('Sistema', `Pista '${pista}' adicionada ao dossiê.`);
      await loadEntities();
    });
    chatLog.appendChild(btn);
  }

  // iniciar
  loadEntities();

  // --- Inicializar Excalibur: criar engine e cena, anexar canvas ao container ---
  try {
    const Ex = window.ex; // Excalibur exportado via <script src>
    if (Ex) {
      const { Engine, Scene, Actor, Vector, Color } = Ex;
      const container = document.getElementById('excalibur-container');
      const canvas = document.createElement('canvas');
      canvas.style.maxWidth = '100%';
      canvas.width = 800;
      canvas.height = 160;
      container.innerHTML = '';
      container.appendChild(canvas);

      const engine = new Engine({ canvasElement: canvas, width: canvas.width, height: canvas.height });
      const scene = new Scene();
      engine.addScene('main', scene);
      window.exEngine = engine;
      window.scene = scene;
      engine.start();

      // fundo
      const bg = new Actor({ pos: new Vector(canvas.width / 2, canvas.height / 2), width: canvas.width, height: canvas.height });
      bg.color = Color.fromHex('#e8f5e9');
      scene.add(bg);
    }
  } catch (e) {
    console.log('Excalibur não inicializado (ok no protótipo):', e);
  }
});

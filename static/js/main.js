// ============================================
// PROJETO SOMBRA ROXA - Main Script
// ============================================

// Efeitos para a página inicial
if (document.querySelector('.terminal-body')) {
  // Animação de digitação para textos
  document.querySelectorAll('.typing-text').forEach(element => {
    const text = element.dataset.text || element.textContent;
    element.textContent = '';
    let i = 0;
    
    const typeWriter = () => {
      if (i < text.length) {
        element.textContent += text.charAt(i);
        i++;
        setTimeout(typeWriter, 50);
      }
    };
    
    // Aguardar animação de fade-in antes de iniciar digitação
    const delay = parseFloat(getComputedStyle(element.closest('.terminal-line')).animationDelay) * 1000 || 0;
    setTimeout(typeWriter, delay + 500);
  });
}

// Sistema de entrevistas (se estiver na página de interview)
if (document.getElementById('entities-grid')) {
  // Import do sistema de entrevistas
  const script = document.createElement('script');
  script.src = document.querySelector('[src*="main.js"]')?.src.replace('main.js', 'interview.js') || '/static/js/interview.js';
  document.body.appendChild(script);
}

// Efeitos visuais globais
document.addEventListener('DOMContentLoaded', () => {
  // Adicionar efeito de hover em botões
  document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-2px)';
    });
    
    btn.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0)';
    });
  });

  // Easter egg: Konami Code
  let konamiCode = [];
  const konamiPattern = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];
  
  document.addEventListener('keydown', (e) => {
    konamiCode.push(e.key);
    konamiCode = konamiCode.slice(-10);
    
    if (konamiCode.join(',') === konamiPattern.join(',')) {
      unlockEasterEgg();
    }
  });
  
  function unlockEasterEgg() {
    const audio = new Audio('data:audio/wav;base64,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');
    audio.play().catch(() => {});
    
    document.body.style.animation = 'rainbow 2s linear infinite';
    
    const style = document.createElement('style');
    style.textContent = `
      @keyframes rainbow {
        0% { filter: hue-rotate(0deg); }
        100% { filter: hue-rotate(360deg); }
      }
    `;
    document.head.appendChild(style);
    
    setTimeout(() => {
      document.body.style.animation = '';
      alert('🎮 Modo Desenvolvedor Ativado!\n\nTodas as entidades foram desbloqueadas temporariamente.');
    }, 2000);
  }
});

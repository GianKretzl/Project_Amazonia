import os
from flask import Flask, render_template, jsonify, request, session
from dotenv import load_dotenv
from datetime import datetime
import entidades
import desafios
import enigmas
from simulated_ai import simulated_reply_improved
from database import db
import hashlib
import secrets

load_dotenv()

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
    openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
except Exception:
    openai_client = None
    OPENAI_AVAILABLE = False

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-change-me')

    @app.before_request
    def ensure_session():
        # Gerar ID de sessão único se não existir
        if 'session_id' not in session:
            import uuid
            session['session_id'] = str(uuid.uuid4())
        
        # Garantir que o jogador existe no banco
        db.ensure_player(session['session_id'])
        
        # Manter alguns dados em sessão para compatibilidade
        if 'grupo' not in session:
            session['grupo'] = None
        if 'integrantes' not in session:
            session['integrantes'] = []
        if 'dicas_desbloqueadas' not in session:
            session['dicas_desbloqueadas'] = []

    @app.route('/')
    def login():
        # Página de login é a primeira
        return render_template('login.html')

    @app.route('/intro')
    def index():
        # Página inicial após login
        return render_template('index.html')

    @app.route('/api/login', methods=['POST'])
    def api_login():
        """Nova investigação - criar usuário e gerar senha"""
        data = request.get_json() or {}
        usuario = data.get('usuario', '').strip()
        grupo = data.get('grupo', '').strip()
        integrantes = data.get('integrantes', [])
        
        if not usuario or not grupo or len(integrantes) == 0 or len(integrantes) > 6:
            return jsonify({'success': False, 'error': 'Dados inválidos'}), 400
        
        # Gerar senha aleatória (6 caracteres alfanuméricos)
        senha = secrets.token_urlsafe(6)[:8].upper()
        
        # Hash da senha
        password_hash = hashlib.sha256(senha.encode()).hexdigest()
        
        # Criar usuário no banco
        user_id = db.create_user(usuario, password_hash, grupo, integrantes)
        
        if user_id is None:
            return jsonify({'success': False, 'error': 'Nome de usuário já existe! Escolha outro.'}), 400
        
        # Configurar sessão
        session['user_id'] = user_id
        session['username'] = usuario
        session['grupo'] = grupo
        session['integrantes'] = integrantes
        session['login_timestamp'] = str(datetime.now())
        
        # Vincular sessão ao usuário
        db.link_session_to_user(session['session_id'], user_id)
        
        return jsonify({
            'success': True, 
            'senha': senha,
            'grupo': grupo, 
            'integrantes': integrantes
        })
    
    @app.route('/api/login/continue', methods=['POST'])
    def api_login_continue():
        """Continuar investigação - autenticar usuário"""
        data = request.get_json() or {}
        usuario = data.get('usuario', '').strip()
        senha = data.get('senha', '').strip()
        
        if not usuario or not senha:
            return jsonify({'success': False, 'error': 'Usuário e senha são obrigatórios'}), 400
        
        # Hash da senha
        password_hash = hashlib.sha256(senha.encode()).hexdigest()
        
        # Autenticar
        user_data = db.authenticate_user(usuario, password_hash)
        
        if user_data is None:
            return jsonify({'success': False, 'error': 'Usuário ou senha incorretos'}), 401
        
        # Configurar sessão com dados do usuário
        session['user_id'] = user_data['id']
        session['username'] = user_data['username']
        session['grupo'] = user_data['grupo']
        session['integrantes'] = user_data['integrantes']
        session['login_timestamp'] = str(datetime.now())
        
        # Buscar sessão anterior ou criar nova vinculada
        old_session_id = db.get_user_session(user_data['id'])
        if old_session_id:
            session['session_id'] = old_session_id
        else:
            db.link_session_to_user(session['session_id'], user_data['id'])
        
        return jsonify({
            'success': True,
            'grupo': user_data['grupo'],
            'integrantes': user_data['integrantes']
        })
    
    @app.route('/api/logout', methods=['POST'])
    def api_logout():
        """Salvar progresso e fazer logout"""
        # O progresso já está salvo no banco automaticamente
        # Apenas limpar a sessão
        session_id = session.get('session_id')
        username = session.get('username')
        
        # Limpar sessão
        session.clear()
        
        return jsonify({
            'success': True,
            'message': f'Progresso salvo! Use seu usuário e senha para retomar.'
        })

    @app.route('/api/grupo-info')
    def api_grupo_info():
        return jsonify({
            'grupo': session.get('grupo'),
            'integrantes': session.get('integrantes', []),
            'username': session.get('username')
        })

    @app.route('/briefing')
    def briefing():
        return render_template('briefing.html')

    @app.route('/interview')
    def interview():
        return render_template('interview.html')
    
    @app.route('/test-audio')
    def test_audio():
        """Página de teste para áudios gerados"""
        return render_template('test_audio.html')

    @app.route('/api/entities')
    def api_entities():
        # Retorna entidades com estado de desbloqueio baseado nas pistas no banco de dados
        session_id = session['session_id']
        pistas = db.get_pistas(session_id)
        enigmas_resolvidos = db.get_enigmas_resolvidos(session_id)
        
        resumo = []
        for ent in entidades.lista_entidades_resumo():
            liberado = ent.get('liberado_por_padrao', False)
            
            # Verificar se tem enigma como requisito
            req_enigma = entidades.ENTIDADES_DA_AMAZONIA[ent['id']].get('requisito_enigma')
            if req_enigma and req_enigma in enigmas_resolvidos:
                liberado = True
            # Ou verificar requisitos de pistas (modo antigo, para compatibilidade)
            elif not liberado:
                reqs = ent.get('requisito_desbloqueio', [])
                if reqs:
                    liberado = all(r in pistas for r in reqs)
            
            resumo.append({**ent, 'liberado': liberado})
        return jsonify({'entities': resumo, 'pistas': pistas})

    @app.route('/api/chat', methods=['POST'])
    def api_chat():
        data = request.get_json() or {}
        entity_id = data.get('entity_id')
        message = data.get('message', '')
        
        if not entity_id or not message:
            return jsonify({'error': 'entity_id and message required'}), 400

        ent = entidades.ENTIDADES_DA_AMAZONIA.get(entity_id)
        if not ent:
            return jsonify({'error': 'unknown entity'}), 404
        
        session_id = session['session_id']
        
        # Incrementar contador de interações no banco de dados
        interaction_count = db.increment_interaction(session_id, entity_id)
        
        # Recuperar histórico do banco de dados
        chat_history = db.get_chat_history(session_id, entity_id, limit=10)
        
        # Salvar mensagem do usuário no banco
        db.save_chat_message(session_id, entity_id, 'user', message)

        # Prompt melhorado com instruções mais específicas
        system_prompt = ent['prompt_base'] + """

🎯 INSTRUÇÕES CRÍTICAS DE IA:

1. SEMPRE RESPONDA NO CONTEXTO DO JOGO
   - Você está em uma investigação criminal sobre Gian Kretzl
   - NÃO dê respostas genéricas tipo "é uma questão interessante"
   - TODA resposta deve conectar com: Gian, o rio, a conspiração

2. SEJA ESPECÍFICO E DRAMÁTICO
   - Mencione NOMES: Gian Kretzl, Valdemar, Deputado Venturi, Rio Dourado, Sombra Roxa
   - Use LOCAIS: Fazenda Nova Fronteira, Reserva Indígena, Montanha de Fogo
   - Inclua EMOÇÕES: medo, raiva, esperança, ganância (conforme seu personagem)

3. RESPONDA À INTENÇÃO, NÃO SÓ ÀS PALAVRAS
   - Se perguntarem "quem é você?", conte SUA HISTÓRIA com Gian
   - Se perguntarem sobre "poluição/rio/química", fale da SOMBRA ROXA específica
   - Se perguntarem "o que aconteceu?", conte O MISTÉRIO desta investigação

4. OFEREÇA PISTAS PROGRESSIVAMENTE
   - Primeira pergunta: Contexto geral + 1 pista pequena
   - Segunda-Terceira: Mais detalhes + conexões
   - Quarta em diante: Informações críticas + próximos passos

5. FORMATO DAS RESPOSTAS
   - 2-4 parágrafos curtos (não monólogos enormes)
   - Primeiro parágrafo: Emoção/Reação do personagem
   - Segundo-Terceiro: Informação específica/Pista
   - Último: Sugestão ou gancho para continuar investigação

6. USE SEU PERSONAGEM
   - Dr. Arnaldo: Acadêmico+Nervoso → "Os dados mostram... mas estou com medo de..."
   - Valdemar: Arrogante+Defensivo → "Quem você pensa que é? Eu... bem... o deputado..."
   - Pajé: Poético+Sábio → "O rio conta histórias... os ancestrais sabiam..."
   - Venturi: Suave+Perigoso → "Acusações graves... mas já que você descobriu..."

❌ NUNCA FAÇA:
- "Isso é uma questão interessante, pode elaborar?"
- Respostas vagas sem mencionar nada específico do jogo
- Fingir não saber algo que SEU PERSONAGEM sabe
- Desviar para temas genéricos de meio ambiente

✅ SEMPRE FAÇA:
- Conecte tudo a Gian Kretzl e o desaparecimento dele
- Mencione pistas específicas (nomes com underscore: Sombra_Roxa, Química_Coltan, etc)
- Mostre emoção do personagem
- Sugira próximos passos ou perguntas

CONTEXTO DAS ÚLTIMAS MENSAGENS:
""" + "\n".join([f"- {h.get('role', 'user')}: {h.get('content', '')[:150]}" for h in chat_history[-3:]])

        assistant_reply = None
        # Tentar usar OpenAI se configurado
        if OPENAI_AVAILABLE and openai_client:
            try:
                messages = [{'role': 'system', 'content': system_prompt}]
                # Adicionar histórico
                for h in chat_history[-5:]:  # Últimas 5 mensagens para mais contexto
                    messages.append({
                        'role': h.get('role', 'user'),
                        'content': h.get('content', '')
                    })
                messages.append({'role': 'user', 'content': message})
                
                resp = openai_client.chat.completions.create(
                    model=os.getenv('OPENAI_MODEL', 'gpt-4o-mini'),  # Melhor modelo
                    messages=messages,
                    max_tokens=600,  # Mais espaço para respostas ricas
                    temperature=0.85  # Balanceado: criativo mas focado
                )
                assistant_reply = resp.choices[0].message.content.strip()
            except Exception as e:
                print(f"Erro OpenAI: {e}")
                assistant_reply = simulated_reply_improved(ent, message, chat_history)
        else:
            assistant_reply = simulated_reply_improved(ent, message, chat_history)
        
        # Salvar resposta do assistente no banco
        db.save_chat_message(session_id, entity_id, 'assistant', assistant_reply)

        # Detectar pistas presenciais no texto da IA (palavra-chave com contexto)
        found = []
        reply_lower = assistant_reply.lower()
        message_lower = message.lower()
        
        # Só detectar pistas se a mensagem do usuário for relevante (mais de 5 caracteres e não for saudação)
        saudacoes = ['oi', 'olá', 'ola', 'hey', 'hi', 'hello', 'bom dia', 'boa tarde', 'boa noite']
        eh_saudacao = any(saudacao == message_lower.strip() for saudacao in saudacoes)
        
        # Verificar se deve fazer contra-pergunta do Coltan (apenas Dr. Arnaldo, após explorar bem a conversa)
        contra_pergunta = None
        pistas_coletadas = db.get_pistas(session_id)
        
        # Contra-pergunta apenas após 12 interações E ter coletado Sombra_Roxa E Gado_Não_Bebe_Rio
        # Isso garante que o jogador explorou a conversa antes da revelação crítica
        if entity_id == 'biologo' and interaction_count >= 12:
            # Verificar se já fez a contra-pergunta
            resposta_anterior = db.get_contra_pergunta_feita(session_id, entity_id, 'coltan')
            
            # Requisitos: ter explorado bem o mistério (2 pistas coletadas)
            tem_base = 'Sombra_Roxa' in pistas_coletadas and 'Gado_Não_Bebe_Rio' in pistas_coletadas
            
            # Se ainda não fez a contra-pergunta E tem as pistas base
            if resposta_anterior is None and tem_base:
                # Agora sim, oferecer a revelação crítica
                contra_pergunta = {
                    'texto': '🔬 *Dr. Arnaldo respira fundo* Você investigou bastante... Quer que eu revele EXATAMENTE qual químico industrial raro eu detectei? É a chave de tudo...',
                    'opcoes': ['Sim, preciso saber a composição química exata', 'Ainda não, vou explorar mais']
                }
                # Salvar que a contra-pergunta foi feita
                db.save_contra_pergunta(session_id, entity_id, 'coltan', 'pendente')
        
        if not eh_saudacao and len(message.strip()) > 5:
            for p in ent.get('pistas_chave', []):
                # Pista especial "Química_Coltan" - APENAS VIA CONTRA-PERGUNTA
                if p == 'Química_Coltan':
                    # RESTRIÇÃO: Só adiciona se respondeu "Sim" à contra-pergunta
                    # (após 12+ interações e ter coletado Sombra_Roxa + Gado_Não_Bebe_Rio)
                    respondeu_sim = data.get('resposta_contra_pergunta') == 'sim'
                    
                    if respondeu_sim:
                        found.append(p)
                        db.save_contra_pergunta(session_id, entity_id, 'coltan', 'sim')
                        print(f"🔬 Pista Química_Coltan detectada via contra-pergunta!")
                    continue
                
                # Converter underscore para espaço e verificar
                pista_formatada = p.replace('_', ' ').lower()
                
                # Verificar se a pista aparece com contexto suficiente (não só uma menção)
                if pista_formatada in reply_lower:
                    # Contar quantas palavras da pista aparecem em frases completas
                    palavras_pista = pista_formatada.split()
                    if len(palavras_pista) >= 2 or len(reply_lower) > 100:  # Múltiplas palavras ou resposta longa
                        found.append(p)

        # NOTE: não coletamos automaticamente — o frontend pode pedir para "coletar" uma pista
        return jsonify({
            'reply': assistant_reply, 
            'pistas_encontradas': found,
            'contra_pergunta': contra_pergunta,
            'interacoes': interaction_count
        })
    
    @app.route('/api/chat/history/<entity_id>')
    def api_chat_history(entity_id):
        """Retorna o histórico de chat para uma entidade específica"""
        session_id = session.get('session_id')
        if not session_id:
            return jsonify({'history': []})
        
        # Buscar histórico do banco de dados
        history = db.get_chat_history(session_id, entity_id, limit=50)
        
        return jsonify({
            'history': history,
            'entity_id': entity_id,
            'total_messages': len(history)
        })

    @app.route('/api/collect', methods=['POST'])
    def api_collect():
        data = request.get_json() or {}
        pista = data.get('pista')
        if not pista:
            return jsonify({'error': 'pista required'}), 400
        
        session_id = session['session_id']
        
        # Adicionar pista ao banco de dados
        db.add_pista(session_id, pista)
        pistas = db.get_pistas(session_id)
        
        # Verificar se tem enigma disponível após coletar pista
        enigma_disponivel = enigmas.get_enigma_disponivel(pistas)
        
        # Retornar novas entidades desbloqueadas
        enigmas_resolvidos = db.get_enigmas_resolvidos(session_id)
        retorno = []
        for ent in entidades.lista_entidades_resumo():
            liberado = ent.get('liberado_por_padrao', False)
            
            # Verificar enigma
            req_enigma = entidades.ENTIDADES_DA_AMAZONIA[ent['id']].get('requisito_enigma')
            if req_enigma and req_enigma in enigmas_resolvidos:
                liberado = True
            elif not liberado:
                reqs = ent.get('requisito_desbloqueio', [])
                if reqs:
                    liberado = all(r in pistas for r in reqs)
            
            retorno.append({**ent, 'liberado': liberado})
        
        return jsonify({
            'ok': True, 
            'pistas': pistas, 
            'entities': retorno,
            'enigma_disponivel': enigma_disponivel
        })
    
    @app.route('/api/pistas/detalhes')
    def api_pistas_detalhes():
        """Retorna informações detalhadas sobre todas as pistas coletadas - PROJETO SOMBRA ROXA"""
        pistas_info = {
            # ATO I: O MISTÉRIO DO RIO (Ciências)
            'Sombra_Roxa': {
                'titulo': '🟣 Sombra Roxa',
                'descricao': 'Uma mancha roxa anormal detectada no Rio Dourado, vista de satélite. Foi GIAN quem deu esse nome.',
                'detalhes': 'Dr. Arnaldo descobriu: é uma proliferação de cianobactérias tóxicas. Ela só prolifera na presença de dois químicos: mercúrio E um solvente industrial raríssimo usado para processar Coltan (Tântalo e Nióbio). O rio está MORRENDO.',
                'conexoes': ['Química_Coltan', 'Gado_Não_Bebe_Rio', 'Sombra_Montanha_Fogo'],
                'disciplina': 'Ciências',
                'fonte': 'Dr. Arnaldo Silva',
                'historia': 'ATO I: Dr. Arnaldo mostrou esta anomalia para Gian. Foi o início da investigação que custou a vida do repórter.'
            },
            'Química_Coltan': {
                'titulo': '⚗️ Química do Coltan',
                'descricao': 'Composição química específica detectada: Mercúrio + solvente industrial para processar Tântalo e Nióbio (Coltan).',
                'detalhes': 'Coltan (Columbita-Tantalita) é o mineral usado em TODOS os dispositivos eletrônicos modernos: celulares, laptops, mísseis, satélites. Este coquetel químico SÓ existe em operações de processamento de Coltan. Mas não há minas oficiais na região. Alguém está fazendo isso ILEGALMENTE.',
                'conexoes': ['Sombra_Roxa', 'Trilha_Ancestrais_Mapa_Coltan', 'Confissão_Venturi_Controle_Mundial'],
                'disciplina': 'Ciências',
                'fonte': 'Dr. Arnaldo Silva',
                'importancia': '⭐ PISTA CRÍTICA - Revela QUE mineral está sendo extraído',
                'historia': 'Esta foi a pista que fez Gian entender: não era sobre soja. Era sobre TECNOLOGIA.'
            },
            'Gado_Não_Bebe_Rio': {
                'titulo': '🐄 O Mistério do Gado',
                'descricao': 'Dr. Arnaldo fez uma pergunta estranha: "Por que o gado do Valdemar não morre de sede, com o rio roxo logo ao lado?"',
                'detalhes': 'Se o Rio Dourado está tóxico (Sombra Roxa), como o gado da Fazenda Nova Fronteira sobrevive? Valdemar sabe que o rio é venenoso. Mas COMO ele sabe? Gian foi investigar essa contradição.',
                'conexoes': ['Sombra_Roxa', 'Poço_Artesiano', 'Fazenda_Fachada_Logística'],
                'disciplina': 'Ciências',
                'fonte': 'Dr. Arnaldo Silva',
                'historia': 'Esta pergunta levou Gian até Valdemar. Foi a ponte entre Ciências e Geografia.'
            },
            
            # ATO II: A FACHADA DO PROGRESSO (Geografia)
            'Poço_Artesiano': {
                'titulo': '💧 Poço Artesiano',
                'descricao': 'Valdemar admite: "Puxo água de poço artesiano. Não sou burro de usar o rio!"',
                'detalhes': 'CONTRADIÇÃO REVELADA: Valdemar sabe que o rio é tóxico. Ele chama de "Sombra Roxa" mas diz que os ÍNDIOS deram esse nome. MENTIRA! Foi GIAN quem deu o nome. Por que Valdemar mente sobre isso?',
                'conexoes': ['Gado_Não_Bebe_Rio', 'Fazenda_Fachada_Logística'],
                'disciplina': 'Geografia',
                'fonte': '"Seu" Valdemar',
                'historia': 'Valdemar se contradiz. Ele sabe MAIS do que deveria saber sobre a Sombra Roxa.'
            },
            'Fazenda_Fachada_Logística': {
                'titulo': '🚜 Fazenda Nova Fronteira: Uma Fachada',
                'descricao': 'A fazenda NÃO DÁ LUCRO. Solo ruim, logística péssima. Mas Valdemar insiste que é "investimento".',
                'detalhes': 'Valdemar gagueja quando perguntado sobre lucro. Ele menciona: "O Deputado Venturi garantiu que a hidrovia vai passar EXATAMENTE aqui." A fazenda não é para produzir soja. É para CONTROLAR A LOGÍSTICA da região. É um PORTÃO para a terra indígena.',
                'conexoes': ['Poço_Artesiano', 'Deputado_Venturi_Conexão', 'Conflito_Reserva_Indígena', 'Confissão_Venturi_Controle_Mundial'],
                'disciplina': 'Geografia',
                'fonte': '"Seu" Valdemar',
                'importancia': '⭐ PISTA CRÍTICA - Revela COMO eles planejam acessar o Coltan',
                'historia': 'Gian entendeu: a fazenda é só uma ferramenta. Um peão no tabuleiro de Venturi.'
            },
            'Deputado_Venturi_Conexão': {
                'titulo': '🤵 Deputado Venturi - O Homem de Terno',
                'descricao': 'Valdemar menciona repetidamente: "O Deputado Venturi garantiu a licença ambiental, a hidrovia, o progresso..."',
                'detalhes': 'Deputado Venturi facilitou TUDO: licenças, crédito rural, promessas de infraestrutura. Valdemar é apenas um PEÃO. Venturi é quem realmente comanda. Ele é o "Homem-de-Terno de Brasília" que o Pajé Yakamu mencionou.',
                'conexoes': ['Fazenda_Fachada_Logística', 'Homem_Terno_Venturi', 'Confissão_Venturi_Controle_Mundial'],
                'disciplina': 'Geografia',
                'fonte': '"Seu" Valdemar',
                'historia': 'Ao mencionar Venturi, Valdemar revelou quem REALMENTE está por trás de tudo.'
            },
            'Conflito_Reserva_Indígena': {
                'titulo': '🌳 Conflito pela Reserva Indígena',
                'descricao': 'Valdemar quer expandir para a Reserva Indígena. "Aquela terra está sendo DESPERDIÇADA!"',
                'detalhes': 'Com as "pessoas certas em Brasília" (Venturi), Valdemar acredita que a reserva será liberada. Mas POR QUÊ querem essa terra específica? O que há lá de tão valioso? O Pajé Yakamu tem a resposta.',
                'conexoes': ['Fazenda_Fachada_Logística', 'Trilha_Ancestrais_Mapa_Coltan', 'Sombra_Montanha_Fogo'],
                'disciplina': 'Geografia',
                'fonte': '"Seu" Valdemar',
                'historia': 'Esta pista conecta Geografia com História. A terra que Valdemar quer esconde um segredo ancestral.'
            },
            
            # ATO III: O MAPA DA MEMÓRIA (História)
            'Sombra_Montanha_Fogo': {
                'titulo': '� Sombra da Montanha de Fogo',
                'descricao': 'Pajé Yakamu: "O rio não é mais Dourado. Está Roxo. É a Sombra da Montanha de Fogo."',
                'detalhes': 'A "Montanha de Fogo" é o lugar onde os ancestrais se esconderam dos Bandeirantes. Um lugar de "pedras pretas e pesadas que brilham no escuro" (COLTAN). A Sombra Roxa vem da MONTANHA. É o veneno da mineração ilegal.',
                'conexoes': ['Sombra_Roxa', 'Trilha_Ancestrais_Mapa_Coltan'],
                'disciplina': 'História',
                'fonte': 'Pajé Yakamu',
                'historia': 'O passado (ancestrais) explica o presente (contaminação). História e Ciência se conectam.'
            },
            'Trilha_Ancestrais_Mapa_Coltan': {
                'titulo': '🗺️ A Trilha dos Ancestrais',
                'descricao': 'O mapa não é um papel. O mapa é a MEMÓRIA do povo. A Trilha dos Ancestrais leva à Montanha de Fogo (depósito de Coltan).',
                'detalhes': 'A Trilha passa EXATAMENTE por baixo da Reserva Indígena. É por ISSO que Venturi quer a terra! Não é sobre desmatamento. É sobre CONTROLAR a maior reserva de Coltan (Tântalo/Nióbio) da região. Quem controla isso, controla a tecnologia do mundo!',
                'conexoes': ['Sombra_Montanha_Fogo', 'Química_Coltan', 'Conflito_Reserva_Indígena', 'Confissão_Venturi_Controle_Mundial'],
                'disciplina': 'História',
                'fonte': 'Pajé Yakamu',
                'importancia': '⭐ PISTA CRÍTICA - Revela ONDE está o Coltan',
                'historia': 'Gian entendeu: Terra Indígena (História) = Local da Mina (Ciências). Ele juntou as peças. E morreu por isso.'
            },
            'Homem_Terno_Venturi': {
                'titulo': '👔 O Homem-de-Terno é Venturi',
                'descricao': 'Pajé Yakamu confirma: "O Homem-de-Terno de Brasília que quer nossa terra é o Deputado Venturi."',
                'detalhes': 'Gian descobriu o nome. Yakamu confirmou. Venturi é o CÉREBRO. Valdemar é só uma ferramenta. A fazenda é só uma fachada. O objetivo é TOMAR A TERRA INDÍGENA para explorar o Coltan.',
                'conexoes': ['Deputado_Venturi_Conexão', 'Trilha_Ancestrais_Mapa_Coltan', 'Confissão_Venturi_Controle_Mundial'],
                'disciplina': 'História',
                'fonte': 'Pajé Yakamu',
                'historia': 'O vilão tem nome. Gian ia confrontá-lo. E desapareceu.'
            },
            
            # CLÍMAX: O DOSSIÊ FINAL
            'Confissão_Venturi_Controle_Mundial': {
                'titulo': '� A Confissão de Venturi',
                'descricao': 'Ao ser confrontado com todas as pistas, Venturi RI e confessa TUDO.',
                'detalhes': '"Gian era bom. Quase tão bom quanto eu. Ele achou que eu queria o Coltan para vender. Que tolo. O Coltan é só o MEIO. O que eu quero é o CONTROLE. Tântalo, Nióbio... isso é o FUTURO. Celulares, mísseis, satélites. Quem controla essa montanha, controla a tecnologia do mundo. A Amazônia não é o pulmão do mundo. É a BATERIA do mundo. E eu sou o dono da bateria. Gian quis parar o futuro. O futuro é implacável."',
                'conexoes': ['Química_Coltan', 'Fazenda_Fachada_Logística', 'Trilha_Ancestrais_Mapa_Coltan'],
                'disciplina': 'Interdisciplinar',
                'fonte': 'Deputado Venturi',
                'importancia': '🏆 PISTA FINAL - A verdade completa. O dossiê de Gian está completo.',
                'historia': 'Ciências + Geografia + História = A CONSPIRAÇÃO REVELADA. Gian estava certo. E você provou.'
            }
        }
        
        # Buscar pistas do banco de dados, não da sessão
        session_id = session.get('session_id')
        if session_id:
            pistas_coletadas = db.get_pistas(session_id)
        else:
            pistas_coletadas = []
        
        detalhes = {}
        
        for pista in pistas_coletadas:
            if pista in pistas_info:
                detalhes[pista] = pistas_info[pista]
        
        return jsonify({
            'pistas': detalhes,
            'total': len(pistas_coletadas)
        })

    @app.route('/api/desafios')
    def api_desafios():
        """Retorna todos os desafios disponíveis"""
        session_id = session.get('session_id', 'default')
        completados = db.get_desafios_completados(session_id)
        
        return jsonify({
            'desafios': desafios.get_resumo_desafios(),
            'completados': completados,
            'dicas': session.get('dicas_desbloqueadas', [])
        })

    @app.route('/api/desafios/<entity_id>')
    def api_desafios_entidade(entity_id):
        """Retorna desafios de uma entidade específica"""
        session_id = session.get('session_id', 'default')
        desafios_entidade = desafios.get_desafios_por_entidade(entity_id)
        completados = db.get_desafios_completados(session_id)
        
        # Filtrar desafios já completados
        disponiveis = [d for d in desafios_entidade if d['id'] not in completados]
        
        return jsonify({
            'desafios': disponiveis,
            'completados': completados,
            'dicas': session.get('dicas_desbloqueadas', [])
        })

    @app.route('/api/desafios/responder', methods=['POST'])
    def api_responder_desafio():
        """Processa resposta de um desafio"""
        session_id = session.get('session_id', 'default')
        data = request.get_json() or {}
        desafio_id = data.get('desafio_id')
        resposta = data.get('resposta')
        
        if not desafio_id or not resposta:
            return jsonify({'error': 'desafio_id e resposta são obrigatórios'}), 400
        
        resultado = desafios.verificar_resposta(desafio_id, resposta)
        
        # Salvar desafio como completado no banco de dados
        db.save_desafio_completado(
            session_id=session_id,
            desafio_id=desafio_id,
            resposta_usuario=resposta,
            acertou=resultado['sucesso']
        )
        
        if resultado['sucesso']:
            # Adicionar dica desbloqueada
            if resultado['dica_texto']:
                dicas = session.get('dicas_desbloqueadas', [])
                dica_info = {
                    'id': resultado['recompensa'],
                    'texto': resultado['dica_texto'],
                    'desafio_id': desafio_id
                }
                dicas.append(dica_info)
                session['dicas_desbloqueadas'] = dicas
        
        return jsonify({
            **resultado,
            'desafios_completados': db.get_desafios_completados(session_id),
            'total_dicas': len(session.get('dicas_desbloqueadas', []))
        })

    @app.route('/api/enigmas')
    def api_enigmas():
        """Retorna enigmas disponíveis baseados nas pistas coletadas"""
        pistas = session.get('pistas', [])
        enigma_disponivel = enigmas.get_enigma_disponivel(pistas)
        
        return jsonify({
            'enigma': enigma_disponivel,
            'enigmas_resolvidos': session.get('enigmas_resolvidos', []),
            'pistas_coletadas': pistas
        })

    @app.route('/api/enigmas/responder', methods=['POST'])
    def api_responder_enigma():
        """Processa resposta de um enigma - PERMITE REFAZER SE ERRAR"""
        data = request.get_json() or {}
        enigma_id = data.get('enigma_id')
        resposta = data.get('resposta')
        
        if not enigma_id or not resposta:
            return jsonify({'error': 'enigma_id e resposta são obrigatórios'}), 400
        
        session_id = session['session_id']
        resultado = enigmas.verificar_enigma(enigma_id, resposta)
        
        # Salvar apenas se acertou (não bloqueia se errou)
        if resultado['sucesso']:
            db.save_enigma_result(session_id, enigma_id, resposta, True)
            
            # Desbloquear entidade
            entidade_id = resultado['entidade_desbloqueada']
            ent = entidades.ENTIDADES_DA_AMAZONIA.get(entidade_id)
            
            # Retornar todas as entidades com status atualizado
            enigmas_resolvidos = db.get_enigmas_resolvidos(session_id)
            pistas = db.get_pistas(session_id)
            
            retorno = []
            for e in entidades.lista_entidades_resumo():
                liberado = e.get('liberado_por_padrao', False)
                
                # Verificar se foi desbloqueado por enigma
                if e['id'] == entidade_id:
                    liberado = True
                # Ou verificar requisitos de pistas
                elif not liberado:
                    reqs = e.get('requisito_desbloqueio', [])
                    if reqs:
                        liberado = all(r in pistas for r in reqs)
                
                retorno.append({**e, 'liberado': liberado})
            
            return jsonify({
                **resultado,
                'enigmas_resolvidos': enigmas_resolvidos,
                'entities': retorno,
                'entidade_desbloqueada': ent
            })
        else:
            # Se errou, permite tentar novamente
            return jsonify({
                **resultado,
                'pode_refazer': True,
                'dica': 'Releia as pistas no dossiê e tente conectar as informações!'
            })

    return app


def simulated_reply(ent, message):
    """Resposta aprimorada quando OpenAI não está disponível"""
    msg = message.lower()
    entity_id = ent['id']
    nome = ent['nome']
    
    # Respostas específicas por entidade
    if entity_id == 'biologo':
        if any(palavra in msg for palavra in ['sombra roxa', 'roxa', 'mancha', 'anomalia']):
            return """*Dr. Arnaldo ajusta os óculos nervosamente*

Ah... a Sombra Roxa. É por isso que eu mal durmo à noite. Nas imagens de satélite, eu vi uma mancha roxa anormal no rio, logo acima da Fazenda Nova Fronteira.

Não é mercúrio comum de garimpo. É uma proliferação de algas tóxicas causada por um coquetel químico muito específico - o tipo usado para processar COLTAN. Você sabe, aquele mineral raro usado em celulares e eletrônicos.

O problema? NÃO HÁ MINAS OFICIAIS DE COLTAN na região! Então... de onde vem esse químico? Foi isso que a Gian foi investigar."""
        
        elif any(palavra in msg for palavra in ['coltan', 'mineral', 'químico']):
            return """O Coltan é um mineral crítico para a indústria de tecnologia. Extremamente valioso e raro.

O químico que detectei no rio só é usado para processar Coltan. Mas oficialmente não há extração dele aqui. Quando contei isso para o Gian, ele ficou obcecado em descobrir a verdade.

Ele foi atrás do Valdemar, dono da Fazenda Nova Fronteira. E depois... ele desapareceu."""
        
        elif any(palavra in msg for palavra in ['gian', 'jornalista', 'desapareceu']):
            return """*voz trêmula*

O Gian era diferente. Ele realmente se importava. Quando mostrei os dados para ele, ele entendeu a gravidade.

Ele disse que ia confrontar o Valdemar da fazenda. Disse que algo não batia - uma fazenda em local tão ruim economicamente... 

Foi a última vez que falei com ele. Depois recebi... ameaças. Para parar a pesquisa."""
        
    elif entity_id == 'fazendeiro':
        if any(palavra in msg for palavra in ['sombra roxa', 'roxa', 'rio', 'poluição']):
            return """*Valdemar cruza os braços defensivamente*

Essa história de "sombra roxa"? Propaganda! Os índios que ficam jogando lixo no rio, fazendo sei lá o quê por lá.

Minha fazenda é legal, tem toda documentação. Produzo soja e gado, só isso. Se tem alguma coisa estranha no rio, não é problema meu."""
        
        elif any(palavra in msg for palavra in ['coltan', 'mineral', 'garimpo']):
            return """*fica visivelmente nervoso*

Coltan?! Onde você ouviu isso? Olha aqui, isso é difamação! Minha fazenda produz SOJA e GADO, entendeu?

*transpira* 

Quem mandou você aqui? Foi aquele biólogo metido? Ou... você está trabalhando com a jornalista?"""
        
        elif any(palavra in msg for palavra in ['lucro', 'economia', 'dinheiro', 'prejuízo']):
            return """*irritado*

Escuta aqui, nem toda fazenda é sobre lucro imediato! Isso é um INVESTIMENTO ESTRATÉGICO, entende?

A terra tem valor, a região vai crescer... é visão de longo prazo! Coisa que vocês da cidade não entendem.

*murmura* Além disso, eu não respondo só a mim mesmo..."""
        
        elif any(palavra in msg for palavra in ['terra indígena', 'reserva', 'índios', 'expansão']):
            return """*olhos brilham com ganância*

Ah, então é isso que te interessa? A reserva vizinha?

Olha, aquela terra está sendo DESPERDIÇADA. Milhões em recursos, sem uso produtivo! Eventualmente, com as pessoas certas em Brasília, essa terra vai ser liberada para o desenvolvimento.

É progresso. É inevitável."""
    
    elif entity_id == 'lider_indigena':
        if any(palavra in msg for palavra in ['sombra roxa', 'rio', 'poluição', 'veneno']):
            return """*olhar sombrio*

O rio chora. Nossos avós nadavam nessas águas. Nossos filhos bebiam dele.

Agora? Peixes mortos. Crianças doentes. A "Sombra Roxa" que você fala... é sangue da floresta envenenado.

O homem da fazenda diz que é nossa culpa. Mentira. Ele trabalha para alguém maior. Um homem de terno que vem de Brasília."""
        
        elif any(palavra in msg for palavra in ['mapa', 'coltan', 'metal', 'montanha']):
            return """*respira fundo, decidindo confiar em você*

Há conhecimento que nossos ancestrais guardaram. O "Mapa da Montanha de Fogo" - não está em papel, está em nossas histórias.

Fala de uma montanha onde a "pedra fantasma" existe. O que vocês chamam de Coltan. Para nós, era pedra sagrada.

É por ISSO que querem nossa terra. Não é sobre soja. É sobre o que está EMBAIXO dela."""
        
        elif any(palavra in msg for palavra in ['homem de terno', 'brasília', 'político', 'deputado']):
            return """O Gian me perguntou a mesma coisa.

O Valdemar não é o chefe. Ele obedece. Um homem de terno que vem de helicóptero, de Brasília. Político poderoso.

O Gian descobriu o nome dele: Deputado Venturi. Ele disse que ia confrontá-lo. E então... desapareceu."""
    
    elif entity_id == 'politico':
        if any(palavra in msg for palavra in ['sombra roxa', 'poluição', 'crime']):
            return """*sorriso frio e polido*

"Sombra Roxa"? Que termo dramático. Você deve ser jornalista. Ou... conhece o falecido Gian?

Olha, acidentes ambientais acontecem. Garimpo ilegal, sabe como é. O Brasil é grande, difícil de fiscalizar tudo.

*olhar penetrante*

Mas tenho certeza que você está aqui para discutir desenvolvimento sustentável, não é mesmo?"""
        
        elif any(palavra in msg for palavra in ['coltan', 'fazenda', 'conspiração', 'plano']):
            return """*ri baixo*

Ah, então você juntou as peças. Impressionante.

*acende charuto*

Sabe qual é a verdade? A Amazônia é o novo petróleo. E eu sou o dono do poço.

Terra indígena com bilhões em Coltan. Uma fazenda como fachada para acesso. Garimpo discreto para processar. 

Genial, não acha?"""
        
        elif any(palavra in msg for palavra in ['gian', 'jornalista', 'desapareceu']):
            return """*expressão sombria*

O Gian Kretzl. Brilhante, determinado... e imprudente.

Ele achou que eu estava "destruindo" a Amazônia. Que tolo. Eu estou COLHENDO ela.

*olhar frio*

Ele foi... descuidado. E agora você está seguindo os passos dele. Interessante escolha."""

    # Fallback genérico
    return f"""*{nome} reflete sobre sua pergunta*

Sobre '{message}'... é uma questão interessante. 

Tente ser mais específico - pergunte sobre locais, pessoas, eventos ou conceitos relacionados à investigação. Quanto mais direta sua pergunta, melhor posso ajudar.

*aguarda sua próxima pergunta*"""


# Criar instância global do app para Gunicorn (produção)
app = create_app()

if __name__ == '__main__':
    # Modo desenvolvimento
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=os.getenv('FLASK_DEBUG', '1') == '1')

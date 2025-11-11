import os
from flask import Flask, render_template, jsonify, request, session
from dotenv import load_dotenv
from datetime import datetime
import entidades
import desafios
import enigmas
from simulated_ai import simulated_reply_improved

load_dotenv()

try:
    import openai
    OPENAI_AVAILABLE = True
    openai.api_key = os.getenv('OPENAI_API_KEY')
except Exception:
    openai = None
    OPENAI_AVAILABLE = False

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-change-me')

    @app.before_request
    def ensure_session():
        if 'pistas' not in session:
            session['pistas'] = []
        if 'grupo' not in session:
            session['grupo'] = None
        if 'integrantes' not in session:
            session['integrantes'] = []
        if 'enigmas_resolvidos' not in session:
            session['enigmas_resolvidos'] = []
        if 'desafios_completados' not in session:
            session['desafios_completados'] = []
        if 'dicas_desbloqueadas' not in session:
            session['dicas_desbloqueadas'] = []
        if 'desafios_completados' not in session:
            session['desafios_completados'] = []
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
        data = request.get_json() or {}
        grupo = data.get('grupo', '').strip()
        integrantes = data.get('integrantes', [])
        
        if not grupo or len(integrantes) == 0 or len(integrantes) > 6:
            return jsonify({'success': False, 'error': 'Dados inválidos'}), 400
        
        session['grupo'] = grupo
        session['integrantes'] = integrantes
        session['login_timestamp'] = str(datetime.now())
        
        return jsonify({'success': True, 'grupo': grupo, 'integrantes': integrantes})

    @app.route('/api/grupo-info')
    def api_grupo_info():
        return jsonify({
            'grupo': session.get('grupo'),
            'integrantes': session.get('integrantes', [])
        })

    @app.route('/briefing')
    def briefing():
        return render_template('briefing.html')

    @app.route('/interview')
    def interview():
        return render_template('interview.html')

    @app.route('/api/entities')
    def api_entities():
        # Retorna entidades com estado de desbloqueio baseado nas pistas na sessão
        pistas = session.get('pistas', [])
        enigmas_resolvidos = session.get('enigmas_resolvidos', [])
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
        chat_history = data.get('history', [])  # Histórico de conversa
        
        if not entity_id or not message:
            return jsonify({'error': 'entity_id and message required'}), 400

        ent = entidades.ENTIDADES_DA_AMAZONIA.get(entity_id)
        if not ent:
            return jsonify({'error': 'unknown entity'}), 404

        # Prompt melhorado com instruções mais específicas
        system_prompt = ent['prompt_base'] + """

INSTRUÇÕES CRÍTICAS:
1. Você DEVE responder de forma direta e natural, como em uma conversa real
2. Interprete a pergunta com FLEXIBILIDADE - entenda a INTENÇÃO, não só as palavras exatas
3. Se a pergunta mencionar qualquer conceito relacionado ao seu conhecimento, responda sobre ele
4. Seja PROATIVO - ofereça informações relevantes mesmo que não perguntadas diretamente
5. Use emoções do personagem (medo, nervosismo, arrogância) para dar vida à conversa
6. Sempre mencione nomes específicos, lugares e conceitos-chave
7. Respostas curtas (2-4 parágrafos) e dinâmicas
8. Se for pergunta vaga, dê a informação mais importante que você tem

CONTEXTO DA CONVERSA ANTERIOR:
""" + "\n".join([f"- {h.get('role', 'user')}: {h.get('content', '')[:100]}" for h in chat_history[-3:]])

        assistant_reply = None
        # Tentar usar OpenAI se configurado
        if OPENAI_AVAILABLE and openai and openai.api_key:
            try:
                messages = [{'role': 'system', 'content': system_prompt}]
                # Adicionar histórico
                for h in chat_history[-4:]:  # Últimas 4 mensagens
                    messages.append({
                        'role': h.get('role', 'user'),
                        'content': h.get('content', '')
                    })
                messages.append({'role': 'user', 'content': message})
                
                resp = openai.ChatCompletion.create(
                    model=os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo'),
                    messages=messages,
                    max_tokens=500,
                    temperature=0.9  # Aumentado para respostas mais criativas
                )
                assistant_reply = resp.choices[0].message['content'].strip()
            except Exception as e:
                print(f"Erro OpenAI: {e}")
                assistant_reply = simulated_reply_improved(ent, message, chat_history)
        else:
            assistant_reply = simulated_reply_improved(ent, message, chat_history)

        # Detectar pistas presenciais no texto da IA (palavra-chave simples)
        found = []
        reply_lower = assistant_reply.lower()
        for p in ent.get('pistas_chave', []):
            # Converter underscore para espaço e verificar
            pista_formatada = p.replace('_', ' ').lower()
            if pista_formatada in reply_lower:
                found.append(p)

        # NOTE: não coletamos automaticamente — o frontend pode pedir para "coletar" uma pista
        return jsonify({'reply': assistant_reply, 'pistas_encontradas': found})

    @app.route('/api/collect', methods=['POST'])
    def api_collect():
        data = request.get_json() or {}
        pista = data.get('pista')
        if not pista:
            return jsonify({'error': 'pista required'}), 400
        pistas = session.get('pistas', [])
        if pista not in pistas:
            pistas.append(pista)
            session['pistas'] = pistas
        
        # Verificar se tem enigma disponível após coletar pista
        enigma_disponivel = enigmas.get_enigma_disponivel(pistas)
        
        # Retornar novas entidades desbloqueadas
        enigmas_resolvidos = session.get('enigmas_resolvidos', [])
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

    @app.route('/api/desafios')

    @app.route('/api/desafios')
    def api_desafios():
        """Retorna todos os desafios disponíveis"""
        return jsonify({
            'desafios': desafios.get_resumo_desafios(),
            'completados': session.get('desafios_completados', []),
            'dicas': session.get('dicas_desbloqueadas', [])
        })

    @app.route('/api/desafios/<entity_id>')
    def api_desafios_entidade(entity_id):
        """Retorna desafios de uma entidade específica"""
        desafios_entidade = desafios.get_desafios_por_entidade(entity_id)
        completados = session.get('desafios_completados', [])
        
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
        data = request.get_json() or {}
        desafio_id = data.get('desafio_id')
        resposta = data.get('resposta')
        
        if not desafio_id or not resposta:
            return jsonify({'error': 'desafio_id e resposta são obrigatórios'}), 400
        
        resultado = desafios.verificar_resposta(desafio_id, resposta)
        
        if resultado['sucesso']:
            # Marcar desafio como completado
            completados = session.get('desafios_completados', [])
            if desafio_id not in completados:
                completados.append(desafio_id)
                session['desafios_completados'] = completados
            
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
            'desafios_completados': session.get('desafios_completados', []),
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
        """Processa resposta de um enigma"""
        data = request.get_json() or {}
        enigma_id = data.get('enigma_id')
        resposta = data.get('resposta')
        
        if not enigma_id or not resposta:
            return jsonify({'error': 'enigma_id e resposta são obrigatórios'}), 400
        
        resultado = enigmas.verificar_enigma(enigma_id, resposta)
        
        if resultado['sucesso']:
            # Marcar enigma como resolvido
            resolvidos = session.get('enigmas_resolvidos', [])
            if enigma_id not in resolvidos:
                resolvidos.append(enigma_id)
                session['enigmas_resolvidos'] = resolvidos
            
            # Desbloquear entidade
            entidade_id = resultado['entidade_desbloqueada']
            ent = entidades.ENTIDADES_DA_AMAZONIA.get(entidade_id)
            
            # Retornar todas as entidades com status atualizado
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
                        liberado = all(r in session['pistas'] for r in reqs)
                
                retorno.append({**e, 'liberado': liberado})
            
            return jsonify({
                **resultado,
                'enigmas_resolvidos': session.get('enigmas_resolvidos', []),
                'entities': retorno,
                'entidade_desbloqueada': ent
            })
        else:
            return jsonify(resultado)

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


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=os.getenv('FLASK_DEBUG', '1') == '1')

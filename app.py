import os
from flask import Flask, render_template, jsonify, request, session
from dotenv import load_dotenv
import entidades

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

    @app.route('/')
    def index():
        return render_template('index.html')

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
        resumo = []
        for ent in entidades.lista_entidades_resumo():
            liberado = ent.get('liberado_por_padrao', False)
            reqs = ent.get('requisito_desbloqueio', [])
            if not liberado and reqs:
                # liberado se todas as reqs estiverem em pistas
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

        prompt = ent['prompt_base'] + "\n\nUsuário pergunta: " + message

        assistant_reply = None
        # Tentar usar OpenAI se configurado
        if OPENAI_AVAILABLE and openai and openai.api_key:
            try:
                resp = openai.ChatCompletion.create(
                    model=os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo'),
                    messages=[
                        {'role': 'system', 'content': ent['prompt_base']},
                        {'role': 'user', 'content': message}
                    ],
                    max_tokens=400
                )
                assistant_reply = resp.choices[0].message['content'].strip()
            except Exception as e:
                assistant_reply = f"(Erro ao acessar OpenAI: {e}) Resposta simulada: " + simulated_reply(ent, message)
        else:
            assistant_reply = simulated_reply(ent, message)

        # Detectar pistas presenciais no texto da IA (palavra-chave simples)
        found = []
        reply_lower = assistant_reply.lower()
        for p in ent.get('pistas_chave', []):
            if p.replace('_', ' ') in reply_lower or p in reply_lower:
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
        # retornar novas entidades desbloqueadas
        retorno = []
        for ent in entidades.lista_entidades_resumo():
            liberado = ent.get('liberado_por_padrao', False)
            reqs = ent.get('requisito_desbloqueio', [])
            if not liberado and reqs:
                liberado = all(r in session['pistas'] for r in reqs)
            retorno.append({**ent, 'liberado': liberado})
        return jsonify({'ok': True, 'pistas': session['pistas'], 'entities': retorno})

    return app


def simulated_reply(ent, message):
    # Resposta simples quando OpenAI não está disponível — mantém protótipo funcional
    base = ent['prompt_base']
    # respostas curtas baseadas em palavras da mensagem
    msg = message.lower()
    if 'mercúrio' in msg or 'mercurio' in msg:
        return "O mercúrio do garimpo pode se bioacumular nos peixes e afetar comunidades ribeirinhas."
    if 'rios' in msg or 'chuva' in msg or 'voadores' in msg:
        return "O desmatamento altera o ciclo da água: os chamados 'rios voadores' diminuem e isso reduz chuvas ao sul."
    if 'fazenda' in msg or 'soja' in msg or 'gado' in msg:
        return "A terra é vista como ativo econômico; o produtor alega gerar emprego e progresso."
    # fallback
    return f"{ent['nome']} diz: (resposta de protótipo) Sobre '{message}', investigue mais com perguntas específicas."


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=os.getenv('FLASK_DEBUG', '1') == '1')

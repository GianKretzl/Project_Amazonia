"""
Sistema de Enigmas para Desbloquear Personagens - Projeto Sombra Roxa
Cada personagem requer resolver um enigma relacionado às pistas do personagem anterior
"""

ENIGMAS = {
    # Enigma para desbloquear Valdemar (após coletar pistas do Dr. Arnaldo)
    'desbloquear_fazendeiro': {
        'id': 'desbloquear_fazendeiro',
        'titulo': 'Enigma: O Rastro Químico',
        'contexto': 'Você coletou informações do Dr. Arnaldo sobre a anomalia no rio. Para entender o que aconteceu com o Gian, você precisa conectar as pistas...',
        'pergunta': 'Se a anomalia química coltan foi encontrada no rio ACIMA da Fazenda Nova Fronteira, e o Gian foi investigar o dono da fazenda, qual era a suspeita dele?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) O fazendeiro estava usando agrotóxicos proibidos',
            'B) A fazenda estava produzindo soja contaminada',
            'C) A fazenda era uma fachada para operação de mineração ilegal',
            'D) O fazendeiro estava desmatando áreas protegidas'
        ],
        'resposta_correta': 'C',
        'explicacao': 'Correto! Se há químicos de processamento de Coltan acima da fazenda, e o Gian investigou o fazendeiro, ele suspeitava que a fazenda era uma fachada para esconder a mineração ilegal desse mineral valioso.',
        'recompensa_entidade': 'fazendeiro',
        'requer_pistas': ['Química_Coltan', 'Sombra_Roxa']
    },
    
    # Enigma para desbloquear Pajé Yakamu (após coletar pistas do Valdemar)
    'desbloquear_lider_indigena': {
        'id': 'desbloquear_lider_indigena',
        'titulo': 'Enigma: A Motivação Oculta',
        'contexto': 'Valdemar revelou que sua fazenda é uma fachada e tem interesse na reserva indígena. Por que alguém manteria uma fazenda não lucrativa?',
        'pergunta': 'Por que alguém manteria uma fazenda que dá prejuízo em uma região de difícil acesso, ao lado de uma reserva indígena?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Por amor à natureza e ao meio ambiente',
            'B) Para ter acesso legal à região e facilitar invasão da terra indígena',
            'C) Para criar empregos para a comunidade local',
            'D) Para experimentar novos métodos de agricultura sustentável'
        ],
        'resposta_correta': 'B',
        'explicacao': 'Exatamente! A fazenda serve como ponto de apoio legal na região. Ter uma propriedade registrada próxima facilita o acesso, cria presença institucional e permite operações secretas na terra indígena vizinha.',
        'recompensa_entidade': 'lider_indigena',
        'requer_pistas': ['Fazenda_Fachada', 'Interesse_na_Reserva']
    },
    
    # Enigma para desbloquear Deputado Venturi (após coletar pistas do Pajé)
    'desbloquear_politico': {
        'id': 'desbloquear_politico',
        'titulo': 'Enigma: A Conspiração Completa',
        'contexto': 'O Pajé revelou que existe um mapa ancestral indicando depósitos de Coltan na terra indígena, e mencionou um homem de terno de Brasília. Quem seria capaz de orquestrar tudo isso?',
        'pergunta': 'Quem teria poder suficiente para: conseguir documentação para uma fazenda fachada, autorizar operações ilegais, e ter interesse em explorar recursos de terra indígena?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Um grande empresário de mineração',
            'B) Um fazendeiro rico da região',
            'C) Um político corrupto com influência em Brasília',
            'D) Um grupo de garimpeiros organizados'
        ],
        'resposta_correta': 'C',
        'explicacao': 'Perfeito! Apenas um político com poder em Brasília teria capacidade de: aprovar documentação fraudulenta, bloquear fiscalizações, influenciar demarcações de terra e coordenar uma operação tão complexa. O Deputado Venturi está por trás de tudo!',
        'recompensa_entidade': 'politico',
        'requer_pistas': ['Mapa_Coltan', 'Deputado_Venturi']
    }
}

def verificar_enigma(enigma_id, resposta_usuario):
    """Verifica se a resposta do enigma está correta"""
    enigma = ENIGMAS.get(enigma_id)
    if not enigma:
        return {'sucesso': False, 'erro': 'Enigma não encontrado'}
    
    resposta_correta = enigma['resposta_correta']
    sucesso = resposta_usuario.upper() == resposta_correta
    
    return {
        'sucesso': sucesso,
        'explicacao': enigma['explicacao'] if sucesso else 'Resposta incorreta. Releia as pistas coletadas e tente novamente.',
        'entidade_desbloqueada': enigma['recompensa_entidade'] if sucesso else None
    }

def get_enigma_disponivel(pistas_coletadas):
    """Retorna o próximo enigma disponível baseado nas pistas coletadas"""
    for enigma_id, enigma in ENIGMAS.items():
        # Verificar se o jogador tem todas as pistas necessárias
        requisitos = enigma.get('requer_pistas', [])
        if all(pista in pistas_coletadas for pista in requisitos):
            return enigma
    return None

def get_resumo_enigmas():
    """Retorna resumo de todos os enigmas (sem respostas)"""
    return [{
        'id': e['id'],
        'titulo': e['titulo'],
        'requer_pistas': e['requer_pistas'],
        'recompensa_entidade': e['recompensa_entidade']
    } for e in ENIGMAS.values()]

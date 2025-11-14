"""
Sistema de Enigmas para Desbloquear Personagens - Projeto Sombra Roxa
Cada personagem requer resolver um enigma relacionado às pistas do personagem anterior
"""

ENIGMAS = {
    # Enigma para desbloquear Valdemar (após coletar pistas do Dr. Arnaldo)
    'desbloquear_fazendeiro': {
        'id': 'desbloquear_fazendeiro',
        'titulo': 'Enigma: A Conexão da Fazenda',
        'contexto': 'Dr. Arnaldo mencionou algo intrigante: "Por que o gado do Valdemar não morre de sede, com o rio venenoso ao lado?" Pense nisso junto com as outras pistas...',
        'pergunta': 'A análise do Dr. Arnaldo (PISTA-C01 e C02) prova que a \'Sombra Roxa\' é poluição industrial de Coltan. A PISTA-C03 mostra que o dono da Fazenda Nova Fronteira, Valdemar, tem uma fonte de água alternativa para o gado. O que essa atitude prova?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Que Valdemar é um fazendeiro cuidadoso e prefere água de poço',
            'B) Que o gado dele é resistente à toxina',
            'C) Que Valdemar SABE que o rio está envenenado e, portanto, está envolvido na operação que causa a poluição',
            'D) Que o rio está contaminado por causas naturais, e Valdemar apenas se adaptou'
        ],
        'resposta_correta': 'C',
        'explicacao': 'Exatamente! Se Valdemar tem uma fonte alternativa de água, significa que ele SABE que o rio está envenenado com a química do Coltan. Ele não é uma vítima, ele é cúmplice. A fazenda é o ponto de partida da investigação!',
        'recompensa_entidade': 'fazendeiro',
        'requer_pistas': ['Química_Coltan', 'Sombra_Roxa', 'Conexão_Fazenda']
    },
    
    # Enigma para desbloquear Pajé Yakamu (após coletar pistas do Valdemar)
    'desbloquear_lider_indigena': {
        'id': 'desbloquear_lider_indigena',
        'titulo': 'Enigma: A Fachada Logística',
        'contexto': 'Valdemar admitiu que a fazenda dá prejuízo e serve como "ponto de apoio logístico". Pense: qual o verdadeiro valor estratégico dessa localização?',
        'pergunta': 'Se a Fazenda Nova Fronteira não produz lucro e fica em região isolada, mas Valdemar mantém funcionários, equipamentos e estrutura cara, qual é o VERDADEIRO propósito dessa propriedade?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) É um investimento de longo prazo esperando valorização da terra',
            'B) Valdemar usa como refúgio pessoal para esconder dinheiro da justiça',
            'C) Serve como base legal para acessar e explorar recursos da reserva indígena vizinha',
            'D) É uma operação de lavagem de dinheiro disfarçada de agropecuária'
        ],
        'resposta_correta': 'C',
        'explicacao': 'Perfeito! A fazenda é uma "fachada logística" - ter propriedade registrada próxima à reserva dá acesso legal à região, justifica presença de pessoas e equipamentos, e permite invasões secretas. É a base de operações para minerar Coltan em terra indígena!',
        'recompensa_entidade': 'lider_indigena',
        'requer_pistas': ['Fazenda_Fachada_Logística', 'Conflito_Reserva_Indígena']
    },
    
    # Enigma para desbloquear Podcaster (após coletar pistas do Pajé)
    'desbloquear_podcaster': {
        'id': 'desbloquear_podcaster',
        'titulo': 'Enigma: A Rede de Poder',
        'contexto': 'O Pajé mencionou mapas ancestrais com Coltan e um "homem de terno que veio de Brasília". Analise toda a cadeia de eventos...',
        'pergunta': 'Para essa operação funcionar, seria necessário: (1) conhecer mapas indígenas secretos, (2) registrar fazenda em área estratégica, (3) evitar fiscalizações ambientais, (4) ter capital para equipamentos. Quem conecta TODAS essas peças?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) Uma máfia internacional de contrabando de minerais',
            'B) Um cartel de mineradoras multinacionais',
            'C) Um político federal com influência em múltiplas esferas (legislação, fiscalização, demarcação de terras)',
            'D) Uma organização criminosa local com apoio de garimpeiros'
        ],
        'resposta_correta': 'C',
        'explicacao': 'Excelente dedução! Apenas alguém com poder em Brasília pode: aprovar registros de propriedade fraudulentos, bloquear ações da FUNAI e IBAMA, acessar mapas de estudos governamentais sobre recursos minerais, e ter capital político para "convencer" autoridades locais. Mas antes de confrontá-lo... há uma distração no caminho.',
        'recompensa_entidade': 'podcaster',
        'requer_pistas': ['Trilha_Ancestrais_Mapa_Coltan', 'Homem_Terno_Venturi']
    },
    
    # Enigma para desbloquear Deputado Venturi (após coletar pistas do Pajé)
    'desbloquear_politico': {
        'id': 'desbloquear_politico',
        'titulo': 'Enigma: A Conspiração Completa',
        'contexto': 'O Coronel Silva revelou a verdade: Ratanabá é mentira, o Coltan é para armas militares, e Gian foi eliminado por "segurança nacional". Agora você tem provas suficientes...',
        'pergunta': 'Você reuniu evidências devastadoras: (1) Poluição química de Coltan, (2) Fazenda-fachada, (3) Contrabando militar, (4) Desinformação orquestrada. Quem é o CÉREBRO por trás de toda essa operação?',
        'tipo': 'multipla_escolha',
        'opcoes': [
            'A) O Coronel Silva - ele comanda a operação no terreno',
            'B) Valdemar - ele é o verdadeiro dono de tudo',
            'C) Deputado Venturi - político com poder para orquestrar cada peça da conspiração',
            'D) Uma organização internacional que usa Venturi como fantoche'
        ],
        'resposta_correta': 'C',
        'explicacao': 'CORRETO! Deputado Venturi é o MASTERMIND. Ele tem: poder legislativo para bloquear fiscalizações, conexões militares para o projeto secreto, capital para financiar a operação, e influência política para eliminar Gian como "risco à segurança nacional". Hora do confronto final.',
        'recompensa_entidade': 'politico',
        'requer_pistas': ['Coltan_Projeto_Militar', 'Ratanabá_É_Desinformação', 'Gian_Segurança_Nacional']
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
        'explicacao': enigma['explicacao'] if sucesso else '❌ Resposta incorreta. Analise melhor as pistas coletadas e tente novamente. Você pode refazer o enigma!',
        'entidade_desbloqueada': enigma['recompensa_entidade'] if sucesso else None,
        'pode_refazer': not sucesso  # Permite tentar de novo se errou
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

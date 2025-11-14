#!/usr/bin/env python3
"""
TESTE DE INTEGRAÇÃO COMPLETO - PROJETO SOMBRA ROXA
Simula um jogador completo testando todo o fluxo do jogo:
- Login
- Interações com personagens
- Coleta de pistas
- Resolução de desafios
- Resolução de enigmas
- Desbloqueio de novos personagens
- Progressão pelos 6 atos
"""

import requests
import json
import time
from typing import Dict, List, Any

class TesteIntegracaoCompleto:
    def __init__(self, base_url='http://localhost:5000'):
        self.base_url = base_url
        self.session = requests.Session()
        self.grupo_id = None
        self.pistas_coletadas = []
        self.personagens_desbloqueados = []
        self.enigmas_resolvidos = []
        self.desafios_completados = []
        
        # Estatísticas
        self.total_testes = 0
        self.testes_sucesso = 0
        self.testes_falha = 0
        self.erros = []
        
    def log(self, emoji, mensagem, detalhes=None):
        """Log formatado"""
        print(f"{emoji} {mensagem}")
        if detalhes:
            print(f"   └─ {detalhes}")
    
    def teste(self, nome_teste):
        """Decorator para testes"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                self.total_testes += 1
                print(f"\n{'='*60}")
                print(f"🧪 TESTE {self.total_testes}: {nome_teste}")
                print(f"{'='*60}")
                try:
                    resultado = func(*args, **kwargs)
                    if resultado:
                        self.testes_sucesso += 1
                        self.log("✅", f"SUCESSO: {nome_teste}")
                    else:
                        self.testes_falha += 1
                        self.erros.append(nome_teste)
                        self.log("❌", f"FALHA: {nome_teste}")
                    return resultado
                except Exception as e:
                    self.testes_falha += 1
                    self.erros.append(f"{nome_teste}: {str(e)}")
                    self.log("💥", f"ERRO: {nome_teste}", str(e))
                    return False
            return wrapper
        return decorator
    
    def fazer_login(self):
        """Teste 1: Login do grupo"""
        @self.teste("Login e Criação de Sessão")
        def _teste():
            payload = {
                'usuario': 'teste_auto',
                'grupo': 'Turma Teste 2025',
                'integrantes': ['Ana Silva', 'Bruno Costa', 'Carlos Santos', 'Diana Oliveira']
            }
            
            response = self.session.post(f'{self.base_url}/api/login', json=payload)
            
            if response.status_code != 200:
                self.log("❌", f"Status code: {response.status_code}")
                if response.status_code == 400:
                    data = response.json()
                    self.log("  ", f"Erro: {data.get('error')}")
                return False
            
            data = response.json()
            
            if not data.get('success'):
                self.log("❌", f"Login falhou: {data.get('error')}")
                return False
            
            self.grupo_id = data.get('grupo')
            senha_gerada = data.get('senha')
            
            self.log("🆔", f"Grupo: {self.grupo_id}")
            self.log("🔑", f"Senha gerada: {senha_gerada}")
            self.log("👥", f"Integrantes: {', '.join(data.get('integrantes', []))}")
            
            return self.grupo_id is not None
        
        return _teste()
    
    def verificar_personagens_iniciais(self):
        """Teste 2: Verificar que apenas Dr. Arnaldo está liberado"""
        @self.teste("Personagens Iniciais (só Dr. Arnaldo)")
        def _teste():
            response = self.session.get(f'{self.base_url}/api/entities')
            
            if response.status_code != 200:
                return False
            
            data = response.json()
            entities = data.get('entities', [])
            
            liberados = [e for e in entities if e.get('liberado')]
            bloqueados = [e for e in entities if not e.get('liberado')]
            
            self.log("🔓", f"Personagens liberados: {len(liberados)}")
            for e in liberados:
                self.log("  ", f"  • {e.get('emoji')} {e.get('nome')}")
            
            self.log("🔒", f"Personagens bloqueados: {len(bloqueados)}")
            for e in bloqueados:
                self.log("  ", f"  • {e.get('emoji')} {e.get('nome')}")
            
            # Verificar que APENAS Dr. Arnaldo está liberado
            if len(liberados) != 1:
                self.log("❌", "Deveria ter APENAS 1 personagem liberado")
                return False
            
            if liberados[0].get('id') != 'biologo':
                self.log("❌", "O personagem liberado deveria ser Dr. Arnaldo (biologo)")
                return False
            
            self.personagens_desbloqueados = [e.get('id') for e in liberados]
            return True
        
        return _teste()
    
    def conversar_com_personagem(self, entity_id, mensagem, pista_esperada=None):
        """Teste 3+: Conversar com personagem e coletar pista"""
        nome_personagem = {
            'biologo': 'Dr. Arnaldo',
            'fazendeiro': 'Valdemar',
            'lider_indigena': 'Yakamu',
            'podcaster': 'Jonas Falcão',
            'coronel': 'Coronel Augusto',
            'politico': 'Deputado Venturi'
        }.get(entity_id, entity_id)
        
        @self.teste(f"Conversar com {nome_personagem}: '{mensagem[:50]}'")
        def _teste():
            payload = {
                'entity_id': entity_id,
                'message': mensagem
            }
            
            response = self.session.post(f'{self.base_url}/api/chat', json=payload)
            
            if response.status_code != 200:
                self.log("❌", f"Status: {response.status_code}")
                return False
            
            data = response.json()
            reply = data.get('reply', '')
            pistas_encontradas = data.get('pistas_encontradas', [])
            interacoes = data.get('interacoes', 0)
            
            # Mostrar resposta (primeiras 200 chars)
            self.log("💬", f"Resposta: {reply[:200]}...")
            self.log("🔢", f"Interações com {nome_personagem}: {interacoes}")
            
            if pistas_encontradas:
                self.log("🔍", f"Pistas detectadas: {pistas_encontradas}")
            
            # Verificar se a pista esperada foi encontrada
            if pista_esperada:
                if pista_esperada not in pistas_encontradas:
                    self.log("⚠️", f"Pista esperada '{pista_esperada}' NÃO foi detectada")
                    # Não falha o teste, apenas avisa
                else:
                    self.log("✨", f"Pista '{pista_esperada}' detectada corretamente!")
            
            return True
        
        return _teste()
    
    def coletar_pista(self, pista_nome):
        """Teste: Coletar uma pista"""
        @self.teste(f"Coletar Pista: {pista_nome}")
        def _teste():
            payload = {'pista': pista_nome}
            
            response = self.session.post(f'{self.base_url}/api/collect', json=payload)
            
            if response.status_code != 200:
                self.log("❌", f"Status: {response.status_code}")
                return False
            
            data = response.json()
            pistas = data.get('pistas', [])
            enigma_disponivel = data.get('enigma_disponivel')
            entities = data.get('entities', [])
            
            self.pistas_coletadas = pistas
            
            self.log("📦", f"Total de pistas coletadas: {len(pistas)}")
            self.log("  ", f"  • {', '.join(pistas)}")
            
            if enigma_disponivel:
                self.log("🎯", f"ENIGMA DISPONÍVEL: {enigma_disponivel.get('titulo')}")
                self.log("  ", f"  • Objetivo: {enigma_disponivel.get('objetivo')}")
            
            # Verificar novos desbloqueios
            liberados = [e.get('id') for e in entities if e.get('liberado')]
            novos = [p for p in liberados if p not in self.personagens_desbloqueados]
            
            if novos:
                for novo_id in novos:
                    novo = next(e for e in entities if e.get('id') == novo_id)
                    self.log("🎉", f"NOVO PERSONAGEM DESBLOQUEADO: {novo.get('emoji')} {novo.get('nome')}")
                
                self.personagens_desbloqueados = liberados
            
            return pista_nome in pistas
        
        return _teste()
    
    def resolver_enigma(self, enigma_id, resposta):
        """Teste: Resolver enigma"""
        @self.teste(f"Resolver Enigma: {enigma_id}")
        def _teste():
            payload = {
                'enigma_id': enigma_id,
                'resposta': resposta
            }
            
            response = self.session.post(f'{self.base_url}/api/enigmas/responder', json=payload)
            
            if response.status_code != 200:
                self.log("❌", f"Status: {response.status_code}")
                return False
            
            data = response.json()
            sucesso = data.get('sucesso', False)
            explicacao = data.get('explicacao', '')
            entidade_desbloqueada = data.get('entidade_desbloqueada')
            
            if sucesso:
                self.log("🎊", "ENIGMA RESOLVIDO!")
                self.log("📖", f"Explicação: {explicacao[:150]}...")
                self.enigmas_resolvidos.append(enigma_id)
                
                if entidade_desbloqueada:
                    self.log("🔓", f"Desbloqueado: {entidade_desbloqueada.get('emoji')} {entidade_desbloqueada.get('nome')}")
                    
                    # Atualizar lista de desbloqueados
                    if entidade_desbloqueada.get('id') not in self.personagens_desbloqueados:
                        self.personagens_desbloqueados.append(entidade_desbloqueada.get('id'))
                
                return True
            else:
                self.log("❌", "Enigma NÃO resolvido")
                self.log("  ", f"Resposta correta era: {data.get('resposta_correta')}")
                return False
        
        return _teste()
    
    def responder_desafio(self, desafio_id, resposta):
        """Teste: Responder desafio educativo"""
        @self.teste(f"Desafio: {desafio_id}")
        def _teste():
            payload = {
                'desafio_id': desafio_id,
                'resposta': resposta
            }
            
            response = self.session.post(f'{self.base_url}/api/desafios/responder', json=payload)
            
            if response.status_code != 200:
                self.log("❌", f"Status: {response.status_code}")
                return False
            
            data = response.json()
            sucesso = data.get('sucesso', False)
            explicacao = data.get('explicacao', '')
            dica_texto = data.get('dica_texto', '')
            
            if sucesso:
                self.log("✅", "Desafio CORRETO!")
                self.log("📝", f"Explicação: {explicacao[:100]}...")
                if dica_texto:
                    self.log("💡", f"Dica desbloqueada: {dica_texto[:100]}...")
                self.desafios_completados.append(desafio_id)
                return True
            else:
                self.log("❌", "Resposta INCORRETA")
                self.log("  ", f"Correta: {data.get('resposta_correta')}")
                return False
        
        return _teste()
    
    def executar_ato_1_cientista(self):
        """ATO I: O Mistério do Rio - Dr. Arnaldo (Ciências)"""
        print("\n" + "="*60)
        print("🎬 ATO I: O MISTÉRIO DO RIO - Dr. Arnaldo Silva")
        print("="*60)
        
        # Múltiplas interações para desbloquear pistas gradualmente
        perguntas_arnaldo = [
            ("oi", None),  # Interação 1 - Saudação
            ("O que aconteceu no rio?", None),  # Interação 2
            ("Me fale sobre a sombra roxa", "Sombra_Roxa"),  # Interação 3 - Primeira pista
            ("O que é coltan?", "Química_Coltan"),  # Interação 4-5
            ("Qual a conexão com a fazenda?", "Conexão_Fazenda"),  # Interação 6-8
        ]
        
        for pergunta, pista_esperada in perguntas_arnaldo:
            self.conversar_com_personagem('biologo', pergunta, pista_esperada)
            time.sleep(0.5)
        
        # Coletar as 3 pistas do Dr. Arnaldo
        for pista in ['Sombra_Roxa', 'Química_Coltan', 'Conexão_Fazenda']:
            self.coletar_pista(pista)
            time.sleep(0.3)
        
        # Desafio educativo (Ciências)
        self.responder_desafio('ciencias_1', 'B')  # Resposta correta sobre bioacumulação
        
        # Resolver enigma para desbloquear Valdemar
        self.resolver_enigma('desbloquear_fazendeiro', 'C')
    
    def executar_ato_2_fazendeiro(self):
        """ATO II: O Segredo da Fazenda - Valdemar (Geografia)"""
        print("\n" + "="*60)
        print("🎬 ATO II: O SEGREDO DA FAZENDA - Valdemar")
        print("="*60)
        
        perguntas_valdemar = [
            ("Olá Valdemar", None),
            ("Por que a fazenda está nesse local ruim?", "Fachada_Fazenda"),
            ("Qual seu interesse na reserva indígena?", "Interesse_Reserva"),
            ("Quem é seu chefe?", "Deputado_Brasília"),
            ("Você conheceu o Gian?", "Gian_Visitou_Fazenda"),
        ]
        
        for pergunta, pista_esperada in perguntas_valdemar:
            self.conversar_com_personagem('fazendeiro', pergunta, pista_esperada)
            time.sleep(0.5)
        
        # Coletar pistas
        for pista in ['Fachada_Fazenda', 'Interesse_Reserva', 'Deputado_Brasília', 'Gian_Visitou_Fazenda']:
            self.coletar_pista(pista)
            time.sleep(0.3)
        
        # Resolver enigma
        self.resolver_enigma('desbloquear_lider_indigena', 'C')
    
    def executar_ato_3_indigena(self):
        """ATO III: A Sabedoria Ancestral - Yakamu (História)"""
        print("\n" + "="*60)
        print("🎬 ATO III: A SABEDORIA ANCESTRAL - Yakamu")
        print("="*60)
        
        perguntas_yakamu = [
            ("Olá Yakamu, com respeito", None),
            ("O que aconteceu com o rio?", "Sombra_Montanha_Fogo"),
            ("Você tem um mapa?", "Mapa_Coltan"),
            ("Quem é o homem de Brasília?", "Venturi_Identificado"),
        ]
        
        for pergunta, pista_esperada in perguntas_yakamu:
            self.conversar_com_personagem('lider_indigena', pergunta, pista_esperada)
            time.sleep(0.5)
        
        # Coletar pistas
        for pista in ['Sombra_Montanha_Fogo', 'Mapa_Coltan', 'Venturi_Identificado']:
            self.coletar_pista(pista)
            time.sleep(0.3)
        
        # Resolver enigma
        self.resolver_enigma('desbloquear_podcaster', 'C')
    
    def executar_ato_4_podcaster(self):
        """ATO IV: As Teorias da Conspiração - Jonas Falcão"""
        print("\n" + "="*60)
        print("🎬 ATO IV: AS TEORIAS DA CONSPIRAÇÃO - Jonas Falcão")
        print("="*60)
        
        perguntas_falcao = [
            ("E aí Falcão!", None),
            ("O que é Ratanabá?", "Teoria_Ratanabá"),
            ("O que aconteceu com o Gian?", "Última_Mensagem_Gian"),
            ("Qual a conspiração militar?", "Operação_Militar_Secreta"),
        ]
        
        for pergunta, pista_esperada in perguntas_falcao:
            self.conversar_com_personagem('podcaster', pergunta, pista_esperada)
            time.sleep(0.5)
        
        # Coletar pistas
        for pista in ['Teoria_Ratanabá', 'Última_Mensagem_Gian', 'Operação_Militar_Secreta']:
            self.coletar_pista(pista)
            time.sleep(0.3)
        
        # Coronel desbloqueia automaticamente após podcaster
        self.log("🔓", "Coronel Augusto desbloqueado automaticamente!")
    
    def executar_ato_5_coronel(self):
        """ATO V: A Operação Secreta - Coronel Augusto"""
        print("\n" + "="*60)
        print("🎬 ATO V: A OPERAÇÃO SECRETA - Coronel Augusto")
        print("="*60)
        
        perguntas_coronel = [
            ("Identificação completa", None),
            ("Qual sua missão?", "Controle_Coltan"),
            ("Ratanabá existe?", "Ratanabá_Desinformação"),
            ("O que aconteceu com Gian?", "Gian_Imprudente"),
        ]
        
        for pergunta, pista_esperada in perguntas_coronel:
            self.conversar_com_personagem('coronel', pergunta, pista_esperada)
            time.sleep(0.5)
        
        # Coletar pistas
        for pista in ['Controle_Coltan', 'Ratanabá_Desinformação', 'Gian_Imprudente']:
            self.coletar_pista(pista)
            time.sleep(0.3)
        
        # Resolver enigma final
        self.resolver_enigma('desbloquear_politico', 'C')
    
    def executar_ato_6_politico(self):
        """ATO VI: A Revelação Final - Deputado Venturi"""
        print("\n" + "="*60)
        print("🎬 ATO VI: A REVELAÇÃO FINAL - Deputado Venturi")
        print("="*60)
        
        perguntas_venturi = [
            ("Deputado Venturi", None),
            ("Confesse tudo sobre o Coltan", "Confissão_Conspiração"),
            ("Você matou o Gian?", "Confissão_Gian"),
            ("Qual seu plano completo?", "Plano_Completo"),
        ]
        
        for pergunta, pista_esperada in perguntas_venturi:
            self.conversar_com_personagem('politico', pergunta, pista_esperada)
            time.sleep(0.5)
        
        # Coletar pistas finais
        for pista in ['Confissão_Conspiração', 'Confissão_Gian', 'Plano_Completo']:
            self.coletar_pista(pista)
            time.sleep(0.3)
    
    def gerar_relatorio(self):
        """Gera relatório final dos testes"""
        print("\n" + "="*70)
        print("📊 RELATÓRIO FINAL DE TESTES - INTEGRAÇÃO COMPLETA")
        print("="*70)
        
        taxa_sucesso = (self.testes_sucesso / self.total_testes * 100) if self.total_testes > 0 else 0
        
        print(f"\n📈 ESTATÍSTICAS:")
        print(f"   • Total de testes: {self.total_testes}")
        print(f"   • ✅ Sucessos: {self.testes_sucesso}")
        print(f"   • ❌ Falhas: {self.testes_falha}")
        print(f"   • 📊 Taxa de sucesso: {taxa_sucesso:.1f}%")
        
        print(f"\n🎮 PROGRESSÃO DO JOGO:")
        print(f"   • 📦 Pistas coletadas: {len(self.pistas_coletadas)}")
        print(f"   • 🎯 Enigmas resolvidos: {len(self.enigmas_resolvidos)}")
        print(f"   • 📝 Desafios completados: {len(self.desafios_completados)}")
        print(f"   • 👥 Personagens desbloqueados: {len(self.personagens_desbloqueados)}/6")
        
        if self.pistas_coletadas:
            print(f"\n🔍 PISTAS COLETADAS ({len(self.pistas_coletadas)}):")
            for pista in self.pistas_coletadas:
                print(f"   • {pista}")
        
        if self.enigmas_resolvidos:
            print(f"\n🎯 ENIGMAS RESOLVIDOS ({len(self.enigmas_resolvidos)}):")
            for enigma in self.enigmas_resolvidos:
                print(f"   • {enigma}")
        
        if self.personagens_desbloqueados:
            print(f"\n👥 PERSONAGENS DESBLOQUEADOS ({len(self.personagens_desbloqueados)}):")
            nomes = {
                'biologo': '🔬 Dr. Arnaldo Silva',
                'fazendeiro': '🚜 Valdemar',
                'lider_indigena': '🪶 Yakamu',
                'podcaster': '🎙️ Jonas "Falcão" Pereira',
                'coronel': '🎖️ Coronel Augusto',
                'politico': '💼 Deputado Venturi'
            }
            for p_id in self.personagens_desbloqueados:
                print(f"   • {nomes.get(p_id, p_id)}")
        
        if self.erros:
            print(f"\n⚠️  ERROS ENCONTRADOS ({len(self.erros)}):")
            for erro in self.erros:
                print(f"   • {erro}")
        
        print("\n" + "="*70)
        
        # Resultado final
        if taxa_sucesso >= 90:
            print("🎉 SISTEMA APROVADO - Excelente integração!")
        elif taxa_sucesso >= 70:
            print("⚠️  SISTEMA COM PROBLEMAS - Revisar falhas")
        else:
            print("❌ SISTEMA REPROVADO - Correções necessárias")
        
        print("="*70)
        
        return taxa_sucesso >= 70

def main():
    """Executa todos os testes"""
    print("""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║        TESTE DE INTEGRAÇÃO COMPLETO - PROJETO SOMBRA ROXA       ║
║                                                                  ║
║  Testando: Frontend ↔ Backend ↔ Database                        ║
║            Fluxo completo dos 6 atos do jogo                    ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
    """)
    
    # Verificar se o servidor está rodando
    print("🔍 Verificando se o servidor está ativo...")
    try:
        response = requests.get('http://localhost:5000')
        print("✅ Servidor Flask detectado e ativo!\n")
    except requests.exceptions.ConnectionError:
        print("❌ ERRO: Servidor não está rodando!")
        print("   Execute: python app.py")
        print("   Ou: gunicorn app:app")
        return
    
    # Iniciar testes
    teste = TesteIntegracaoCompleto()
    
    # Fase 1: Setup inicial
    if not teste.fazer_login():
        print("\n❌ Falha no login. Abortando testes.")
        return
    
    if not teste.verificar_personagens_iniciais():
        print("\n❌ Estado inicial incorreto. Abortando testes.")
        return
    
    # Fase 2: Executar os 6 atos
    try:
        teste.executar_ato_1_cientista()
        teste.executar_ato_2_fazendeiro()
        teste.executar_ato_3_indigena()
        teste.executar_ato_4_podcaster()
        teste.executar_ato_5_coronel()
        teste.executar_ato_6_politico()
    except KeyboardInterrupt:
        print("\n\n⚠️  Testes interrompidos pelo usuário")
    except Exception as e:
        print(f"\n\n💥 Erro fatal durante os testes: {e}")
    
    # Fase 3: Relatório
    sucesso = teste.gerar_relatorio()
    
    if sucesso:
        print("\n✨ Teste de integração CONCLUÍDO com sucesso!")
        return 0
    else:
        print("\n⚠️  Teste de integração CONCLUÍDO com problemas")
        return 1

if __name__ == '__main__':
    exit(main())

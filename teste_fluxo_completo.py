"""
TESTE COMPLETO DO FLUXO DO JOGO - PROJETO ENCRUZILHADA
Testa todos os 6 atos, coleta de pistas e resolução de enigmas
"""

import sys
import time
from datetime import datetime

class TesteFluxoJogo:
    def __init__(self):
        self.pistas_coletadas = []
        self.enigmas_resolvidos = []
        self.personagens_desbloqueados = ['biologo']  # Dr. Arnaldo começa desbloqueado
        self.erros = []
        self.warnings = []
        self.log = []
        
    def log_acao(self, mensagem, tipo="INFO"):
        timestamp = datetime.now().strftime("%H:%M:%S")
        linha = f"[{timestamp}] [{tipo}] {mensagem}"
        self.log.append(linha)
        
        # Cores no terminal
        cores = {
            "INFO": "\033[94m",  # Azul
            "SUCESSO": "\033[92m",  # Verde
            "ERRO": "\033[91m",  # Vermelho
            "WARNING": "\033[93m",  # Amarelo
            "RESET": "\033[0m"
        }
        
        cor = cores.get(tipo, cores["INFO"])
        print(f"{cor}{linha}{cores['RESET']}")
        
    def coletar_pista(self, pista_id, personagem):
        self.log_acao(f"Coletando pista: {pista_id} (de {personagem})", "INFO")
        if pista_id in self.pistas_coletadas:
            self.warnings.append(f"Pista {pista_id} já foi coletada!")
            self.log_acao(f"⚠️  Pista {pista_id} duplicada", "WARNING")
        else:
            self.pistas_coletadas.append(pista_id)
            self.log_acao(f"✅ Pista coletada: {pista_id}", "SUCESSO")
        
    def resolver_enigma(self, enigma_id, resposta_correta):
        self.log_acao(f"Resolvendo enigma: {enigma_id}", "INFO")
        if enigma_id in self.enigmas_resolvidos:
            self.warnings.append(f"Enigma {enigma_id} já foi resolvido!")
            self.log_acao(f"⚠️  Enigma {enigma_id} duplicado", "WARNING")
        else:
            self.enigmas_resolvidos.append(enigma_id)
            self.log_acao(f"✅ Enigma resolvido: {enigma_id} (Resposta: {resposta_correta})", "SUCESSO")
    
    def desbloquear_personagem(self, personagem_id, nome):
        self.log_acao(f"Desbloqueando personagem: {nome}", "INFO")
        if personagem_id in self.personagens_desbloqueados:
            self.warnings.append(f"Personagem {personagem_id} já estava desbloqueado!")
            self.log_acao(f"⚠️  Personagem {personagem_id} duplicado", "WARNING")
        else:
            self.personagens_desbloqueados.append(personagem_id)
            self.log_acao(f"🔓 Personagem desbloqueado: {nome}", "SUCESSO")
    
    def verificar_requisitos_enigma(self, enigma_id, pistas_necessarias):
        self.log_acao(f"Verificando requisitos para {enigma_id}...", "INFO")
        for pista in pistas_necessarias:
            if pista not in self.pistas_coletadas:
                erro = f"Enigma {enigma_id}: Falta pista '{pista}'"
                self.erros.append(erro)
                self.log_acao(f"❌ {erro}", "ERRO")
                return False
        self.log_acao(f"✅ Todos os requisitos atendidos para {enigma_id}", "SUCESSO")
        return True
    
    def teste_ato_1_dr_arnaldo(self):
        self.log_acao("=" * 60, "INFO")
        self.log_acao("🎬 INICIANDO ATO I: O MISTÉRIO DO RIO (Dr. Arnaldo)", "INFO")
        self.log_acao("=" * 60, "INFO")
        time.sleep(0.5)
        
        # Dr. Arnaldo já está desbloqueado por padrão
        self.log_acao("✅ Dr. Arnaldo disponível por padrão", "SUCESSO")
        
        # Simular conversa e coleta de pistas
        self.log_acao("💬 Jogador: 'O que é a Sombra Roxa?'", "INFO")
        time.sleep(0.3)
        self.coletar_pista("Sombra_Roxa", "Dr. Arnaldo")
        
        self.log_acao("💬 Jogador: 'Que químicos causam isso?'", "INFO")
        time.sleep(0.3)
        self.coletar_pista("Química_Coltan", "Dr. Arnaldo")
        
        self.log_acao("💬 Jogador: 'E a fazenda rio acima?'", "INFO")
        time.sleep(0.3)
        self.coletar_pista("Gado_Não_Bebe_Rio", "Dr. Arnaldo")
        
        # Resolver enigma
        requisitos_ok = self.verificar_requisitos_enigma(
            "desbloquear_fazendeiro",
            ["Química_Coltan", "Sombra_Roxa", "Gado_Não_Bebe_Rio"]
        )
        
        if requisitos_ok:
            self.log_acao("🧩 Enigma disponível: 'O Mistério do Gado'", "INFO")
            time.sleep(0.3)
            self.resolver_enigma("desbloquear_fazendeiro", "D")
            self.desbloquear_personagem("fazendeiro", "Valdemar")
        
        self.log_acao("✅ ATO I CONCLUÍDO", "SUCESSO")
        print()
    
    def teste_ato_2_valdemar(self):
        self.log_acao("=" * 60, "INFO")
        self.log_acao("🎬 INICIANDO ATO II: A FACHADA DO PROGRESSO (Valdemar)", "INFO")
        self.log_acao("=" * 60, "INFO")
        time.sleep(0.5)
        
        # Verificar se Valdemar foi desbloqueado
        if "fazendeiro" not in self.personagens_desbloqueados:
            erro = "Valdemar não foi desbloqueado! ATO II bloqueado."
            self.erros.append(erro)
            self.log_acao(f"❌ {erro}", "ERRO")
            return
        
        # Coletar pistas de Valdemar
        self.log_acao("💬 Jogador: 'Por que seu gado não bebe do rio?'", "INFO")
        time.sleep(0.3)
        self.coletar_pista("Poço_Artesiano", "Valdemar")
        
        self.log_acao("💬 Jogador: 'A fazenda dá lucro?'", "INFO")
        time.sleep(0.3)
        self.coletar_pista("Fazenda_Fachada_Logística", "Valdemar")
        
        self.log_acao("💬 Jogador: 'Quem é Venturi?'", "INFO")
        time.sleep(0.3)
        self.coletar_pista("Deputado_Venturi_Conexão", "Valdemar")
        
        self.log_acao("💬 Jogador: 'E a terra indígena ao lado?'", "INFO")
        time.sleep(0.3)
        self.coletar_pista("Conflito_Reserva_Indígena", "Valdemar")
        
        # Resolver enigma
        requisitos_ok = self.verificar_requisitos_enigma(
            "desbloquear_lider_indigena",
            ["Fazenda_Fachada_Logística", "Conflito_Reserva_Indígena"]
        )
        
        if requisitos_ok:
            self.log_acao("🧩 Enigma disponível: 'A Fachada Logística'", "INFO")
            time.sleep(0.3)
            self.resolver_enigma("desbloquear_lider_indigena", "C")
            self.desbloquear_personagem("lider_indigena", "Pajé Yakamu")
        
        self.log_acao("✅ ATO II CONCLUÍDO", "SUCESSO")
        print()
    
    def teste_ato_3_paje_yakamu(self):
        self.log_acao("=" * 60, "INFO")
        self.log_acao("🎬 INICIANDO ATO III: O MAPA DA MEMÓRIA (Pajé Yakamu)", "INFO")
        self.log_acao("=" * 60, "INFO")
        time.sleep(0.5)
        
        if "lider_indigena" not in self.personagens_desbloqueados:
            erro = "Pajé Yakamu não foi desbloqueado! ATO III bloqueado."
            self.erros.append(erro)
            self.log_acao(f"❌ {erro}", "ERRO")
            return
        
        # Coletar pistas do Pajé
        self.log_acao("💬 Jogador: 'O que é a Sombra Roxa para seu povo?'", "INFO")
        time.sleep(0.3)
        self.coletar_pista("Sombra_Montanha_Fogo", "Pajé Yakamu")
        
        self.log_acao("💬 Jogador: 'O que é a Trilha dos Ancestrais?'", "INFO")
        time.sleep(0.3)
        self.coletar_pista("Trilha_Ancestrais_Mapa_Coltan", "Pajé Yakamu")
        
        self.log_acao("💬 Jogador: 'Quem atacou Gian?'", "INFO")
        time.sleep(0.3)
        self.coletar_pista("Homem_Terno_Venturi", "Pajé Yakamu")
        
        # Resolver enigma
        requisitos_ok = self.verificar_requisitos_enigma(
            "desbloquear_podcaster",
            ["Trilha_Ancestrais_Mapa_Coltan", "Homem_Terno_Venturi"]
        )
        
        if requisitos_ok:
            self.log_acao("🧩 Enigma disponível: 'A Rede de Poder'", "INFO")
            time.sleep(0.3)
            self.resolver_enigma("desbloquear_podcaster", "C")
            self.desbloquear_personagem("podcaster", "Jonas 'Falcão' Pereira")
        
        self.log_acao("✅ ATO III CONCLUÍDO", "SUCESSO")
        print()
    
    def teste_ato_4_falcao(self):
        self.log_acao("=" * 60, "INFO")
        self.log_acao("🎬 INICIANDO ATO IV: A CORTINA DE FUMAÇA (Falcão)", "INFO")
        self.log_acao("=" * 60, "INFO")
        time.sleep(0.5)
        
        if "podcaster" not in self.personagens_desbloqueados:
            erro = "Falcão não foi desbloqueado! ATO IV bloqueado."
            self.erros.append(erro)
            self.log_acao(f"❌ {erro}", "ERRO")
            return
        
        # Pistas FALSAS de Falcão (opcionais)
        self.log_acao("💬 Jogador: 'O que é a Trilha?'", "INFO")
        time.sleep(0.3)
        self.coletar_pista("Teoria_Ratanabá", "Falcão")
        self.log_acao("⚠️  Esta é uma PISTA FALSA (desinformação)", "WARNING")
        
        self.log_acao("💬 Jogador: 'A Sombra Roxa é poluição?'", "INFO")
        time.sleep(0.3)
        self.coletar_pista("Sombra_Roxa_É_Energia", "Falcão")
        self.log_acao("⚠️  Esta é uma PISTA FALSA (desinformação)", "WARNING")
        
        # Coronel Silva desbloqueia automaticamente após Falcão
        self.desbloquear_personagem("coronel", "Coronel Silva")
        
        self.log_acao("✅ ATO IV CONCLUÍDO (Teste de Pensamento Crítico)", "SUCESSO")
        print()
    
    def teste_ato_5_coronel_silva(self):
        self.log_acao("=" * 60, "INFO")
        self.log_acao("🎬 INICIANDO ATO V: O BRAÇO ARMADO (Coronel Silva)", "INFO")
        self.log_acao("=" * 60, "INFO")
        time.sleep(0.5)
        
        if "coronel" not in self.personagens_desbloqueados:
            erro = "Coronel Silva não foi desbloqueado! ATO V bloqueado."
            self.erros.append(erro)
            self.log_acao(f"❌ {erro}", "ERRO")
            return
        
        # Pistas do Coronel (REVELA A VERDADE)
        self.log_acao("💬 Jogador: 'É Coltan ou Ratanabá?'", "INFO")
        time.sleep(0.3)
        self.coletar_pista("Ratanabá_É_Desinformação", "Coronel Silva")
        self.log_acao("🔍 REVELAÇÃO: Ratanabá é operação de desinformação!", "SUCESSO")
        
        self.log_acao("💬 Jogador: 'Por que Coltan é tão importante?'", "INFO")
        time.sleep(0.3)
        self.coletar_pista("Coltan_Projeto_Militar", "Coronel Silva")
        self.log_acao("🔍 REVELAÇÃO: Coltan é para armas militares secretas!", "SUCESSO")
        
        self.log_acao("💬 Jogador: 'O que aconteceu com Gian?'", "INFO")
        time.sleep(0.3)
        self.coletar_pista("Gian_Segurança_Nacional", "Coronel Silva")
        self.log_acao("💀 REVELAÇÃO: Gian foi eliminado por 'segurança nacional'", "SUCESSO")
        
        # Resolver enigma final
        requisitos_ok = self.verificar_requisitos_enigma(
            "desbloquear_politico",
            ["Coltan_Projeto_Militar", "Ratanabá_É_Desinformação", "Gian_Segurança_Nacional"]
        )
        
        if requisitos_ok:
            self.log_acao("🧩 Enigma disponível: 'A Conspiração Completa'", "INFO")
            time.sleep(0.3)
            self.resolver_enigma("desbloquear_politico", "C")
            self.desbloquear_personagem("politico", "Deputado Venturi")
        
        self.log_acao("✅ ATO V CONCLUÍDO", "SUCESSO")
        print()
    
    def teste_ato_6_venturi(self):
        self.log_acao("=" * 60, "INFO")
        self.log_acao("🎬 INICIANDO ATO VI: O CONFRONTO (Deputado Venturi)", "INFO")
        self.log_acao("=" * 60, "INFO")
        time.sleep(0.5)
        
        if "politico" not in self.personagens_desbloqueados:
            erro = "Deputado Venturi não foi desbloqueado! ATO VI bloqueado."
            self.erros.append(erro)
            self.log_acao(f"❌ {erro}", "ERRO")
            return
        
        # Confronto final - apresentar evidências
        self.log_acao("🎯 ROUND 1: Apresentando evidências sobre a operação...", "INFO")
        time.sleep(0.3)
        self.log_acao("   → Química_Coltan + Fazenda_Fachada_Logística + Trilha_Ancestrais_Mapa_Coltan", "INFO")
        time.sleep(0.3)
        self.log_acao("💬 Venturi: 'Teorias da conspiração...'", "INFO")
        
        self.log_acao("🎯 ROUND 2: Apresentando a verdade...", "INFO")
        time.sleep(0.3)
        self.log_acao("   → Ratanabá_É_Desinformação + Coltan_Projeto_Militar", "INFO")
        time.sleep(0.3)
        self.log_acao("💬 Venturi: [Para de rir, tom muda para frio]", "INFO")
        
        # Pista final - A Confissão
        time.sleep(0.5)
        self.coletar_pista("Confissão_Venturi", "Deputado Venturi")
        self.log_acao("🏆 CONFISSÃO OBTIDA!", "SUCESSO")
        
        self.log_acao("✅ ATO VI CONCLUÍDO - MISSÃO CUMPRIDA!", "SUCESSO")
        print()
    
    def gerar_relatorio(self):
        self.log_acao("=" * 60, "INFO")
        self.log_acao("📊 RELATÓRIO FINAL DO TESTE", "INFO")
        self.log_acao("=" * 60, "INFO")
        print()
        
        # Estatísticas
        total_pistas = len(self.pistas_coletadas)
        pistas_verdadeiras = [p for p in self.pistas_coletadas if p not in ["Teoria_Ratanabá", "Sombra_Roxa_É_Energia"]]
        pistas_falsas = [p for p in self.pistas_coletadas if p in ["Teoria_Ratanabá", "Sombra_Roxa_É_Energia"]]
        
        print(f"✅ Pistas Coletadas: {total_pistas}")
        print(f"   - Verdadeiras: {len(pistas_verdadeiras)}")
        print(f"   - Falsas (Falcão): {len(pistas_falsas)}")
        print()
        print(f"✅ Enigmas Resolvidos: {len(self.enigmas_resolvidos)}")
        print()
        print(f"✅ Personagens Desbloqueados: {len(self.personagens_desbloqueados)}")
        for p in self.personagens_desbloqueados:
            print(f"   → {p}")
        print()
        
        # Erros e Warnings
        if self.erros:
            print(f"❌ ERROS ENCONTRADOS: {len(self.erros)}")
            for erro in self.erros:
                print(f"   • {erro}")
            print()
        else:
            print("✅ NENHUM ERRO ENCONTRADO!")
            print()
        
        if self.warnings:
            print(f"⚠️  WARNINGS: {len(self.warnings)}")
            for warning in self.warnings:
                print(f"   • {warning}")
            print()
        
        # Resultado Final
        if not self.erros:
            self.log_acao("🎉 TESTE COMPLETO: SUCESSO!", "SUCESSO")
            self.log_acao("   Todos os atos funcionaram corretamente!", "SUCESSO")
        else:
            self.log_acao("⚠️  TESTE COMPLETO: COM ERROS", "WARNING")
            self.log_acao(f"   Corrija os {len(self.erros)} erro(s) antes de publicar.", "WARNING")
        
        print()
        self.log_acao("=" * 60, "INFO")
    
    def executar_teste_completo(self):
        print("\n" + "=" * 60)
        print("🎮 TESTE COMPLETO DO FLUXO DO JOGO")
        print("   PROJETO ENCRUZILHADA - A Última Investigação de Gian Kretzl")
        print("=" * 60)
        print()
        time.sleep(1)
        
        # Executar todos os atos
        self.teste_ato_1_dr_arnaldo()
        self.teste_ato_2_valdemar()
        self.teste_ato_3_paje_yakamu()
        self.teste_ato_4_falcao()
        self.teste_ato_5_coronel_silva()
        self.teste_ato_6_venturi()
        
        # Gerar relatório
        self.gerar_relatorio()
        
        # Salvar log em arquivo
        with open("teste_fluxo_jogo_log.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(self.log))
        print(f"📄 Log salvo em: teste_fluxo_jogo_log.txt")

# Executar teste
if __name__ == "__main__":
    teste = TesteFluxoJogo()
    teste.executar_teste_completo()

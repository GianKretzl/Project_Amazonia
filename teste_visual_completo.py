#!/usr/bin/env python3
"""
TESTE VISUAL COMPLETO - PROJETO SOMBRA ROXA
Inicia o servidor e abre automaticamente o navegador para teste visual interativo
Permite testar toda a integração com interface gráfica real
"""

import subprocess
import webbrowser
import time
import os
import sys
import signal
from pathlib import Path

class TesteVisualCompleto:
    def __init__(self):
        self.servidor_processo = None
        self.base_url = 'http://localhost:5000'
        self.diretorio_projeto = Path(__file__).parent
        
    def limpar_tela(self):
        """Limpa a tela do terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def banner(self):
        """Exibe banner do teste visual"""
        self.limpar_tela()
        print("=" * 70)
        print("🎮 TESTE VISUAL COMPLETO - PROJETO SOMBRA ROXA".center(70))
        print("=" * 70)
        print()
    
    def verificar_requisitos(self):
        """Verifica se todos os requisitos estão instalados"""
        print("🔍 Verificando requisitos...")
        
        try:
            import flask
            print("   ✅ Flask instalado")
        except ImportError:
            print("   ❌ Flask não encontrado!")
            print("   💡 Execute: pip install -r requirements.txt")
            return False
        
        try:
            import requests
            print("   ✅ Requests instalado")
        except ImportError:
            print("   ❌ Requests não encontrado!")
            print("   💡 Execute: pip install -r requirements.txt")
            return False
        
        # Verificar arquivos principais
        arquivos_necessarios = [
            'app.py',
            'templates/index.html',
            'templates/interview.html',
            'static/js/main.js',
            'static/js/interview.js'
        ]
        
        for arquivo in arquivos_necessarios:
            caminho = self.diretorio_projeto / arquivo
            if caminho.exists():
                print(f"   ✅ {arquivo}")
            else:
                print(f"   ❌ {arquivo} não encontrado!")
                return False
        
        print()
        return True
    
    def iniciar_servidor(self):
        """Inicia o servidor Flask em background"""
        print("🚀 Iniciando servidor Flask...")
        
        try:
            # Iniciar servidor em processo separado
            self.servidor_processo = subprocess.Popen(
                [sys.executable, 'app.py'],
                cwd=self.diretorio_projeto,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == 'nt' else 0
            )
            
            print(f"   ✅ Servidor iniciado (PID: {self.servidor_processo.pid})")
            print(f"   🌐 URL: {self.base_url}")
            print()
            
            # Aguardar servidor ficar pronto
            print("⏳ Aguardando servidor ficar pronto...")
            max_tentativas = 30
            
            for i in range(max_tentativas):
                try:
                    import requests
                    response = requests.get(self.base_url, timeout=1)
                    if response.status_code == 200:
                        print("   ✅ Servidor pronto!")
                        print()
                        return True
                except:
                    time.sleep(0.5)
                    print(f"   ⏳ Tentativa {i+1}/{max_tentativas}...", end='\r')
            
            print("\n   ❌ Servidor não respondeu a tempo")
            return False
            
        except Exception as e:
            print(f"   ❌ Erro ao iniciar servidor: {e}")
            return False
    
    def abrir_navegador(self):
        """Abre o navegador automaticamente"""
        print("🌐 Abrindo navegador...")
        try:
            webbrowser.open(self.base_url)
            print("   ✅ Navegador aberto!")
            print()
            return True
        except Exception as e:
            print(f"   ❌ Erro ao abrir navegador: {e}")
            print(f"   💡 Abra manualmente: {self.base_url}")
            print()
            return False
    
    def exibir_instrucoes(self):
        """Exibe instruções para o teste visual"""
        print("=" * 70)
        print("📋 INSTRUÇÕES DE TESTE".center(70))
        print("=" * 70)
        print()
        print("🎯 FLUXO DE TESTE COMPLETO:")
        print()
        print("1️⃣  LOGIN")
        print("   • Acesse a tela de login")
        print("   • Crie um grupo com nome e integrantes")
        print("   • Anote a senha gerada")
        print()
        print("2️⃣  ATO I - DR. ARNALDO SILVA (Biólogo)")
        print("   • Faça perguntas sobre o rio e a sombra roxa")
        print("   • Colete pistas: Sombra_Roxa, Química_Coltan, Conexão_Fazenda")
        print("   • Responda desafios de Ciências")
        print("   • Resolva enigma para desbloquear Valdemar")
        print()
        print("3️⃣  ATO II - VALDEMAR (Fazendeiro)")
        print("   • Investigue a fazenda suspeita")
        print("   • Colete pistas sobre o deputado e a reserva indígena")
        print("   • Responda desafios de Geografia")
        print("   • Resolva enigma para desbloquear Yakamu")
        print()
        print("4️⃣  ATO III - PAJÉ YAKAMU (Líder Indígena)")
        print("   • Aprenda sobre a sabedoria ancestral")
        print("   • Descubra mapas e o homem de Brasília")
        print("   • Responda desafios de História")
        print("   • Resolva enigma para desbloquear Jonas Falcão")
        print()
        print("5️⃣  ATO IV - JONAS FALCÃO (Podcaster)")
        print("   • Navegue pelas teorias da conspiração")
        print("   • Separe fatos de desinformação")
        print("   • Coronel é desbloqueado automaticamente")
        print()
        print("6️⃣  ATO V - CORONEL AUGUSTO (Militar)")
        print("   • Descubra a operação secreta")
        print("   • Entenda a verdade sobre Ratanabá")
        print("   • Resolva enigma final para confrontar Venturi")
        print()
        print("7️⃣  ATO VI - DEPUTADO VENTURI (Político)")
        print("   • Confronto final com o vilão")
        print("   • Revele toda a conspiração")
        print("   • Complete a investigação")
        print()
        print("=" * 70)
        print("🎮 COMPONENTES A TESTAR:".center(70))
        print("=" * 70)
        print()
        print("   ✅ Sistema de Login/Autenticação")
        print("   ✅ Interface de Conversa com Personagens")
        print("   ✅ Sistema de Coleta de Pistas")
        print("   ✅ Desafios Educacionais (Quiz)")
        print("   ✅ Sistema de Enigmas")
        print("   ✅ Desbloqueio Progressivo de Personagens")
        print("   ✅ Áudio dos Personagens (TTS)")
        print("   ✅ Efeitos Visuais e Animações")
        print("   ✅ Responsividade Mobile/Desktop")
        print("   ✅ Salvamento de Progresso")
        print()
        print("=" * 70)
        print()
        print("💡 DICAS:")
        print("   • Use o DevTools do navegador (F12) para ver logs")
        print("   • Teste em diferentes tamanhos de tela")
        print("   • Verifique se os áudios estão funcionando")
        print("   • Teste salvar e carregar progresso")
        print()
        print("=" * 70)
        print()
        print("⌨️  COMANDOS:")
        print("   • Pressione Ctrl+C para encerrar o servidor")
        print("   • Digite 'logs' para ver logs do servidor")
        print("   • Digite 'url' para ver a URL novamente")
        print()
        print("=" * 70)
        print()
    
    def monitorar_servidor(self):
        """Monitora o servidor e permite comandos interativos"""
        print("🎮 Servidor rodando! Teste a aplicação no navegador.")
        print("   Digite comandos ou Ctrl+C para encerrar.")
        print()
        
        try:
            while True:
                try:
                    comando = input(">>> ").strip().lower()
                    
                    if comando == 'logs':
                        print("\n📋 Logs do servidor:")
                        print("   (Implementação futura - veja o terminal do servidor)")
                        print()
                    
                    elif comando == 'url':
                        print(f"\n🌐 URL do servidor: {self.base_url}")
                        print()
                    
                    elif comando == 'help' or comando == 'ajuda':
                        print("\n📚 Comandos disponíveis:")
                        print("   logs  - Exibir logs do servidor")
                        print("   url   - Mostrar URL do servidor")
                        print("   help  - Mostrar esta ajuda")
                        print("   quit  - Encerrar servidor")
                        print()
                    
                    elif comando == 'quit' or comando == 'sair':
                        print("\n👋 Encerrando servidor...")
                        break
                    
                    elif comando:
                        print(f"\n❓ Comando desconhecido: '{comando}'")
                        print("   Digite 'help' para ver comandos disponíveis")
                        print()
                
                except EOFError:
                    break
                    
        except KeyboardInterrupt:
            print("\n\n👋 Encerrando servidor...")
    
    def encerrar_servidor(self):
        """Encerra o servidor Flask"""
        if self.servidor_processo:
            print("\n🛑 Encerrando servidor...")
            try:
                if os.name == 'nt':  # Windows
                    os.kill(self.servidor_processo.pid, signal.CTRL_BREAK_EVENT)
                else:  # Linux/Mac
                    self.servidor_processo.terminate()
                
                self.servidor_processo.wait(timeout=5)
                print("   ✅ Servidor encerrado com sucesso!")
            except:
                print("   ⚠️  Forçando encerramento...")
                self.servidor_processo.kill()
                print("   ✅ Servidor encerrado (forçado)")
    
    def executar(self):
        """Executa o teste visual completo"""
        try:
            # Banner
            self.banner()
            
            # Verificar requisitos
            if not self.verificar_requisitos():
                print("\n❌ Requisitos não atendidos. Corrija os problemas acima.")
                return False
            
            # Iniciar servidor
            if not self.iniciar_servidor():
                print("\n❌ Falha ao iniciar servidor.")
                return False
            
            # Abrir navegador
            self.abrir_navegador()
            
            # Exibir instruções
            self.exibir_instrucoes()
            
            # Monitorar servidor
            self.monitorar_servidor()
            
            return True
            
        except KeyboardInterrupt:
            print("\n\n⚠️  Interrompido pelo usuário")
            return False
        
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            import traceback
            traceback.print_exc()
            return False
        
        finally:
            # Sempre encerrar servidor
            self.encerrar_servidor()
            print("\n" + "=" * 70)
            print("🎉 Teste visual concluído!".center(70))
            print("=" * 70)
            print()


def main():
    """Função principal"""
    teste = TesteVisualCompleto()
    sucesso = teste.executar()
    sys.exit(0 if sucesso else 1)


if __name__ == '__main__':
    main()

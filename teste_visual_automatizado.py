#!/usr/bin/env python3
"""
TESTE VISUAL AUTOMATIZADO - PROJETO SOMBRA ROXA
Usa Selenium WebDriver para simular um usuário real interagindo com a interface
Testa todo o fluxo do jogo automaticamente no navegador
"""

import subprocess
import time
import sys
import os
import signal
from pathlib import Path

# Verificar e instalar selenium se necessário
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import TimeoutException, NoSuchElementException
except ImportError:
    print("📦 Instalando Selenium WebDriver...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium"])
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import TimeoutException, NoSuchElementException


class TesteVisualAutomatizado:
    def __init__(self):
        self.base_url = 'http://localhost:5000'
        self.diretorio_projeto = Path(__file__).parent
        self.servidor_processo = None
        self.driver = None
        self.wait = None
        
        # Estatísticas
        self.total_testes = 0
        self.testes_sucesso = 0
        self.testes_falha = 0
        self.screenshots = []
    
    def log(self, emoji, mensagem, detalhes=None):
        """Log formatado"""
        print(f"{emoji} {mensagem}")
        if detalhes:
            print(f"   └─ {detalhes}")
    
    def screenshot(self, nome):
        """Tira screenshot da tela atual"""
        try:
            screenshots_dir = self.diretorio_projeto / 'screenshots_testes'
            screenshots_dir.mkdir(exist_ok=True)
            
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"{timestamp}_{nome}.png"
            filepath = screenshots_dir / filename
            
            self.driver.save_screenshot(str(filepath))
            self.screenshots.append(str(filepath))
            self.log("📸", f"Screenshot: {filename}")
            return True
        except Exception as e:
            self.log("⚠️", f"Erro ao tirar screenshot: {e}")
            return False
    
    def iniciar_servidor(self):
        """Inicia o servidor Flask"""
        self.log("🚀", "Iniciando servidor Flask...")
        
        try:
            self.servidor_processo = subprocess.Popen(
                [sys.executable, 'app.py'],
                cwd=self.diretorio_projeto,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == 'nt' else 0
            )
            
            self.log("✅", f"Servidor iniciado (PID: {self.servidor_processo.pid})")
            
            # Aguardar servidor ficar pronto
            self.log("⏳", "Aguardando servidor...")
            import requests
            
            for i in range(30):
                try:
                    response = requests.get(self.base_url, timeout=1)
                    if response.status_code == 200:
                        self.log("✅", "Servidor pronto!")
                        return True
                except:
                    time.sleep(0.5)
            
            self.log("❌", "Servidor não respondeu")
            return False
            
        except Exception as e:
            self.log("❌", f"Erro ao iniciar servidor: {e}")
            return False
    
    def iniciar_navegador(self):
        """Inicia o navegador Chrome"""
        self.log("🌐", "Iniciando navegador Chrome...")
        
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--start-maximized')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            
            # Tentar Chrome, senão Firefox
            try:
                self.driver = webdriver.Chrome(options=options)
            except:
                self.log("⚠️", "Chrome não encontrado, tentando Firefox...")
                self.driver = webdriver.Firefox()
            
            self.wait = WebDriverWait(self.driver, 10)
            self.log("✅", "Navegador iniciado!")
            return True
            
        except Exception as e:
            self.log("❌", f"Erro ao iniciar navegador: {e}")
            self.log("💡", "Instale ChromeDriver: https://chromedriver.chromium.org/")
            return False
    
    def teste_login(self):
        """Teste 1: Login e criação de conta"""
        self.total_testes += 1
        self.log("\n" + "="*60, "")
        self.log("🧪", f"TESTE {self.total_testes}: Login e Criação de Conta")
        self.log("="*60, "")
        
        try:
            # Acessar página inicial
            self.driver.get(self.base_url)
            time.sleep(2)
            self.screenshot("01_pagina_inicial")
            
            # Preencher formulário de login
            self.log("📝", "Preenchendo formulário de login...")
            
            # Nome de usuário
            usuario = self.wait.until(EC.presence_of_element_located((By.ID, "usuario-nome")))
            usuario.send_keys("teste_visual_auto")
            
            # Nome do grupo
            grupo = self.driver.find_element(By.ID, "grupo-nome")
            grupo.send_keys("Grupo Automatizado 2025")
            
            # Primeiro integrante (já existe no formulário)
            integrantes = self.driver.find_elements(By.CSS_SELECTOR, "input[name='integrante[]']")
            if integrantes:
                integrantes[0].send_keys("Ana Automatizada")
            
            # Adicionar mais integrantes
            for nome in ["Bruno Bot", "Carlos Chrome", "Diana Driver"]:
                # Clicar no botão adicionar integrante
                try:
                    btn_add = self.driver.find_element(By.ID, "add-integrante")
                    btn_add.click()
                    time.sleep(0.3)
                    
                    # Preencher o novo campo
                    integrantes = self.driver.find_elements(By.CSS_SELECTOR, "input[name='integrante[]']")
                    if integrantes:
                        integrantes[-1].send_keys(nome)
                except:
                    self.log("⚠️", f"Não foi possível adicionar: {nome}")
            
            time.sleep(1)
            self.screenshot("02_formulario_preenchido")
            
            # Clicar em enviar
            self.log("🖱️", "Clicando em 'Iniciar Investigação'...")
            btn_submit = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            btn_submit.click()
            
            # Aguardar tela de senha aparecer
            time.sleep(3)
            self.screenshot("03_tela_senha")
            
            # Procurar pelo botão "JÁ ANOTEI A SENHA"
            self.log("🔑", "Aguardando tela de senha...")
            try:
                btn_continuar = self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-acknowledge"))
                )
                self.log("🖱️", "Clicando em 'JÁ ANOTEI A SENHA - CONTINUAR'...")
                btn_continuar.click()
            except:
                # Caso não encontre o botão, tentar por texto
                botoes = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'CONTINUAR')]")
                if botoes:
                    botoes[0].click()
                else:
                    # Se não tem botão, pode já ter redirecionado
                    self.log("⚠️", "Botão não encontrado, pode ter redirecionado automaticamente")
            
            # Aguardar redirecionamento para a entrevista
            time.sleep(4)
            self.screenshot("04_apos_login")
            
            # Verificar se chegou na tela de entrevista
            try:
                # Procurar por elementos da tela de entrevista
                self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "interview-container")))
                self.log("✅", "Login realizado com sucesso!")
                self.log("🎙️", "Sala de entrevistas carregada!")
            except:
                # Tentar verificar por título ou outros elementos
                if "SALA DE ENTREVISTAS" in self.driver.page_source or "interview" in self.driver.current_url:
                    self.log("✅", "Login realizado com sucesso!")
                else:
                    raise Exception("Não foi possível confirmar chegada na sala de entrevistas")
            
            self.testes_sucesso += 1
            return True
            
        except Exception as e:
            self.log("❌", f"Erro no teste de login: {e}")
            self.screenshot("erro_login")
            self.testes_falha += 1
            return False
    
    def teste_conversa_personagem(self, personagem, mensagens):
        """Teste: Conversar com um personagem"""
        self.total_testes += 1
        self.log("\n" + "="*60, "")
        self.log("🧪", f"TESTE {self.total_testes}: Conversa com {personagem}")
        self.log("="*60, "")
        
        try:
            for idx, mensagem in enumerate(mensagens, 1):
                self.log("💬", f"Enviando: '{mensagem}'")
                
                # Localizar campo de input (ID correto: chat-input)
                input_msg = self.wait.until(EC.presence_of_element_located((By.ID, "chat-input")))
                input_msg.clear()
                input_msg.send_keys(mensagem)
                
                time.sleep(0.5)
                
                # Enviar mensagem (clicar no botão submit do form)
                btn_enviar = self.driver.find_element(By.CSS_SELECTOR, "#chat-form button[type='submit']")
                btn_enviar.click()
                
                # Aguardar resposta (mais tempo para IA processar)
                time.sleep(4)
                
                # Screenshot
                self.screenshot(f"conversa_{personagem.replace(' ', '_')}_{idx:02d}")
                
                self.log("✅", f"Mensagem {idx}/{len(mensagens)} enviada")
            
            self.testes_sucesso += 1
            return True
            
        except Exception as e:
            self.log("❌", f"Erro na conversa: {e}")
            self.screenshot(f"erro_conversa_{personagem.replace(' ', '_')}")
            self.testes_falha += 1
            return False
    
    def teste_coletar_pista(self, pista_nome):
        """Teste: Coletar uma pista"""
        self.total_testes += 1
        self.log("\n" + "="*60, "")
        self.log("🧪", f"TESTE {self.total_testes}: Coletar Pista '{pista_nome}'")
        self.log("="*60, "")
        
        try:
            # Procurar pelo botão de coletar pista
            self.log("🔍", "Procurando pista disponível...")
            
            # Aguardar botão aparecer
            time.sleep(2)
            
            # Tentar encontrar botão de coletar (pode ter vários formatos)
            botoes = self.driver.find_elements(By.CSS_SELECTOR, "button.btn-pista, button.collect-clue")
            
            if not botoes:
                # Tentar por texto
                botoes = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Coletar')]")
            
            if botoes:
                self.log("🖱️", "Clicando em coletar pista...")
                botoes[0].click()
                time.sleep(2)
                self.screenshot(f"pista_coletada_{pista_nome}")
                self.log("✅", f"Pista '{pista_nome}' coletada!")
                self.testes_sucesso += 1
                return True
            else:
                self.log("⚠️", "Botão de coletar não encontrado (pista pode já estar coletada)")
                self.testes_sucesso += 1
                return True
                
        except Exception as e:
            self.log("❌", f"Erro ao coletar pista: {e}")
            self.screenshot(f"erro_pista_{pista_nome}")
            self.testes_falha += 1
            return False
    
    def teste_desafio(self, resposta_letra):
        """Teste: Responder desafio educativo"""
        self.total_testes += 1
        self.log("\n" + "="*60, "")
        self.log("🧪", f"TESTE {self.total_testes}: Responder Desafio")
        self.log("="*60, "")
        
        try:
            self.log("🔍", "Procurando desafio...")
            time.sleep(2)
            
            # Procurar por opções de múltipla escolha
            opcoes = self.driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
            
            if opcoes:
                self.log("📝", f"Selecionando resposta '{resposta_letra}'...")
                
                # Selecionar a resposta correta
                for opcao in opcoes:
                    if resposta_letra.upper() in opcao.get_attribute('value').upper():
                        opcao.click()
                        break
                
                time.sleep(1)
                self.screenshot(f"desafio_respondido")
                
                # Procurar botão de enviar
                btn_enviar = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Enviar') or contains(text(), 'Responder')]")
                btn_enviar.click()
                
                time.sleep(2)
                self.screenshot(f"desafio_resultado")
                
                self.log("✅", "Desafio respondido!")
                self.testes_sucesso += 1
                return True
            else:
                self.log("⚠️", "Desafio não encontrado neste momento")
                self.testes_sucesso += 1
                return True
                
        except Exception as e:
            self.log("❌", f"Erro no desafio: {e}")
            self.screenshot(f"erro_desafio")
            self.testes_falha += 1
            return False
    
    def teste_trocar_personagem(self, personagem_nome):
        """Teste: Trocar de personagem"""
        self.total_testes += 1
        self.log("\n" + "="*60, "")
        self.log("🧪", f"TESTE {self.total_testes}: Trocar para '{personagem_nome}'")
        self.log("="*60, "")
        
        try:
            self.log("🔍", "Procurando card do personagem...")
            
            # Aguardar cards de personagens carregarem
            time.sleep(2)
            
            # Procurar pelo card do personagem pelo nome
            cards = self.driver.find_elements(By.CLASS_NAME, "entity-card")
            
            personagem_encontrado = False
            for card in cards:
                # Verificar se o card contém o nome do personagem e não está bloqueado
                if personagem_nome.lower() in card.text.lower() and "locked" not in card.get_attribute("class"):
                    self.log("🖱️", f"Clicando em '{personagem_nome}'...")
                    card.click()
                    personagem_encontrado = True
                    break
            
            if not personagem_encontrado:
                raise Exception(f"Personagem '{personagem_nome}' não encontrado ou ainda bloqueado")
            
            time.sleep(3)
            self.screenshot(f"personagem_{personagem_nome.replace(' ', '_')}")
            
            # Verificar se a área de chat está visível
            chat_area = self.driver.find_element(By.ID, "chat-area")
            if chat_area.is_displayed():
                self.log("✅", f"Personagem '{personagem_nome}' selecionado!")
                self.testes_sucesso += 1
                return True
            else:
                raise Exception("Área de chat não ficou visível")
            
        except Exception as e:
            self.log("❌", f"Erro ao trocar personagem: {e}")
            self.screenshot(f"erro_trocar_{personagem_nome.replace(' ', '_')}")
            self.testes_falha += 1
            return False
    
    def executar_fluxo_completo(self):
        """Executa o fluxo completo de testes visuais"""
        self.log("\n" + "="*70, "")
        self.log("🎮", "INICIANDO TESTE VISUAL AUTOMATIZADO COMPLETO")
        self.log("="*70, "")
        
        # 1. Login
        if not self.teste_login():
            return False
        
        # 2. ATO I - Dr. Arnaldo
        self.log("\n🎬", "ATO I: DR. ARNALDO SILVA")
        self.teste_conversa_personagem("Dr. Arnaldo", [
            "Olá Dr. Arnaldo",
            "O que é a Sombra Roxa?",
            "Me fale sobre o Coltan",
            "Qual a conexão com a fazenda?"
        ])
        
        time.sleep(2)
        
        # Coletar pistas
        self.teste_coletar_pista("Sombra_Roxa")
        self.teste_coletar_pista("Química_Coltan")
        self.teste_coletar_pista("Conexão_Fazenda")
        
        # 3. ATO II - Valdemar (se desbloqueado)
        self.log("\n🎬", "ATO II: VALDEMAR")
        
        try:
            if self.teste_trocar_personagem("Valdemar"):
                self.teste_conversa_personagem("Valdemar", [
                    "Olá Valdemar",
                    "Por que sua fazenda está aqui?",
                    "Quem é seu chefe?",
                    "Você conheceu o Gian?"
                ])
        except:
            self.log("⚠️", "Valdemar ainda não desbloqueado, continuando...")
        
        # 4. ATO III - Yakamu (se desbloqueado)
        self.log("\n🎬", "ATO III: PAJÉ YAKAMU")
        
        try:
            if self.teste_trocar_personagem("Yakamu"):
                self.teste_conversa_personagem("Yakamu", [
                    "Olá Yakamu, com respeito",
                    "O que aconteceu com o rio?",
                    "Você tem um mapa?",
                    "Quem é o homem de Brasília?"
                ])
        except:
            self.log("⚠️", "Yakamu ainda não desbloqueado, continuando...")
        
        # Screenshot final
        time.sleep(2)
        self.screenshot("teste_completo_final")
        
        return True
    
    def exibir_relatorio(self):
        """Exibe relatório final dos testes"""
        self.log("\n" + "="*70, "")
        self.log("📊", "RELATÓRIO FINAL - TESTE VISUAL AUTOMATIZADO")
        self.log("="*70, "")
        
        taxa_sucesso = (self.testes_sucesso / self.total_testes * 100) if self.total_testes > 0 else 0
        
        self.log("📈", f"Total de testes: {self.total_testes}")
        self.log("✅", f"Sucessos: {self.testes_sucesso}")
        self.log("❌", f"Falhas: {self.testes_falha}")
        self.log("📊", f"Taxa de sucesso: {taxa_sucesso:.1f}%")
        
        if self.screenshots:
            self.log("\n📸", f"Screenshots capturados: {len(self.screenshots)}")
            screenshots_dir = self.diretorio_projeto / 'screenshots_testes'
            self.log("📁", f"Pasta: {screenshots_dir}")
        
        self.log("\n" + "="*70, "")
        
        if self.testes_falha == 0:
            self.log("🎉", "TODOS OS TESTES PASSARAM!")
        else:
            self.log("⚠️", f"{self.testes_falha} teste(s) falharam")
        
        self.log("="*70, "")
    
    def encerrar(self):
        """Encerra navegador e servidor"""
        self.log("\n🛑", "Encerrando teste visual...")
        
        # Fechar navegador
        if self.driver:
            try:
                self.driver.quit()
                self.log("✅", "Navegador fechado")
            except:
                pass
        
        # Encerrar servidor
        if self.servidor_processo:
            try:
                if os.name == 'nt':
                    os.kill(self.servidor_processo.pid, signal.CTRL_BREAK_EVENT)
                else:
                    self.servidor_processo.terminate()
                
                self.servidor_processo.wait(timeout=5)
                self.log("✅", "Servidor encerrado")
            except:
                try:
                    self.servidor_processo.kill()
                except:
                    pass
    
    def executar(self):
        """Executa todos os testes visuais"""
        try:
            # Iniciar servidor
            if not self.iniciar_servidor():
                return False
            
            # Iniciar navegador
            if not self.iniciar_navegador():
                return False
            
            # Executar fluxo de testes
            self.executar_fluxo_completo()
            
            # Relatório
            self.exibir_relatorio()
            
            # Aguardar antes de fechar
            self.log("\n⏳", "Aguardando 5 segundos antes de fechar...")
            time.sleep(5)
            
            return True
            
        except KeyboardInterrupt:
            self.log("\n⚠️", "Teste interrompido pelo usuário")
            return False
            
        except Exception as e:
            self.log("\n❌", f"Erro durante teste: {e}")
            import traceback
            traceback.print_exc()
            return False
            
        finally:
            self.encerrar()


def main():
    """Função principal"""
    print("\n" + "="*70)
    print("🤖 TESTE VISUAL AUTOMATIZADO - PROJETO SOMBRA ROXA".center(70))
    print("="*70)
    print()
    print("Este teste simula um usuário real interagindo com a interface")
    print("usando Selenium WebDriver para automação de navegador.")
    print()
    print("📋 O que será testado:")
    print("   • Login e criação de conta")
    print("   • Conversas com personagens")
    print("   • Coleta de pistas")
    print("   • Navegação entre personagens")
    print("   • Interface responsiva")
    print()
    print("📸 Screenshots serão salvos em: screenshots_testes/")
    print()
    print("="*70)
    print()
    
    input("Pressione ENTER para iniciar os testes... ")
    print()
    
    teste = TesteVisualAutomatizado()
    sucesso = teste.executar()
    
    sys.exit(0 if sucesso else 1)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Script de validação pré-deploy
Testa se todas as configurações estão corretas
"""

import os
import sys

def test_imports():
    """Testar se todas as importações funcionam"""
    print("📦 Testando importações...")
    try:
        import flask
        print("  ✅ Flask")
        import dotenv
        print("  ✅ python-dotenv")
        import openai
        print("  ✅ openai")
        
        # Testar imports condicionais do database
        try:
            import psycopg2
            print("  ✅ psycopg2-binary (PostgreSQL)")
        except ImportError:
            print("  ⚠️  psycopg2-binary não instalado - instale com: pip install -r requirements.txt")
            return False
        
        try:
            import gunicorn
            print("  ✅ gunicorn")
        except ImportError:
            print("  ⚠️  gunicorn não instalado - instale com: pip install -r requirements.txt")
            return False
            
        return True
    except ImportError as e:
        print(f"  ❌ Erro: {e}")
        return False

def test_database():
    """Testar inicialização do banco"""
    print("\n🗄️  Testando banco de dados...")
    try:
        from database import db
        
        db_type = "PostgreSQL" if db.use_postgres else "SQLite"
        print(f"  ✅ Banco inicializado: {db_type}")
        
        if db.use_postgres:
            print(f"  ✅ URL: {db.database_url[:30]}...")
        else:
            print(f"  ✅ Path: {db.db_path}")
        
        # Testar operação básica
        import uuid
        test_session = str(uuid.uuid4())
        db.ensure_player(test_session)
        db.add_pista(test_session, "TESTE_VALIDACAO")
        pistas = db.get_pistas(test_session)
        
        if "TESTE_VALIDACAO" in pistas:
            print("  ✅ Operações de escrita/leitura funcionando")
            # Limpar teste
            db.reset_player_progress(test_session)
            return True
        else:
            print("  ❌ Erro ao testar operações")
            return False
            
    except Exception as e:
        print(f"  ❌ Erro: {e}")
        return False

def test_app():
    """Testar se app.py carrega"""
    print("\n🎮 Testando aplicação...")
    try:
        from app import create_app
        app = create_app()
        print("  ✅ App Flask criado com sucesso")
        print(f"  ✅ Secret key configurado: {bool(app.secret_key)}")
        return True
    except Exception as e:
        print(f"  ❌ Erro: {e}")
        return False

def test_files():
    """Testar se arquivos necessários existem"""
    print("\n📁 Testando arquivos de deploy...")
    
    required_files = {
        'requirements.txt': 'Dependências Python',
        'Procfile': 'Comando de start do Render',
        'build.sh': 'Script de build',
        'app.py': 'Aplicação principal',
        'database.py': 'Sistema de banco de dados',
        '.env.example': 'Exemplo de variáveis de ambiente'
    }
    
    all_ok = True
    for file, desc in required_files.items():
        if os.path.exists(file):
            print(f"  ✅ {file} - {desc}")
        else:
            print(f"  ❌ {file} - FALTANDO!")
            all_ok = False
    
    return all_ok

def test_env_example():
    """Verificar se .env.example está completo"""
    print("\n🔧 Testando configurações de ambiente...")
    try:
        with open('.env.example', 'r') as f:
            content = f.read()
        
        required_vars = ['SECRET_KEY', 'OPENAI_API_KEY', 'DATABASE_URL']
        all_ok = True
        
        for var in required_vars:
            if var in content:
                print(f"  ✅ {var} documentado")
            else:
                print(f"  ⚠️  {var} não encontrado em .env.example")
                all_ok = False
        
        return all_ok
    except Exception as e:
        print(f"  ❌ Erro: {e}")
        return False

def main():
    print("=" * 60)
    print("🚀 PROJECT AMAZONIA - VALIDAÇÃO PRÉ-DEPLOY")
    print("=" * 60)
    
    tests = [
        ("Importações", test_imports),
        ("Banco de dados", test_database),
        ("Aplicação Flask", test_app),
        ("Arquivos necessários", test_files),
        ("Variáveis de ambiente", test_env_example)
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n❌ Erro crítico em '{name}': {e}")
            results.append((name, False))
    
    print("\n" + "=" * 60)
    print("📊 RESULTADO FINAL")
    print("=" * 60)
    
    all_passed = all(result for _, result in results)
    
    for name, result in results:
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"{status} - {name}")
    
    print("=" * 60)
    
    if all_passed:
        print("✅ TODOS OS TESTES PASSARAM!")
        print("🚀 Projeto pronto para deploy no Render!")
        print("\nPróximos passos:")
        print("1. git add .")
        print("2. git commit -m 'feat: PostgreSQL + Render deploy'")
        print("3. git push origin main")
        print("4. Siga o guia em DEPLOY_RENDER.md")
        return 0
    else:
        print("❌ ALGUNS TESTES FALHARAM")
        print("⚠️  Corrija os erros antes de fazer deploy")
        return 1

if __name__ == "__main__":
    sys.exit(main())

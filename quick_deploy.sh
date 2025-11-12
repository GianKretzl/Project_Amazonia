#!/bin/bash
# Comandos rápidos para deploy no Render

echo "🚀 PROJECT AMAZONIA - Deploy Rápido"
echo ""
echo "Escolha uma opção:"
echo ""
echo "1. 📤 Push para GitHub (deploy automático no Render)"
echo "2. 🧪 Rodar testes de validação"
echo "3. 🏃 Rodar servidor local"
echo "4. 📖 Abrir guia de deploy"
echo ""

read -p "Opção (1-4): " option

case $option in
  1)
    echo ""
    echo "📤 Fazendo push para GitHub..."
    git push origin main
    echo ""
    echo "✅ Push concluído!"
    echo "🔄 Render vai fazer deploy automaticamente em ~5 minutos"
    echo "📊 Acompanhe em: https://dashboard.render.com"
    ;;
  2)
    echo ""
    echo "🧪 Executando testes..."
    python test_deploy.py
    ;;
  3)
    echo ""
    echo "🏃 Iniciando servidor local..."
    echo "🌐 Acesse: http://localhost:5000"
    python app.py
    ;;
  4)
    echo ""
    echo "📖 Abrindo guia de deploy..."
    cat DEPLOY_RENDER.md
    ;;
  *)
    echo "❌ Opção inválida"
    exit 1
    ;;
esac

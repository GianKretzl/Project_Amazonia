#!/bin/bash
# Script para executar teste completo de integração

echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║     TESTE DE INTEGRAÇÃO - PROJETO SOMBRA ROXA                    ║"
echo "╚══════════════════════════════════════════════════════════════════╝"
echo ""

# Cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Verificar se o servidor já está rodando
echo -e "${BLUE}🔍 Verificando servidor Flask...${NC}"
if curl -s http://localhost:5000 > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Servidor já está rodando!${NC}"
    SERVER_RUNNING=true
else
    echo -e "${YELLOW}⚠️  Servidor não detectado. Iniciando...${NC}"
    SERVER_RUNNING=false
    
    # Iniciar servidor em background
    python3 app.py > logs_servidor_teste.log 2>&1 &
    SERVER_PID=$!
    
    echo -e "${BLUE}⏳ Aguardando servidor inicializar (PID: $SERVER_PID)...${NC}"
    sleep 3
    
    # Verificar se iniciou
    if curl -s http://localhost:5000 > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Servidor iniciado com sucesso!${NC}"
    else
        echo -e "${RED}❌ Falha ao iniciar servidor. Verifique logs_servidor_teste.log${NC}"
        exit 1
    fi
fi

echo ""
echo -e "${BLUE}🧪 Executando teste de integração completo...${NC}"
echo ""

# Executar testes
python3 teste_integracao_completo.py
TEST_RESULT=$?

echo ""

# Parar servidor se foi iniciado por este script
if [ "$SERVER_RUNNING" = false ]; then
    echo -e "${YELLOW}🛑 Parando servidor de teste (PID: $SERVER_PID)...${NC}"
    kill $SERVER_PID 2>/dev/null
    echo -e "${GREEN}✅ Servidor parado${NC}"
fi

# Resultado final
echo ""
if [ $TEST_RESULT -eq 0 ]; then
    echo -e "${GREEN}╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║  ✅ TESTES CONCLUÍDOS COM SUCESSO!                               ║${NC}"
    echo -e "${GREEN}╚══════════════════════════════════════════════════════════════════╝${NC}"
else
    echo -e "${RED}╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${RED}║  ⚠️  TESTES CONCLUÍDOS COM PROBLEMAS                             ║${NC}"
    echo -e "${RED}╚══════════════════════════════════════════════════════════════════╝${NC}"
fi

exit $TEST_RESULT

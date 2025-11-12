# 🚨 CONFIGURAÇÃO PARA PRODUÇÃO

## ⚠️ IMPORTANTE: Banco Zerado a Cada Deploy

Por padrão, o sistema está configurado para **ZERAR o banco de dados a cada deploy**. Isso é útil para:
- ✅ Testes e desenvolvimento
- ✅ Demonstrações sempre limpas
- ✅ Evitar dados inconsistentes durante mudanças

**PORÉM**, isso significa que:
- ❌ **Todos os dados são perdidos** a cada `git push`
- ❌ Contas de usuários são deletadas
- ❌ Progresso do jogo é resetado
- ❌ Histórico de chat é apagado

---

## 🔧 Como DESABILITAR para Produção Real

### Passo 1: Editar `build.sh`

Abra o arquivo `build.sh` e **comente ou remova** a seção:

```bash
# ZERAR banco de dados a cada deploy (remover para produção real)
echo "🗑️  ZERANDO banco de dados..."
python -c "
# ... todo o código de zeramento ...
"
```

**Resultado esperado:**

```bash
# Inicializar banco de dados (criar tabelas)
echo "📊 Inicializando banco de dados..."
python -c "from database import db; print('✅ Banco de dados inicializado!')"

# --- SEÇÃO DE ZERAMENTO COMENTADA OU REMOVIDA ---

echo "🎮 Pronto! Iniciando servidor..."
```

### Passo 2: Fazer Deploy

```bash
git add build.sh
git commit -m "chore: desabilitar zeramento de banco para produção"
git push origin main
```

---

## 📊 Gerenciamento de Banco em Produção

### Quando MANTER o zeramento:
- 🧪 **Ambiente de testes/demo**
- 🎓 **Apresentações escolares** (dados sempre limpos)
- 🔄 **Desenvolvimento ativo** (muitas mudanças de schema)

### Quando REMOVER o zeramento:
- 🏭 **Produção real** com usuários reais
- 💾 **Dados devem persistir** entre deploys
- 📈 **Acumulação de estatísticas**

---

## 🗄️ Backups Manuais (se necessário)

Se precisar fazer backup do banco PostgreSQL no Render:

1. Acesse o Dashboard do Render
2. Vá em PostgreSQL → seu banco
3. Clique em "Backups" (planos pagos)
4. Ou use `pg_dump` manualmente:

```bash
# Exportar backup
pg_dump $DATABASE_URL > backup.sql

# Restaurar backup
psql $DATABASE_URL < backup.sql
```

---

## 🔄 Alternativa: Zeramento Condicional

Você pode modificar `build.sh` para zerar apenas em desenvolvimento:

```bash
# Zerar apenas se variável RESET_DB=true
if [ "$RESET_DB" = "true" ]; then
    echo "🗑️  ZERANDO banco de dados..."
    # ... código de zeramento ...
fi
```

Depois configure no Render:
- **Desenvolvimento**: Adicione variável `RESET_DB=true`
- **Produção**: Não adicione a variável (banco persiste)

---

## 📝 Status Atual

**✅ CONFIGURAÇÃO ATUAL:** Banco é zerado a cada deploy  
**🎯 RECOMENDADO PARA:** Testes, demos, desenvolvimento  
**⚠️ NÃO RECOMENDADO PARA:** Produção com usuários reais  

**Para mudar:** Edite `build.sh` conforme instruções acima.

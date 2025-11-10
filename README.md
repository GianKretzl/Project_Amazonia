# Encruzilhada da Amazônia — Simulador de Investigação

Protótipo inicial do projeto descrito: backend em Flask + frontend leve (esqueleto com Excalibur.js) para uma sala de entrevistas com "personas" interdisciplinares.

Principais arquivos:
- `app.py` — servidor Flask, endpoints de API e lógica de pistas/desbloqueio.
- `entidades.py` — definição das personas (biólogo, fazendeiro, líder indígena, político) e pistas.
- `templates/` e `static/` — frontend mínimo e assets.

Como rodar (ambiente virtual recomendado):

1) Criar e ativar um virtualenv (opcional):

```bash
python -m venv venv
source venv/bin/activate
```

2) Instalar dependências:

```bash
pip install -r requirements.txt
```

3) Criar um arquivo `.env` (copiar de .env.example se houver) com pelo menos:

```
SECRET_KEY=algo-secreto
OPENAI_API_KEY=seu_api_key_aqui  # opcional; sem isso o protótipo usa respostas simuladas
```

4) Rodar o app:

```bash
python app.py
```

5) Abrir http://localhost:5000

Observações:
- O backend detecta palavras-chave nas respostas da IA e retorna pistas encontradas. O frontend permite "coletar" pistas para desbloquear novas entidades.
- Integração com OpenAI é opcional; se estiver disponível, será usada para gerar respostas mais ricas.
# Project_Amazonia
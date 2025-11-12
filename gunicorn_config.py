# Configuração do Gunicorn para produção
import os
import multiprocessing

# Servidor
bind = f"0.0.0.0:{os.getenv('PORT', '10000')}"

# Workers
workers = int(os.getenv('GUNICORN_WORKERS', '2'))
worker_class = 'gthread'
threads = int(os.getenv('GUNICORN_THREADS', '4'))

# Timeouts (aumentado para chamadas API externas)
timeout = 60  # Tempo máximo para processar request
graceful_timeout = 30  # Tempo para worker terminar gracefully
keepalive = 5  # Keep-alive connections

# Worker lifecycle
max_requests = 1000  # Restart worker após N requests (previne memory leak)
max_requests_jitter = 50  # Adiciona randomização
worker_tmp_dir = '/dev/shm'  # Usa RAM para worker heartbeat (mais rápido)

# Logging
accesslog = '-'  # STDOUT
errorlog = '-'   # STDERR
loglevel = 'info'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Performance
preload_app = True  # Carrega app antes de forkar workers (economiza memória)
worker_connections = 1000

# Segurança
limit_request_line = 4096
limit_request_fields = 100
limit_request_field_size = 8190

def on_starting(server):
    print("🚀 Gunicorn starting...")

def when_ready(server):
    print("✅ Gunicorn is ready. Accepting connections.")

def on_exit(server):
    print("👋 Gunicorn shutting down.")

def worker_int(worker):
    print(f"⚠️  Worker {worker.pid} received INT or QUIT signal")

def worker_abort(worker):
    print(f"🔴 Worker {worker.pid} received SIGABRT - timeout exceeded")

"""
Sistema de Banco de Dados para Project Amazonia
Persiste histórico de chat, pistas, enigmas e progresso do jogador
"""

import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Optional

class GameDatabase:
    def __init__(self, db_path='game_data.db'):
        self.db_path = db_path
        self.init_database()
    
    def get_connection(self):
        """Criar conexão com o banco de dados"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Retornar resultados como dicionários
        return conn
    
    def init_database(self):
        """Inicializar tabelas do banco de dados"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Tabela de usuários (para autenticação)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                grupo_nome TEXT NOT NULL,
                integrantes TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Tabela de jogadores/sessões
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT UNIQUE NOT NULL,
                user_id INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_activity TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES usuarios(id)
            )
        ''')
        
        # Tabela de histórico de chat
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                entity_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (session_id) REFERENCES players(session_id)
            )
        ''')
        
        # Índice para buscar chat por sessão e entidade
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_chat_session_entity 
            ON chat_history(session_id, entity_id)
        ''')
        
        # Tabela de pistas coletadas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pistas_coletadas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                pista TEXT NOT NULL,
                collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (session_id) REFERENCES players(session_id),
                UNIQUE(session_id, pista)
            )
        ''')
        
        # Tabela de enigmas resolvidos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS enigmas_resolvidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                enigma_id TEXT NOT NULL,
                resposta TEXT,
                acertou BOOLEAN NOT NULL,
                solved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (session_id) REFERENCES players(session_id),
                UNIQUE(session_id, enigma_id)
            )
        ''')
        
        # Tabela de interações por entidade
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS entity_interactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                entity_id TEXT NOT NULL,
                interaction_count INTEGER DEFAULT 0,
                last_interaction TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (session_id) REFERENCES players(session_id),
                UNIQUE(session_id, entity_id)
            )
        ''')
        
        # Tabela de contra-perguntas feitas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contra_perguntas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                entity_id TEXT NOT NULL,
                pergunta_tipo TEXT NOT NULL,
                resposta TEXT,
                asked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (session_id) REFERENCES players(session_id),
                UNIQUE(session_id, entity_id, pergunta_tipo)
            )
        ''')
        
        # Tabela de desafios completados
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS desafios_completados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                desafio_id TEXT NOT NULL,
                resposta_usuario TEXT,
                acertou BOOLEAN NOT NULL,
                completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (session_id) REFERENCES players(session_id),
                UNIQUE(session_id, desafio_id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    # ========== GERENCIAMENTO DE JOGADORES ==========
    
    def create_user(self, username: str, password_hash: str, grupo_nome: str, integrantes: list) -> Optional[int]:
        """Criar novo usuário e retornar ID"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            integrantes_json = json.dumps(integrantes)
            cursor.execute('''
                INSERT INTO usuarios (username, password_hash, grupo_nome, integrantes, created_at, last_login)
                VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
            ''', (username, password_hash, grupo_nome, integrantes_json))
            
            user_id = cursor.lastrowid
            conn.commit()
            conn.close()
            return user_id
        except sqlite3.IntegrityError:
            conn.close()
            return None  # Usuário já existe
    
    def authenticate_user(self, username: str, password_hash: str) -> Optional[Dict]:
        """Autenticar usuário e retornar dados"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, username, grupo_nome, integrantes, created_at
            FROM usuarios
            WHERE username = ? AND password_hash = ?
        ''', (username, password_hash))
        
        row = cursor.fetchone()
        
        if row:
            # Atualizar last_login
            cursor.execute('''
                UPDATE usuarios SET last_login = CURRENT_TIMESTAMP
                WHERE id = ?
            ''', (row['id'],))
            conn.commit()
            
            user_data = {
                'id': row['id'],
                'username': row['username'],
                'grupo': row['grupo_nome'],
                'integrantes': json.loads(row['integrantes']),
                'created_at': row['created_at']
            }
            conn.close()
            return user_data
        
        conn.close()
        return None
    
    def link_session_to_user(self, session_id: str, user_id: int):
        """Vincular sessão a um usuário"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Garantir que a sessão existe antes de atualizar
        cursor.execute('''
            INSERT OR IGNORE INTO players (session_id, user_id, created_at, last_activity)
            VALUES (?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
        ''', (session_id, user_id))
        
        # Atualizar user_id se a sessão já existia
        cursor.execute('''
            UPDATE players SET user_id = ?, last_activity = CURRENT_TIMESTAMP
            WHERE session_id = ?
        ''', (user_id, session_id))
        
        conn.commit()
        conn.close()
    
    def get_user_session(self, user_id: int) -> Optional[str]:
        """Buscar session_id mais recente de um usuário"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT session_id FROM players
            WHERE user_id = ?
            ORDER BY last_activity DESC
            LIMIT 1
        ''', (user_id,))
        
        row = cursor.fetchone()
        conn.close()
        
        return row['session_id'] if row else None
    
    def ensure_player(self, session_id: str, user_id: int = None):
        """Garantir que o jogador existe no banco"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR IGNORE INTO players (session_id, user_id, created_at, last_activity)
            VALUES (?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
        ''', (session_id, user_id))
        
        cursor.execute('''
            UPDATE players SET last_activity = CURRENT_TIMESTAMP
            WHERE session_id = ?
        ''', (session_id,))
        
        conn.commit()
        conn.close()
    
    # ========== HISTÓRICO DE CHAT ==========
    
    def save_chat_message(self, session_id: str, entity_id: str, role: str, content: str):
        """Salvar mensagem no histórico de chat"""
        self.ensure_player(session_id)
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO chat_history (session_id, entity_id, role, content)
            VALUES (?, ?, ?, ?)
        ''', (session_id, entity_id, role, content))
        
        conn.commit()
        conn.close()
    
    def get_chat_history(self, session_id: str, entity_id: str, limit: int = 10) -> List[Dict]:
        """Recuperar histórico de chat para uma entidade"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT role, content, timestamp
            FROM chat_history
            WHERE session_id = ? AND entity_id = ?
            ORDER BY timestamp DESC
            LIMIT ?
        ''', (session_id, entity_id, limit))
        
        rows = cursor.fetchall()
        conn.close()
        
        # Retornar em ordem cronológica (mais antiga primeiro)
        return [{'role': r['role'], 'content': r['content'], 'timestamp': r['timestamp']} 
                for r in reversed(rows)]
    
    def clear_chat_history(self, session_id: str, entity_id: str = None):
        """Limpar histórico de chat (opcional: apenas para uma entidade)"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        if entity_id:
            cursor.execute('DELETE FROM chat_history WHERE session_id = ? AND entity_id = ?', 
                         (session_id, entity_id))
        else:
            cursor.execute('DELETE FROM chat_history WHERE session_id = ?', (session_id,))
        
        conn.commit()
        conn.close()
    
    # ========== PISTAS COLETADAS ==========
    
    def add_pista(self, session_id: str, pista: str):
        """Adicionar pista coletada"""
        self.ensure_player(session_id)
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO pistas_coletadas (session_id, pista)
                VALUES (?, ?)
            ''', (session_id, pista))
            conn.commit()
        except sqlite3.IntegrityError:
            # Pista já existe
            pass
        
        conn.close()
    
    def get_pistas(self, session_id: str) -> List[str]:
        """Recuperar todas as pistas coletadas"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT pista FROM pistas_coletadas
            WHERE session_id = ?
            ORDER BY collected_at
        ''', (session_id,))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [r['pista'] for r in rows]
    
    # ========== ENIGMAS RESOLVIDOS ==========
    
    def save_enigma_result(self, session_id: str, enigma_id: str, resposta: str, acertou: bool):
        """Salvar resultado de enigma"""
        self.ensure_player(session_id)
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR REPLACE INTO enigmas_resolvidos 
            (session_id, enigma_id, resposta, acertou, solved_at)
            VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
        ''', (session_id, enigma_id, resposta, acertou))
        
        conn.commit()
        conn.close()
    
    def get_enigmas_resolvidos(self, session_id: str) -> List[str]:
        """Recuperar IDs dos enigmas resolvidos corretamente"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT enigma_id FROM enigmas_resolvidos
            WHERE session_id = ? AND acertou = 1
        ''', (session_id,))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [r['enigma_id'] for r in rows]
    
    # ========== INTERAÇÕES COM ENTIDADES ==========
    
    def increment_interaction(self, session_id: str, entity_id: str) -> int:
        """Incrementar contador de interações e retornar novo total"""
        self.ensure_player(session_id)
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Tentar inserir ou incrementar
        cursor.execute('''
            INSERT INTO entity_interactions (session_id, entity_id, interaction_count, last_interaction)
            VALUES (?, ?, 1, CURRENT_TIMESTAMP)
            ON CONFLICT(session_id, entity_id) 
            DO UPDATE SET 
                interaction_count = interaction_count + 1,
                last_interaction = CURRENT_TIMESTAMP
        ''', (session_id, entity_id))
        
        # Buscar o novo total
        cursor.execute('''
            SELECT interaction_count FROM entity_interactions
            WHERE session_id = ? AND entity_id = ?
        ''', (session_id, entity_id))
        
        row = cursor.fetchone()
        count = row['interaction_count'] if row else 0
        
        conn.commit()
        conn.close()
        
        return count
    
    def get_interaction_count(self, session_id: str, entity_id: str) -> int:
        """Obter número de interações com uma entidade"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT interaction_count FROM entity_interactions
            WHERE session_id = ? AND entity_id = ?
        ''', (session_id, entity_id))
        
        row = cursor.fetchone()
        conn.close()
        
        return row['interaction_count'] if row else 0
    
    # ========== CONTRA-PERGUNTAS ==========
    
    def save_contra_pergunta(self, session_id: str, entity_id: str, pergunta_tipo: str, resposta: str):
        """Salvar resposta de contra-pergunta"""
        self.ensure_player(session_id)
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR REPLACE INTO contra_perguntas 
            (session_id, entity_id, pergunta_tipo, resposta, asked_at)
            VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
        ''', (session_id, entity_id, pergunta_tipo, resposta))
        
        conn.commit()
        conn.close()
    
    def get_contra_pergunta_feita(self, session_id: str, entity_id: str, pergunta_tipo: str) -> Optional[str]:
        """Verificar se contra-pergunta já foi feita e retornar resposta"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT resposta FROM contra_perguntas
            WHERE session_id = ? AND entity_id = ? AND pergunta_tipo = ?
        ''', (session_id, entity_id, pergunta_tipo))
        
        row = cursor.fetchone()
        conn.close()
        
        return row['resposta'] if row else None
    
    # ========== DESAFIOS COMPLETADOS ==========
    
    def save_desafio_completado(self, session_id: str, desafio_id: str, resposta_usuario: str, acertou: bool):
        """Salvar desafio completado (correto ou incorreto)"""
        self.ensure_player(session_id)
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR REPLACE INTO desafios_completados 
            (session_id, desafio_id, resposta_usuario, acertou, completed_at)
            VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
        ''', (session_id, desafio_id, resposta_usuario, acertou))
        
        conn.commit()
        conn.close()
    
    def get_desafios_completados(self, session_id: str) -> List[str]:
        """Recuperar IDs dos desafios já completados (corretos ou incorretos)"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT desafio_id FROM desafios_completados
            WHERE session_id = ?
        ''', (session_id,))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [r['desafio_id'] for r in rows]
    
    def get_desafios_acertados(self, session_id: str) -> List[str]:
        """Recuperar IDs dos desafios acertados"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT desafio_id FROM desafios_completados
            WHERE session_id = ? AND acertou = 1
        ''', (session_id,))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [r['desafio_id'] for r in rows]
    
    def get_desafio_status(self, session_id: str, desafio_id: str) -> Optional[Dict]:
        """Verificar status de um desafio específico"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT desafio_id, resposta_usuario, acertou, completed_at
            FROM desafios_completados
            WHERE session_id = ? AND desafio_id = ?
        ''', (session_id, desafio_id))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {
                'desafio_id': row['desafio_id'],
                'resposta_usuario': row['resposta_usuario'],
                'acertou': bool(row['acertou']),
                'completed_at': row['completed_at']
            }
        return None
    
    # ========== LIMPEZA E RESET ==========
    
    def reset_player_progress(self, session_id: str):
        """Resetar todo o progresso de um jogador"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM chat_history WHERE session_id = ?', (session_id,))
        cursor.execute('DELETE FROM pistas_coletadas WHERE session_id = ?', (session_id,))
        cursor.execute('DELETE FROM enigmas_resolvidos WHERE session_id = ?', (session_id,))
        cursor.execute('DELETE FROM entity_interactions WHERE session_id = ?', (session_id,))
        cursor.execute('DELETE FROM contra_perguntas WHERE session_id = ?', (session_id,))
        cursor.execute('DELETE FROM desafios_completados WHERE session_id = ?', (session_id,))
        
        conn.commit()
        conn.close()
    
    def get_player_stats(self, session_id: str) -> Dict:
        """Obter estatísticas do jogador"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        stats = {
            'pistas_coletadas': len(self.get_pistas(session_id)),
            'enigmas_resolvidos': len(self.get_enigmas_resolvidos(session_id)),
            'total_mensagens': 0,
            'entidades_interagidas': []
        }
        
        # Total de mensagens
        cursor.execute('''
            SELECT COUNT(*) as total FROM chat_history WHERE session_id = ?
        ''', (session_id,))
        row = cursor.fetchone()
        stats['total_mensagens'] = row['total'] if row else 0
        
        # Entidades com as quais interagiu
        cursor.execute('''
            SELECT entity_id, interaction_count FROM entity_interactions
            WHERE session_id = ?
            ORDER BY interaction_count DESC
        ''', (session_id,))
        rows = cursor.fetchall()
        stats['entidades_interagidas'] = [
            {'entity_id': r['entity_id'], 'interactions': r['interaction_count']}
            for r in rows
        ]
        
        conn.close()
        return stats

# Instância global do banco de dados
db = GameDatabase()

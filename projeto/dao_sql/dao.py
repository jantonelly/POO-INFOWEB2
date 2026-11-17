import sqlite3
from abc import ABC, abstractmethod

class DAO:
    conn = None
    nome_bd="agenda.db"

    @classmethod
    def abrir(cls):
        cls.conn = sqlite3.connect(cls.nome_bd)
        cls.conn.execute("PRAGMA foreign_keys = ON")
 
    @classmethod
    def fechar(cls):
        cls.conn.close()
       
    @classmethod
    def execute(cls, sql, params = None):
        cursor = cls.conn.cursor()
        cursor.execute(sql, params or [])
        cls.conn.commit()
        return cursor

    @abstractmethod
    def inserir(self, obj):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def listar_id(self, id):
        pass

    @abstractmethod
    def atualizar(self, obj):
        pass

    @abstractmethod
    def excluir(self, id):
        pass
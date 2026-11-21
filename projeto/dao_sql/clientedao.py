from dao_sql.dao import DAO
from models.cliente import Cliente

class ClienteDAO(DAO):
    def inserir(self, obj):
        self.abrir()
        sql = '''
            INSERT INTO cliente (nome, email, fone, senha, foto)
            VALUES (?, ?, ?, ?, ?)
        '''
        self.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_senha(), obj.get_foto()))
        self.fechar()

    def listar(self):
        self.abrir()
        sql = '''
            SELECT id, nome, email, fone, senha, foto
            FROM cliente
        '''
        cursor = self.execute(sql)
        rows = cursor.fetchall()
        objs = [
            Cliente(id, nome, email, fone, senha, foto)
            for id, nome, email, fone, senha, foto in rows
        ]
        self.fechar()
        return objs

    def listar_id(self, id):
        self.abrir()
        sql = '''
            SELECT id, nome, email, fone, senha, foto
            FROM cliente
            WHERE id = ?
        '''
        cursor = self.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Cliente(*row) if row else None
        self.fechar()
        return obj

    def atualizar(self, obj):
        self.abrir()

        sql = '''
            UPDATE cliente
            SET nome=?, email=?, fone=?, senha=?, foto=?
            WHERE id=?
        '''

        self.execute(sql, (
            obj.get_nome(),
            obj.get_email(),
            obj.get_fone(),
            obj.get_senha(),
            obj.get_foto(),
            obj.get_id()
        ))

        self.fechar()
    # def atualizar(self, obj):
    #     self.abrir()
    #     sql = '''
    #         UPDATE cliente SET nome=?, email=?, fone=?, senha=?, foto=?
    #         WHERE id=?
    #     '''
    #     self.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_senha(), obj.get_id(), obj.get_foto()))
    #     self.fechar()

    # def excluir(self, id):
    #     self.abrir()
    #     sql = 'DELETE FROM cliente WHERE id=?'
    #     self.execute(sql, (id,))
    #     self.fechar()
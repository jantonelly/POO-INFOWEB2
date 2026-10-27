from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, nasc, fone):
        self.__nome = nome
        self.__cpf = cpf
        self.__nasc = nasc
        self.__fone = fone
    def __str__(self):
        return f"{self.__nome} - {self.__cpf} - {self.__nasc.strftime('%d/%m/%Y')} - {self.__fone}"
    def idade(self):
        x = datetime.now() - self.__nasc
        dias = x.days
        anos = dias // 365
        meses = dias % 356 // 30
        return f"{anos} ANO(S) E {meses} MES(ES)"
        
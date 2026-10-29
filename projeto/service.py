from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.servico import Servico
from models.servicodao import ServicoDAO
from models.horario import Horario
from models.horariosdao import HorariosDAO
from models.profissional import Profissional
from models.profissionaldao import ProfissionalDAO
from models.atendimento import Atendimento
from models.atendimentodao import AtendimentoDAO
from datetime import datetime, timedelta

class Service:
    #CLIENTE
    # @staticmethod
    # def cliente_inserir(nome, email, fone, senha):
    #     obj = Cliente(0, nome, email, fone, senha)
    #     ClienteDAO().inserir(obj)
    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        Service.validar_email_unico(email, "cliente")
        obj = Cliente(0, nome, email, fone, senha)
        ClienteDAO().inserir(obj)
    @staticmethod
    def cliente_listar():
        r = ClienteDAO().listar()
        r.sort(key = lambda obj : obj.get_nome().casefold())
        return r
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        Service.validar_email_unico(email, "cliente", id)
        obj = Cliente(id, nome, email, fone, senha)
        ClienteDAO().atualizar(obj)
    @staticmethod
    def cliente_excluir(id):
        horarios = Service.horario_listar_cliente(id)
        if len(horarios) > 0:
            raise ValueError("Não é possível excluir um cliente que possui horários agendados.")
    ClienteDAO().excluir(id)
    # @staticmethod
    # def cliente_atualizar(id, nome, email, fone, senha):
    #     obj = Cliente(id, nome, email, fone, senha)
    #     ClienteDAO().atualizar(obj)
    # @staticmethod
    # def cliente_excluir(id):
    #     ClienteDAO().excluir(id)
    @staticmethod
    def cliente_criar_admin():
        for c in Service.cliente_listar():
            if c.get_email() == "admin": return
        Service.cliente_inserir("admin", "admin", "fone", "1234")
    @staticmethod
    def cliente_autenticar(email, senha):
        for c in Service.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return{"id": c.get_id(), "nome": c.get_nome()}
        return None
    @staticmethod
    def horario_listar_cliente(id_cliente):
        r = []
        for h in Service.horario_listar():
            if h.get_id_cliente() == id_cliente:
                r.append(h)
        return r
    @staticmethod
    def cliente_alterar_senha(id, senha):
        cliente = Service.cliente_listar_id(id)
        if cliente != None:
            cliente.set_senha(senha)
            ClienteDAO().atualizar(cliente)

    #SERVIÇO
    @staticmethod
    def servico_inserir(descricao, valor):
        obj = Servico(0, descricao, valor)
        ServicoDAO().inserir(obj)
    @staticmethod
    def servico_listar():
        r = ServicoDAO().listar()
        r.sort(key = lambda obj : obj.get_descricao().casefold())
        return r
    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO().listar_id(id)
    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().atualizar(obj)
    @staticmethod
    def servico_excluir(id):
        ServicoDAO().excluir(id)

    #HORÁRIO
    # @staticmethod
    # def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
    #     obj = Horario(0, data)
    #     obj.set_confirmado(confirmado)
    #     obj.set_id_cliente(id_cliente)
    #     obj.set_id_servico(id_servico)
    #     obj.set_id_profissional(id_profissional)
    #     HorariosDAO().inserir(obj)
    @staticmethod
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        obj = Horario(0, data)
        Service.validar_horario_profissional( data, id_profissional)
        obj.set_confirmado(confirmado)
        obj.set_id_cliente(id_cliente)
        obj.set_id_servico(id_servico)
        obj.set_id_profissional(id_profissional)
        HorariosDAO().inserir(obj)
    @staticmethod
    def horario_listar():
        r = HorariosDAO().listar()
        r.sort(key = lambda obj : obj.get_data())
        return r
    @staticmethod
    def horario_listar_id(id):
          return HorariosDAO().listar_id(id)
    # @staticmethod
    # def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
    #     obj = Horario(id, data)
    #     obj.set_confirmado(confirmado)
    #     obj.set_id_cliente(id_cliente)
    #     obj.set_id_servico(id_servico)
    #     obj.set_id_profissional(id_profissional)
    #     HorariosDAO().atualizar(obj)
    @staticmethod
    def horario_atualizar(
        id, data, confirmado, id_cliente, id_servico,
        id_profissional):
        obj = Horario(id, data)
        Service.validar_horario_profissional(data, id_profissional, id)
        obj.set_confirmado(confirmado)
        obj.set_id_cliente(id_cliente)
        obj.set_id_servico(id_servico)
        obj.set_id_profissional(id_profissional)
        HorariosDAO().atualizar(obj)
    # @staticmethod
    # def horario_excluir(id):
    #     HorariosDAO().excluir(id)
    @staticmethod
    def horario_excluir(id):
        horario = Service.horario_listar_id(id)
        if horario is None:
            raise ValueError("Horário não encontrado.")
        if horario.get_id_cliente() not in (None, 0):
            raise ValueError(
                "Não é possível excluir um horário "
                "que já foi agendado por um cliente."
            )
        HorariosDAO().excluir(id)
    @staticmethod
    def horario_listar_disponiveis(id_profissional):
        r = []
        agora = datetime.now()
        for h in Service.horario_listar():
            if (h.get_data() >= agora and h.get_confirmado() == False \
                and h.get_id_cliente() == 0 and h.get_id_profissional() == id_profissional):
                r.append(h)
        r.sort(key=lambda h: h.get_data())
        return r
    @staticmethod
    def horario_visualizar_minha_agenda(id_profissional):
        r = []
        for h in Service.horario_listar():
            if h.get_id_profissional( ) == id_profissional:
                r.append(h)
            r.sort(key=lambda h: h.get_data())
            return r
    @staticmethod
    def horario_visualizar_meus_servicos(id_cliente):
        r = []
        for h in Service.horario_listar():
            if h.get_id_cliente( ) == id_cliente:
                r.append(h)
            r.sort(key=lambda h: h.get_data())
            return r
    @staticmethod
    def horario_abrir_agenda(data, hora_inicio, hora_fim, intervalo, id_profissional):
        data_inicio = datetime.strptime(data + " " + hora_inicio, "%d/%m/%Y %H:%M")
        data_fim = datetime.strptime (data + " " + hora_fim, "%d/%m/%Y %H:%M")
        delta = timedelta(minutes = intervalo)
        data = data_inicio
        while data <= data_fim:
            # INSERA UM HORÁRIO
            Service.horario_inserir(data, False, 0, 0, id_profissional)
            # E DEPOIS VAI PAR UM PRÓXIMO HORÁRIO
            data = data + delta
    @staticmethod
    def horario_confirmar(id):
        horario = Service.horario_listar_id(id)
        if horario != None:
            horario.set_confirmado(True)
            HorariosDAO().atualizar(horario)
    @staticmethod
    def horario_agendar(id, id_cliente, id_servico):
        horario = Service.horario_listar_id(id)
        if horario != None:
            horario.set_id_cliente(id_cliente)
            horario.set_id_servico(id_servico)
            HorariosDAO().atualizar(horario)

    #PROFISSIONAL
    @staticmethod
    def profissional_inserir(nome, email, especialidade, senha):
        Service.validar_email_unico(email, "profissional")
        obj = Profissional(0, nome, email, especialidade, senha)
        ProfissionalDAO().inserir(obj)
    # @staticmethod
    # def profissional_inserir(nome, email, especialidade, senha):
    #     obj = Profissional(0, nome, email, especialidade, senha)
    #     ProfissionalDAO().inserir(obj)
    @staticmethod
    def profissional_listar():
        r = ProfissionalDAO().listar()
        r.sort(key = lambda obj : obj.get_nome ().casefold())
        return r
    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO().listar_id(id)
    @staticmethod
    def profissional_atualizar(
        id, nome, email, especialidade, senha):
        Service.validar_email_unico(email, "profissional", id)
        obj = Profissional(id, nome, email, especialidade, senha)
        ProfissionalDAO().atualizar(obj)
    # @staticmethod
    # def profissional_atualizar(id, nome, email, especialidade, senha):
    #     obj = Profissional(id, nome, email, especialidade, senha)
    #     ProfissionalDAO().atualizar(obj)
    @staticmethod
    def profissional_excluir(id):
        horarios = Service.horario_listar_profissional(id)
        if len(horarios) > 0:
            raise ValueError("Não é possível excluir um profissional que possui horários cadastrados.")
        ProfissionalDAO().excluir(id)
    # @staticmethod
    # def profissional_excluir(id):
    #     ProfissionalDAO().excluir(id)
    @staticmethod
    def profissional_autenticar(email, senha):
        for c in Service.profissional_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None
    @staticmethod
    def horario_listar_profissional(id_profissional):
        r = []
        for h in Service.horario_listar():
            if h.get_id_profissional() == id_profissional:
                r.append(h)
        return r
    @staticmethod
    def profissional_alterar_senha(id, senha):
        profissional = Service.profissional_listar_id(id)
        if profissional != None:
            profissional.set_senha(senha)
            ProfissionalDAO().atualizar(profissional)
    @staticmethod
    def horario_confirmar_servico(id_profissional):
        r = []
        for h in Service.horario_listar():
            if h.get_confimado() == False and h.get_id_cliente() != None \
                and h.get_id_profissional() == 0 and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort(key=lambda h: h.get_data())
        return r
    
    #ATENDIMENTO
    @staticmethod
    def atendimento_inserir(data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
        obj = Atendimento(0, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
        AtendimentoDAO().inserir(obj)
    @staticmethod
    def atendimento_listar():
        return AtendimentoDAO().listar()
    @staticmethod
    def atendimento_listar_id(id):
        return AtendimentoDAO().listar_id(id)
    @staticmethod
    def atendimento_atualizar(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
        obj = Atendimento(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
        AtendimentoDAO().atualizar(obj)
    @staticmethod
    def atendimento_excluir(id):
        AtendimentoDAO().excluir(id) 

    #TOTALIZAR ATENDIMENTOS DOS PROFISSIONAIS
    @staticmethod
    def atendimento_totalizar_profissionais(data_inicial, data_final):
        profissionais = Service.profissional_listar()
        horarios = Service.horario_listar()
        resultado = []
        for profissional in profissionais:
            quantidade = 0
            for h in horarios:
                data_horario = h.get_data().date()
                if (
                    h.get_id_profissional() == profissional.get_id()
                    and h.get_confirmado() == True
                    and data_inicial <= data_horario <= data_final
                ):
                    quantidade = quantidade + 1
            resultado.append({
                "PROFISSIONAL": profissional.get_nome(),
                "ATENDIMENTOS CONFIRMADOS": quantidade
            })
        return resultado

    @staticmethod
    def validar_email_unico(email, tipo, id_atual=None):
        email = email.strip()
        if email.casefold() == "admin":
            raise ValueError("O e-mail 'admin' é reservado para o administrador.")
        for cliente in Service.cliente_listar():
            if (
                cliente.get_email().casefold() == email.casefold()
                and not (tipo == "cliente" and cliente.get_id() == id_atual)
            ):
                raise ValueError(
                    "Este e-mail já está cadastrado.")
        for profissional in Service.profissional_listar():
            if (
                profissional.get_email().casefold() == email.casefold()
                and not (tipo == "profissional" and profissional.get_id() == id_atual)
            ):
                raise ValueError("Este e-mail já está cadastrado.")

    @staticmethod
    def validar_horario_profissional(
        data, id_profissional, id_atual=None):
        if id_profissional in (None, 0):
            return
        for horario in Service.horario_listar():
            if (horario.get_id() != id_atual and horario.get_id_profissional() == id_profissional and horario.get_data() == data):
                raise ValueError("Este profissional já possui um horário cadastrado nessa data e hora.")
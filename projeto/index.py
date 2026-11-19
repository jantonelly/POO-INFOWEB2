from templates.manterclienteui import ManterClienteUI
from templates.manterservicoui import ManterServicoUI
from templates.manterhorarioui import ManterHorarioUI
from templates.manterprofissionalui import ManterProfissionalUI
from templates.manteratenimentoui import ManterAtendimentoUI
from templates.abrircontaui import AbrirContaUI
from templates.loginui import LoginUI
from templates.perfilclienteui import PerfilClienteUI
from templates.perfilprofissionalui import PerfilProfissionalUI
from templates.agendarservicoui import AgendarServicoUI
from templates.abrirminhaagendaui import AbrirMinhaAgendaUI
#from templates.visu import VisualizarAgendaUI
#from templates.visualizarservicosui import VisualizarServicosUI
from templates.confirmarservicoui import ConfirmarServicoUI
from templates.alterarsenhaui import AlterarSenhaUI
from templates.registraratendimentoui import RegistrarAtendimentoUI
from templates.pagaratendimentoui import PagarAtendimentoUI
#from templates.totalatendimentos import TotalAtendimentosUI
#from templates.listarhorariosconfirmadoshoje import ListarHorariosConfirmadosHojeUI
#from templates.listaragendaprofissional import ListarAgendaProfissionalUI
from templates.totalizarmeusatendimentosui import TotalizarMeusAtendimentosUI
from templates.minhaagendaui import MinhaAgendaUI
from templates.meusservicosui import MeusServicosUI
from templates.mostraragendasemanaui import MostrarAgendaSemanaUI
from templates.pesquisarservicoui import PesquisarServicoUI
from service import Service
import streamlit as st

class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("MENU", ['ENTRAR NO SISTEMA', 'ABRIR CONTA'])
        if op == "ENTRAR NO SISTEMA": LoginUI.main()
        if op == "ABRIR CONTA": AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("MENU", ['MEUS DADOS', 'AGENDAR SERVIÇO', 'MEUS SERVIÇOS', 'PAGAR ATENDIMENTO', "PESQUISAR SERVIÇOS"])
        if op == "MEUS DADOS": PerfilClienteUI.main()
        if op == "AGENDAR SERVIÇO": AgendarServicoUI.main()
        if op == "MEUS SERVIÇOS": MeusServicosUI.main()
        if op == "PAGAR ATENDIMENTO": PagarAtendimentoUI.main()
        if op == "PESQUISAR SERVIÇOS": PesquisarServicoUI.main()

    def menu_profissional():
        op = st.sidebar.selectbox("MENU", ["MEUS DADOS", "ABRIR MINHA AGENDA", "MINHA AGENDA", "CONFIRMAR SERVIÇO", "REGISTRAR ATENDIMENTOS", "TOTALIZAR MEUS ATENDIMENTOS"])
        if op == "MEUS DADOS": PerfilProfissionalUI.main()
        if op == "ABRIR MINHA AGENDA": AbrirMinhaAgendaUI.main()
        if op == "MINHA AGENDA": MinhaAgendaUI.main()
        if op == "CONFIRMAR SERVIÇO": ConfirmarServicoUI.main()
        if op == "REGISTRAR ATENDIMENTO": RegistrarAtendimentoUI.main()
        if op == "TOTALIZAR MEUS ATENDIMENTOS": TotalizarMeusAtendimentosUI.main()

    def menu_admin():
        Service.cliente_criar_admin()
        op = st.sidebar.selectbox("MENU", ['CLIENTES', 'SERVIÇOS', 'HORÁRIOS', "PROFISSIONAIS", "ATENDIMENTOS", "ALTERAR SENHA", "TOTALIZAR ATENDIMENTOS", "AGENDA DA SEMANA"])
        if op  == "CLIENTES": ManterClienteUI.main()
        if op  == "SERVIÇOS": ManterServicoUI.main()
        if op  == "HORÁRIOS": ManterHorarioUI.main()
        if op  == "PROFISSIONAIS": ManterProfissionalUI.main()
        if op  == "ATENDIMENTOS": ManterAtendimentoUI.main()
        if op  == "ALTERAR SENHA": AlterarSenhaUI.main()
        if op == "TOTALIZAR ATENDIMENTOS": TotalizarMeusAtendimentosUI.main()
        if op == "AGENDA DA SEMANA": MostrarAgendaSemanaUI.main()

    def sair_do_sistema():
        if st.sidebar.button("SAIR"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("BEM-VINDO(A), " + st.session_state["usuario_nome"])
            if admin: IndexUI.menu_admin()
            else:
                if st.session_state["usuario_tipo"] == "cliente": IndexUI.menu_cliente()
                else: IndexUI.menu_profissional()
            IndexUI.sair_do_sistema()

    def main():
        # verifica a existe o usuário admin
        Service.cliente_criar_admin()
        # monta o sidebar
        IndexUI.sidebar()
        
IndexUI.main()
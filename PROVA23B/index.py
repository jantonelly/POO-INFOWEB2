from templates.manterclienteui import ManterClienteUI
from templates.manterservicoui import ManterServicoUI
from templates.manterprofissionalui import ManterProfissionalUI
from templates.manterhorarioui import ManterHorarioUI
from templates.listaagendaclienteui import ListarAgendaClienteUI
from templates.listarhorariosnaoconfirmadoshojeui import ListarHorariosNaoConfirmadosHojeUI
from service import Service
import streamlit as st

class IndexUI:
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços", "Horários", "Profissionais", "Horários não confimados", "Agenda do Cliente"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == "Horários": ManterHorarioUI.main()
        if op == "Profissionais": ManterProfissionalUI.main()
        if op == "Agenda do Cliente": ListarAgendaClienteUI.main()
        if op == "Horários Não Confimados Hoje": ListarHorariosNaoConfirmadosHojeUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
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
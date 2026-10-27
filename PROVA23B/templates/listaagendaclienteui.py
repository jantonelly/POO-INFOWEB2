
import streamlit as st
import pandas as pd
from service import Service

class ListarAgendaClienteUI:
    def main():
        st.header("Listar Agenda do Cliente")
        clientes = Service.cliente_listar()
        if not clientes:
            st.write("Nenhum cliente cadastrado.")
            return
        cliente_selecionado = st.selectbox(
            "Selecione o cliente:", clientes,
            format_func=lambda cliente: cliente.get_nome(),key="cliente_agenda_admin")
        if cliente_selecionado is None:
            return
        horarios = Service.horario_listar_agenda_cliente(cliente_selecionado.get_id())
        if not horarios:
            st.write("Este cliente não possui horários cadastrados.")
            return
        dados = []
        for horario in horarios:
            dados.append({
                "Data": horario["data"].strftime("%d/%m/%Y"),
                "Hora": horario["data"].strftime("%H:%M"),
                "Profissional": horario["profissional"],
                "Serviço": horario["servico"]
            })
        st.dataframe(
            pd.DataFrame(dados),
            hide_index=True, use_container_width=True)
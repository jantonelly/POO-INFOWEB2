import streamlit as st
from service import Service
from datetime import datetime
import time

class AbrirMinhaAgendaUI:
    def main():
        st.header("ABRIR MINHA AGENDA")
        data = st.text_input("Informe a data no formato dd/mm/aaaa", datetime.now().strftime("%d/%m/%Y"))
        hora_inicio = st.text_input("Informe o horário inicial no formato HH:MM")
        hora_fim = st.text_input("Informe o horário final no formato HH:MM")
        intervalo = st.text_input("Informe o intervalo entre os horários (min)")
        if st.button("Abrir Agenda"):
            try:
                if not intervalo.strip():
                    raise ValueError("Informe o intervalo entre os horários.")
                intervalo_minutos = int(intervalo)
                if intervalo_minutos <= 0:
                    raise ValueError("O intervalo deve ser maior que zero.")
                Service.horario_abrir_agenda(
                    data,
                    hora_inicio,
                    hora_fim,
                    intervalo_minutos,
                    st.session_state["usuario_id"])
                st.success("Horários cadastrados com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))
import streamlit as st
from paciente import Paciente 
from datetime import date, datetime

class PacienteUI:
    def main():
            st.header("DADOS DO PACIENTE")
            nome = st.text_input("INFORME O NOME")
            cpf = st.text_input("INFORME O CPF")
            nasc = st.date_input("INFORME A DATA DE NASCIMENTO", min_value=date(1990, 1,1), max_value=date.today(), value=date(2000, 1, 1), format=('DD/MM/YYYY'))
            nasc = datetime.combine(nasc, datetime.min.time())
            fone = st.text_input("INFORME O TELEFONE")
            if st.button("IDADE"):
                x = Paciente(nome, cpf, nasc, fone)
                st.wrire(x.idade())
                
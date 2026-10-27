
import streamlit as st
import pandas as pd
from service import Service

class ListarHorariosNaoConfirmadosHojeUI:
    def main():
        st.header("Horários não confimados hoje")
        horarios = Service.horario_listar_nao_confirmados_hoje()
        if not horarios:
            st.write("Nenhum horário não confirmado para hoje.")
            return
        dados = []
        for horario in horarios:
            dados.append({
                "Data": horario["data"].strftime("%d/%m/%Y"),
                "Hora": horario["data"].strftime("%H:%M"),
                "Cliente": horario["cliente"],
                "Serviço": horario["servico"],
                "Profissional": horario["profissional"]
            })
        st.dataframe(
            pd.DataFrame(dados),
            hide_index=True,
            use_container_width=True )

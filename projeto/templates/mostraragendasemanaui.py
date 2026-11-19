
import streamlit as st
import pandas as pd
from service import Service

class MostrarAgendaSemanaUI:
    def main():
        st.header("AGENDA DA SEMANA")
        horarios = Service.horario_agenda_semana()
        if len(horarios) == 0:
            st.info("Não existem horários agendados para esta semana.")
        else:
            df = pd.DataFrame(horarios)
            st.subheader("Próximos sete dias")
            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )
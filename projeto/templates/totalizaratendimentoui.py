
import streamlit as st
import pandas as pd
from datetime import date
from service import Service

class TotalizarAtendimentosUI:
    def main():
        st.header("TOTALIZAR ATENDIMENTOS DOS PROFISSIONAIS")
        data_inicial = st.date_input(
            "INFORME A DATA INICIAL",value=date.today())
        data_final = st.date_input(
            "INFORME A DATA FINAL",value=date.today())
        if st.button("TOTALIZAR"):
            if data_inicial > data_final:
                st.warning("A data inicial não pode ser posterior à final.")
            else:
                resultado = Service.atendimento_totalizar_profissionais(
                    data_inicial,
                    data_final)
                df = pd.DataFrame(resultado)
                st.subheader("Resultado dos atendimentos")
                st.dataframe(df, use_container_width=True)
                if len(df) > 0:
                    st.subheader("Gráfico de atendimentos")
                    st.bar_chart(df,x="PROFISSIONAL",y="TOTAL DE ATENDIMENTOS")

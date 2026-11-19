import streamlit as st
import pandas as pd
from datetime import date
from service import Service

class TotalizarMeusAtendimentosUI:
    def main():
        st.header("TOTALIZAR MEUS ATENDIMENTOS")
        data_inicial = st.date_input(
            "DATA INICIAL",
            value=date.today())
        data_final = st.date_input(
            "DATA FINAL",
            value=date.today())
        if st.button("TOTALIZAR"):
            if data_inicial > data_final:
                st.warning("Data inicial inválida.")
            else:
                resultado = Service.atendimento_totalizar_meus_servicos(
                    st.session_state["usuario_id"],data_inicial,data_final)
                if len(resultado) == 0:
                    st.info("Nenhum atendimento encontrado nesse período.")
                else:
                    df = pd.DataFrame(resultado)
                    st.subheader("Atendimentos realizados")
                    st.dataframe(df, use_container_width=True)
                    st.subheader("Gráfico de atendimentos")
                    st.bar_chart(
                        df,x="SERVIÇO",y="QUANTIDADE")
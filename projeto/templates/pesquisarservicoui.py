import streamlit as st
import pandas as pd
from service import Service

class PesquisarServicoUI:
    def main():
        st.header("PESQUISAR SERVIÇOS")
        servicos = Service.servico_listar()
        pesquisa = st.text_input("Digite o nome do serviço")
        encontrados = []
        for servico in servicos:
            if pesquisa.casefold() in servico.get_descricao().casefold():
                encontrados.append({
                    "SERVIÇO": servico.get_descricao(),
                    "VALOR": servico.get_valor()
                })
        if encontrados:
            df = pd.DataFrame(encontrados)
            st.dataframe(df, use_container_width=True)

        elif pesquisa:
            st.warning("Nenhum serviço encontrado.")

        else:
            st.info("Digite o nome de um serviço para pesquisar.")

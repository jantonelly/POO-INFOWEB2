
import streamlit as st
import pandas as pd
import time
from service import Service

class ManterProfissionalUI:
    def main():
        st.header("CADASTRO DE PROFISSIONAIS")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["LISTAR", "INSERIR", "ATUALIZAR", "EXCLUIR"])
        with tab1:ManterProfissionalUI.listar()
        with tab2:ManterProfissionalUI.inserir()
        with tab3:ManterProfissionalUI.atualizar()
        with tab4:ManterProfissionalUI.excluir()

    def listar():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0:
            st.write("NENHUM PROFISSIONAL CADASTRADO")
        else:
            list_dic = []
            for obj in profissionais:
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():#
        nome = st.text_input("INFORME O NOME")
        email = st.text_input("INFORME O E-MAIL")
        especialidade = st.text_input("INFORME A ESPECIALIDADE")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("INSERIR"):
            try:
                Service.profissional_inserir(nome, email, especialidade, senha)
                st.success("PROFISSIONAL INSERIDO COM SUCESSO")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))

    def atualizar():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0:
            st.write("NENHUM PROFISSIONAL CADASTRADO")
        else:
            op = st.selectbox(
                "ATUALIZAÇÃO DE PROFISSIONAL",
                profissionais)
            nome = st.text_input(
                "NOVO NOME",
                op.get_nome())
            email = st.text_input(
                "NOVO E-MAIL",
                op.get_email())
            especialidade = st.text_input(
                "NOVA ESPECIALIDADE",
                op.get_especialidade())
            senha = st.text_input("Nova senha", op.get_senha(), type="password")
            if st.button("ATUALIZAR"):
                id = op.get_id()
                Service.profissional_atualizar(
                    id,
                    nome,
                    email,
                    especialidade,
                    senha
                    )
                st.success("PROFISSIONAL CADASTRADO COM SUCESSO")
                st.rerun()

    def excluir():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0:
            st.write("NENHUM PROFISSIONAL CADASTRADO")
        else:
            op = st.selectbox(
                "EXCLUSÃO DE PROFISSIONAIS",
                profissionais
            )
            if st.button("EXCLUIR"):
                id = op.get_id()
                Service.profissional_excluir(id)
                st.success("PROFISSIONAL EXCLUÍDO COM SUCESSO")
                st.rerun()

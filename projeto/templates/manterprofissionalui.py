import streamlit as st
import pandas as pd
import time
from service import Service

class ManterProfissionalUI:
    def main():
        st.header("CADASTRO DE PROFISSIONAIS")

        tab1, tab2, tab3, tab4 = st.tabs([
            "LISTAR", "INSERIR", "ATUALIZAR", "EXCLUIR"
        ])

        with tab1:
            ManterProfissionalUI.listar()

        with tab2:
            ManterProfissionalUI.inserir()

        with tab3:
            ManterProfissionalUI.atualizar()

        with tab4:
            ManterProfissionalUI.excluir()

    def listar():
        profissionais = Service.profissional_listar()

        if len(profissionais) == 0:
            st.write("NENHUM PROFISSIONAL CADASTRADO")
        else:
            dados = []

            for obj in profissionais:
                dados.append({
                    "ID": obj.get_id(),
                    "NOME": obj.get_nome(),
                    "E-MAIL": obj.get_email(),
                    "ESPECIALIDADE": obj.get_especialidade()
                })

            st.dataframe(pd.DataFrame(dados))

    def inserir():
        nome = st.text_input("INFORME O NOME")
        email = st.text_input("INFORME O E-MAIL")
        especialidade = st.text_input("INFORME A ESPECIALIDADE")
        senha = st.text_input("INFORME A SENHA", type="password")

        foto = st.file_uploader(
            "ESCOLHA A FOTO DO PROFISSIONAL",
            type=["jpg", "jpeg", "png"],
            key="foto_profissional_novo"
        )

        if foto:
            st.image(foto, width=150)

        if st.button("INSERIR"):
            try:
                imagem = foto.getvalue() if foto else None

                Service.profissional_inserir(
                    nome, email, especialidade, senha, imagem
                )

                st.success("PROFISSIONAL INSERIDO COM SUCESSO")
                time.sleep(2)
                st.rerun()

            except ValueError as erro:
                st.error(str(erro))

    def atualizar():
        profissionais = Service.profissional_listar()

        if len(profissionais) == 0:
            st.write("NENHUM PROFISSIONAL CADASTRADO")
            return

        op = st.selectbox(
            "ATUALIZAÇÃO DE PROFISSIONAL",
            profissionais
        )

        nome = st.text_input("NOVO NOME", op.get_nome())
        email = st.text_input("NOVO E-MAIL", op.get_email())
        especialidade = st.text_input(
            "NOVA ESPECIALIDADE", op.get_especialidade()
        )
        senha = st.text_input(
            "NOVA SENHA", op.get_senha(), type="password"
        )

        foto = st.file_uploader(
            "ESCOLHA UMA NOVA FOTO",
            type=["jpg", "jpeg", "png"],
            key="foto_profissional_atualizar"
        )

        if foto:
            st.image(foto, width=150)
        elif op.get_foto():
            st.image(op.get_foto(), width=150)

        if st.button("ATUALIZAR"):
            try:
                imagem = foto.getvalue() if foto else None

                Service.profissional_atualizar(
                    op.get_id(),
                    nome,
                    email,
                    especialidade,
                    senha,
                    imagem
                )

                st.success("PROFISSIONAL ATUALIZADO COM SUCESSO")
                time.sleep(2)
                st.rerun()

            except ValueError as erro:
                st.error(str(erro))

    def excluir():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0:
            st.write("NENHUM PROFISSIONAL CADASTRADO")
            return
        op = st.selectbox(
            "EXCLUSÃO DE PROFISSIONAIS",
            profissionais
        )
        if st.button("EXCLUIR"):
            try:
                Service.profissional_excluir(op.get_id())

                st.success("PROFISSIONAL EXCLUÍDO COM SUCESSO")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))
import streamlit as st
import pandas as pd
import time
from service import Service

class ManterClienteUI:
    def main():
        st.header("CADASTRO DE CLIENTES")
        tab1, tab2, tab3, tab4 = st.tabs(["LISTAR", "INSERIR","ATUALIZAR", "EXCLUIR"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()
    def listar():
        clientes = Service.cliente_listar()
        if len(clientes) == 0: st.write("NENHUM CLIENTE CADASTRADO")
        else: 
            list_dic = [] 
            for obj in clientes: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        nome = st.text_input("INFORME O NOME")
        email = st.text_input("INFORME O E-MAIL")
        fone = st.text_input("INFORM O TELEFONE")
        senha = st.text_input("INFORME A SENHA", type="password")
        if st.button("INSERIR"):
            try:
                Service.cliente_inserir(nome, email, fone, senha)
                st.success("CLIENTE INSERIDO COM SUCESSO")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))
    def atualizar():
        clientes = Service.cliente_listar()
        if len(clientes) == 0: st.write("NENHUM CLIENTE CADASTRADO")
        else:
            op = st.selectbox("ATUALIZAÇÃO DE CLIENTE", clientes)
            nome = st.text_input("NOVO NOME", op.get_nome())
            email = st.text_input("NOVO E-MAIL", op.get_email())
            fone = st.text_input("NOVO TELEFONE", op.get_fone())
            senha = st.text_input("NOVA SENHA", op.get_senha(), type="password")
            if st.button("ATUALIZAR"):
                try:
                    Service.cliente_atualizar(id, nome, email, fone, senha)
                    st.success("CLIENTE ATUALIZADO COM SUCESSO")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(str(erro))
    def excluir():
        clientes = Service.cliente_listar()
        if len(clientes) == 0: st.write("NENHUM CLIENTE CADASTRADO")
        else:
            op = st.selectbox("EXCLUSÃO DE CLIENTES", clientes)
            if st.button("INSERIR"):
                try:
                    Service.cliente_excluir(id)
                    st.success("CLIENTE EXCLUIDO COM SUCESSO")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(str(erro))
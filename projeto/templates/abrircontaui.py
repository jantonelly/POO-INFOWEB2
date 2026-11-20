import streamlit as st
from service import Service
import time

class AbrirContaUI:
    def main():
        st.header("ABRIR CONTA NO SISTEMA")
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")
        foto = st.file_uploader("Escolha sua foto de perfil",type=["jpg", "jpeg", "png"])
        if foto is not None:
            st.image(foto, width=150)
        if st.button("Inserir"):
            try:
                imagem = foto.getvalue() if foto else None
                Service.cliente_inserir(nome, email, fone, senha, imagem)
                st.success("Conta criada com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))
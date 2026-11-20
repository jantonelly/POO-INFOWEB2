
import streamlit as st
from service import Service
import time

class PerfilProfissionalUI:

    def main():
        st.header("MEUS DADOS")

        id = st.session_state["usuario_id"]

        op = Service.profissional_listar_id(id)

        if op is None:
            st.error("Profissional não encontrado.")
            return

        st.subheader("Minha foto de perfil")

        if op.get_foto():
            st.image(op.get_foto(), width=180)
        else:
            st.info("Você ainda não possui uma foto.")

        nova_foto = st.file_uploader(
            "Escolha uma nova foto",
            type=["jpg", "jpeg", "png"],
            key="foto_perfil_profissional"
        )

        if nova_foto:
            st.image(nova_foto, width=180)

        if st.button("ALTERAR FOTO"):
            try:
                if nova_foto is None:
                    st.warning("Escolha uma foto primeiro.")
                else:
                    Service.profissional_atualizar_foto(
                        id, nova_foto.getvalue()
                    )

                    st.success("Foto alterada com sucesso!")
                    time.sleep(2)
                    st.rerun()

            except ValueError as erro:
                st.error(str(erro))

        st.divider()

        st.subheader("Dados profissionais")

        nome = st.text_input("Nome", op.get_nome())
        email = st.text_input("E-mail", op.get_email())

        especialidade = st.text_input(
            "Especialidade", op.get_especialidade()
        )

        senha = st.text_input(
            "Senha", op.get_senha(), type="password"
        )

        if st.button("ATUALIZAR DADOS"):
            try:
                Service.profissional_atualizar(
                    id, nome, email, especialidade, senha
                )

                st.success("Dados atualizados com sucesso!")
                time.sleep(2)
                st.rerun()

            except ValueError as erro:
                st.error(str(erro))

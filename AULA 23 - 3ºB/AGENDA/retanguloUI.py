import streamlit as st
from retangulo import Retangulo

class RetanguloUI:
    def main():
        st.header("CÁLCULOS COM RETÂNGULOS")
        b = st.text_input("INFORME A BASE")
        h = st.text_input("INFORME A ALTURA")
        if st.button("CALCULAR"):
            r = Retangulo(float(b), float(h))
            st.whire(f"ÁREA = {r.calc_area()}")
            st.whire(f"DIAGONAL = {r.calc_diagonal()}")
            st.write(r)

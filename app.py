import streamlit as st

def procesar_bloqueador(texto):
    # Elimina [R1] y agrega %11 luego de [Si]
    texto = texto.replace('[R1]', '')
    texto = texto.replace('[Si]', '[Si]%11')
    return texto

def procesar_puente(texto):
    # Elimina [A], reemplaza ([R1]) por %10, agrega %11 luego de N1
    texto = texto.replace('[A]', '')
    texto = texto.replace('([R1])', '%10')
    texto = texto.replace('N1', 'N1%11')
    return texto

def procesar_direccionador(texto):
    # Elimina [A] y agrega %10 después de la primera letra
    texto = texto.replace('[A]', '')
    if texto:
        texto = texto[0] + '%10' + texto[1:]
    return texto

def main():
    st.title('COMBIMOL')

    st.write("Creador de molécula a partir de fragmentos.")
    
    st.subheader('Ingrese los grupos a procesar:')
    grupo_bloqueador = st.text_input('Grupo Bloqueador', "[R1][Si](C1=CC=CC=C1)(C2=CC=CC=C2)C(C)(C)C")
    grupo_puente = st.text_input('Grupo Puente', "[A]N1C2=CC=CC(I)=C2C(C[C@@]3([H])N([R1])CC(C=C3)=O)=C1")
    grupo_direccionador = st.text_input('Grupo Direccionador', "[A]C(OCC(Cl)(Cl)Cl)=O")

    if st.button('Procesar'):
        bloqueador_procesado = procesar_bloqueador(grupo_bloqueador)
        puente_procesado = procesar_puente(grupo_puente)
        direccionador_procesado = procesar_direccionador(grupo_direccionador)

        resultado_final = f"{bloqueador_procesado}.{puente_procesado}.{direccionador_procesado}"

        st.subheader('Resultado Final:')
        st.code(resultado_final, language='text')

if __name__ == "__main__":
    main()

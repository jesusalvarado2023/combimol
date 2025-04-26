import streamlit as st

def procesar_grupo_bloqueador(texto):
    texto = texto.replace('[R1]', '')  # Eliminar [R1]
    texto = texto.replace('[Si]', '[Si]%11')  # Agregar %11 después de [Si]
    return texto

def procesar_grupo_puente(texto):
    texto = texto.replace('[A]', '')  # Eliminar [A]
    texto = texto.replace('N1', 'N1%11')  # Agregar %11 después de N1
    texto = texto.replace('([R1])', '%10')  # Reemplazar ([R1]) por %10
    return texto

def procesar_grupo_direccionador(texto):
    texto = texto.replace('[A]', '')  # Eliminar [A]
    texto = texto.replace('C(', 'C%10(')  # Agregar %10 después de la letra C y antes del paréntesis
    return texto

def main():
    st.title('Generador de Cadena de Grupos Modificados')

    st.header('Ingrese los datos:')
    grupo_bloqueador = st.text_input('Grupo Bloqueador:')
    grupo_puente = st.text_input('Grupo Puente:')
    grupo_direccionador = st.text_input('Grupo Direccionador:')

    if st.button('Procesar'):
        if grupo_bloqueador and grupo_puente and grupo_direccionador:
            bloqueador_mod = procesar_grupo_bloqueador(grupo_bloqueador)
            puente_mod = procesar_grupo_puente(grupo_puente)
            direccionador_mod = procesar_grupo_direccionador(grupo_direccionador)

            resultado_final = f"{bloqueador_mod}.{puente_mod}.{direccionador_mod}"

            st.subheader('Resultado:')
            st.code(resultado_final, language='text')
        else:
            st.warning('Por favor, complete los tres campos.')

if __name__ == '__main__':
    main()

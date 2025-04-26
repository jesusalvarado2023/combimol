import streamlit as st
import pandas as pd
from rdkit import Chem
from rdkit.Chem import rdChemReactions

# Función para combinar los SMILES
def combinar_smiles(grupo_A, grupo_B, grupo_R):
    combinaciones = []
    for a in grupo_A:
        for b in grupo_B:
            for r in grupo_R:
                smiles_combinado = a + b + r
                combinaciones.append(smiles_combinado)
    return combinaciones

# Interfaz de usuario con Streamlit
st.title("Combinador de Moléculas SMILES")

st.header("Cargar archivos CSV")
archivo_A = st.file_uploader("Carga el grupo A (CSV con columna 'SMILES')", type="csv")
archivo_B = st.file_uploader("Carga el grupo B (CSV con columna 'SMILES')", type="csv")
archivo_R = st.file_uploader("Carga el grupo R (CSV con columna 'SMILES')", type="csv")

if archivo_A and archivo_B and archivo_R:
    df_A = pd.read_csv(archivo_A)
    df_B = pd.read_csv(archivo_B)
    df_R = pd.read_csv(archivo_R)
    
    if "SMILES" not in df_A.columns or "SMILES" not in df_B.columns or "SMILES" not in df_R.columns:
        st.error("Los archivos deben contener una columna llamada 'SMILES'")
    else:
        smiles_A = df_A["SMILES"].dropna().tolist()
        smiles_B = df_B["SMILES"].dropna().tolist()
        smiles_R = df_R["SMILES"].dropna().tolist()
        
        # Combinación de los fragmentos
        smiles_combinados = combinar_smiles(smiles_A, smiles_B, smiles_R)
        
        # Crear DataFrame con los resultados
        df_resultado = pd.DataFrame({"SMILES Combinados": smiles_combinados})
        st.success(f"Se generaron {len(smiles_combinados)} combinaciones")
        
        # Mostrar tabla
        st.dataframe(df_resultado.head(10))
        
        # Botón para descargar
        csv = df_resultado.to_csv(index=False).encode('utf-8')
        st.download_button("Descargar CSV", csv, "combinaciones_smiles.csv", "text/csv")

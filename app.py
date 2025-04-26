import streamlit as st
import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem

def unir_fragmentos(grupo_bloqueador, grupo_puente, grupo_direccionador):
    # Eliminar los marcadores [R1] y [A] antes de unir
    bloqueador_limpio = grupo_bloqueador.replace("[R1]", "")
    puente_limpio = grupo_puente.replace("[R1]", "").replace("[A]", "")
    direccionador_limpio = grupo_direccionador.replace("[A]", "")

    # Concatenar los fragmentos usando puntos
    smiles_resultante = f"{bloqueador_limpio}.{puente_limpio}.{direccionador_limpio}"
    return smiles_resultante

def main():
    st.title("Generador de SMILES a partir de fragmentos")

    st.header("Entradas de fragmentos")
    grupo_bloqueador = st.text_input("Grupo Bloqueador", "[R1][Si](C1=CC=CC=C1)(C2=CC=CC=C2)C(C)(C)C")
    grupo_puente = st.text_input("Grupo Puente", "[A]N1C2=CC=CC(I)=C2C(C[C@@]3([H])N([R1])CC(C=C3)=O)=C1")
    grupo_direccionador = st.text_input("Grupo Direccionador", "[A]C(OCC(Cl)(Cl)Cl)=O")

    if st.button("Generar SMILES"):
        smiles_resultante = unir_fragmentos(grupo_bloqueador, grupo_puente, grupo_direccionador)
        st.success(f"SMILES Resultante:\n{smiles_resultante}")
        
        try:
            # Mostrar la molécula (puede ser varias moléculas separadas por '.')
            mol = Chem.MolFromSmiles(smiles_resultante)
            mol = Chem.AddHs(mol)
            AllChem.EmbedMolecule(mol, AllChem.ETKDG())
            st.subheader("Estructura Molecular")
            show_mol(mol, width=500, height=500)
        except Exception as e:
            st.error(f"No se pudo renderizar la molécula: {e}")

if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
from stmol import show_mol, render_mol

def unir_fragmentos(grupo_bloqueador, grupo_puente, grupo_direccionador):
    # Remplazar los puntos de unión [R1] y [A]
    grupo_puente_actualizado = grupo_puente.replace("[R1]", grupo_bloqueador)
    molecula_intermedia = grupo_puente_actualizado.replace("[A]", grupo_direccionador)
    return molecula_intermedia

def main():
    st.title("Generador de moléculas SMILES a partir de fragmentos")
    
    st.header("Entradas de fragmentos")
    grupo_bloqueador = st.text_input("Grupo Bloqueador", "[R1][Si](C1=CC=CC=C1)(C2=CC=CC=C2)C(C)(C)C")
    grupo_puente = st.text_input("Grupo Puente", "[A]N1C2=CC=CC(I)=C2C(C[C@@]3([H])N([R1])CC(C=C3)=O)=C1")
    grupo_direccionador = st.text_input("Grupo Direccionador", "[A]C(OCC(Cl)(Cl)Cl)=O")
    
    if st.button("Generar SMILES"):
        smiles_resultante = unir_fragmentos(grupo_bloqueador, grupo_puente, grupo_direccionador)
        st.success(f"SMILES Resultante:\n{smiles_resultante}")
        
        try:
            # Mostrar la molécula
            mol = Chem.MolFromSmiles(smiles_resultante)
            mol = Chem.AddHs(mol)
            AllChem.EmbedMolecule(mol, AllChem.ETKDG())
            st.subheader("Estructura Molecular")
            show_mol(mol, width=500, height=500)
        except Exception as e:
            st.error(f"No se pudo renderizar la molécula: {e}")

if __name__ == "__main__":
    main()

# app.py
import pandas as pd
import streamlit as st

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("resultado_sequencias.csv", sep=";")

df = load_data()

# Title and description
st.title("🧬 Soltu–PGSC Gene ID Converter")
st.write("Ingresá un ID de gen y obtené su correspondencia entre las nomenclaturas **Soltu** y **PGSC** junto con el valor E.")

# Initialize session state
if "last_query_type" not in st.session_state:
    st.session_state.last_query_type = "Buscar por Soltu ID"
if "input_value" not in st.session_state:
    st.session_state.input_value = ""

# Selection: query type
query_type = st.radio("Seleccioná el tipo de búsqueda:", ["Buscar por Soltu ID", "Buscar por PGSC ID"])

# Clear input when query type changes
if query_type != st.session_state.last_query_type:
    st.session_state.input_value = ""
    st.session_state.last_query_type = query_type

# Input
user_input = st.text_input("Ingresá el ID:", value=st.session_state.input_value, key="input_value")

# Process
if user_input:
    if query_type == "Buscar por Soltu ID":
        match = df[df['soltu_id'] == user_input]
        if not match.empty:
            row = match.iloc[0]
            st.success(f"**PGSC ID:** `{row['pgsc_id']}`\n\n**E-value:** `{row['evalue']}`")
        else:
            st.error("Soltu ID no encontrado.")
    else:
        match = df[df['pgsc_id'] == user_input]
        if not match.empty:
            row = match.iloc[0]
            st.success(f"**Soltu ID:** `{row['soltu_id']}`\n\n**E-value:** `{row['evalue']}`")
        else:
            st.error("PGSC ID no encontrado.")

# Footer
st.markdown("---")
st.markdown(
    "🧬 App desarrollada por **Juan Ignacio Cortelezzi** en el "
    "[Laboratorio de Biología Molecular Vegetal (INGEBI, CONICET)](https://www.ingebi-conicet.gov.ar).",
    unsafe_allow_html=True
)
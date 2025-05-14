# app.py
import pandas as pd
import streamlit as st

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("Assembly.csv", sep=";")

df = load_data()

# Title and description
st.title("🧬 Soltu–PGSC Gene ID Converter")
st.write("Enter the gene ID and obtain the correspondent between *Soltu* and *PGSC* alongside the associated e-value.")

# Initialize session state
if "last_query_type" not in st.session_state:
    st.session_state.last_query_type = "Convert Soltu"
if "input_value" not in st.session_state:
    st.session_state.input_value = ""

# Selection: query type
query_type = st.radio("Select type of conversion:", ["Convert Soltu ID", "Convert PGSC ID"])

# Clear input when query type changes
if query_type != st.session_state.last_query_type:
    st.session_state.input_value = ""
    st.session_state.last_query_type = query_type

# Input
user_input = st.text_input("Ingresá el ID:", value=st.session_state.input_value, key="input_value")

# Process
if user_input:
    if query_type == "Convert Soltu ID":
        match = df[df['soltu_id'] == user_input]
        if not match.empty:
            row = match.iloc[0]
            st.success(f"**PGSC ID:** `{row['pgsc_id']}`\n\n**E-value:** `{row['evalue']}`")
        else:
            st.error("Soltu ID not found.")
    else:
        match = df[df['pgsc_id'] == user_input]
        if not match.empty:
            row = match.iloc[0]
            st.success(f"**Soltu ID:** `{row['soltu_id']}`\n\n**E-value:** `{row['evalue']}`")
        else:
            st.error("PGSC ID not found.")
#Mensaje
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; font-size: 0.9em;'>
        <a href="https://ingebi-conicet.gov.ar/es_ingenieria-genetica-de-plantas/" target="_blank">
        Genetic Engineering in Plants Laboratory (INGEBI-CONICET)</a><br>
        Developed by <strong>Juan Ignacio Cortelezzi</strong>
    </div>
    """,
    unsafe_allow_html=True
)

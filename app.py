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
st.write("Enter a gene ID to retrieve the corresponding Soltu or PGSC identifier, along with the associated e-value (if available)")

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
user_input = st.text_input("Enter gene ID:", value=st.session_state.input_value, key="input_value")

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
# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; margin-top: 30px;'>
        <img src='logo-ingebi.jpg' alt='INGEBI-CONICET' width='100'><br><br>
        <a href="https://ingebi-conicet.gov.ar/es_ingenieria-genetica-de-plantas/" target="_blank"
           style="color: #1f77b4; text-decoration: none; font-weight: bold; font-size: 0.95em;">
            Genetic Engineering in Plants Laboratory (INGEBI-CONICET)
        </a><br>
        <span style="font-style: italic; color: #555;">Developed by Juan Ignacio Cortelezzi</span>
    </div>
    """,
    unsafe_allow_html=True
)

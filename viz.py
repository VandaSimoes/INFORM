import duckdb
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px  # Importando plotly.express
import time  # Importando time para medições

# Conectando ao DuckDB
conn = duckdb.connect()

# Criando tabela a partir do arquivo CSV
query = """
CREATE TABLE mytable AS
SELECT 
    column0 AS MCV,
    column1 AS ALP,
    column2 AS ALT,
    column3 AS AST,
    column4 AS GGT,
    column5 AS DRINKS
FROM read_csv_auto('/Users/vandasimoes/bupa.data');
"""
conn.execute(query)

# Consultando os dados
query = "SELECT * FROM mytable"
df = conn.sql(query).df()

# Dashboard no Streamlit
st.title("Streamlit + duckdb Dashboard")

# Botão para amostra de dados
if st.button(label="Show a Sample"):
    st.write("## Sample Data")
    st.dataframe(df.head(10), height=300)

# Visualização dos dados
st.write("## Visualization")
option = st.selectbox(
    "Select a dimension (X-axis):",
    ["MCV", "ALP", "ALT", "AST", "GGT", "DRINKS"],
    key="option",
)
if option:
    option2 = st.selectbox(
        "Select another dimension (Y-axis):",
        ["MCV", "ALP", "ALT", "AST", "GGT", "DRINKS"],
        key="option2",
    )
    if option2:
        st.write(f"### Scatter Plot: {option} x {option2}")

        # Criando scatter plot
        fig = px.scatter(
            df,
            x=option,
            y=option2,
            title=f"Scatter Plot: {option} vs {option2}",
        )
        st.plotly_chart(fig)

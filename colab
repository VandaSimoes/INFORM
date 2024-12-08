!pip install duckdb streamlit matplotlib plotly seaborn pandas numpy

import duckdb
import plotly.express as px
import seaborn as sns

conn = duckdb.connect()

query = """
CREATE TABLE bupa AS
SELECT
    column0 AS MCV,
    column1 AS ALP,
    column2 AS ALT,
    column3 AS AST,
    column4 AS GGT,
    column5 AS Drinks
FROM read_csv_auto('bupa.data');
"""

conn.execute(query)

query = """
select *
from bupa
"""
df = conn.sql(query).df()
df

bupa = conn.execute("SELECT * FROM bupa").df()

correlation_matrix = bupa[['MCV', 'ALP', 'ALT', 'AST', 'GGT', 'Drinks']].corr()

plt.figure(figsize=(10, 8))

sns.heatmap(
    correlation_matrix,
    annot=True,        
    cmap="coolwarm",   
    fmt=".2f",         
    square=True,       
    cbar_kws={'shrink': 0.8}  
)

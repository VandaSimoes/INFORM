import duckdb
import matplotlib.pyplot as plt
import streamlit as st

conn = duckdb.connect()

st.title("Streamlit + duckdb Tutorial")
button = st.button(label="Check for a sample")
if button:
    #  generate_dataset_orders(filename=filename, num_rows=1000)
    # load_file(db=db, infile_path=filename, table_name=destination_table_name)

    st.write("Half-pint fall")

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

start_time = time.time()

query = """
select * 
from mytable
"""

df = conn.sql(query).df()
df

# title of the dashboard
st.title("Streamlit + duckdb Tutorial")
try:
    #create a button to use
    button = st.button(label="Check for a sample")

    # if button is pressed do something
    if button:
        # title if button is pressed
        st.write("## Sample")
        # show dataframe (first 10 rows) if button is pressed.
        st.dataframe(df.head(10), height=300)

    # another title
    st.write("## Visualization")
    ## create a selection box with the 4 options (sepal and petal length and width)
    option = st.selectbox(
        "Select a dimension",
        ["MCV", "ALP", "ALT", "AST" , "GGT", "DRINKS"],
        key="option",
    )
    # if a option is selected show something
    if option:
        # second option to use in double plots
        option2 = st.selectbox(
            "Select another dimension",
            ["MCV", "ALP", "ALT", "AST" , "GGT", "DRINKS"],
            key="option2",
        )
        # another title (is using markdown - hence the ###)
        st.write(f"### Scatter Plot: {option} x {option2}")

        ## create a scatter plot 
        fig = px.scatter(
            df,
            x=option,
            y=option2,
            color="species",
            hover_name="species",
            log_x=True,
        )

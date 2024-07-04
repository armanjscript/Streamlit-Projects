import streamlit as st
import pandas as pd

###### Display Elements #######

df = pd.read_csv('data/template.csv', dtype='int')

st.dataframe(df)
st.write(df)

st.table(df) #wider dataframe in form of table

# st.metric(label="Population", value=900, delta=-20, delta_color="normal")
st.metric(label="Expense", value=900, delta=-20, delta_color="inverse") #sth like increasing and decreasing prices
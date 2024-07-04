import streamlit as st
import pandas as pd

#Buttons
primary_btn = st.button(label="Primary", type="primary")
secondary_btn = st.button(label="Secondary", type="secondary")

if primary_btn:
    st.write("Hello from primary")
    
if secondary_btn:
    st.write("Hello from secondary")

#Checkbox
st.divider()

checkbox = st.checkbox("Remember me")

if checkbox:
    st.write("I will remember you")
else:
    st.write("I will forget you")

#Radio Buttons
st.divider()

df = pd.read_csv("data/template.csv")

radio = st.radio("Choose a column", options=df.columns[1:], index=0, horizontal=False)
st.write(radio)



#Select Box
st.divider()

select = st.selectbox("Choose a column", options=df.columns[1:], index=0)
st.write(select)

#Multiselect
st.divider()

multiselect = st.multiselect("Choose as many columns as you want", options=df.columns[1:], default=["col1"], max_selections=3)
st.write(multiselect)

#Slider
st.divider()

slider = st.slider("Pick a number", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
st.write(slider)

#Text Input
st.divider()

text_in = st.text_input("What's your name?", placeholder="Arman Daneshdoost")
st.write(f"Your name is {text_in}")

#Number Input
st.divider()

num_input = st.number_input("Pick a number", min_value=0, max_value=10, value=0, step=1)
st.write(f"You picked {num_input}")

#Textarea
st.divider()

text_area = st.text_area("What do you want to tell me?", height=200, placeholder="Write your message here...")
st.write(text_area)
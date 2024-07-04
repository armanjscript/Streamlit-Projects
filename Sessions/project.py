import streamlit as st

st.title("Exercise: State Management")

st.subheader("Temperature Conversion")

#Initialize state with temperatures.
#Use the freezing point of water

if "celsius" not in st.session_state:
    st.session_state["celsius"] = 0.00
    
if "farenheit" not in st.session_state:
    st.session_state["farenheit"] = 32.00
    
if "kelvin" not in st.session_state:
    st.session_state["kelvin"] = 273.15
    

#Write a callback to convert the temperature in Celsius 
# to Farenheit and Kelvin. Change the values in the state
# appropriately

def celsius_conversion():
    celsius = st.session_state["celsius"]
    
    st.session_state["farenheit"] = celsius * 1.80 + 32
    st.session_state["kelvin"] = celsius + 273.15

#Same thing, but converting from Farenheit to Celsius 
# and Kelvin

def farenheit_conversion():
    farenheit = st.session_state["farenheit"]
    farenheit_converted = (farenheit - 32.00) / 1.80
    
    st.session_state["celsius"] = farenheit_converted
    st.session_state["kelvin"] = farenheit_converted + 273.15

#Same thing, but converting from Kelvin to Celsius
# and Farenheit

def kelvin_conversion():
    kelvin = st.session_state["kelvin"]
    celsius = kelvin - 273.15
    
    st.session_state["celsius"] = celsius
    st.session_state["farenheit"] = (celsius * 1.80) + 32.00
    
#Write a callback that adds whatever number the user
# inputs to the Celsius box. Use args.

def add_to_celsius(num):
    st.session_state["celsius"] += num
    celsius_conversion()
    
#Write a callback to set temperatures depending on 
# which button the user clicks. Use kwargs.

def set_temperatures(celsius, farenheit, kelvin):
    st.session_state["celsius"] = celsius
    st.session_state["farenheit"] = farenheit
    st.session_state["kelvin"] = kelvin 
    
col1, col2, col3 = st.columns(3)

col1.number_input("Celsius", step=0.01, key="celsius", on_change=celsius_conversion)
col2.number_input("Farenheit", step=0.01, key="farenheit", on_change=farenheit_conversion)
col3.number_input("Kelvin", step=0.01, key="kelvin", on_change=kelvin_conversion)

col1, _, _ = st.columns(3)
num = col1.number_input("Add to Celsius", step=1)
col1.button("Add", type="primary", on_click=add_to_celsius,
            args=(num,))

col1, col2, col3 = st.columns(3)

col1.button(" Freeze point of water",
            on_click=set_temperatures,
            kwargs=dict(celsius=0.00, farenheit=32.00, kelvin=273.15))
col2.button(" Boiling point of water", on_click=set_temperatures,
            kwargs=dict(celsius=100.00, farenheit=212.00, kelvin=373.15))
col3.button(" Absolute zero", on_click=set_temperatures,
            kwargs=dict(celsius= -273.15, farenheit= -459.67, kelvin=0.00))

st.write(st.session_state)

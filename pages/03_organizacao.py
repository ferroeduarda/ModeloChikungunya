import streamlit as st

st.title("Organização")

st.sidebar.title("Menu lateral")

st.sidebar.write("Aqui é o menu lateral")

nome = st.sidebar.text_input("Digite seu nome")
st.sidebar.write("Seu nome é [lateral]:", nome)
st.write("Seu nome é [principal]:", nome)

tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
var_select = tab1.selectbox("Selectbox", ["a", "b", "c"])
st.write("You selected ", var_select)
tab2.write("this is tab 2")
number = tab2.number_input("Number input", min_value=0, max_value=10, value=5)
st.write("You selected", number)

col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")
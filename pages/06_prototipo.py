import streamlit as st
import pickle


st.title("Protótipo")

with open("model.sav", "rb") as f:
    clf = pickle.load(f)

with st.form(key='my_form'):

    sexo_escolha = st.selectbox('Sexo', ['Masculino', 'Feminino'])
    if (sexo_escolha == 'Masculino'):
        sexo = 1
    else:
        sexo = 0
    
    idade = st.number_input('Idade', min_value=0, max_value=100, value=0)

    n_irmaos = st.number_input('Número de irmãos', min_value=0, max_value=10, value=0)

    n_parentes = st.number_input('Número de parentes', min_value=0, max_value=10, value=0)

    if (st.form_submit_button('Classificar')):
        saida = clf.predict([[sexo, idade, n_irmaos, n_parentes]])[0]
        if (saida == 1):
            st.write("Você provavelmente não sobreviveria ao naufrágio do Titanic")
        else:
            st.write("Você provavelmente sobreviveria ao naufrágio do Titanic")

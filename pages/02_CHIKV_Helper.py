import streamlit as st
import pickle 
import pandas as pd
#ChikungunyaModel = pickle.load('ChikungunyaGRIDrf.sav')
st.header('CHIKV Helper')
with st.form(key='my_form'):
    febre = st.checkbox("Febre")
    mialgia = st.checkbox("Mialgia")
    cefaleia = st.checkbox("Cefaleia")
    exantema = st.checkbox("Exantema")
    vomito = st.checkbox("Vômito")
    nauseas = st.checkbox("Náuseas")
    dor_costas = st.checkbox("Dor nas costas")
    conjutivite = st.checkbox("Conjutivite")
    artrite = st.checkbox("Artrite")
    artralgia = st.checkbox("Artralgia")
    petequia = st.checkbox("Petequias")
    dor_retro = st.checkbox("Dor retrorbital")
    genero_paciente_texto = st.selectbox("Gênero", ["Feminino", "Masculino", "Outros"])
    if (genero_paciente_texto == 'Feminino'):
        genero_paciente = 0
    elif (genero_paciente_texto == 'Masculino'):
        genero_paciente = 1
    else: 
        genero_paciente = 2
    if (st.form_submit_button('Classificar')):
        with open('ChikungunyaGRIDrf.sav', "rb") as file: model = pickle.load(file)
        resultado = model.predict([[
            genero_paciente, 
            febre,
            mialgia,
            cefaleia,
            exantema,
            vomito,
            nauseas,
            dor_costas,
            conjutivite,
            artrite,
            artralgia,
            petequia,
            dor_retro
        ]])[0]
        resultado_proba = model.predict_proba([[
            genero_paciente, 
            febre,
            mialgia,
            cefaleia,
            exantema,
            vomito,
            nauseas,
            dor_costas,
            conjutivite,
            artrite,
            artralgia,
            petequia,
            dor_retro
        ]])
        if resultado == 'CHIKUNGUNYA':
            resultado_porcentagem = resultado_proba[0][0]
            resultado_porcentagem = resultado_porcentagem*100
            resultado_porcentagem = round(resultado_porcentagem, 2)
            st.write('Você provavelmente está com Chikungunya, com probabilidade de ' + str(resultado_porcentagem) + '%.')
        else:
            resultado_porcentagem = resultado_proba[0][1]    
            resultado_porcentagem = resultado_porcentagem*100
            resultado_porcentagem = round(resultado_porcentagem, 2)
            st.write('Você provavelmente não está com Chikungunya, com probabilidade de ' + str(resultado_porcentagem) + '%.')
            
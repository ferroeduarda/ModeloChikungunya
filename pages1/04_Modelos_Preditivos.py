import streamlit as st
import pickle 
import pandas as pd

st.title('Modelos preditivos')
st.header('Etapa de pré-processamento dos dados')
st.write('Para o desenvolvimento do modelo foram utilizados os dados obtidos da base de dados do Sistema de Informação de Agravos de Notificação (SINAN), contendo 140.516 registros (sendo 7.095 casos de Chikungunya e 133.421 casos para outras doenças) e 120 atributos.')
st.write('Esse conjunto de dados foi pré-processado e foram selecionados 14 atributos associados à doença. Após o balanceamento dos dados das classes, totalizando 7.095 registros, a base de dados foi dividida em 70% para treinamento e 30% para teste dos modelos.')
st.header('Treinamento dos modelos preditivos')
st.write('Utilizamos duas técnicas de *machine learning*: *Decision Tree* e *Random Forest*. Para selecionar os valores dos parâmetros dos modelos, foi aplicada a técnica de *grid search*.')
st.write('Ambos modelos apresentam boa performance. O modelo de *Decision Tree* apresentou acurácia de 84,14% e *Random Forest*, 84,21%. Esses resultados demonstram que técnicas baseadas em árvores utilizando dados clínicos apresentam bons resultados.')
st.header('Implatação do modelo preditivo no Streamlit')
st.write('No Streamlit foi implantado o modelo de Random Forest pela sua melhor performance.')

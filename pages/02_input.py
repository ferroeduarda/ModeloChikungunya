import streamlit as st

st.title("Tipos de Input")

# input de texto
st.write("Informe seu nome:")
nome = st.text_input("Nome")
st.write("Seu nome é:", nome)

# input de senha
st.write("Informe sua senha:")
senha = st.text_input("Senha", type="password")

# input de numero
st.write("Informe sua idade:")
idade = st.number_input("Idade", min_value=0, max_value=150, value=18)
st.write("Sua idade é:", idade)

# input de data
st.write("Informe sua data de nascimento:")
data = st.date_input("Data de Nascimento")
st.write("Sua data de nascimento é:", data)

# checkbox
st.write("Informe se você é maior de idade:")
maior = st.checkbox("Maior de Idade")
st.write("Você é maior de idade:", maior)

# radio
st.write("Informe seu sexo:")
sexo = st.radio("Sexo", ["Masculino", "Feminino"])
st.write("Seu sexo é:", sexo)

# selectbox
st.write("Informe seu estado civil:")
estado_civil = st.selectbox("Estado Civil", ["Solteiro", "Casado", "Divorciado", "Viúvo"])
st.write("Seu estado civil é:", estado_civil)

# multiselect
st.write("Informe seus hobbies:")
hobbies = st.multiselect("Hobbies", ["Natação", "Futebol", "Vôlei", "Basquete", "Tênis"])
st.write("Seus hobbies são:", hobbies)

# slider
st.write("Informe sua nota:")
nota = st.slider("Nota", min_value=0.0, max_value=10.0, value=5.0, step=2.0)
st.write("Sua nota é:", nota)

# botão
st.write("Clique no botão para ver o resultado:")
if st.button("Clique Aqui"):
    st.write("Você clicou no botão!")

# textarea
st.write("Informe seu comentário:")
comentario = st.text_area("Comentário")
st.write("Seu comentário é:", comentario)

st.error('Error message')
st.warning('Warning message')
st.info('Info message')
st.success('Success message')


# tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
# tab1.write("this is tab 1")
# tab2.write("this is tab 2")
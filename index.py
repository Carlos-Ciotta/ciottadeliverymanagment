import streamlit as st
from controllers import get_all, delete_by_id, put_status, post
import pandas as pd
from PIL import Image


icon = Image.open('Logo.jpeg')
st.set_page_config(
    page_title="Ciotta - Delivery Managment",
    layout="wide",
    page_icon=icon,  # Você pode usar um emoji ou uma URL de uma imagem
)

val = ['Em andamento', 'Aguardando']
val1 = ['Entregue']
val2= ['Aguardando']
def insere_entrega():
    nome_cliente = st.text_input("Nome cliente", key="nome_cliente_key")
    rua = st.text_input("Rua", key="rua_key")
    bairro = st.text_input("Bairro", key="bairro_key")
    telefone = st.text_input("Telefone", key="telefone_key")
    previsao = st.text_input("Previsão de entrega", key="previsao_key")
    if len(telefone)==0:
        telefone = "49911111111"

    if st.button("Enviar Entrega"):
        if all(s != "" for s in [nome_cliente, rua, bairro, previsao]):
            data = {
                "nome_cliente": nome_cliente,
                "logradouro": rua,
                "bairro": bairro,
                "telefone": telefone,
                "id": 0,
                "status": "Aguardando",
                "hora": "NULL",
                "data": "NULL",
                "previsao":previsao
            }
            response = post(data)
            return response
        else:
            return st.write("Campos de texto inválidos")
        
def deleta_entrega():
    id = st.text_input("Id")
    if st.button("Excluir"):
        response = delete_by_id(id)
        st.write(f"Resposta do servidor: {response}")
        
def atualiza_status():
    id = st.text_input("ID")
    status = st.selectbox(
    "Status Entrega",
    ("Aguardando", "Em andamento", "Entregue")
    )

    if st.button("Atualizar"):
        response = put_status(status, id)
        st.write(f"Resposta do servidor: {response}")

def populate_table(valor):
    dados = get_all()
    
    colunas = ["ID", "Nome Cliente", "Rua", "Bairro", "Telefone", "Status", "Hora", "Data", "Previsão de Entrega"]
    data = pd.DataFrame(dados, columns=colunas)
    df = data[data['Status'].isin(valor)]
    st.table(df)

def populate_table_entregues(valor):
    dados = get_all()
    
    colunas = ["ID", "Nome Cliente", "Rua", "Bairro", "Telefone", "Status", "Hora", "Data", "Previsão de Entrega"]
    data = pd.DataFrame(dados, columns=colunas)
    df_1 = data[data['Status'].isin(valor)]
    df = df_1.tail(20)
    st.table(df)

def main():
    st.title("Gestão de Entregas - Ciotta")
    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            insere_entrega()

        with col2:
            deleta_entrega()

        with col3:
            atualiza_status()

    with st.container():
        populate_table(val)
    
    with st.container():
        if st.button("Ver entregues"):
            populate_table(val1)


if __name__ == "__main__":
    main()

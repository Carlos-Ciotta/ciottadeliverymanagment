import streamlit as st
from models import Entrega
from controllers import post
import requests


st.set_page_config(
    page_title="Ciotta - Delivery Managment",
    page_icon=":chart_with_upwards_trend:",  # You can use an emoji or a URL to an image
)
def insere_entrega():
    st.subheader(f"Inserir Entregas")
    nome_cliente = st.text_input(f"Nome cliente")
    rua = st.text_input(f"Rua")
    bairro = st.text_input(f"Bairro")
    telefone = st.text_input(f"Telefone")

    if st.button(f"Enviar Entrega"):
        #entrega_i = Entrega
        #entrega_i.nome_cliente = nome_cliente
        #entrega_i.bairro = bairro
        #entrega_i.telefone = telefone
        #entrega_i.logradouro = rua
        data = {
            "nome_cliente": nome_cliente,
            "logradouro": rua,
            "bairro": bairro,
            "telefone": telefone,
            "id":0,
            "status":"Aguardando",
            "hora":"NULL",
            "data":"NULL"
        }
        url = 'https://api-production-e20e.up.railway.app/entregas/post'

        response = requests.post(url, json=data)

        if response.status_code == 200:
            data = response.json()
            print("Dados da API:", data)
        else:
            print("Falha na solicitação. Código de status:", response.status_code)
            print("Conteúdo da resposta:", response.text)

        st.write(f"Resposta do servidor: {response.text}")

def main():
    st.title("Gestão de Entregas - Ciotta")
    insere_entrega()



if __name__ == "__main__":
    main()
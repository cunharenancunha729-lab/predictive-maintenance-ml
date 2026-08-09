import streamlit as st
import requests

st.set_page_config(
    page_title="Manutenção Preditiva com IA",
    page_icon="",
    layout="centered"
)

st.title(" Manutenção Preditiva com IA")

st.write(
    "Sistema de previsão de falhas em máquinas utilizando "
    "Machine Learning e FastAPI."
)

st.divider()

st.subheader(" Dados da Máquina")

temperatura = st.number_input(
    "Temperatura (°C)",
    min_value=0.0,
    max_value=150.0,
    value=70.0,
    step=0.1
)

vibracao = st.number_input(
    "Vibração",
    min_value=0.0,
    max_value=10.0,
    value=3.0,
    step=0.1
)

corrente = st.number_input(
    "Corrente (A)",
    min_value=0.0,
    max_value=30.0,
    value=12.0,
    step=0.1
)

pressao = st.number_input(
    "Pressão",
    min_value=0.0,
    max_value=15.0,
    value=6.0,
    step=0.1
)

horas_operacao = st.number_input(
    "Horas de Operação",
    min_value=0,
    max_value=10000,
    value=2500,
    step=100
)

ciclos = st.number_input(
    "Ciclos",
    min_value=0,
    max_value=100000,
    value=25000,
    step=1000
)

st.divider()

if st.button("Analisar Máquina", use_container_width=True):

    dados = {
        "temperatura": temperatura,
        "vibracao": vibracao,
        "corrente": corrente,
        "pressao": pressao,
        "horas_operacao": horas_operacao,
        "ciclos": ciclos
    }

    url_api = "http://127.0.0.1:8000/prever"

    try:
        resposta = requests.post(
            url_api,
            json=dados,
            timeout=10
        )

        if resposta.status_code == 200:

            resultado = resposta.json()

            st.subheader("Resultado da Análise")

            probabilidade = resultado["probabilidade_falha"]

            if resultado["previsao"] == 1:

                st.error(
                    "ALERTA: Máquina com risco de falha!"
                )

            else:

                st.success(
                    "Máquina sem indicação de falha."
                )

            st.metric(
                "Probabilidade de Falha",
                f"{probabilidade:.2%}"
            )

        else:

            st.error(
                f"Erro na API: {resposta.status_code}"
            )

    except requests.exceptions.ConnectionError:

        st.error(
            "Não foi possível conectar à API. "
            "Verifique se o FastAPI está funcionando."
        )

    except requests.exceptions.Timeout:

        st.error(
            "A API demorou muito para responder."
        )
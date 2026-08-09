from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path


# Criar a aplicação
app = FastAPI(
    title="API de Manutenção Preditiva",
    description="API para previsão de falhas em máquinas utilizando Machine Learning",
    version="1.0.0"
)


# Localizar o modelo treinado
CAMINHO_MODELO = (
    Path(__file__).resolve().parent.parent
    / "models"
    / "modelo_manutencao_preditiva.pkl"
)


# Carregar o modelo
modelo = joblib.load(CAMINHO_MODELO)


# Estrutura dos dados recebidos pela API
class DadosMaquina(BaseModel):
    temperatura: float
    vibracao: float
    corrente: float
    pressao: float
    horas_operacao: int
    ciclos: int


# Rota inicial
@app.get("/")
def inicio():
    return {
        "mensagem": "API de Manutenção Preditiva funcionando!",
        "status": "online"
    }


# Rota de previsão
@app.post("/prever")
def prever(dados: DadosMaquina):

    entrada = pd.DataFrame({
        "temperatura": [dados.temperatura],
        "vibracao": [dados.vibracao],
        "corrente": [dados.corrente],
        "pressao": [dados.pressao],
        "horas_operacao": [dados.horas_operacao],
        "ciclos": [dados.ciclos]
    })

    previsao = modelo.predict(entrada)[0]

    probabilidades = modelo.predict_proba(entrada)[0]

    probabilidade_falha = probabilidades[1]

    if previsao == 1:
        resultado = "Com risco de falha"
    else:
        resultado = "Sem indicação de falha"

    return {
        "previsao": int(previsao),
        "resultado": resultado,
        "probabilidade_falha": round(float(probabilidade_falha), 4)
    }
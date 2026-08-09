# 🤖 Manutenção Preditiva com Inteligência Artificial

Sistema de **Manutenção Preditiva** desenvolvido em Python, utilizando conceitos de **Ciência de Dados, Machine Learning, FastAPI e Streamlit** para analisar dados operacionais de máquinas e estimar o risco de falhas.

O projeto apresenta um fluxo completo de aplicação de Machine Learning, desde a preparação e análise dos dados até a disponibilização do modelo por meio de uma API e sua utilização em um dashboard interativo.

## 🎯 Objetivo

Desenvolver uma solução capaz de analisar diferentes parâmetros operacionais de uma máquina e realizar uma **previsão de risco de falha**, auxiliando na identificação antecipada de possíveis problemas.

Os principais dados utilizados são:

* 🌡️ Temperatura
* 📳 Vibração
* ⚡ Corrente elétrica
* 🔧 Pressão
* ⏱️ Horas de operação
* 🔄 Número de ciclos

## 🧠 Ciência de Dados e Machine Learning

O desenvolvimento do projeto envolve diferentes etapas do processo de Ciência de Dados:

1. Geração e organização dos dados
2. Análise exploratória dos dados
3. Preparação dos dados para o modelo
4. Treinamento do modelo de Machine Learning
5. Realização das previsões
6. Estimativa da probabilidade de falha
7. Serialização do modelo treinado
8. Integração do modelo com uma API
9. Desenvolvimento de um dashboard para visualização dos resultados

Os notebooks disponíveis no projeto documentam parte do processo de análise e desenvolvimento do modelo.

## 📊 Dashboard Interativo

O dashboard foi desenvolvido com **Streamlit** e permite ao usuário informar os parâmetros operacionais da máquina e solicitar uma análise.

Após o envio dos dados, o sistema apresenta:

* Status da previsão;
* Indicação de risco de falha;
* Probabilidade estimada de falha.

### Fluxo da análise

```text
Dados da máquina
       ↓
Dashboard Streamlit
       ↓
API FastAPI
       ↓
Modelo de Machine Learning
       ↓
Previsão
       ↓
Probabilidade de falha
       ↓
Resultado apresentado no Dashboard
```

## ⚡ API REST com FastAPI

A aplicação utiliza **FastAPI** para disponibilizar o modelo de Machine Learning como uma API REST.

### Endpoint

```text
POST /prever
```

A API recebe os parâmetros da máquina em formato JSON e retorna a previsão e a probabilidade estimada de falha.

### Exemplo de entrada

```json
{
    "temperatura": 70,
    "vibracao": 3,
    "corrente": 12,
    "pressao": 6,
    "horas_operacao": 2500,
    "ciclos": 25000
}
```

### Exemplo de resposta

```json
{
    "previsao": 0,
    "resultado": "Sem indicação de falha",
    "probabilidade_falha": 0.0
}
```

## 🛠️ Tecnologias utilizadas

### Programação

* Python

### Ciência de Dados

* Pandas
* NumPy
* Jupyter Notebook
* Análise Exploratória de Dados

### Machine Learning

* Scikit-learn
* Treinamento de modelos
* Predição
* Estimativa de probabilidade

### API e Backend

* FastAPI
* Pydantic
* Uvicorn

### Dashboard

* Streamlit

### Ferramentas

* Git
* GitHub
* VS Code
* Joblib

## 📁 Estrutura do projeto

```text
Manutenção Preditiva/
│
├── api/
│   └── main.py
│
├── dashboard/
│   └── app.py
│
├── Data/
│   └── dados_maquina.csv
│
├── models/
│   └── modelo_manutencao_preditiva.pkl
│
├── Notebbok/
│   ├── 01_analise_dados.ipynb
│   └── 02_machine_learning.ipynb
│
├── generate_dataset.py
│
├── .gitignore
│
└── README.md
```

> **Observação:** a pasta `Notebbok` mantém o nome utilizado atualmente no projeto para preservar a estrutura existente.

## 🚀 Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/cunharenancunha729-lab/Manuten-o---Preditiva.git
```

### 2. Entrar na pasta

```bash
cd Manuten-o---Preditiva
```

### 3. Criar o ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual no Windows

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Instalar as dependências

```bash
pip install fastapi uvicorn streamlit requests pandas scikit-learn joblib
```

## ▶️ Executando a API

Execute:

```bash
uvicorn api.main:app --reload
```

A API ficará disponível em:

```text
http://127.0.0.1:8000
```

Também é possível acessar a documentação automática da API:

```text
http://127.0.0.1:8000/docs
```

## 📊 Executando o Dashboard

Abra outro terminal e execute:

```bash
streamlit run dashboard/app.py
```

O dashboard será disponibilizado em:

```text
http://localhost:8501
```

## 🔍 Exemplo de funcionamento

O usuário informa os dados operacionais da máquina:

```text
Temperatura:       70 °C
Vibração:          3
Corrente:          12 A
Pressão:           6
Horas de operação: 2500
Ciclos:            25000
```

O dashboard envia essas informações para a API, que utiliza o modelo de Machine Learning para realizar a previsão.

O resultado pode indicar:

```text
✅ Máquina sem indicação de falha
```

ou:

```text
⚠️ Máquina com risco de falha
```

Além disso, o sistema apresenta a **probabilidade estimada de falha**.

## 💡 Aplicação na indústria

A manutenção preditiva utiliza dados operacionais para identificar padrões que podem indicar possíveis problemas em equipamentos.

Este projeto demonstra como tecnologias de:

**Ciência de Dados + Machine Learning + Python + APIs + Dashboard + Automação Industrial**

podem ser integradas em uma solução aplicada ao contexto industrial.

## 📚 Conhecimentos demonstrados

Este projeto demonstra conhecimentos em:

* Ciência de Dados;
* Análise e preparação de dados;
* Machine Learning;
* Python;
* Pandas;
* Scikit-learn;
* Desenvolvimento de APIs REST;
* FastAPI;
* Streamlit;
* Integração de modelos de Machine Learning;
* Git e GitHub;
* Automação Industrial.

## 🚧 Status do projeto

**Em desenvolvimento / projeto de portfólio.**

Novas funcionalidades podem ser adicionadas futuramente, como:

* Monitoramento contínuo de máquinas;
* Armazenamento histórico das previsões;
* Gráficos de indicadores;
* Sistema de alertas;
* Melhorias na avaliação do modelo;
* Integração com sensores industriais;
* Banco de dados para histórico de manutenção.

## 👨‍💻 Autor

**Renan Henrique Martins Cunha**

Estudante de **Análise e Desenvolvimento de Sistemas** e **Técnico em Inteligência Artificial**, com formação em **Eletrotécnica** e experiência na área de **Automação Industrial**.

Interesses profissionais:

**Ciência de Dados | Inteligência Artificial | Machine Learning | Python | Análise de Dados | Automação Industrial**

### 🔗 GitHub

https://github.com/cunharenancunha729-lab

---

⭐ Projeto desenvolvido para fins de estudo, portfólio profissional e aplicação prática de **Ciência de Dados, Machine Learning e Inteligência Artificial na manutenção preditiva industrial**.

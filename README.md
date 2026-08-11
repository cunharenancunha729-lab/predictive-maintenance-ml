
 #  Sistema de Manutenção Preditiva com Inteligência artificial e automação. 

Sistema de **Manutenção Preditiva** desenvolvido em Python para análise de condições operacionais de máquinas e previsão de risco de falhas utilizando **Machine Learning**.

O projeto integra **Ciência de Dados, Machine Learning, API REST, Dashboard web e conceitos de Automação Industrial**, permitindo que dados operacionais de uma máquina sejam analisados automaticamente e utilizados para estimar o risco de falha.

A aplicação está publicada na nuvem e possui integração entre **Dashboard Streamlit → API FastAPI → Modelo de Machine Learning → Resultado da previsão**.

---

##  Demonstração Online

### Dashboard

Acesse o sistema:

https://manutencao-preditiva-dashboard.onrender.com

### 🔌 API

API responsável pelo processamento das previsões:

https://manutencao-preditiva-api.onrender.com

###  Documentação da API

Documentação interativa Swagger:

https://manutencao-preditiva-api.onrender.com/docs

---

#  Arquitetura do Sistema

A aplicação foi desenvolvida com uma arquitetura dividida em **interface, API e modelo de Machine Learning**.

```text
                         👤 USUÁRIO
                             │
                             ▼
                  ┌────────────────────┐
                  │     DASHBOARD      │
                  │     Streamlit      │
                  │    dashboard/      │
                  └─────────┬──────────┘
                            │
                            │ HTTP POST
                            │ /prever
                            ▼
                  ┌────────────────────┐
                  │        API         │
                  │      FastAPI       │
                  │       api/         │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │ MACHINE LEARNING   │
                  │      models/       │
                  │                    │
                  │ Modelo treinado    │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │      PREVISÃO      │
                  │                    │
                  │ 0 = Sem indicação  │
                  │ 1 = Risco de falha │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │     DASHBOARD      │
                  │                    │
                  │ Resultado          │
                  │ Probabilidade      │
                  │ Alerta de risco    │
                  └────────────────────┘
```

---

#  Fluxo de Desenvolvimento do Machine Learning

Antes de disponibilizar o modelo através da API, os dados passam pelo processo de desenvolvimento e treinamento.

```text
Data/
   │
   │ Dados
   ▼
Notebbok/
   │
   │ Análise exploratória
   │ Tratamento dos dados
   │ Treinamento
   │ Avaliação
   ▼
Machine Learning
   │
   ▼
models/
   │
   │ Modelo treinado
   ▼
API FastAPI
```

O projeto separa o processo de **desenvolvimento do modelo** do processo de **execução da aplicação**.

---

#  Estrutura do Projeto

```text
Manutenção Preditiva/
│
├── api/
│   └── API FastAPI
│
├── dashboard/
│   └── app.py
│
├── Data/
│   └── Dados utilizados no projeto
│
├── models/
│   └── Modelos de Machine Learning treinados
│
├── Notebbok/
│   └── Notebooks de análise e treinamento
│
├── src/
│   └── Códigos-fonte auxiliares
│
├── venv/
│   └── Ambiente virtual Python
│
├── .gitignore
│
├── generate_dataset.py
│
├── README.md
│
└── requirements.txt
```

### Descrição das principais pastas

#### `api/`

Contém a aplicação **FastAPI**, responsável por disponibilizar o modelo através de uma API REST.

A API recebe os dados da máquina enviados pelo Dashboard e retorna a previsão.

---

#### `dashboard/`

Contém a aplicação **Streamlit**.

O arquivo principal é:

```text
dashboard/app.py
```

O Dashboard permite ao usuário informar os parâmetros da máquina e executar uma análise.

---

#### `Data/`

Contém os dados utilizados durante o desenvolvimento do projeto.

Os dados são utilizados para análise e treinamento do modelo.

---

#### `models/`

Contém os modelos de **Machine Learning treinados**.

Esses modelos são utilizados pela API para realizar as previsões.

---

#### `Notebbok/`

Contém os notebooks utilizados durante o desenvolvimento.

Nessa etapa são realizadas atividades como:

* Análise exploratória
* Tratamento dos dados
* Visualização
* Engenharia de atributos
* Treinamento
* Avaliação do modelo

---

### `src/`

Contém códigos-fonte auxiliares utilizados no projeto.

---

#### `venv/`

Ambiente virtual Python utilizado no desenvolvimento local.

A pasta é mantida apenas no ambiente de desenvolvimento e não deve ser utilizada no deploy.

---

### `generate_dataset.py`

Script Python utilizado para geração do dataset utilizado no projeto.

---

####`requirements.txt`

Arquivo responsável por listar as principais dependências Python necessárias para executar a aplicação.

---

# 🤖 Machine Learning

O projeto utiliza **Machine Learning supervisionado** para realizar a classificação do estado operacional da máquina.

O modelo recebe características relacionadas às condições de operação e retorna uma previsão relacionada ao risco de falha.

## Variáveis utilizadas

O Dashboard permite informar:

| Variável          | Descrição                          |
| ----------------- | ---------------------------------- |
| Temperatura       | Temperatura de operação da máquina |
| Vibração          | Nível de vibração                  |
| Corrente          | Corrente elétrica consumida        |
| Pressão           | Pressão de operação                |
| Horas de operação | Tempo acumulado de operação        |
| Ciclos            | Quantidade de ciclos realizados    |

---

# 🔌 API REST

A API foi desenvolvida utilizando **FastAPI**.

Seu principal endpoint é:

```text
POST /prever
```

Esse endpoint recebe os dados da máquina através de JSON.

### Exemplo de requisição

```json
{
    "temperatura": 140,
    "vibracao": 9,
    "corrente": 28,
    "pressao": 13,
    "horas_operacao": 9000,
    "ciclos": 90000
}
```

### Exemplo de resposta

```json
{
    "previsao": 1,
    "probabilidade_falha": 1.0
}
```

### Interpretação

```text
previsao = 0
```

Máquina sem indicação de falha.

```text
previsao = 1
```

Máquina com indicação de risco de falha.

A API também retorna a probabilidade estimada pelo modelo.

---

# 🖥️ Dashboard

O Dashboard foi desenvolvido utilizando **Streamlit**.

O usuário informa os parâmetros da máquina e seleciona:

```text
Analisar Máquina
```

O Dashboard então envia os dados para a API utilizando uma requisição HTTP.

Exemplo da comunicação:

```text
Dashboard
    │
    │ requests.post()
    ▼
https://manutencao-preditiva-api.onrender.com/prever
```

A resposta da API é processada pelo Dashboard e apresentada ao usuário.

---

#  Comunicação entre Dashboard e API

A comunicação é realizada através de uma API REST.

```text
┌───────────────────────┐
│      Streamlit        │
│       Dashboard       │
└───────────┬───────────┘
            │
            │ POST
            │ JSON
            ▼
┌───────────────────────┐
│       FastAPI         │
│       /prever         │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Machine Learning      │
│ Modelo treinado       │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Resultado da previsão │
└───────────┬───────────┘
            │
            │ JSON
            ▼
┌───────────────────────┐
│      Streamlit        │
│  Exibe o resultado    │
└───────────────────────┘
```

---

#  Testes Realizados

Após a publicação do sistema, foram realizados testes diretamente no Dashboard online.

## 🟢 Teste 1 — Condição normal

### Dados utilizados

```text
Temperatura: 70 °C
Vibração: 3
Corrente: 12 A
Pressão: 6
Horas de operação: 2500
Ciclos: 25000
```

### Resultado

```text
Máquina sem indicação de falha.

Probabilidade de Falha:
0,00%
```

---

## 🔴 Teste 2 — Condição severa

### Dados utilizados

```text
Temperatura: 140 °C
Vibração: 9
Corrente: 28 A
Pressão: 13
Horas de operação: 9000
Ciclos: 90000
```

### Resultado

```text
ALERTA: Máquina com risco de falha!

Probabilidade de Falha:
100,00%
```

Esses testes demonstraram a comunicação completa entre o Dashboard, a API e o modelo de Machine Learning.

> **Observação:** a probabilidade apresentada é a estimativa produzida pelo modelo para os dados fornecidos. Ela não representa uma garantia de ocorrência de uma falha física real.

---

#  Deploy

O projeto foi disponibilizado na nuvem utilizando a plataforma **Render**.

A arquitetura de publicação é:

```text
                         GitHub
                            │
                            ▼
                         Render
                            │
             ┌──────────────┴──────────────┐
             │                             │
             ▼                             ▼
      Dashboard Render                API Render
             │                             │
             ▼                             ▼
        Streamlit                       FastAPI
             │                             │
             └──────────────┬──────────────┘
                            │
                            ▼
                     Machine Learning
```

### Dashboard

```text
https://manutencao-preditiva-dashboard.onrender.com
```

### API

```text
https://manutencao-preditiva-api.onrender.com
```

##Swagger

```text
https://manutencao-preditiva-api.onrender.com/docs
```

---

#  Tecnologias Utilizadas

# Linguagem

* Python

# Ciência de Dados

* Pandas
* NumPy

# Machine Learning

* Scikit-learn
* Joblib

# Backend

* FastAPI
* Uvicorn
* Pydantic

# Dashboard

* Streamlit

# Comunicação

* Requests
* HTTP
* JSON
* API REST

# Desenvolvimento

* Git
* GitHub
* VS Code
* Jupyter Notebook
* Ambiente virtual Python

## Deploy

* Render

---

#  Aplicação na Indústria

A proposta do projeto está relacionada aos conceitos de **Manutenção Preditiva e Indústria 4.0**.

Em uma aplicação industrial real, os dados poderiam ser coletados automaticamente através de sensores e sistemas industriais.

Uma possível arquitetura futura seria:

```text
Sensores
   │
   ▼
CLP
   │
   ▼
SCADA / IoT
   │
   ▼
Banco de Dados
   │
   ▼
API
   │
   ▼
Machine Learning
   │
   ▼
Previsão de Falha
   │
   ▼
Dashboard
   │
   ▼
Equipe de Manutenção
```

Essa arquitetura poderia permitir o monitoramento contínuo de equipamentos e auxiliar na tomada de decisões relacionadas à manutenção.

---

#  Objetivos do Projeto

O projeto foi desenvolvido para:

* Aplicar Machine Learning em um cenário industrial.
* Desenvolver uma solução de Manutenção Preditiva.
* Criar uma API REST para disponibilização do modelo.
* Desenvolver um Dashboard interativo.
* Integrar Python, Machine Learning e APIs.
* Automatizar o processo de análise dos dados.
* Realizar deploy de uma aplicação de Machine Learning.
* Aplicar conceitos de Ciência de Dados.
* Demonstrar uma aplicação relacionada à Indústria 4.0.

---

# Possíveis Evoluções

O projeto pode ser expandido futuramente com:

* Integração com sensores industriais.
* Integração com CLP.
* Integração com sistemas SCADA.
* Comunicação MQTT.
* Banco de dados para armazenamento histórico.
* Monitoramento em tempo real.
* Histórico das previsões.
* Gráficos de temperatura e vibração.
* Sistema de notificações.
* Monitoramento de múltiplas máquinas.
* Autenticação de usuários.
* Novos algoritmos de Machine Learning.
* Comparação entre modelos.
* Re-treinamento automático do modelo.

---

 Autor

 Renan Henrique Martins Cunha

Estudante de **Análise e Desenvolvimento de Sistemas** e **Técnico em Inteligência Artificial**, com formação técnica em **Eletrotécnica** e experiência em **Automação Industrial**.

Interesses profissionais:

* Inteligência Artificial
* Ciência de Dados
* Machine Learning
* Python
* APIs
* Automação Industrial
* Indústria 4.0
* Análise de Dados
* Desenvolvimento de Sistemas

 Links

GitHub:

https://github.com/cunharenancunha729-lab

Repositório do projeto:

https://github.com/cunharenancunha729-lab/Manuten-o---Preditiva

Dashboard:

https://manutencao-preditiva-dashboard.onrender.com

API:

https://manutencao-preditiva-api.onrender.com

---

# Licença

Este projeto foi desenvolvido para fins de **estudo, portfólio e demonstração de conhecimentos** em Python, Ciência de Dados, Machine Learning, APIs, Inteligência Artificial e Automação Industrial.

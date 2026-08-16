# 🔧 Sistema de Manutenção Preditiva com Inteligência Artificial e Automação.

Sistema completo de manutenção preditiva industrial, com arquitetura end-to-end: dashboard interativo, API própria e modelo de Machine Learning treinado — tudo publicado em produção na nuvem.

🔗 **[Acessar Dashboard ao vivo](https://manutencao-preditiva-dashboard.onrender.com)**
🔗 **[Acessar API (Swagger Docs)](https://manutencao-preditiva-api.onrender.com)**

> ⚠️ Hospedado no plano gratuito do Render — o primeiro acesso pode levar até 1 minuto para "acordar" o servidor.

## 📌 Sobre o projeto

O objetivo é prever falhas em equipamentos antes que aconteçam, a partir de dados de sensores, permitindo que a manutenção seja feita de forma preditiva (e não corretiva). O projeto simula um cenário real de uma equipe de engenharia/operações que precisa monitorar máquinas continuamente.

## 🏗️ Arquitetura

```
Dashboard (Streamlit)  →  API (FastAPI)  →  Modelo de ML (Random Forest)
```

- **Modelo**: Random Forest treinado com Scikit-learn, serializado com Joblib
- **API**: FastAPI + Uvicorn + Pydantic, com documentação automática via Swagger
- **Dashboard**: Streamlit, consumindo a API para exibir previsões em tempo real
- **Dados**: gerados sinteticamente via `generate_dataset.py`, simulando leituras de sensores industriais

## 🛠️ Tecnologias

Python · Pandas · NumPy · Scikit-learn · Joblib · FastAPI · Uvicorn · Pydantic · Streamlit · Render

## ▶️ Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/cunharenancunha729-lab/predictive-maintenance-ml.git
cd predictive-maintenance-ml

# Instale as dependências
pip install -r requirements.txt

# Gere o dataset sintético
python generate_dataset.py

# Suba a API
uvicorn api:app --reload

# Em outro terminal, suba o dashboard
streamlit run dashboard.py
```

## 📈 Próximos passos

- [ ] Adicionar testes automatizados
- [ ] Treinar com dataset real de sensores industriais (ex: NASA Turbofan)
- [ ] Adicionar monitoramento de drift do modelo em produção

---

📫 Desenvolvido por [Renan Cunha](https://github.com/cunharenancunha729-lab)

import os
import streamlit as st
import pandas as pd
import joblib  # para carregar o modelo
import numpy as np

st.header("Regressão: Expectativa de Vida com dados da WHO")

"""

## O que é o dataset Life Expectancy (WHO)?

Esse conjunto de dados contém informações de saúde pública fornecidas pela **Organização Mundial da Saúde (WHO)**, abrangendo diferentes países e anos. Ele inclui variáveis socioeconômicas, sanitárias e ambientais, relacionadas à **expectativa de vida ao nascer**.

"""

"""

## Qual o objetivo da regressão?

Construir um modelo de **regressão supervisionada** para **prever a expectativa de vida** de um país em um determinado ano, com base em variáveis como:
- PIB per capita,
- Escolaridade média,
- Taxa de mortalidade,
- Gasto com saúde, entre outras.

"""

"""

## Sobre o dataset

O dataset utilizado foi pré-processado e salvo em `dataset/life_expectancy.csv`. Ele possui várias colunas, entre elas:

- `Life expectancy`: variável alvo (o que queremos prever)
- `GDP`, `Schooling`, `Adult Mortality`, `Alcohol` ... (entradas para o modelo)

"""

# Carregando o dataset
if "life_df" not in st.session_state:
    current_dir = os.path.dirname(__file__)
    dataset_path = os.path.abspath(os.path.join(current_dir, "..", "..", "dataset", "life-expectancy", "Life Expectancy Data.csv"))
    df = pd.read_csv(dataset_path)
    st.session_state.life_df = df

df = st.session_state.life_df
st.dataframe(df.sample(10))

"""

### Análise gráfica

(Coloque aqui seus plots com `matplotlib`, `seaborn` ou `plotly` para explorar as variáveis mais relevantes)

"""

"""

## Resultado da Regressão

Vamos carregar o modelo treinado e testar uma previsão:

"""

# Inputs do usuário (exemplo simplificado)
st.subheader("Prever expectativa de vida")

gdp = st.slider("GDP (PIB per capita)", float(df.GDP.min()), float(df.GDP.max()), float(df.GDP.mean()))
schooling = st.slider("Schooling (anos de escolaridade)", float(df.Schooling.min()), float(df.Schooling.max()), float(df.Schooling.mean()))
alcohol = st.slider("Consumo de álcool", float(df.Alcohol.min()), float(df.Alcohol.max()), float(df.Alcohol.mean()))

# Carregando o modelo
model_path = os.path.join(os.path.dirname(os.getcwd()), "modelo_regressao.joblib")
modelo = joblib.load(model_path)

# Organizando os dados de entrada (ajuste os nomes e ordem conforme seu modelo!)
X_input = pd.DataFrame([[gdp, schooling, alcohol]], columns=["GDP", "Schooling", "Alcohol"])

# Fazendo a predição
pred = modelo.predict(X_input)[0]

st.success(f"🧬 A expectativa de vida prevista é **{pred:.2f} anos**")

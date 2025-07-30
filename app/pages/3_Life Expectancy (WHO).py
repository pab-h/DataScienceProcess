import os
import streamlit as st
import pandas as pd
import joblib 
import numpy as np

st.header("Regressão: Expectativa de Vida com dados da WHO")

"""

## O que é o dataset Life Expectancy (WHO)?

Esse conjunto de dados contém informações de saúde pública fornecidas pela **Organização Mundial da Saúde (WHO)**, abrangendo diferentes países e anos. Ele inclui variáveis socioeconômicas, sanitárias e ambientais, relacionadas à **expectativa de vida ao nascer**.

"""

"""

## Qual o objetivo da regressão?

Construir um modelo de **regressão supervisionada** para **prever a expectativa de vida** de um país em um determinado ano, com base nas seguintes variáveis do dataset:

- Gastos totais com saúde (`Total expenditure`)
- HIV/AIDS (`HIV/AIDS`)
- Magreza em jovens (thinness 1-19 years) (`thinness  1-19 years`)
- Composição da renda (`Income composition of resources`)
- Escolaridade média (`Schooling`)

"""

"""

## Sobre o dataset

O dataset utilizado foi pré-processado e salvo em `dataset/life_expectancy.csv`. Ele possui 22 colunas, sendo a variável alvo:

- `Life expectancy`: expectativa de vida ao nascer (variável a ser prevista)

E as principais variáveis preditoras (entradas para o modelo), incluem:

- `Total expenditure`: gastos totais com saúde (como porcentagem em relação aos gastos públicos totais do país)
- `HIV/AIDS`: número de mortes por HIV/AIDS por 1.000 habitantes
- `thinness  1-19 years`: prevalência de magreza em jovens de 1 a 19 anos
- `Income composition of resources`: índice composto de recursos de renda (0 a 1)
- `Schooling`: número médio de anos de escolaridade das pessoas com 25 anos ou mais

### Fonte e descrição

O conjunto de dados foi retirado do [Kaggle](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who), com dados provenientes do repositório da Global Health Observatory (GHO) da Organização Mundial da Saúde (OMS), complementados com dados econômicos das Nações Unidas. 

Ele contém registros de **193 países**, abrangendo os anos de **2000 a 2015**, com **2938 observações** no total. Foram selecionadas variáveis críticas representativas entre os muitos fatores relacionados à saúde, divididas em quatro grandes categorias:

- Fatores de imunização
- Fatores de mortalidade
- Fatores econômicos
- Fatores sociais

O objetivo do dataset é analisar quais fatores mais impactam a expectativa de vida entre os países ao longo do tempo, fornecendo uma base sólida para análises de regressão, classificação e visualização de dados.

"""

if "life_df" not in st.session_state:
    current_dir = os.path.dirname(__file__)
    dataset_path = os.path.abspath(os.path.join(current_dir, "..", "..", "dataset", "life-expectancy", "Life Expectancy Data.csv"))
    df = pd.read_csv(dataset_path)
    df.columns = df.columns.str.strip() 
    st.session_state.life_df = df

df = st.session_state.life_df
st.dataframe(df.sample(10))

"""

### Análise gráfica

"""

current_dir = os.path.dirname(__file__)
figures_dir = os.path.abspath(os.path.join(current_dir, "..", "..", "figures", "lifeExpectancy"))

figuras = [
    "highest-lowest-life-expectancy.png",
    "life-expectancy-over-the-years.png",
    "correlation-matrix.png",
    "bloxplot.png",
    "pairplot.png",
    "regression.png"
]

captions = [
    "Países com maior e menor expectativa de vida",
    "Expectativa de vida média global ao longo dos anos",
    "Matriz de correlação das variáveis",
    "Boxplot de atributos relevantes para a expectativa de vida",
    "Pairplot das variáveis selecionadas",
    "Regressão: Real x Previsto"
]

for fig_name, caption in zip(figuras, captions):
    fig_path = os.path.join(figures_dir, fig_name)
    st.image(fig_path, caption=caption, use_container_width=True)

"""

## Informações do país e ano selecionados

Selecione um país e um ano para visualizar as informações reais registradas no dataset, incluindo:

- Gastos totais com saúde  
- Taxa de mortalidade por HIV/AIDS  
- Prevalência de magreza em jovens (1-19 anos)  
- Índice de composição da renda  
- Escolaridade média  
- Expectativa de vida registrada  

"""

paises = df['Country'].unique()
pais_escolhido = st.selectbox("Selecione o país", sorted(paises))

anos = df['Year'].unique()
ano_escolhido = st.selectbox("Selecione o ano", sorted(anos))

dados_pais_ano = df[(df['Country'] == pais_escolhido) & (df['Year'] == ano_escolhido)]

if not dados_pais_ano.empty:
    st.subheader(f"Informações de {pais_escolhido} em {ano_escolhido}")
    
    colunas_mostrar = ['Total expenditure', 'HIV/AIDS', 'thinness  1-19 years',
                       'Income composition of resources', 'Schooling', 'Life expectancy']
    
    info = dados_pais_ano[colunas_mostrar].iloc[0]
    
    for col in colunas_mostrar:
        st.write(f"**{col}:** {info[col]}")
else:
    st.warning("Dados não encontrados para esse país e ano selecionados.")

"""

## Resultado da Regressão

Vamos carregar o modelo treinado e testar uma previsão:

"""

st.subheader("Prever expectativa de vida")

total_expenditure = st.slider("Total expenditure", float(df["Total expenditure"].min()), float(df["Total expenditure"].max()), float(df["Total expenditure"].mean()))
hiv_aids = st.slider("HIV/AIDS", float(df["HIV/AIDS"].min()), float(df["HIV/AIDS"].max()), float(df["HIV/AIDS"].mean()))
thinness_1_19 = st.slider("Thinness 1-19 years", float(df["thinness  1-19 years"].min()), float(df["thinness  1-19 years"].max()), float(df["thinness  1-19 years"].mean()))
income_composition = st.slider("Income composition of resources", float(df["Income composition of resources"].min()), float(df["Income composition of resources"].max()), float(df["Income composition of resources"].mean()))
schooling = st.slider("Schooling", float(df["Schooling"].min()), float(df["Schooling"].max()), float(df["Schooling"].mean()))

current_dir = os.path.dirname(__file__) 
model_path = os.path.abspath(os.path.join(current_dir, "..", "..", "notebooks", "modelo_regressao.joblib"))
modelo = joblib.load(model_path)

X_input = pd.DataFrame([[total_expenditure, hiv_aids, thinness_1_19, income_composition, schooling]],
                       columns=['Total expenditure', 'HIV/AIDS', 'thinness  1-19 years', 'Income composition of resources', 'Schooling'])

pred = modelo.predict(X_input)[0]

st.success(f"🧬 A expectativa de vida prevista é **{pred:.2f} anos**")

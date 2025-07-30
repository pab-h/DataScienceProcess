import os

import streamlit as st
import pandas    as pd

st.header("Classificação usando os dados do Datatran")

"""

## O que é o Datatran?

Datatran é uma sigla para Sistema de Declaração de Acidentes de Trânsito Eletrônico, é uma plataforma da Polícia Rodoviária Federal (PRF) utilizada para o registro e acompanhamento de acidentes de trânsito ocorridos em rodovias federais. Ele permite a declaração online de acidentes sem vítimas ou com vítimas leves, e também a consulta de dados sobre acidentes registrados, contribuindo para a análise e segurança no trânsito.

"""

"""

## Qual o objetivo da classificação?

Constuir um modelo de classificação que defina se um acidente foi **causa principal** do acidente.
> Uma **causa principal** é um registro quee indica que aquele acidente foi o estopim para outros acidentes 

"""

"""

## Sobre o dataset

O dataset utilizado é o Acidentes 2024 (Agrupados por pessoa - Todas as causas e tipos de acidentes) disponível para download [aqui](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf). Esse dataset é composto por $ 37 $ características e $ 603.215 $ amostras.

"""

if "datatran" not in st.session_state:
    datasetPath = os.path.join(
        os.getcwd(),
        "dataset",
        "prf",
        "acidentes2024_todas_causas_tipos.csv"
    )

    datatran = pd.read_csv(
        datasetPath,
        sep      = ";",
        encoding = "latin1"
    )

    st.session_state.datatran = datatran


datatran = st.session_state.datatran


'Dataframe com 100 amostras aleatórios do dataset', datatran.sample(10)

"""

Uma explicação detalhada sobre cada coluna pode ser encontrada [aqui](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dicionario-acidentes). Porém, destacaremos as utilizadas como entrada no classificador:

- **ui**: cu

"""

"""

### Análise gráfica do dataset 

COLOCAR OS PLOTS GERADOS AQUI

E O PLOT DE MAPA


"""

"""

## Resultados 

Mostrar os desempenhos dos classificadores

"""

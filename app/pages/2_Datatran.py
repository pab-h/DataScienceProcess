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

    datasetPath = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), 
            "..", 
            "..", 
            "dataset", 
            "prf", 
            "acidentes2024_todas_causas_tipos.csv"
         )
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

* **Tipo Acidente**: Identificação do tipo de acidente. Exemplos: Colisão frontal, Saída de pista, etc.
* **Classificação Acidente**: Classificação quanto à gravidade do acidente: Sem Vítimas, Com Vítimas Feridas, Com Vítimas Fatais e Ignorado.
* **Fase Dia**: Fase do dia no momento do acidente. Exemplos: Amanhecer, Pleno dia, etc.
* **Condição Meteorológica**: Condição do clima no momento do acidente. Exemplos: Céu claro, Chuva, Vento, etc.
* **Tipo Pista**: Tipo da pista com base na quantidade de faixas. Exemplos: Dupla, Simples ou Múltipla.
* **Uso Solo**: Descrição sobre as características do local do acidente. Exemplo: Urbano = Sim; Rural = Não.
* **Tipo Veículo**: Tipo do veículo conforme o Art. 96 do Código de Trânsito Brasileiro. Exemplos: Automóvel, Caminhão, Motocicleta, etc.
* **Tipo Envolvido**: Tipo de envolvido no acidente conforme sua participação. Exemplos: Condutor, Passageiro, Pedestre, etc.
* **Estado Físico**: Condição do envolvido conforme a gravidade das lesões. Exemplos: Morto, Ferido leve, etc.

"""

"""

### Análise gráfica do dataset 

"""

figuresDir = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", 
        "..", 
        "assets", 
        "prf"
        )
    )

figures = os.listdir(figuresDir)

for figureName in figures:
    figurePath = os.path.join(figuresDir, figureName)
    st.image(
        figurePath, 
        caption             = figureName.split(".")[0], 
        use_container_width = True
    )

"""

## Resultados 

"""

figuresClassifierDir = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", 
        "..", 
        "assets", 
        "classifier"
    )
)

figuresClassifier = os.listdir(figuresClassifierDir)

for figureName in figuresClassifier:
    figurePath = os.path.join(figuresClassifierDir, figureName)
    st.image(
        figurePath, 
        caption             = figureName.split(".")[0], 
        use_container_width = True
    )


"""

## Modelo Online

Vai ficar para a próxima =( 

"""
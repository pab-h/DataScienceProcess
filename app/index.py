import streamlit as st

"""

# 📊 Projeto de Análise de Dados com o Método OSEMN

Este repositório apresenta um projeto de **Análise de Dados** desenvolvido como parte da disciplina de Tópicos Especiais. Nele, aplicamos o processo OSEMN para explorar e analisar dois conjuntos de dados abertos distintos:

- **Expectativa de Vida (WHO)**: dados globais sobre expectativa de vida, indicadores socioeconômicos e sanitários.
- **Acidentes de Trânsito (PRF)**: dados da Polícia Rodoviária Federal contendo informações sobre acidentes e suas causas no Brasil.

## 🧠 Objetivo

Nosso objetivo é aplicar o processo **OSEMN** (Obter, Limpar, Explorar, Modelar e Interpretar) para:

- Investigar padrões e correlações nos dados;
- Aplicar **técnicas de regressão** no dataset da OMS para prever expectativa de vida;
- Aplicar **técnicas de classificação** no dataset da PRF para prever causas ou gravidade dos acidentes;
- Gerar insights relevantes a partir dos dados analisados.

## 🧰 Ferramentas Utilizadas

- Python 3.x
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/)
- [Streamlit](https://streamlit.io/) — para visualização web interativa

## ▶️ Como Executar 

1. Clone o repositório

```bash
git clone https://github.com/pab-h/DataScienceProcess
```
2. Inicialize as variáveis de ambientes virtuais

```bash
python -m venv .venv
```
3. Ative as variáveis de ambiente

```bash
source .venv/bin/activate
```
> Sempre faça esse passo ao manipular o projeto

4. Instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

5. Baixe os datasets

```bash
python scripts/downloadDatasets.py
```

6. Execute o dataApp

```bash
streamlit run app/index.py
```

## 👥 Equipe

- [Miguel Edson](https://github.com/Miguel-Edson)  
- [Laisa Mireli](https://github.com/LaisaMireli)  
- [Ryan Lael](https://github.com/RyamLael)  
- [Francisco Lairton](https://github.com/LairtonPessoa)  
- [Pablo Hugo](https://github.com/pab-h)  
- [Yan Marcelo](https://github.com/YanMarcelo)  

"""

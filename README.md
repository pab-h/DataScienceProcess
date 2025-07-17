# Processo de Ciência de Dados

Uma metodologia para soluções de problemas ligados à ciência de dados pode ser definida a partir da aplicação do processo OSEMN. Este mesmo é definido por um conjunto de etapas recomendadas para desenvolvimento da solução em 5 (cinco) momentos bem específicos:
1. A primeira etapa envolve obter os dados (Obtain). Os dados podem ser coletados praticamente de qualquer lugar, como redes sociais, exames médicos, sensores, APIs, datasets públicos e privados, etc. A maioria das bases coletadas apresentam falhas, como dados faltantes, por exemplo. 
2. Para realizar o tratamento desses dados é aplicada a segunda etapa do processo OSEMN, definido por limpeza (Scrub), que atuará na remoção ou substituição dos dados desnecessários. 
3. Na terceira etapa, relacionada à exploração (Explore), a propriedade dos dados é verificada. Em uma base de dados há diferentes tipos de dados, como numérico, categóricos, datas, etc. Para cada um desses dados faz-se necessário realizar um tratamento diferente, seja para extração de novos dados ou para conversão. 
4. O quarto passo associa-se à modelagem (Model), em que os algoritmos de aprendizado de máquina são utilizados para realizar classificação ou regressão sobre os dados. Este passo é completamente dependente da etapa anterior, o que reforça que uma boa análise exploratória dos dados influi diretamente nas predições do modelo. Após o uso do modelo e assim alcançar o resultado de suas predições, faz-se necessário interpretar os dados alcançados. 
5. Esta é a última etapa, que se trata da interpretação (iNterpret). Este passo se mostra relevante para dar significado ao que o modelo apresentou como saída, o que aquela predição representa e como ela pode ser aplicada. Esse tipo de inferência pode ser apresentada de forma gráfica, permitindo um melhor entendimento por parte do público-alvo da solução.

## Inicializando o repositório

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

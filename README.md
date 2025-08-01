# Projeto de Análise de Risco de Crédito 

### `Autor: Frederico Lemes Rosa`

---

## Visão Geral do Projeto

Este projeto é um estudo de caso e um protótipo de um sistema de **análise de risco de crédito**, utilizando técnicas de **Análise Exploratória de Dados (EDA)** e banco de dados. O objetivo principal é demonstrar como insights valiosos podem ser extraídos de dados de clientes para otimizar e aprimorar as decisões de concessão de crédito no setor financeiro.

A análise foi conduzida utilizando uma base de dados de clientes, com foco em identificar os principais fatores preditores de **inadimplência**.

## Metodologia e Tecnologias

* **Extração e Armazenamento de Dados:** Os dados foram extraídos de uma base de dados simulada no **Oracle Database (XE)**.
* **Análise Exploratória de Dados (EDA):** A análise foi realizada em um ambiente **Jupyter Notebook** para visualização interativa e criação de uma narrativa clara.
* **Tecnologias Utilizadas:**
    * **Python** (Linguagem de Programação)
    * **Pandas** e **NumPy** (Manipulação e Análise de Dados)
    * **Matplotlib** e **Seaborn** (Visualização de Dados)
    * **oracledb** (Conexão com o Oracle)
    * **Jupyter Notebook** (Ambiente Interativo)

## Principais Descobertas (Análise Exploratória de Dados)

A análise exploratória revelou insights cruciais sobre o perfil de clientes e os fatores de risco. As principais descobertas incluem:

* **Balanceamento do Dataset:** O dataset apresenta um leve desbalanceamento, com a classe 'inadimplente' sendo majoritária.
* **Poder Preditivo do Score de Crédito:** O `Score de Crédito Externo` demonstrou ser o fator mais forte para prever a inadimplência. Observou-se uma **forte correlação negativa (-0.69)**, indicando que scores mais baixos estão diretamente associados a uma maior probabilidade de inadimplência.
* **Histórico de Pagamento:** O `Histórico de Pagamento` também se mostrou um preditor extremamente relevante. O gráfico de barras empilhadas confirma que a proporção de inadimplência aumenta drasticamente à medida que o histórico de pagamento piora, validando uma premissa básica do mercado de crédito.
* **Variáveis com Baixa Correlação:** Variáveis como `Salário Mensal` (-0.03) e `Dívida Total` (0.09) apresentaram uma correlação linear muito fraca com a inadimplência, sugerindo que, isoladamente, não são preditores fortes neste dataset.

## Visualizando a Análise Detalhada

Para uma análise mais aprofundada, com todos os gráficos, estatísticas e o código-fonte, por favor, explore o notebook Jupyter: `(Analise_Dados_Risco_Credito.ipynb)`

---

## Como Contribuir ou Executar o Projeto

Se você deseja executar a análise, as instruções de configuração do ambiente e os scripts necessários estão detalhados no notebook.

---

### `https://www.linkedin.com/in/frederico-l-rosa/`

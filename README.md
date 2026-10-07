# 📊 Introdução a Bancos de Dados com SQL & Python

Este é um projeto didático e prático projetado para ensinar e praticar os fundamentos da linguagem **SQL** utilizando **Python** e o banco de dados leve **SQLite**. 

O projeto simula o ecossistema de uma **loja virtual**, criando tabelas de clientes, produtos e pedidos para demonstrar como consultar, filtrar, ordenar e cruzar dados do mundo real.

## 🚀 Tecnologias Utilizadas

* **Python 3**
* **SQLite3** (Módulo nativo do Python para banco de dados)
* **Pandas** (Para visualização de dados em formato de tabelas/DataFrames)
* **Jupyter Notebook** (Para execução interativa dos códigos)

## 📁 Estrutura do Projeto

* `criar_banco.py`: Script Python responsável por criar o banco de dados `loja.db`, estruturar as tabelas e inserir os dados fictícios de teste.
* `introducao_sql.ipynb`: Notebook interativo contendo as explicações teóricas e práticas dos comandos SQL essenciais.
* `loja.db`: Arquivo gerado automaticamente que armazena o banco de dados relacional.

## 🗄️ Estrutura do Banco de Dados (`loja.db`)

O banco de dados é composto por 3 tabelas interligadas:
1. **`clientes`**: Armazena `id`, `nome` e `cidade`.
2. **`produtos`**: Armazena `id`, `nome` e `preco`.
3. **`pedidos`**: Registra as vendas ligando `cliente_id` e `produto_id` à `quantidade` comprada.

## 🧠 Conceitos de SQL Abordados

No notebook principal, você aprenderá e executará na prática os seguintes comandos:
* **`SELECT`**: Como selecionar e extrair colunas das tabelas.
* **`WHERE`**: Como aplicar filtros condicionais (ex: produtos acima de um valor ou clientes de uma cidade específica).
* **`ORDER BY` & `LIMIT`**: Como ordenar os resultados (crescente/decrescente) e limitar o número de linhas exibidas (útil para rankings).
* **`JOIN`**: Como cruzar dados de múltiplas tabelas para transformar IDs numéricos em relatórios fáceis de ler.

## 🛠️ Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com
cd NOME-DO-REPOSITORIO
```

### 2. Instalar as dependências
Certifique-se de ter o Python instalado. Em seguida, instale a biblioteca Pandas e o ecossistema Jupyter:
```bash
pip install pandas notebook
```

### 3. Criar e popular o Banco de Dados
Execute o script para gerar o arquivo `loja.db` preenchido com os dados simulados:
```bash
python criar_banco.py
```

### 4. Abrir o ambiente de estudos
Inicie o Jupyter Notebook para abrir e rodar o arquivo de exercícios:
```bash
jupyter notebook
```
Abra o arquivo `introducao_sql.ipynb` e execute as células para ver o SQL funcionando em tempo real!

## 🔗 Links Úteis Recomendados no Projeto
* [SQLFormat](https://sqlformat.org) — Para formatar e deixar suas queries SQL elegantes.
* [SQLite Online](https://sqliteonline.com) — Para testar e visualizar bancos de dados diretamente no navegador.

## Conversor de Moedas

Conversor de Moedas é um aplicativo de conversão de moedas simples, desenvolvido com Python e a interface gráfica PySimpleGUI. Este projeto permite que os usuários convertam um valor de uma moeda para outra usando uma API de câmbio em tempo real. A ideia é fornecer uma solução prática e fácil para usuários que necessitam de conversões rápidas entre moedas.

## Objetivo

O objetivo principal do Conversor de Moedas é fornecer uma ferramenta simples e eficaz para converter valores entre diferentes moedas, utilizando taxas de câmbio atualizadas pela API. O projeto também serve como uma demonstração do uso de APIs externas para alimentar um aplicativo com dados em tempo real, e como exemplo prático do uso da biblioteca PySimpleGUI para criação de interfaces gráficas.

Seja bem-vindo ao Conversor de Moedas e comece a converter valores de maneira simples e rápida!

## Capturas de Tela 

Aqui estão algumas capturas de tela do Conversor de Moedas:

## Moedas Disponiveis

![Captura de tela 2025-01-03 161244](https://github.com/user-attachments/assets/239a4fc0-64ac-4dfd-86fd-984bcefc2d99)


## Exemplo de Conversão

![Captura de tela 2025-01-03 161321](https://github.com/user-attachments/assets/9e23171d-54df-455f-876e-83b8c46042fd)


## Tecnologias Utilizadas

O Conversor de Moedas utiliza as seguintes tecnologias e ferramentas:


Python 3.x

PySimpleGUI - Para a criação da interface gráfica.

Requests - Para consumir a API de câmbio em tempo real.

API de Câmbio - A API usada é a ExchangeRate-API para obter taxas de câmbio atualizadas.

## Instalação

Para executar o Conversor de Moedas localmente, siga as instruções abaixo:

Clone o repositório:
git clone https://github.com/gabrielms040/ConversorDeMoeda.py.git

Navegue até o diretório do projeto

Instale as dependências com:
pip install -r requirements.txt

Execute o script :
pyton Calculadora_cambio.py

A interface gráfica será aberta, onde você poderá selecionar as moedas de origem e destino, inserir o valor que deseja converter e ver o valor convertido.

## API Utilizada

O Conversor de Moedas consome dados de câmbio em tempo real através da API de Câmbio. A API é acessada utilizando uma chave de API (que você deve configurar em seu código, se necessário). A API retorna as taxas de câmbio mais recentes para as moedas que você escolheu.

## Como Obter uma Chave da API

Acesse https://www.exchangerate-api.com/.

Crie uma conta ou faça login.

Obtenha a chave da API e substitua-a no código onde api_key está configurado.

## Contribuindo

Se você quiser contribuir com o Conversor de Moedas, siga estas etapas:

1. Abra uma issue para discutir a mudança que você gostaria de fazer.
2. Faça um fork do repositório e crie um branch para sua contribuição.
3. Envie suas alterações com um pull request.

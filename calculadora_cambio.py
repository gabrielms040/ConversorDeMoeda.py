import requests
import PySimpleGUI as sg

def calcular_cambio_api(moeda_origem, moeda_destino, valor):
    api_key = "408957b3b739ff7aed081c7e" 

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{moeda_origem}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        if moeda_destino in dados['conversion_rates']:
            taxa = dados['conversion_rates'][moeda_destino]
            valor_convertido = valor * taxa
            return valor_convertido
        else:
            return(f"Erro: Moeda de destino '{moeda_destino}' não encontrada.")
    else:
        return("Erro ao acessar a API.")

#interface gráfica
moedas = [
    'Dólar Americano (USD)', 
    'Euro (EUR)', 
    'Libra Esterlina (GBP)', 
    'Iene Japonês (JPY)', 
    'Franco Suíço (CHF)', 
    'Dólar Australiano (AUD)', 
    'Dólar Canadense (CAD)',
    'Real Brasileiro (BRL)'
]  

#Linhas da interface
layout = [
    [sg.Text('Moeda de Origem:'), sg.Combo(moedas, key='-MOEDA_ORIGEM-', default_value='Dólar Americano (USD)'),
     sg.Text('Valor:'), sg.InputText('', key='-VALOR-', size=(15, 1))],

    [sg.Text('Moeda de Destino:'), sg.Combo(moedas, key='-MOEDA_DESTINO-', default_value='Real Brasileiro (BRL)'),
     sg.Text('Valor Convertido:', size=(12, 1)), sg.Text('', key='-VALOR_CONVERTIDO-', size=(15, 1))],

    [sg.Button('Transformar', key='-TRANSFORMAR-')]
]

window = sg.Window('Conversor de Moedas', layout)

#retorna a sigla da moeda pra API
def obter_codigo_moeda(nome_completo):
    nome_completo = nome_completo.strip()
    if 'Dólar Americano (USD)' in nome_completo:
        return 'USD'
    elif 'Euro (EUR)' in nome_completo:
        return 'EUR'
    elif 'Libra Esterlina (GBP)' in nome_completo:
        return 'GBP'
    elif 'Iene Japonês (JPY)' in nome_completo:
        return 'JPY'
    elif 'Franco Suíço (CHF)' in nome_completo:
        return 'CHF'
    elif 'Dólar Australiano (AUD)' in nome_completo:
        return 'AUD'
    elif 'Dólar Canadense (CAD)' in nome_completo:
        return 'CAD'
    elif 'Real Brasileiro (BRL)' in nome_completo:  
        return 'BRL'
    else:
        return None

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == '-TRANSFORMAR-':
        try:
            #pega os valores
            valor = float(values['-VALOR-'])
            moeda_origem_completa = values['-MOEDA_ORIGEM-']
            moeda_destino_completa = values['-MOEDA_DESTINO-']

            # retorna as siglas das moedas
            moeda_origem = obter_codigo_moeda(moeda_origem_completa)
            moeda_destino = obter_codigo_moeda(moeda_destino_completa)

            if moeda_origem and moeda_destino:
                #chama a api
                valor_convertido = calcular_cambio_api(moeda_origem, moeda_destino, valor)

                # mostra o valor do resultado
                if isinstance(valor_convertido, float):
                    window['-VALOR_CONVERTIDO-'].update(f'{valor_convertido:.2f}')
                else:
                    sg.popup_error(valor_convertido)  
            else:
                sg.popup_error("Moeda de origem ou destino inválida.")
        except ValueError:
            sg.popup_error('Por favor, insira um valor numérico válido.')

window.close()
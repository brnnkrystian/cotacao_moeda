import requests

def execute():
    moeda_desejada = input('Insira a moeda que deseja: (D) Dolar, (E) Euro, (B) BTC: ')
    if moeda_desejada == 'D':
        moeda = 'USD-BRL'
    elif moeda_desejada == 'E':
        moeda = 'EUR-BRL'
    elif moeda_desejada == 'B':
        moeda = 'BTC-BRL'

    valor_desejado = float(input('Insira o valor em R$: '))
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}'
    response = requests.get(url)
    body = response.json()
    if moeda == 'USD-BRL':
        coin = 'USDBRL'
    elif moeda == 'EUR-BRL':
        coin = 'EURBRL'
    elif moeda == 'BTC-BRL':
        coin = 'BTCBRL'

    price = float(body[f'{coin}']['bid'])
    valor_convertido = valor_desejado / price
    
    print(f'Cotação da moeda escolhida: {price:.2f}')
    print(f'Valor convertido da moeda escolhida: {valor_convertido:.2f}')

execute()
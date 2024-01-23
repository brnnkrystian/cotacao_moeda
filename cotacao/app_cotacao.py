import requests

def execute():
    real = float(input('Insira o valor em R$: '))
    url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
    response = requests.get(url)
    body = response.json()
    price = float(body['USDBRL']['bid'])
    valor_convertido = real / price
    print(f'Cotação do dolar atual: {price:.2f}')
    print(f'Valor convertido: ${valor_convertido:.2f}')

execute()
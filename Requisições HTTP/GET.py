import requests

url = 'https://API'

response_get = requests.get(url)

if response_get.status_code == 200:
    print('GET bem-sucedido!')
    print('Conteúdo da resposta GET:', response_get.json())

elif response_get.status_code == 404:
    print('Erro 404: Recurso não encontrado para GET.')

else:
    print('Erro GET:', response_get.status_code)

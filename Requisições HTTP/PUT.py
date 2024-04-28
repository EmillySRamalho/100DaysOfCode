import requests

url = 'https://API'

data_put = {'key': 'value'}
response_put = requests.put(url, json=data_put)


if response_put.status_code == 200:
    print('PUT bem-sucedido!')

elif response_put.status_code == 404:
    print('Erro 404: Recurso não encontrado para PUT.')

else:
    print('Erro PUT:', response_put.status_code)

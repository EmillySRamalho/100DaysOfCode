import requests

url = 'https://API'

data_post = {'key': 'value'}
response_post = requests.post(url, json=data_post)

if response_post.status_code == 200:
    print('POST bem-sucedido!')

elif response_post.status_code == 404:
    print('Erro 404: Recurso não encontrado para POST.')

else:
    print('Erro POST:', response_post.status_code)

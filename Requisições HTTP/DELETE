import requests

url = 'https://API'

response_delete = requests.delete(url)

if response_delete.status_code == 200:
    print('DELETE bem-sucedido!')

elif response_delete.status_code == 404:
    print('Erro 404: Recurso não encontrado para DELETE.')
else:
    print('Erro DELETE:', response_delete.status_code)

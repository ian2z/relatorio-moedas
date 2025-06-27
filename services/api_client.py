import requests #biblioteca em python que permite realizar requisições de APIs
from datetime import datetime #bilioteca usada para calcular o tempo de log

def get_json(url): #função que realiza uma requisição GET, através de uma URL, e também os erros gerados pela mesma requisição
    try:
        response = requests.get(url, timeout=5) #Realiza a requisição, em até no máximo 5 segundos
        response.raise_for_status() #Obtem o código da requisição: 200, 401, etc
        return response.json() #Retorna o json que recebeu da API
    except Exception as e:
        return {"erro na requisição": str(e)}

#funcões criadas para as requisições específicas
def get_cotacoes():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    return get_json(url)

def get_historico_bitcoin():
    url = "https://economia.awesomeapi.com.br/json/daily/BTC-BRL/30"
    return get_json(url)

def get_taxa_selic():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    return get_json(url)

print("debugando")
#print(get_historico_bitcoin())
#print(get_cotacoes())
print(get_taxa_selic())
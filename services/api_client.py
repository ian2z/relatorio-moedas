import requests #biblioteca em python que permite realizar requisições de APIs
from datetime import datetime #bilioteca de tempo para registrar os logs

def getJson(url): #função que realiza uma requisição GET, através de uma URL, e também os erros gerados pela mesma requisição
    try:
        response = requests.get(url, timeout=5) #Realiza a requisição, em até no máximo 5 segundos
        response.raise_for_status() #Obtem o código da requisição: 200, 401, etc
        return response.json() #Retorna o json que recebeu da API
    except Exception as e:
        return {"erro na requisição": str(e)}

#funcões criadas para as requisições específicas
def getCotacoes():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    return getJson(url)

def getHistoricoBitcoin():
    url = "https://economia.awesomeapi.com.br/json/daily/BTC-BRL/30"
    return getJson(url)

def getTaxaSelic():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados/ultimos/1?formato=json"
    return getJson(url)

#Criando funções que retornam os arquivos .json formatados em arrays
def formatarCotacoes(json_cotacoes):
    cotacoes = []
    for chave, dados in json_cotacoes.items():
        registro = {
            "moeda": dados["code"],
            "nome": dados["name"],
            "data_hora": datetime.fromtimestamp(int(dados["timestamp"])).strftime("%d/%m/%Y %H:%M:%S"),
            "alta": float(dados["high"]),
            "baixa": float(dados["low"]),
            "compra": float(dados["bid"]),
            "venda": float(dados["ask"]),
            "variacao (%)": float(dados["pctChange"])
        }
        cotacoes.append(registro)
    return cotacoes

def formatarHistorico(json_historico):
    historicoBTC = []
    for item in json_historico:
        registro = {
            "data_hora": (datetime.fromtimestamp(int(item["timestamp"]))).strftime("%d/%m/%Y %H:%M:%S"),
            "high": float(item["high"]),
            "low": float(item["low"]),
            "bid": float(item["bid"]),
            "ask": float(item["ask"])
        }
        historicoBTC.append(registro)
    return historicoBTC

#esta API já retorna um array com os dados fornecidos, e usaremos todos eles, portanto, não há necessidade dela, mas por motivo de um futuro tratamento ou troca de API, ela foi criada.
def formatarSelic(json_selic):
    historicoSelic = []
    for item in json_selic:
        registro = {
            "data": str(item["data"]),
            "valor": float(item["valor"])
        }
    historicoSelic.append(registro)
    return historicoSelic
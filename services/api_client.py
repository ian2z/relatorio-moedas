import requests
from datetime import datetime

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
def cotacoes(json_cotacoes):
    cotacoes = []
    for chave, dados in json_cotacoes.items():
        registro = {
            "Moeda": dados["code"],
            "Nome": dados["name"],
            "data_hora": datetime.fromtimestamp(int(dados["timestamp"])).strftime("%d/%m/%Y %H:%M:%S"),
            "Alta": float(dados["high"]),
            "Baixa": float(dados["low"]),
            "Compra": float(dados["bid"]),
            "Venda": float(dados["ask"]),
            "Variacao (%)": float(dados["pctChange"])
        }
        cotacoes.append(registro)
    return cotacoes

def historicoBTC(json_historico):
    historicoBTC = []
    for item in json_historico:
        registro = {
            "data_hora": (datetime.fromtimestamp(int(item["timestamp"]))).strftime("%d/%m/%Y %H:%M:%S"),
            "Alta": float(item["high"]),
            "Baixa": float(item["low"]),
            "Compra": float(item["bid"]),
            "Venda": float(item["ask"])
        }
        historicoBTC.append(registro)
    return historicoBTC

#esta API já retorna um array com os dados fornecidos, e usaremos todos eles, portanto, não há necessidade dela. Por motivo de uma futura alteração ou troca de API, ela foi criada.
def selic(json_selic):
    historicoSelic = []
    for item in json_selic:
        registro = {
            "Data": str(item["data"]),
            "Valor": float(item["valor"])
        }
    historicoSelic.append(registro)
    return historicoSelic
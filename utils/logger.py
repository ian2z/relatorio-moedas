from datetime import datetime

#Função responsável por retornar um registro com data e hora e uma mensagem do log
def gerarLog(mensagem):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return [{"Data/Hora": agora, "Status": mensagem}]

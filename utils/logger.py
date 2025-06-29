from datetime import datetime

def gerarLog(mensagem):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return [{"Data/Hora": agora, "Status": mensagem}]

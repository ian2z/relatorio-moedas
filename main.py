from services.api_client import (
getCotacoes,
getHistoricoBitcoin,
getTaxaSelic,
cotacoes,
historicoBTC,
selic
)
from utils.excel_writer import criarArquivo
from utils.logger import gerarLog


def main():
    try:
        print("[*] Iniciando coleta de dados...")

        #Coleta de dados das APIs
        cotacoes_json = getCotacoes()
        historico_btc_json = getHistoricoBitcoin()
        selic_json = getTaxaSelic()

        print("[✓] Dados coletados com sucesso!")

        #Formatação dos dados usando as funções de array
        cotacoesFormatadas = cotacoes(cotacoes_json)
        historicoBTCFormatado = historicoBTC(historico_btc_json)
        selicFormatada = selic(selic_json)
        log_gerado = gerarLog("Coleta realizada com sucesso")

        #Gerar Excel através do openpyxl
        criarArquivo(
            cotacoes=cotacoesFormatadas,
            historico=historicoBTCFormatado,
            selic=selicFormatada,
            log=log_gerado
        )

        print("[✓] Relatório Excel gerado com sucesso!")

    #Tratamento de erros caso o arquivo não possa ser gerado. Também verifica se o log foi criado
    except Exception as e:
        print("[X] Erro durante a execução:", e)
        log_erro = gerarLog(f"Erro na execução: {e}")
        criarArquivo([], [], [], log_erro)


if __name__ == "__main__":
    main()
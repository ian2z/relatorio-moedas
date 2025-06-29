# 📊 Relatório de Moedas
Este projeto coleta cotações de moedas (USD, EUR, BTC), histórico de preços e taxas de juros (SELIC), e gera um arquivo Excel formatado com resumo, histórico, taxas e log de execução.

## Como usar?
### 1. Crie e ative um ambiente virtual (recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute o script principal

```bash
python main.py
```

Isso vai gerar um arquivo Excel com formato semelhante a `relatorio_20250629_103045.xlsx`.

---

## 📂 Estrutura do projeto

```
relatorio-moedas/
├── main.py                   # Coordena execução: coleta, formatação, gravação
├── config.py                 # URLs e configurações das APIs
├── services/
│   └── api_client.py         # Funções que fazem requisição e formatam os dados
└── utils/
    ├── excel_writer.py       # Geração do arquivo Excel com formatação
    └── logger.py             # Função de log de execução
```

---

## 🛠️ Módulos e responsabilidades

### `config.py`
Contém as URLs para coletar:
- Cotações atuais de USD, EUR, BTC
- Histórico dos últimos 30 dias de uma moeda (BTC por padrão)
- Taxas de juros SELIC (Data da coleta + Porcentagem)

### `services/api_client.py`
Funções que interagem com APIs:
- `getCotacoes()`: busca cotação atual
- `getHistoricoBTC()`: busca histórico de 30 dias
- `getTaxaSelic()`: coleta dados da SELIC
- Funções de formatação para transformar JSON em listas para o Excel

### `utils/excel_writer.py`
Geração do Excel com `openpyxl`:
- 4 abas: Resumo Atual, Histórico, Taxas de Juros, Log
- Cabeçalhos em negrito, números com 2 casas decimais

### `utils/logger.py`
- `gerarLog()`: cria registro de execução para salvar no Excel

---

## 📝 Licença

Este projeto está sob a licença MIT. Fique à vontade para usar, adaptar e contribuir!

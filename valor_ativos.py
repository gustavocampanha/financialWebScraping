import yfinance as yf
from dados_acao import acao

x = 'EMBR3.SA'

def valor_acao(lista_acao):
    for a in range(0, len(lista_acao)):
        acao_info = yf.Ticker(lista_acao).info
        acao_valor = acao_info['currentPrice']
        print(acao_valor)

 
y = 'BRL=X'

def valor_moeda(lista_moeda):

    moeda_info = yf.Ticker(lista_moeda).info
    moeda_valor = moeda_info['regularMarketPrice']
    print(moeda_valor)
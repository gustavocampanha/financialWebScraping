import yfinance as yf

x = ''
def valor_acao(x):
        
    stock_info = yf.Ticker(x).info



    print(stock_info)

    #Moeda = 'regularMarketPrice'
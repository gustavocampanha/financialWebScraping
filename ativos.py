#Importando as bibliotecas necessárias para criarmos a função
import requests
from bs4 import BeautifulSoup
import yfinance as yf

#Criando a função que obtém os dados das moedas na web
""" def ativos(url): """

url = 'https://gustavocampanha.github.io/carteira_investimento/index.html'

#Utilizando as bibliotecas para acessar o conteúdo do site na web
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

#Buscando a classe "moeda" no código HTML
content = soup.find('div', class_='moeda')
#Buscando a tag "td" na classe "moeda"
conteudo_moeda = content.find_all('td')
tam_moeda = len(conteudo_moeda)

#Criando um dicionario e uma lista para armazenarmos os dados das ações
dicionario_ativos = dict()
moedas_estrangeiras = dict()


#Ajustando o armazenamento do conteúdo
for a in range(0,tam_moeda,2):

    #Criando um dicionário do ativo
    dicionario_ativos[conteudo_moeda[a].text] = dict()

    #Adicionando a quantidade de moedas do ativo no dicionário do ativo
    dicionario_ativos[conteudo_moeda[a].text]['Quantidade de Moeda'] = float(conteudo_moeda[a+1].text)

    #Solicitando informações do ativo no Yahoo
    moeda_info = yf.Ticker(conteudo_moeda[a].text).info

    #Adicionando o valor da moeda no dicionário do ativo
    dicionario_ativos[conteudo_moeda[a].text]['Valor de Moeda'] = moeda_info['regularMarketPrice']

    #Descobrindo o valor investido nesse ativo
    quant = float(conteudo_moeda[a+1].text)
    valor = float(moeda_info['regularMarketPrice'])
    tot = quant * valor
    tot = round(tot, 2)

    #Adicionando o valor investido na moeda no dicionário do ativo
    dicionario_ativos[conteudo_moeda[a].text]['Valor Investido'] = tot

    #Adicionando o tipo de ativo
    dicionario_ativos[conteudo_moeda[a].text]['Tipo'] = 'Moeda'


#Buscando a classe "acao" no código HTML
content = soup.find('div', class_='acao')
#Buscando a tag "td" na classe "moeda"
conteudo_acao = content.find_all('td')
tam_acao = len(conteudo_acao)


for a in range(0,tam_acao,2):

    #Criando um dicionário do ativo
    dicionario_ativos[conteudo_acao[a].text] = dict()    
    
    #Adicionando a quantidade de ações do ativo no dicionário do ativo
    dicionario_ativos[conteudo_acao[a].text]['Quantidade de Ações'] = float(conteudo_acao[a+1].text)

    #Solicitando informações do ativo no Yahoo
    acao_info = yf.Ticker(conteudo_acao[a].text).info

    #Adicionando o valor da ação no dicionário do ativo
    dicionario_ativos[conteudo_acao[a].text]['Valor de Ação'] = acao_info['regularMarketPrice']

    #Descobrindo o valor investido nesse ativo
    quant = float(conteudo_acao[a+1].text)
    valor = float(acao_info['regularMarketPrice'])
    tot = quant * valor
    tot = round(tot, 2)

    #Adicionando o valor investido na moeda no dicionário do ativo
    dicionario_ativos[conteudo_acao[a].text]['Valor Investido'] = tot

    #Adicionando o tipo de ativo
    dicionario_ativos[conteudo_acao[a].text]['Tipo'] = 'Ação'

    unidade_moeda_acao = acao_info['currency']

    dicionario_ativos[conteudo_acao[a].text]['Currency'] = unidade_moeda_acao


    if (unidade_moeda_acao != "BRL"):
        moedas_estrangeiras[unidade_moeda_acao] = {"ticker": unidade_moeda_acao.upper() + "BRL=X"}

for unidade_moeda_acao, moeda in moedas_estrangeiras.items():
    ticker = moeda.get("ticker")
    
    t = yf.Ticker(ticker)
    info_ticker = t.info
    moeda["fator_conversao_BRL"] = info_ticker["regularMarketPrice"]


#Testar o codigo antes de tirar esse do comentario
for ticker_ativo, dict_ativo in dicionario_ativos.items():
    unidade_moeda_acao = dict_ativo.get("Currency")
    
    if unidade_moeda_acao == "BRL":
        continue
    
    moeda = moedas_estrangeiras.get(unidade_moeda_acao)
    fator_conversao_BRL = moeda.get("fator_conversao_BRL")
    
    dict_ativo["current_value"] = dict_ativo.get("current_value") * fator_conversao_BRL

print(dicionario_ativos)
print(moedas_estrangeiras)
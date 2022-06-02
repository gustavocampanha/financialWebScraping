from locale import currency
import requests
from bs4 import BeautifulSoup
import yfinance as yf

url = 'https://gustavocampanha.github.io/carteira_investimento/index.html'

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

print(conteudo_moeda)

#Ajustando o armazenamento do conteúdo
for a in range(0,tam_moeda,2):

    #Criando um dicionário do ativo
    dicionario_ativos[conteudo_moeda[a].text] = dict()

    currency = 

    #Adicionando o nome da moedas do ativo no dicionário do ativo
    dicionario_ativos[conteudo_moeda[a].text]['Nome do Ativo'] = conteudo_moeda[a].text

    #Adicionando a quantidade de moedas do ativo no dicionário do ativo
    dicionario_ativos[conteudo_moeda[a].text]['Quantidade do Ativo'] = float(conteudo_moeda[a+1].text)

    #Solicitando informações do ativo no Yahoo
    moeda_info = yf.Ticker(conteudo_moeda[a].text).info

    #Adicionando o valor da moeda no dicionário do ativo
    dicionario_ativos[conteudo_moeda[a].text]['Valor do Ativo'] = moeda_info['regularMarketPrice']

    #Descobrindo o valor investido nesse ativo
    quant = float(conteudo_moeda[a+1].text)
    valor = float(moeda_info['regularMarketPrice'])
    tot = quant * valor
    tot = round(tot, 2)

    #Adicionando o valor investido na moeda no dicionário do ativo
    dicionario_ativos[conteudo_moeda[a].text]['Valor Investido'] = tot

    #Adicionando o tipo de ativo
    dicionario_ativos[conteudo_moeda[a].text]['Tipo'] = 'Moeda'

    dicionario_ativos[conteudo_moeda[a].text]['Currency'] = conteudo_moeda[a].text

print(dicionario_ativos)
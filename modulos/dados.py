#Importando as bibliotecas necessárias para criarmos a função
import bs4
import requests
from bs4 import BeautifulSoup
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import qrcode
import openpyxl
from openpyxl.drawing.image import Image
from openpyxl.styles.alignment import Alignment
from openpyxl.styles import Border, Side, Color, Font, PatternFill
import validators
from time import sleep

#Criando a função para verificar se a URL inserida realmente existe
def verifica_url(url):
    valid = validators.url(url)
    return valid

#Criando a função que obtém os dados dos ativos na página
def ativos(url):

    #Utilizando as bibliotecas para acessar o conteúdo do site na web
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    #Buscando a classe "moeda" no código HTML
    content = soup.find('div', class_='moeda')

    #Buscando a tag "td" na classe "moeda"
    conteudo_moeda = content.find_all('td')
    tam_moeda = len(conteudo_moeda)

    #Criando um dicionario e uma lista para armazenarmos os dados dos ativos
    dicionario_ativos = dict()
    moedas_estrangeiras = dict()

    #Adicionando as moedas no dicionario "dicionario_ativos"
    for a in range(0,tam_moeda,2):

        #Criando um dicionário do ativo
        dicionario_ativos[conteudo_moeda[a].text] = dict()

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

        #Adicionando a currency da moeda
        dicionario_ativos[conteudo_moeda[a].text]['Currency'] = conteudo_moeda[a].text[0:3]


    #Buscando a classe "acao" no código HTML
    content = soup.find('div', class_='acao')

    #Buscando a tag "td" na classe "moeda"
    conteudo_acao = content.find_all('td')
    tam_acao = len(conteudo_acao)

    #Adicionando as ações no dicionario "dicionario_ativos"
    for a in range(0,tam_acao,2):

        #Criando um dicionário do ativo
        dicionario_ativos[conteudo_acao[a].text] = dict()    

        #Adicionando o nome da moedas do ativo no dicionário do ativo
        dicionario_ativos[conteudo_acao[a].text]['Nome do Ativo'] = conteudo_acao[a].text
        
        #Adicionando a quantidade de ações do ativo no dicionário do ativo
        dicionario_ativos[conteudo_acao[a].text]['Quantidade do Ativo'] = float(conteudo_acao[a+1].text)

        #Solicitando informações do ativo no Yahoo
        acao_info = yf.Ticker(conteudo_acao[a].text).info

        #Adicionando o valor da ação no dicionário do ativo
        dicionario_ativos[conteudo_acao[a].text]['Valor do Ativo'] = acao_info['regularMarketPrice']

        #Descobrindo o valor investido nesse ativo
        quant = float(conteudo_acao[a+1].text)
        valor = float(acao_info['regularMarketPrice'])
        tot = quant * valor
        tot = round(tot, 2)

        #Adicionando o valor investido na moeda no dicionário do ativo
        dicionario_ativos[conteudo_acao[a].text]['Valor Investido'] = tot

        #Adicionando o tipo de ativo
        dicionario_ativos[conteudo_acao[a].text]['Tipo'] = 'Ação'

        #Pegando a currency da ação
        unidade_moeda_acao = acao_info['currency']

        #Adicionando a currency da ação no dicionário
        dicionario_ativos[conteudo_acao[a].text]['Currency'] = unidade_moeda_acao

    #Ajustando a currency correta dos ativos
    for dicionario in dicionario_ativos:

        #Pegando a currency do ativo
        currency = dicionario_ativos[dicionario].get("Currency")

        if currency == 'BRL':
            continue

        #Ajustando os cambios para fazer a consulta ao Yahoo Finance
        moedas_estrangeiras[currency] = {"Ticker": currency.upper() + "BRL=X"}
        
        #Fazendo a consulta ao Yahoo Finance
        ativo = yf.Ticker(moedas_estrangeiras[currency]['Ticker'])
        info_ativo = ativo.info

        #Pegando o valor do cambio atual
        fator_multiplicativo = info_ativo['regularMarketPrice']

        #Adicionando o fator do cambio no dicionario das moedas estrangeiras
        moedas_estrangeiras[currency]["Fator Multiplicativo"] = fator_multiplicativo

    #Ajustando o valor do ativo para o cambio do real
    for ticker_ativo, dict_ativo in dicionario_ativos.items():

        unidade_moeda = dict_ativo.get("Currency")
        
        if unidade_moeda == "BRL":
            continue

        if unidade_moeda == None:
            continue
        
        if dict_ativo["Tipo"] == 'Moeda':
            continue

        moeda = moedas_estrangeiras[unidade_moeda]
        fator_conversao_BRL = moeda.get("Fator Multiplicativo")
        
        dict_ativo["Valor do Ativo"] = round(dict_ativo.get("Valor do Ativo") * fator_conversao_BRL, 2)

    #Retornando o dicionario completo e sem necessidade de ajuste
    return dicionario_ativos
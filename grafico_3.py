#Importando as bibliotecas necessárias para criarmos a função
""" from random import randint
import requests
from bs4 import BeautifulSoup
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import qrcode
import openpyxl
from openpyxl.drawing.image import Image
from openpyxl.styles.alignment import Alignment
from openpyxl.styles import Border, Side, Color, Font, PatternFill """

from gusta_tech import ativos

url = 'https://gustavocampanha.github.io/carteira_investimento/joao.html'

dicionario_ativos = {
    'BRL=X': {
        'Nome do Ativo': 'BRL=X',
        'Quantidade do Ativo': 3000.0,
        'Valor do Ativo': 4.7912,
        'Valor Investido': 14373.6,
        'Tipo': 'Moeda',
        'Currency': 'BRL=X'
    },
    'CNYBRL=X': {
        'Nome do Ativo': 'CNYBRL=X',
        'Quantidade do Ativo': 20000.0,
        'Valor do Ativo': 0.71857,
        'Valor Investido': 14371.4,
        'Tipo': 'Moeda',
        'Currency': 'CNYBRL=X'
    },
    'EURBRL=X': {
        'Nome do Ativo': 'EURBRL=X',
        'Quantidade do Ativo': 1500.0,
        'Valor do Ativo': 5.1209,
        'Valor Investido': 7681.35,
        'Tipo': 'Moeda',
        'Currency': 'EURBRL=X'
    },
    'EMBR3.SA': {
        'Nome do Ativo': 'EMBR3.SA',
        'Quantidade do Ativo': 100.0,
        'Valor do Ativo': 12.84,
        'Valor Investido': 1284.0,
        'Tipo': 'Ação',
        'Currency': 'BRL=X'
    },
    'PRIO3.SA': {
        'Nome do Ativo': 'PRIO3.SA',
        'Quantidade do Ativo': 325.0,
        'Valor do Ativo': 28.15,
        'Valor Investido': 9148.75,
        'Tipo': 'Ação',
        'Currency': 'BRL=X'
    },
    'CASH3.SA': {
        'Nome do Ativo': 'CASH3.SA',
        'Quantidade do Ativo': 200.0,
        'Valor do Ativo': 1.91,
        'Valor Investido': 382.0,
        'Tipo': 'Ação',
        'Currency': 'GBPBRL=X'
    },
    'PETR4.SA': {
        'Nome do Ativo': 'PETR4.SA',
        'Quantidade do Ativo': 50.0,
        'Valor do Ativo': 30.02,
        'Valor Investido': 1501.0,
        'Tipo': 'Ação',
        'Currency': 'BRL=X'
    },
    'VIIA3.SA': {
        'Nome do Ativo': 'VIIA3.SA',
        'Quantidade do Ativo': 100.0,
        'Valor do Ativo': 3.09,
        'Valor Investido': 309.0,
        'Tipo': 'Ação',
        'Currency': 'EURBRL=X'
    },
    'ITUB3.SA': {
        'Nome do Ativo': 'ITUB3.SA',
        'Quantidade do Ativo': 200.0,
        'Valor do Ativo': 22.09,
        'Valor Investido': 4418.0,
        'Tipo': 'Ação',
        'Currency': 'USDBRL=X'
    }
}

lista_moedas = list()

for ativo in dicionario_ativos:
    unidade_moeda = dicionario_ativos[ativo].get('Currency')
    valor_investido = dicionario_ativos[ativo].get('Valor Investido')
    lista_moedas.append(unidade_moeda)
    lista_moedas.append(valor_investido)


print(lista_moedas)


""" 
        
    
        

valor_total_acao = round(valor_total_acao, 2)
valor_total_moeda = round(valor_total_moeda, 2)

data = {
    'Moeda': valor_total_moeda,
    'Ação': valor_total_acao
}
plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
plt.title('Disposição de Ativos')


plt.savefig('grafico_2.png')
plt.close() """
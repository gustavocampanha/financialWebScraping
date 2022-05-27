#Importando as bibliotecas necessárias para criarmos a função
import requests
from bs4 import BeautifulSoup
import yfinance as yf

#Criando a função que obtém os dados das moedas na web
def moeda(url):

	#Utilizando as bibliotecas para acessar o conteúdo do site na web
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'lxml')

	#Buscando a classe "acao" no código HTML
	content = soup.find('div', class_='moeda')

	#Buscando a tag "td" na classe "acao"
	conteudo_moeda = content.find_all('td')

	tam = len(conteudo_moeda)

	#Criando um dicionario e uma lista para armazenarmos os dados das ações
	dicionario_moeda = dict()
	lista_dados_moeda = list()

	#Ajustando o armazenamento do conteúdo
	for a in range(0,tam,2):

		dicionario_moeda['Nome da Moeda'] = conteudo_moeda[a].text
		dicionario_moeda['Quantidade de Moeda'] = int(conteudo_moeda[a+1].text)

		moeda_nome = conteudo_moeda[a].text
		moeda_info = yf.Ticker(moeda_nome).info
		moeda_valor = moeda_info['regularMarketPrice']
		dicionario_moeda['Valor da Moeda'] = moeda_valor

		quant = float(conteudo_moeda[a+1].text)
		valor = float(moeda_valor)
		tot = quant * valor

		dicionario_moeda['Valor Investido'] = tot

		lista_dados_moeda.append(dicionario_moeda.copy())

		del dicionario_moeda['Nome da Moeda']
		del dicionario_moeda['Quantidade de Moeda']
		del dicionario_moeda['Valor da Moeda']
		del dicionario_moeda['Valor Investido']

	print(lista_dados_moeda)
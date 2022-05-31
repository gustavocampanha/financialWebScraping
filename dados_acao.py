#Importando as bibliotecas necessárias para criarmos a função
import requests
from bs4 import BeautifulSoup
import yfinance as yf

#Criando a função que obtém os dados das ações na web
def acao(url):

	#Utilizando as bibliotecas para acessar o conteúdo do site na web
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'lxml')

	#Buscando a classe "acao" no código HTML
	content = soup.find('div', class_='acao')

	#Buscando a tag "td" na classe "acao"
	conteudo_acao = content.find_all('td')

	tam = len(conteudo_acao)

	#Criando um dicionario e uma lista para armazenarmos os dados das ações
	dicionario_acao = dict()
	lista_dados_acao = list()

	#Ajustando o armazenamento do conteúdo
	for a in range(0,tam,2):
		
		dicionario_acao['Nome da Ação'] = conteudo_acao[a].text
		dicionario_acao['Quantidade de Ações'] = float(conteudo_acao[a+1].text)

		acao_nome = conteudo_acao[a].text
		acao_info = yf.Ticker(acao_nome).info
		acao_valor = acao_info['currentPrice']
		dicionario_acao['Valor da Ação'] = acao_valor

		quant = float(conteudo_acao[a+1].text)
		valor = float(acao_valor)
		tot = quant * valor
		tot = round(tot, 2)

		dicionario_acao['Valor Investido'] = tot

		lista_dados_acao.append(dicionario_acao.copy())

		del dicionario_acao['Nome da Ação']
		del dicionario_acao['Quantidade de Ações']
		del dicionario_acao['Valor da Ação']
		del dicionario_acao['Valor Investido']

	return lista_dados_acao
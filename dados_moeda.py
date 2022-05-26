#Importando as bibliotecas necessárias para criarmos a função
import requests
from bs4 import BeautifulSoup

#Criando a função que obtém os dados das moedas na web
def moeda(url):

	#Criando um dicionario e uma lista para armazenarmos os dados das moedas
	dicionario_moeda = dict()
	lista_moeda = list()

	#Utilizando as bibliotecas para acessar o conteúdo do site na web
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')

	#Buscando a classe "moeda" no código HTML
	content = soup.find('div', attrs={"class": "moeda"})

	#Buscando a tag "td" na classe "moeda"
	acao = content.find_all('td')

	#Criando uma lista para colocarmos os dados obtidos na forma de string
	acao2 = list()

	#Transformando os tipos primitivos dos dados obtidos em string
	for b in range(0,len(acao)):
		acao2.append(acao[b])
		acao2[b] = str(acao2[b])

	#Removendo as tags de abertura
	for c in range(0, len(acao)):
		acao2[c] = acao2[c][4:]

	#Removendo as tags de fechamento
	for d in range(0, len(acao)):
		acao2[d] = acao2[d][:-5]

	#Ajustando o armazenamento do conteúdo
	for a in range(0,len(acao),2):
		dicionario_moeda['Nome da Moeda'] = acao2[a]
		dicionario_moeda['Quantidade de Moedas'] = acao2[a+1]
		lista_moeda.append(dicionario_moeda.copy())
		del dicionario_moeda['Nome da Moeda']
		del dicionario_moeda['Quantidade de Moedas']

	print(lista_moeda)
import openpyxl
from dados_acao import acao
from dados_moeda import moeda
from random import randint
from openpyxl.drawing.image import Image

""" url = 'https://gustavocampanha.github.io/carteira_investimento/index.html' """

""" ls_acao = acao(url)"""
""" ls_moeda = moeda(url) """


ls_acao = [{'Nome da Ação': 'EMBR3.SA', 'Quantidade de Ações': 100, 'Valor da Ação': 12.5, 'Valor Investido': 1250.0}, {'Nome da Ação': 'PRIO3.SA', 'Quantidade de Ações': 325, 'Valor da Ação': 27.98, 'Valor Investido': 9093.5}]

ls_moeda = [{'Nome da Moeda': 'BRL=X', 'Quantidade de Moeda': 3000, 'Valor da Moeda': 4.7495, 'Valor Investido': 14248.5}, {'Nome da Moeda': 'CNYBRL=X', 'Quantidade de Moeda': 20000, 'Valor da Moeda': 0.70916, 'Valor Investido': 14183.2}]

#Adicionando o Tipo de Investimento no Dicionário de cada Ativo
for a in range(0, len(ls_acao)):
    ls_acao[a]['Tipo'] = 'Ação'

for a in range(0, len(ls_moeda)):
    ls_moeda[a]['Tipo'] = 'Moeda'


#Criar uma planilha chamada book
arquivo = openpyxl.Workbook()

ws = arquivo.active
ws.title = "Tabela"

#Descobrindo o patrimonio total da pessoa
valor_da_carteira = 0
for v_acao in range(0, len(ls_acao)):
    valor_da_carteira += ls_acao[v_acao]['Valor Investido']
for v_moeda in range(0, len(ls_moeda)):
    valor_da_carteira += ls_moeda[v_moeda]['Valor Investido']


#Criar uma página
arquivo.create_sheet('Grafico 1')
arquivo.create_sheet('Grafico 2')
arquivo.create_sheet('Grafico 3')
arquivo.create_sheet('Valor da Carteira')

#Selecionar uma página
pag_inicial = arquivo['Tabela']

header = ["Nome", "Quantidade", "Valor Unitário", "Valor Investido", "Tipo"]

pag_inicial.append(header)

tam_acao = len(ls_acao)
tam_moeda = len(ls_moeda)
tam_total = tam_acao + tam_moeda

#Adicionando dados das ações na tabela
for f in range(0,tam_acao):
    dados_acao_individual = list()
    dados_acao_individual.append(ls_acao[f]['Nome da Ação'])
    dados_acao_individual.append(ls_acao[f]['Quantidade de Ações'])
    dados_acao_individual.append(ls_acao[f]['Valor da Ação'])
    dados_acao_individual.append(ls_acao[f]['Valor Investido'])
    dados_acao_individual.append(ls_acao[f]['Tipo'])
    pag_inicial.append(dados_acao_individual)

#Adicionando dados das moedas na tabela
for f in range(0,tam_moeda):
    dados_moeda_individual = list()
    dados_moeda_individual.append(ls_moeda[f]['Nome da Moeda'])
    dados_moeda_individual.append(ls_moeda[f]['Quantidade de Moeda'])
    dados_moeda_individual.append(ls_moeda[f]['Valor da Moeda'])
    dados_moeda_individual.append(ls_moeda[f]['Valor Investido'])
    dados_moeda_individual.append(ls_acao[f]['Tipo'])
    pag_inicial.append(dados_moeda_individual)


ls_patrimonio = ["Patrimonio Total", valor_da_carteira]
pag_inicial.append(ls_patrimonio)



#Adicionando o QRCode na planilha
pag_qrcode = arquivo['Valor da Carteira']

openpyxl.load_workbook

img = Image("QRCode_Secreto.png") 

img.height = 500

img.width = 500

pag_qrcode.add_image(img, "A1") # “A” representa a coluna e “1” representa a linha em que o canto superior esquerdo da imagem está localizado.

#Salvar a planilha
x = randint(0,100)
arquivo.save(f'Investimento{x}.xlsx')
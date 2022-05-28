import openpyxl
from dados_acao import acao
from dados_moeda import moeda
from random import randint

""" url = 'https://gustavocampanha.github.io/carteira_investimento/index.html' """

""" ls_acao = acao(url)"""
""" ls_moeda = moeda(url) """


#Criar uma planilha chamada book
book = openpyxl.Workbook()

ls_acao = [{'Nome da Ação': 'EMBR3.SA', 'Quantidade de Ações': 100, 'Valor da Ação': 12.5, 'Valor Investido': 1250.0}, {'Nome da Ação': 'PRIO3.SA', 'Quantidade de Ações': 325, 'Valor da Ação': 27.98, 'Valor Investido': 9093.5}]

ls_moeda = [{'Nome da Moeda': 'BRL=X', 'Quantidade de Moeda': 3000, 'Valor da Moeda': 4.7495, 'Valor Investido': 14248.5}, {'Nome da Moeda': 'CNYBRL=X', 'Quantidade de Moeda': 20000, 'Valor da Moeda': 0.70916, 'Valor Investido': 14183.2}]

#Descobrindo o patrimonio total da pessoa
valor_da_carteira = 0
for v_acao in range(0, len(ls_acao)):
    valor_da_carteira += ls_acao[v_acao]['Valor Investido']

for v_moeda in range(0, len(ls_moeda)):
    valor_da_carteira += ls_moeda[v_moeda]['Valor Investido']


""" #Visualizar paginas existentes
print(book.sheetnames) """

""" #Criar uma página
book.create_sheet('Frutas') """

#Selecionar uma página
""" pag_inicial = book['Tabela']

pag_inicial.append(['Nome da Ação', 'Quantidade de Ações', 'Valor da Ação', 'Valor Investido']) """

""" for a in range(0, len(ls_acao)):
    pag_inicial.append(ls_acao[0])
 """


""" pag_inicial.append(['Nome da Moeda', 'Quantidade de Moedas', 'Valor da Moeda', 'Valor Investido']) """


#Salvar a planilha
x = randint(0,100)
""" book.save(f'Carteira{x}.xlsx') """
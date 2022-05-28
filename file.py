#Importando os modulos criados que contem as funcoes do programa
from dados_moeda import moeda
from dados_acao import acao
from qr_generator import qr_generator

#Interface grafica do software
print('-='*60)
print('\033[32m{:^120}\033[m'.format('Bem Vindo ao Gusta TechPy'))
print('-='*60)
print('Somos um software capazes de \033[1manalisarmos dados\033[m de carteira de investidores e colocarmos esses dados em uma planilha Excel')
print('-='*60)

#Solicitando a URL ao usuário
url = input('\033[7mInforme a URL:\033[m ')

ls_acao = acao(url)
ls_moeda = moeda(url)

""" print(ls_acao)
print(ls_moeda)"""

qr_generator(url)
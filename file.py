
#Ajustar ações estrangeiras para BRL


#Importando os modulos criados que contem as funcoes do programa
from dados_moeda import moeda
from dados_acao import acao
from qr_generator import qr_generator
from excel_tabela import excel_tabela
from grafico_1 import graf1

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


graf1(url)
qr_generator(url)
excel_tabela(url)
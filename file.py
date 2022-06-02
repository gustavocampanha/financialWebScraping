#Importando os modulos criados que contem as funcoes do programa
from gusta_tech import ativos, graf1, graf2, graf3, qr_generator, excel_tabela

#Interface grafica do software
print('-='*60)
print('\033[32m{:^120}\033[m'.format('Bem Vindo ao Gusta TechPy'))
print('-='*60)
print('Somos um software capazes de \033[1manalisarmos dados\033[m de carteira de investidores e colocarmos esses dados em uma planilha Excel')
print('-='*60)

#Solicitando a URL ao usuário
url_user = input('\033[7mInforme a URL:\033[m ')

url = url_user.strip()

dicionario_ativos = ativos(url)
graf1(dicionario_ativos)
graf2(dicionario_ativos)
graf3(dicionario_ativos)
qr_generator(dicionario_ativos)
excel_tabela(dicionario_ativos)
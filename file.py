#Importando os modulos criados que contem as funcoes do programa
import dados_moeda
import dados_acao

#Interface grafica do software
print('-='*60)
print('\033[32m{:^120}\033[m'.format('Bem Vindo ao Gusta TechPy'))
print('-='*60)
print('Somos um software capazes de analisarmos dados de carteira de investidores e colocarmos esses dados em uma planilha Excel')
print('-='*60)

#Solicitando a URL ao usuário
url = input('Informe a URL: ')

dados_moeda.moeda(url)
dados_acao.acao(url)
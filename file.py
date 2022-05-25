#Importando o modulo criando que contem as funcoes do programa
import dados_moeda
import dados_acao

#Interface grafica do software
""" print('-='*30)
print('\033[32m{:^60}\033[m'.format('Bem Vindo ao Gusta TechPy'))
print('-='*30)
print('Somos um software capazes de analisarmos dados de carteira de investidores e colocarmos esses dados em uma planilha Excel') """

#Solicitando a URL ao usuário
""" url = input('Informe a URL: ') """


url = 'https://gustavocampanha.github.io/carteira_investimento/index.html'

dados_acao.acao(url)
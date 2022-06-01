import pandas as pd
import matplotlib.pyplot as plt
from dados_acao import acao
from dados_moeda import moeda

def graf2(url):

    ls_moeda = moeda(url)
    ls_acao = acao(url)

    valor_total_moeda = 0
    valor_total_acao = 0

    for a in range(0, len(ls_moeda)):
        valor_total_moeda += ls_moeda[a]['Valor Investido']
    for b in range(0, len(ls_acao)):
        valor_total_acao += ls_acao[b]['Valor Investido']

    valor_total_acao = round(valor_total_acao, 2)
    valor_total_moeda = round(valor_total_moeda, 2)

    ls_ativos = {
        'Moeda': valor_total_moeda,
        'Ação': valor_total_acao
    }
    plt.pie(ls_ativos.values(), labels=ls_ativos.keys(), autopct='%1.1f%%')
    plt.title('Disposição de Ativos')


    plt.savefig('grafico_2.png')
    plt.close()

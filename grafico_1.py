import pandas as pd
import matplotlib.pyplot as plt

from dados_acao import acao
from dados_moeda import moeda

def graf1(url):
    ls_moeda = moeda(url)
    ls_acao = acao(url)

    ls_ativos = list()
    for a in range(0, len(ls_moeda)):
        ls_ativos.append(ls_moeda[a]['Nome da Moeda'])
    for b in range(0, len(ls_acao)):
        ls_ativos.append(ls_acao[b]['Nome da Ação'])

    ls_valor_investido = list()
    for a in range(0, len(ls_moeda)):
        ls_valor_investido.append(ls_moeda[a]['Valor Investido'])
    for b in range(0, len(ls_acao)):
        ls_valor_investido.append(ls_acao[b]['Valor Investido'])

    data = {
        'Ativos': ls_ativos,
        'Valor Investido': ls_valor_investido
    }
    
    df = pd.DataFrame(data,columns=['Ativos','Valor Investido'])
    df.plot(x ='Ativos', y='Valor Investido', kind = 'bar')
    plt.show()
    plt.savefig('grafico_1.png')

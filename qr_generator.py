import qrcode
from dados_acao import acao
from dados_moeda import moeda

def qr_generator(url):

    ls_acao = acao(url)
    ls_moeda = moeda(url)
    #Descobrindo o patrimonio total da pessoa
    valor_da_carteira = 0
    for v_acao in range(0, len(ls_acao)):
        valor_da_carteira += ls_acao[v_acao]['Valor Investido']

    for v_moeda in range(0, len(ls_moeda)):
        valor_da_carteira += ls_moeda[v_moeda]['Valor Investido']


    #Creating an instance of qrcode
    qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)

    valor_final = (f'R$ {valor_da_carteira}')

    qr.add_data(valor_final)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('QRCode_Secreto.png')
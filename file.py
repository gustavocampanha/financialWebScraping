#Importando os modulos criados que contem as funcoes do programa
import modulos

#Função necessária para rodar o programa
url = modulos.interface()
dicionario_ativos = modulos.ativos(url)
graf1 = modulos.graf1(dicionario_ativos)
graf2 = modulos.graf2(dicionario_ativos)
graf3 = modulos.graf3(dicionario_ativos)
qr_code = modulos.qr_generator(dicionario_ativos)
modulos.excel_tabela(dicionario_ativos)
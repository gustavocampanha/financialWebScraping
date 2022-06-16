#Importando os modulos criados que contem as funcoes do programa
import modulos

#Função necessária para rodar o programa
url = modulos.interface()
dicionario_ativos = modulos.ativos(url)
modulos.graf1(dicionario_ativos)
modulos.graf2(dicionario_ativos)
modulos.graf3(dicionario_ativos)
modulos.qr_generator(dicionario_ativos)
modulos.excel_tabela(dicionario_ativos)
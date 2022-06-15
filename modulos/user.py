#Importando as bibliotecas necessárias para criarmos a função
from time import sleep
from modulos.dados import verifica_url, ativos
from modulos.excel import graf1, graf2, graf3, qr_generator, excel_tabela

#Código da interface
def interface():
    print('-='*60)
    sleep(0.2)
    print('\033[32m{:^120}\033[m'.format('Bem Vindo ao Gusta TechPy'))
    sleep(0.2)

    #Criando um ciclo infinito para caso o usuário faça algo que não deva
    while True:
        sleep(0.2)
        print('-='*60)
        sleep(0.2)
        print("""
    [ 1 ] Adicionar URL
    [ 2 ] Sair
            """)
        sleep(0.2)
        print('-='*60)
        sleep(0.2)
        escolha = input('\nEscolha sua opção: ').strip() 

        #Caso o usuário escolha certo, seguimos com o programa
        if escolha == '1':
            sleep(0.2)

            #Vamos armazenar a URL do usuário
            url = input('\n\033[7mInforme a URL:\033[m ')
            while True:

                #A função vai verificar se a URL digitada existe
                if verifica_url(url):
                    return url

                #Tratamento para caso a URL não exista
                else:
                    sleep(0.2)
                    url = input('\n\033[7mInforme a URL:\033[m ') #Vamos armazenar a URL do usuário
                    verifica_url(url)
            break

        #Tratamento caso o usuário deseje sair do programa
        elif escolha == '2':
            break
        
        #Tratamento caso o usuário não escolha nenhuma das opções disoníveis
        else:
            sleep(0.2)
            print("\n\033[31mPor favor, escolha uma opção válida!\033[m")
    
    #Encerrando o código
    sleep(0.2)
    print("\n\033[32mObrigado, Volte Sempre!!\033[m\n")
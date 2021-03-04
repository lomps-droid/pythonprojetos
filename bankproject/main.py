#---------------------------------#
#Criado por: Alexandre Douglas    #
#Open Source!!                    #
#---------------------------------#
from passlib.hash import pbkdf2_sha256 as cryp
import modules #Onde estão armazenado as classes e as funções
from random import randint
#---------------------------------------------------------------------------------------------------------#
# Onde serão armazenados os dados cadastrados                                                             #
#---------------------------------------------------------------------------------------------------------#
# Os dados serão armazenados da seguinte forma:                                                           # 
# Numero da conta: ( Nome do cliente | Senha do cliente | RG | CPF | Email | Telefone | Saldo do cliente )#
dados = {}                                                                                                #
#                                                                                                         #
# Ex: 000: (000,000,000,000,000,000,000.0)                                                                #
#---------------------------------------------------------------------------------------------------------#

#Onde será processado o código
if __name__ == '__main__':
    modules.salvando(dados)
    while True:
        print("1- Login")
        print("2- Cadastro")
        menu = int(input('Opção: '))
        if menu == 1:
            #DECLARAÇÃO DE ALGUMAS VARAVEIS PARA NÃO FICAREM SALVA CASO PRECISE REPITIR O PROCESSO#
            novosaldo = 0
            #-------------------------------------------------------------------------------------#
            contaadd = input('Digite o numero da conta: ')
            for i, x in dados.items():
                nome,senha,rg,cpf, email, telefone, saldo = x
                if cryp.verify(contaadd,i):
                    senhaadd = input('Digite sua senha:')
                    if cryp.verify(senhaadd,senha):
                        continuar = 1
                        while continuar == 1:
                            alterardados = i
                            alterar = 1
                            print(f'Seja bem vindo(a) {nome}')
                            print("1- Realizar um saque")
                            print("2- Fazer uma transferência")
                            print("3- Pagar Boleto")
                            print("4- Exibir Saldo")
                            print("5- Realizar um depósito")
                            print("6- Exibir meus dados")
                            print("0- Sair")
                            menu = int(input('Opção: '))
                            if menu == 3:
                                #O sistema aceita qualquer código que inserir e o valor do boleto é gerado de forma aleatoria entre 100 e 10.000
                                boleto = input('Código do boleto: ')
                                boletovalor = randint(100,1000) #Para alterar o valor gerado pelo boleto, edite os numeros : (100,1000)
                                boletovalor = float(boletovalor)
                                print(f'Valor do boleto: R${boletovalor}')
                                if boletovalor > saldo:
                                    print("Seu saldo não é o suficiente para pagar esse boleto")
                                else:
                                    saldo = saldo - boletovalor
                                    novosaldo = saldo
                                    print(f'Boleto pago com sucesso, seu novo saldo é R${saldo}')
                            if menu == 4:
                                print("|----------SALDO ATUAL----------|")
                                print(f'|Saldo: {saldo}')
                                print("|-------------------------------|")
                            if menu == 5:
                                print("|-------------------------------|")
                                print("Utilize ponto '.' para seperar, caso queira adicionar valores quebrados")
                                depositar = float(input('Valor do deposito: R$ '))
                                saldo = float(saldo)
                                saldo = depositar + saldo
                                print(f'Valor de R${depositar} foi adicionado a conta.')
                                print(f'Novo valor: {saldo}')
                                novosaldo = saldo
                            if menu == 0:
                                continuar = 0
                    else:
                        print("Senha incorreta, tente novamente")
            #-----------------------------IMPORTANTE---------------------------------------------#
            #Nessa área, os valores alterados devem ser enviados para a biblioteca para depois ser enviados para o arquivo
            #Durante as alterações, é salvo o nome da conta na variavel "alterardados" e os outros novos valores em outros variaveis
            #Após isso, é utilizado um 'for' para procurar o valor salvo em "alterardados" e depois é repassado o valor para biblioteca
            if alterar == 1:
                for i, x in dados.items():
                    if i == alterardados:
                        nome,senha,rg,cpf, email, telefone, saldo = x
                adicionar = {alterardados: (nome, senha, rg, cpf, email, telefone, novosaldo)}
            dados.update(adicionar)
            modules.escrevendo(dados)
            #-----------------------------IMPORTANTE---------------------------------------------#
        if menu == 2:
            modules.cadastrado(dados)
            #Salvando dados dentro do arquivo
            modules.escrevendo(dados)       #
            #-------------------------------#
        if menu == 0:
            exit(4)


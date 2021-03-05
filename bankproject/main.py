#---------------------------------#
#Criado por: Alexandre Douglas    #
#Open Source!!                    #
#Email: superb1991@academico.ufs.br #
#---------------------------------#
from passlib.hash import pbkdf2_sha256 as cryp
import modules #Onde estão armazenado as classes e as funções
from random import randint
import os
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
        modules.escrevendo(dados)
        print("1- Login")
        print("2- Cadastro")
        menu = int(input('Opção: '))
        if menu == 1:
            #DECLARAÇÃO DE ALGUMAS VARAVEIS PARA NÃO FICAREM SALVA CASO PRECISE REPITIR O PROCESSO#
            novosaldo = 0
            continuar = 0
            #-------------------------------------------------------------------------------------#
            contaadd = input('Digite o numero da conta: ')
            for i, x in dados.items():
                nome,senha,rg,cpf, email, telefone, saldo = x
                if cryp.verify(contaadd,i):
                    senhaadd = input('Digite sua senha:')
                    if cryp.verify(senhaadd,senha):
                        continuar = 1
                        contalogin = i
                        nomelogin,senhalogin,rglogin,cpflogin,emaillogin,telefonelogin,saldologin = x
                    else:
                        print("Senha incorreta, tente novamente")
            #------------------------------------------------------------------------------------#
            if continuar == 1:
                saldologin = float(saldologin)
                os.system('cls' if os.name == 'nt' else 'clear')
                while continuar == 1:
                    print(f'Seja bem vindo {nomelogin}')
                    print("Seleciona uma operação: ")
                    print("1- Exibir minhas informações")
                    print("2- Realizar um depósito")
                    print("3- Realizar uma transferência")
                    print("0- Sair")
                    menulogin = int(input('Opção: '))
                    if menulogin == 1:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("====================================================")
                        print(f'Nome: {nomelogin}')
                        print(f'RG: {rglogin}')
                        print(f'CPF: {cpflogin}')
                        print(f'Telefone: {telefonelogin}')
                        print(f'Email cadastrado: {emaillogin}')
                        print(f'Saldo: R${saldologin}')
                        print("=====================================================")
                    if menulogin == 2:
                        depositoadd = float(input('Insira o valor que deseja depositar: R$'))
                        saldologin = depositoadd + saldologin
                        adicionarlogin = {contalogin: (nomelogin,senhalogin,rglogin,cpflogin,emaillogin,telefonelogin,saldologin)}
                        dados.update(adicionarlogin)
                    if menulogin == 3:
                        realizartransferencia = 0
                        contatransfere = input('Digite o número da conta que deseja fazer a transferência: ')
                        for i, x in dados.items():
                            nome,senha,rg,cpf, email, telefone, saldo = x
                            if cryp.verify(contatransfere,i):
                                realizartransferencia = 1
                        if realizartransferencia == 1:
                            for y,z in dados.items():
                                nome,senha,rg,cpf, email, telefone, saldo = z
                                if cryp.verify(contatransfere,y):
                                    valortransfere = float(input('Digite o valor: R$'))
                                    if saldologin > valortransfere:
                                        saldo = float(saldo)
                                        totaltransfere = saldo + valortransfere
                                        saldologin = saldologin - valortransfere
                                        adicionar = {y: (nome, senha, rg, cpf, email, telefone, totaltransfere)}
                                        adicionarlogin = {contalogin: (nomelogin,senhalogin,rglogin,cpflogin,emaillogin,telefonelogin,saldologin)}
                                        dados.update(adicionar)
                                        dados.update(adicionarlogin)
                                    else:
                                        print("=====================================================")
                                        print("Saldo não corresponde ao valor introduzido")
                        else:
                            print("Conta não encontrada, tente novamente")
                    if menulogin == 0:
                        continuar = 0
            #-----------------------------IMPORTANTE---------------------------------------------#
        if menu == 2:
            modules.cadastrado(dados)
            #Salvando dados dentro do arquivo
            modules.escrevendo(dados)       #
            #-------------------------------#
        if menu == 0:
            exit(4)


#---------------------------------#
#Criado por: Alexandre Douglas    #
#Open Source!!                    #
#---------------------------------#
from passlib.hash import pbkdf2_sha256 as cryp
import modules #Onde estão armazenado as classes e as funções
#---------------------------------------------------------------------------------------------------------#
# Onde serão armazenados os dados cadastrados                                                             #
#---------------------------------------------------------------------------------------------------------#
# Os dados serão armazenados da seguinte forma:                                                           # 
# Numero da conta: ( Nome do cliente | Senha do cliente | RG | CPF | Email | Telefone | Saldo do cliente )#
dados = {}                                                                                                #
#                                                                                                         #
# Ex: 000: (000,000,000,000,000,000,000)                                                                  #
#---------------------------------------------------------------------------------------------------------#


#Onde será processado o código
if __name__ == '__main__':
    modules.salvando(dados)
    while True:
        print("1- Login")
        print("2- Cadastro")
        menu = int(input('Opção: '))
        if menu == 1:
            contaadd = input('Digite o numero da conta: ')
            for i, x in dados.items():
                nome,senha,rg,cpf, email, telefone, saldo = x
                if cryp.verify(contaadd,i):
                    senhaadd = input('Digite sua senha:')
                    if cryp.verify(senhaadd,senha):
                        print(f'Seja bem vindo(a) {nome}')
                        print("1- Realizar um saque")
                        print("2- Fazer uma transferência")
                        print("3- Pagar Boleto")
                        print("4- Exibir Saldo")
                        print("5- Sair")
                        menu = int(input('Opção: '))
                    else:
                        print("Senha incorreta, tente novamente")
        if menu == 2:
            modules.cadastrado(dados)
            modules.escrevendo(dados)


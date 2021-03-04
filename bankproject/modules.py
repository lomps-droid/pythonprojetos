
from passlib.hash import pbkdf2_sha256 as cryp
from csv import DictReader
from csv import writer
from random import randint
import getpass

# Onde é feita a escrita dos dados dentro do arquivo de clientes
def escrevendo(users):
    with open('clientes.csv', 'w') as arquivo:
        escritor_cvs = writer(arquivo)
        escritor_cvs.writerow(
            ['Conta', 'Nome', 'Senha', 'RG', 'CPF', 'Email', 'Telefone', 'Saldo do cliente'])
        for i, x in users.items():
            nome, senha, rg, cpf, email, telefone, saldo = x
            escritor_cvs.writerow([i, nome, senha,rg,cpf,email,telefone,saldo])
    arquivo.close()
#---------------------------------------------------------------#
# Onde é feita a leitura dos dados dentro do arquivo de clientes
# Nesse código, ele pega as linhas do arquivo, e salva dentro de um dicionário


def salvando(users):
    with open('clientes.csv') as arquivo:
        leitor_cvs = DictReader(arquivo, delimiter=',')
        for linha in leitor_cvs:
            conta = linha['Conta']
            nome = linha['Nome']
            senha = linha['Senha']
            rg = linha['RG']
            cpf = linha['CPF']
            email = linha['Email']
            telefone = linha['Telefone']
            saldo = linha['Saldo do cliente']
            adicionar = {conta: (nome, senha, rg, cpf, email, telefone, saldo)}
            users.update(adicionar)
    arquivo.close()
#---------------------------------------------------------------#


def cadastrado(users):
    cadastrooff = 0
    print("Ao inserir seu CPF e o RG, não insira vírgulas")
    cpfcadastro = input('Digite seu CPF: ')
    for i, x in users.items():
        nome, senha, rg, cpf, email, telefone, saldo = x
        if cpf == cpfcadastro:
            print("Já existe uma conta cadastrada com esse CPF")
            cadastrooff = 1
    if cadastrooff == 0:
        rgcadastro = input('Digite seu RG: ')
        for i, x in users.items():
            nome, senha, rg, cpf, email, telefone, saldo = x
            if rg == rgcadastro:
                print("Já existe uma conta cadastrada com esse RG")
                cadastrooff = 1
    if cadastrooff == 0:
        nomecadastro = input('Digite seu Nome: ')
        emailcadastro = input('Digite seu email: ')
        telefonecadastro = input('Digite seu telefone: ')
        #Gerando numero e senha da conta
        senhacadastro = randint(100000, 999999)
        c = randint(1000, 100000)
        senhaconvert = str(senhacadastro)
        cconvert = str(c)
        print(f'Guarde o número da sua conta: {c}')
        print(f'Senha gerada: {senhacadastro}')
        cconvert = cryp.hash(cconvert, rounds=200000, salt_size = 16)
        senhaconvert = cryp.hash(senhaconvert, rounds=200000, salt_size = 16)
        adicionar = {cconvert: (nomecadastro, senhaconvert, rgcadastro,cpfcadastro, emailcadastro, telefonecadastro, '0')}
    
        users.update(adicionar)

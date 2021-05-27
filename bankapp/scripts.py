from random import randint

users = {}


class Cadastro:
    def __init__(self, name, password, email, cpf, numero = None, cadastro_status = True, senha_status = True):
        self.name = name
        self.password = password
        self.email = email
        self.cpf = cpf
        self.numero = numero
        self.cadastro_status = cadastro_status
        self.senha_status = senha_status

    def cadastro_process(self):
        self.cadastro_status = True
        self.senha_status = True
        if len(str(self.password)) >= 4:
            for i, x in users.items():
                nome, passw, email, cpf, saldo = x
                if self.email == email and self.cpf == cpf:
                    self.cadastro_status = False

            if self.cadastro_status == True:
                self.numero = randint(1000, 10000)
                cadastro_info = { self.numero:(self.name,int(self.password),self.email, self.cpf, 0)}
                users.update(cadastro_info)
                print(users)
        else:
            self.senha_status = False
            return






class Login:
    def __init__(self, numero, password, status = False) -> None:
        #É preciso transformar em inteiro, já que de inicio o sistema só recebe str
        self.numero = int(numero)
        self.password = int(password)
        self.status = status
    def login_process(self):
        for i, x in users.items():
            self.nome, passw, self.email, self.cpf, self.saldo = x
            if i == self.numero:
                if passw == self.password:
                    self.status = True
                    return


class Depositar:
    def __init__(self, numero, valor) -> None:
        self.numero = int(numero)
        self.valor = int(valor)
        self.saldo = 0
        self.nome = ""
        self.passw = 0
        self.email = ""
        self.cpf = ""
    def finish_deposito(self):
        for i , x in users.items():
            if i == self.numero:
                self.nome, self.passw, self.email, self.cpf, self.saldo = x
                self.saldo += self.valor
                users[self.numero] = (self.nome, int(self.passw), self.email, self.cpf, int(self.saldo))
                print(users[self.numero])
                return




                
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import designer
import sqlite3
from random import randint
from passlib.hash import pbkdf2_sha256


def db_create():
    #Aqui será criado nosso Banco de Dados caso ele não exista
    #Conectando ao Banco de Dados
    conexao = sqlite3.connect('baseoriginal.db')
    cursor = conexao.cursor()
    #Criando tabela no Banco de dados caso NÃO exista
    cursor.execute('CREATE TABLE IF NOT EXISTS clients('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'nome STR,'
    'account INTEGER,'
    'password STR,'
    'cpf STR,'
    'email STR'
    ')')
    #Fechando tabela
    cursor.close()
    conexao.close()

class DbServer:
    def __init__(self, usuario, senha, status = False):
        #Variaveis que vão interagir com o banco de dados
        self.nome = None
        self.account = None
        self.password = None
        self.id = None
        self.cpf = None
        self.email = None
        ################################################
        self.usuario = usuario
        self.senha = senha
        self.conexao = None
        self.cursor = None
        ################################################
        self.status = False

    def login_processing(self):
        #Verificando se as entradas estão vazias -> Caso estejam, a função é encerrada
        if self.password == '' or self.usuario == '':
            return
        #Conectando ao Banco de Dados
        self.conexao = sqlite3.connect('baseoriginal.db')
        self.cursor = self.conexao.cursor()
        self.cursor.execute('SELECT * FROM clients')
        for i in self.cursor.fetchall():
            #Salvando tabela dentro das variaveis
            self.id , self.nome, self.account, self.password , self.cpf , self.email = i
            if self.account == int(self.usuario):
                if pbkdf2_sha256.verify(self.senha, self.password):
                    #Variavel que diz se o login foi realizado ( True )  ou não ( False )
                    self.status = True
                    #Fechando Banco de Dados
                    self.cursor.close()
                    self.conexao.close()
                    #Finalizando método
                    return
        #Fechando Banco de Dados
        self.cursor.close()
        self.conexao.close()

class DbRegister:
    def __init__(self, nome, password, cpf, email, status = True) -> None:
        self.nome = nome
        self.password = password
        self.cpf = cpf
        self.email = email
        self.conexao = None
        self.cursor = None
        #Esse Status serve para definir se foi possivel realizar ou não o cadastro
        self.status = True
        self.gerar_numero = None

    def cadastro_processing(self):
        #Verificando se as entradas estão vazias -> Caso estejam, a função é encerrada
        if self.password == '':
            return
        #Conectando ao Banco de Dados
        self.gerar_numero = randint(10000,100000)
        self.conexao = sqlite3.connect('baseoriginal.db')
        self.cursor = self.conexao.cursor()
        self.cursor.execute('SELECT * FROM clients')
        for i in self.cursor.fetchall():
            #Salvando tabela dentro das variaveis
            id , nome, account, password , cpf , email = i
            if self.cpf == cpf or self.email == email:
                #Caso o sistema encontre dados parecidos, abortar a criação de uma nova conta
                self.status = False
                #Fechando Banco de Dados
                self.cursor.close()
                self.conexao.close()
                #Finalizando método
                return
        if self.status == True:

            #Inserindo dados na tabela
            #self.password = int(self.password)
            self.password = pbkdf2_sha256.hash(self.password, rounds= 200000, salt_size = 16)
            self.cursor.execute('INSERT INTO clients (nome, account, password, cpf, email) VALUES (?,?,?,?,?)', (self.nome, self.gerar_numero, self.password, self.cpf, self.email))
            self.conexao.commit()
        #Fechando Banco de Dados
        self.cursor.close()
        self.conexao.close()


#ONDE A APLICAÇÃO EM SI FICA LOCALIZADA
class Aplicacao(QMainWindow, designer.Ui_MainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.btn_login_page1.clicked.connect(self.loginTurn)
        self.btn_register_page1.clicked.connect(self.registerClick)

    def loginTurn(self):
        db_instancia = DbServer(self.inputAccont.text(), self.inputPassword.text())
        db_instancia.login_processing()
        #Caso realize o login, alterar a página
        if db_instancia.status == True:
            self.stackedWidget.setCurrentWidget(self.page_3)
            self.pushButtonReturn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
    def registerClick(self):
        self.stackedWidget.setCurrentWidget(self.page_2)
        self.registerRegister.clicked.connect(self.registerFinish)
        self.registerReturn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))

    def registerFinish(self): #Finalizando o registro
        #self.registerReturn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        db_cadastro = DbRegister(self.registerName.text(),self.registerPassword.text(),self.registerCPF.text(),self.registerEmail.text())
        db_cadastro.cadastro_processing()
        value = str(db_cadastro.gerar_numero)
        self.gerarNumber.setText(value)
        

if __name__ == '__main__':
    db_create()
    qt = QApplication(sys.argv)
    app_open = Aplicacao()
    app_open.show()
    qt.exec_()

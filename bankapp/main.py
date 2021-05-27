import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import design
import scripts


#Adicionando usuários a tabela
u1 = {8899:("Alexandre Douglas",1546,"xand.douglass@gmail.com","046.309.605-38",158000)}
u2 = {6899:("Leandro Oliveira",1234,"leo.oliveira@gmail.com","337.876.810-00",13000)}
u3 = {4899:("Luiz Antônio",1234,"luiz.antonio@gmail.com","500.377.080-40",43750)}
u4 = {9899:("Felipe Loz",1234,"felipe.loz@gmail.com","329.600.560-94",90000)}

scripts.users.update(u1)
scripts.users.update(u2)
scripts.users.update(u3)
scripts.users.update(u4)

class Banco(QMainWindow,design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btn_login.clicked.connect(self.loginTurn)
        self.btn_cadastro.clicked.connect(self.cadastroTurn)

    def loginTurn(self):
        #self.stackedWidget.setCurrentWidget(self.page_3)
        self.login_instancia = scripts.Login(self.inputLogin.text(), self.inputSenha.text())
        self.login_instancia.login_process()
        if self.login_instancia.status == True:
            self.stackedWidget.setCurrentWidget(self.page_3) #Indo para página de login
            self.btn_return.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
            self.btn_saldo.clicked.connect(self.dados_exibir)
            self.btn_deposito.clicked.connect(self.inserir_deposito)
        else:
            self.inputError.setText(
                "Número da conta ou senha incorreta"
            )
            return
    
    def cadastroTurn(self):
        self.stackedWidget.setCurrentWidget(self.page_2)
        #user_login = int(self.inputLogin.text())
        self.buttonCadastro.clicked.connect(self.cadastroEnd)
        self.buttonIniciar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))

    def cadastroEnd(self):
        cadastro_finish = scripts.Cadastro(self.inputName.text(), self.inputSenhaCadastro.text(), self.inputEmail.text(), self.inputCPF.text())
        cadastro_finish.cadastro_process()
        if cadastro_finish.cadastro_status == True:
            exibir_numero = str(cadastro_finish.numero)
            self.contaGerador.setText(
                exibir_numero
            )
        if cadastro_finish.cadastro_status == False:
            self.contaGerador.setText(
                "Dados de conta já existente, tente novamente!"
            )
        if cadastro_finish.senha_status == False:
            self.contaGerador.setText(
                "Senha inválida, tente novamente"
            )

    def dados_exibir(self):
        self.login_instancia.login_process() #Para Atualizar os dados
        self.stackedWidget.setCurrentWidget(self.page_4)
        self.exibir_nome.setText(self.login_instancia.nome)
        exibir_numero = str(self.login_instancia.numero)
        exibir_saldo = f"R${str(self.login_instancia.saldo)},00"
        self.exibir_conta.setText(
            exibir_numero
        )
        self.exibir_saldo.setText(exibir_saldo)
        self.exibir_cpf.setText(self.login_instancia.cpf)
        self.return_button_page_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))

    def inserir_deposito(self):
        self.stackedWidget.setCurrentWidget(self.page_5)
        self.btn_depositar.clicked.connect(self.end_deposito)

    def end_deposito(self):
        deposito_finish = scripts.Depositar(self.login_instancia.numero, self.inputDeposito.text())
        deposito_finish.finish_deposito()
        self.btn_return_page5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    banco_open = Banco()
    banco_open.show()
    qt.exec_()
from PyQt5 import QtWidgets
from tinydb import TinyDB, Query

class BancoApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.db = TinyDB('banco.json')
        self.user = 'usuario'
        self.init_usuario()
        self.init_ui()

    def init_usuario(self):
        User = Query()
        if not self.db.search(User.nome == self.user):
            self.db.insert({'nome': self.user, 'saldo': 0.0})

    def get_saldo(self):
        User = Query()
        return self.db.search(User.nome == self.user)[0]['saldo']

    def set_saldo(self, novo_saldo):
        User = Query()
        self.db.update({'saldo': novo_saldo}, User.nome == self.user)

    def init_ui(self):
        self.setWindowTitle('Terminal Bancário PyQt5')
        self.saldo_label = QtWidgets.QLabel(f"Saldo: R$ {self.get_saldo():.2f}")

        depositar_btn = QtWidgets.QPushButton('Depositar')
        depositar_btn.clicked.connect(self.depositar)
        sacar_btn = QtWidgets.QPushButton('Sacar')
        sacar_btn.clicked.connect(self.sacar)
        sair_btn = QtWidgets.QPushButton('Sair')
        sair_btn.clicked.connect(self.close)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.saldo_label)
        vbox.addWidget(depositar_btn)
        vbox.addWidget(sacar_btn)
        vbox.addWidget(sair_btn)
        self.setLayout(vbox)

    def depositar(self):
        valor, ok = QtWidgets.QInputDialog.getDouble(self, 'Depositar', 'Valor a depositar:')
        if ok and valor > 0:
            novo_saldo = self.get_saldo() + valor
            self.set_saldo(novo_saldo)
            self.saldo_label.setText(f"Saldo: R$ {novo_saldo:.2f}")

    def sacar(self):
        valor, ok = QtWidgets.QInputDialog.getDouble(self, 'Sacar', 'Valor a sacar:')
        if ok and 0 < valor <= self.get_saldo():
            novo_saldo = self.get_saldo() - valor
            self.set_saldo(novo_saldo)
            self.saldo_label.setText(f"Saldo: R$ {novo_saldo:.2f}")

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = BancoApp()
    window.show()
    app.exec_()
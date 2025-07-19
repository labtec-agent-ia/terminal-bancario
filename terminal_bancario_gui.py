import tkinter as tk
from tkinter import messagebox, simpledialog

class BancoApp:
    def __init__(self, master):
        self.master = master
        master.title("Terminal Bancário")
        self.saldo = 0.0

        self.label = tk.Label(master, text="Bem-vindo ao Banco!", font=("Arial", 16))
        self.label.pack(pady=10)

        self.saldo_label = tk.Label(master, text=f"Saldo: R$ {self.saldo:.2f}", font=("Arial", 14))
        self.saldo_label.pack(pady=10)

        self.depositar_btn = tk.Button(master, text="Depositar", command=self.depositar)
        self.depositar_btn.pack(pady=5)

        self.sacar_btn = tk.Button(master, text="Sacar", command=self.sacar)
        self.sacar_btn.pack(pady=5)

        self.sair_btn = tk.Button(master, text="Sair", command=master.quit)
        self.sair_btn.pack(pady=5)

    def atualizar_saldo(self):
        self.saldo_label.config(text=f"Saldo: R$ {self.saldo:.2f}")

    def depositar(self):
        valor = simpledialog.askfloat("Depositar", "Valor a depositar:")
        if valor and valor > 0:
            self.saldo += valor
            self.atualizar_saldo()
            messagebox.showinfo("Sucesso", "Depósito realizado!")
        else:
            messagebox.showwarning("Erro", "Valor inválido.")

    def sacar(self):
        valor = simpledialog.askfloat("Sacar", "Valor a sacar:")
        if valor and 0 < valor <= self.saldo:
            self.saldo -= valor
            self.atualizar_saldo()
            messagebox.showinfo("Sucesso", "Saque realizado!")
        else:
            messagebox.showwarning("Erro", "Saldo insuficiente ou valor inválido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BancoApp(root)
    root.mainloop()
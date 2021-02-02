import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import fn as fn

class EditBankAcount(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.title('Editar cuenta bancaria')
        self.master.geometry('720x150')
        self.master.config(bg = '#34378b')

        frame = tk.LabelFrame(self.master, bg = '#34378b', fg = '#ffffff')
        frame.place(x = 10, y = 20)

        tk.Label(frame, text = 'Número', width = 10).grid(row = 0, column = 0, padx = 10, pady = 5)
        self.number = ttk.Entry(frame, width = 15, justify = tk.CENTER)
        self.number.grid(row = 0, column = 1, padx = 10)

        tk.Label(frame, text = 'Tipo', width = 10).grid(row = 0, column = 2, padx = 10, pady = 5)
        self.type = ttk.Combobox(frame, width = 22)
        self.type.grid(row = 0, column = 3, padx = 10)
        self.type['values'] = self.get_type_acount()

        tk.Label(frame, text = 'Banco', width = 10).grid(row = 1, column = 0, padx = 10, pady = 5)
        self.bank = ttk.Combobox(frame, width = 15)
        self.bank.grid(row = 1, column = 1, padx = 10)
        self.bank['values'] = self.get_bank()

        tk.Label(frame, text = 'CBU', width = 10).grid(row = 1, column = 2)
        self.cbu = ttk.Entry(frame, width = 22, justify = tk.CENTER)
        self.cbu.grid(row = 1, column = 3, padx = 5, pady = 5)

        tk.Label(frame, text = 'Saldo', width = 10).grid(row = 2, column = 2, padx = 5, pady = 5)
        self.balance = ttk.Entry(frame, width = 11, justify = tk.CENTER)
        self.balance.grid(row = 2, column = 3, padx = 5, pady = 5)

        self.update = tk.Button(self.master, text = 'Actualizar', width = 10, height = 2, command = self.update_bank_acount)
        self.update.place(x = 600, y = 20)
        self.close = tk.Button(self.master, text = 'Cerrar', width = 10, height = 2, command = self.master.destroy)
        self.close.place(x = 600, y = 70)

    def get_type_acount(self):
        query = fn.selectDB('acountype', 'ASC')
        db_rows = fn.run_query(query)
        ls_acount = []
        for row in db_rows:
            ls_acount.append(row[1])

        return ls_acount

    def get_bank(self):
        query = fn.selectDB('banks', 'ASC')
        db_rows = fn.run_query(query)
        ls_banks = []
        for row in db_rows:
            ls_banks.append(row[1])

        return ls_banks

    def update_bank_acount(self):
        iid = self.tree.item(self.tree.selection())['text']
        col = ['name', 'cbu', 'balance']
        query = fn.updateBD('bankacount', iid, col)

        num = self.number.get()
        cbu = self.cbu.get()
        balance = self.balance.get()

        parameters = (num, cbu, balance, iid)
        fn.run_query(query, parameters)

        self.get_bank_acount()
        self.disable_edit()


if __name__== '__main__':
    root = tk.Tk()
    app = EditBankAcount(master = root)
    app.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import fn as fn
import bankacount as ba

class addBankAcount(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.title('Agregar cuenta bancaria')
        self.master.geometry('500x185')
        self.master.config(bg = '#34378b')

        frame = tk.LabelFrame(self.master)
        frame.place(x = 10, y = 10)

        tk.Label(frame, text = 'Nombre').grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.name = tk.Entry(frame, width = 23)
        self.name.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = 'w')
        tk.Label(frame, text = 'Tipo').grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.typeacount = ttk.Combobox(frame, state = 'readonly', width = 22)
        self.typeacount.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'w')
        self.typeacount['values'] = fn.get_names('acountype')
        tk.Label(frame, text = 'Banco').grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.bank = ttk.Combobox(frame, state = 'readonly', width = 22)
        self.bank.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'w')
        self.bank['values'] = fn.get_names('banks')
        tk.Label(frame, text = 'CBU').grid(row = 3, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.cbu = tk.Entry(frame, width = 23)
        self.cbu.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = 'w')
        tk.Label(frame, text = 'Saldo').grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.balance = tk.Entry(frame, width = '10')
        self.balance.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')

        tk.Button(self.master, text = 'Aceptar', width = 15, height = 3, command = self.add_bank_acount).place(x = 330, y = 10)
        tk.Button(self.master, text = 'Cancelar', width = 15, height = 3, command = self.close_add_bank_acount).place(x = 330, y = 110)

    def close_add_bank_acount(self):
        self.master.destroy()

    def validar(self):
        return len(self.name.get()) !=0 and len(self.typeacount.get()) !=0 and len(self.bank.get()) !=0 and len(self.cbu.get()) !=0 and len(self.balance.get()) !=0

    def add_bank_acount(self):
        if self.validar():
            idtype = fn.get_id('acountype', self.typeacount.get())
            idbank = fn.get_id('banks', self.bank.get())
            parameters = (self.name.get(), idtype, idbank, self.cbu.get(), self.balance.get())
            fn.run_query(fn.insertDB('bankacount', 5), parameters)
            messagebox.showinfo(title = 'Éxito', message = 'Cuenta agregada con éxito', parent = self.master)
            self.master.destroy()
            ba.BankAcount.get_bank_acount(self)
        else:
            messagebox.showwarning(title = 'Error', message = 'No pueden haber datos incompletos', parent = self.master)
            




if __name__ == "__main__":
    root = tk.Tk()
    app = addBankAcount(master = root)
    app.mainloop()
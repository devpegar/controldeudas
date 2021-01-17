import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import fn as fn
import mod_addbankacount as maba
import mod_editbankacount as meba

class BankAcount(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.title('Cuentas bancarias')
        self.master.geometry('800x300')
        self.master.config(bg = '#34378b')

        frame = tk.LabelFrame(self.master, text = 'Listado de cuentas', bg = '#34378b', fg = '#ffffff')
        frame.place(x = 10, y = 10)

        self.tree = ttk.Treeview(frame, height = 5, columns = ('#1','#2','#3','#4', '#5'))
        self.tree.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 2, sticky = 'ew')

        self.tree.column('#0', width = 30)
        self.tree.heading('#0', text = 'ID')
        self.tree.column('#1', width = 120, anchor = 'center')
        self.tree.heading('#1', text = 'Número')
        self.tree.column('#2', width = 170, anchor = 'center')
        self.tree.heading('#2', text = 'Tipo')
        self.tree.column('#3', width = 130, anchor = 'center')
        self.tree.heading('#3', text = 'Banco')
        self.tree.column('#4', width = 200, anchor = 'center')
        self.tree.heading('#4', text = 'CBU')
        self.tree.column('#5', width = 100, anchor = 'e')
        self.tree.heading('#5', text = 'Saldo')

        #self.tree.bind('<<TreeviewSelect>>', self.selectedItem)
        self.tree.bind('<Button-3>', self.copy_cbu)

        frameBtn = tk.LabelFrame(self.master)
        frameBtn.place(x = 10, y = 200)

        tk.Button(frameBtn, text = 'Agregar', width = 17, bg = '#359f79', activebackground = '#309070', fg = '#ffffff', command = self.open_add_bank_acount).grid(row = 0, column = 0, padx = 5)
        tk.Button(frameBtn, text = 'Editar', width = 17, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 0, column = 1, padx = 5)
        tk.Button(frameBtn, text = 'Cerrar', width = 17, bg = '#359f79', activebackground = '#309070', fg = '#ffffff', command = self.close_add_bank_acount).grid(row = 0, column = 2, padx = 5)

        self.get_bank_acount()

    def get_bank_acount(self):
        records = self.tree.get_children()
        for elements in records:
                self.tree.delete(elements)
        
        db_rows = fn.run_query(fn.selectDB('bankacount'))

        for row in db_rows:
            id = row[0]
            name = row[1]
            typeacc = fn.get_name('acountype', row[2])
            bank = fn.get_name('banks', row[3])
            cbu = str(row[4])
            balance = fn.format_currency(row[5])

            xRow = [id, name, typeacc, bank, cbu, balance]
            self.tree.insert('', 0, text = xRow[0], values = xRow[1:])


    def open_add_bank_acount(self):
        top_level = Toplevel(self)
        maba.addBankAcount(top_level)

    def open_edit_bank_acount(self):
        top_level = Toplevel(self)
        meba.EditBankAcount(top_level)
        
    def close_add_bank_acount(self):
        self.master.destroy()

    def copy_cbu(self, event):
        print(self.tree.item)

if __name__ == "__main__":
    root = tk.Tk()
    app = BankAcount(master = root)
    app.mainloop()

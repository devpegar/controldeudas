import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import mod_addbankacount as maba
import fn as fn

class BankAcount(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.title('Cuentas bancarias')
        self.master.geometry('800x400')
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
        self.tree.bind('<<TreeviewSelect>>', self.get_selected_item)

        tk.Label(frame, text = 'Total saldos', width = 15).grid(row = 1, column = 1, pady = 10, sticky = 'w')
        self.total = tk.Entry(frame, width = 12, justify = tk.CENTER)
        self.total.grid(row = 1, column = 1, padx = 10, sticky = 'e')

        frame_edit = tk.LabelFrame(self.master, bg = '#34378b', fg = '#ffffff')
        frame_edit.place(x = 10, y = 230)

        tk.Label(frame_edit, text = 'Número', width = 10).grid(row = 0, column = 0, padx = 10, pady = 5)
        self.number = ttk.Entry(frame_edit, width = 15, justify = tk.CENTER, state = 'disable')
        self.number.grid(row = 0, column = 1, padx = 10)

        tk.Label(frame_edit, text = 'Tipo', width = 10).grid(row = 0, column = 2, padx = 10, pady = 5)
        self.type = ttk.Combobox(frame_edit, width = 22, state = 'disable')
        self.type.grid(row = 0, column = 3, padx = 10)
        self.type['values'] = self.get_type_acount()

        tk.Label(frame_edit, text = 'Banco', width = 10).grid(row = 1, column = 0, padx = 10, pady = 5)
        self.bank = ttk.Combobox(frame_edit, width = 15, state = 'disable')
        self.bank.grid(row = 1, column = 1, padx = 10)
        self.bank['values'] = self.get_bank()

        tk.Label(frame_edit, text = 'CBU', width = 10).grid(row = 1, column = 2)
        self.cbu = ttk.Entry(frame_edit, width = 22, justify = tk.CENTER, state = 'disable')
        self.cbu.grid(row = 1, column = 3, padx = 5, pady = 5)

        tk.Label(frame_edit, text = 'Saldo', width = 10).grid(row = 0, column = 4, padx = 5, pady = 5)
        self.balance = ttk.Entry(frame_edit, width = 11, justify = tk.CENTER, state = 'disable')
        self.balance.grid(row = 0, column = 5, padx = 5, pady = 5)

        self.update = tk.Button(frame_edit, text = 'Actualizar', width = 10, command = self.update_bank_acount, state = 'disable')
        self.update.grid(row = 1, column = 4, padx = 5, pady = 5, columnspan = 2, sticky = 'ew')

        frameBtn = tk.LabelFrame(self.master)
        frameBtn.place(x = 10, y = 320)

        tk.Button(frameBtn, text = 'Agregar', width = 17, command = self.open_add_bank_acount, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 0, column = 0, padx = 5)
        tk.Button(frameBtn, text = 'Editar', width = 17, command = self.enable_edit, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 0, column = 1, padx = 5)
        tk.Button(frameBtn, text = 'Cerrar', width = 17, bg = '#359f79', activebackground = '#309070', fg = '#ffffff', command = self.close_add_bank_acount).grid(row = 0, column = 2, padx = 5)

        self.get_bank_acount()

    def get_bank_acount(self):
        records = self.tree.get_children()
        for elements in records:
                self.tree.delete(elements)
        
        db_rows = fn.run_query(fn.selectDB('bankacount', 'DESC'))
        suma = 0

        for row in db_rows:
            id = row[0]
            name = row[1]
            typeacc = fn.get_name('acountype', row[2])
            bank = fn.get_name('banks', row[3])
            cbu = str(row[4])
            balance = fn.format_currency(row[5])
            suma += row[5]

            xRow = [id, name, typeacc, bank, cbu, balance]
            self.tree.insert('', 0, text = xRow[0], values = xRow[1:])

        total = '{:.2f}'.format(suma)
        self.total.insert(0, fn.format_currency(total))


    def open_add_bank_acount(self):
        top_level = Toplevel(self)
        maba.addBankAcount(top_level)

    def enable_edit(self):
        if (self.tree.selection()):
            self.number.config(state = 'normal')
            self.cbu.config(state = 'normal')
            self.balance.config(state = 'normal')
            self.enable_btn()
        else:
            messagebox.showwarning(message = 'Debe seleccionar un item a editar', title = 'Advertencia')
    
    def disable_edit(self):
        if (self.tree.selection()):
            self.number.config(state = 'disable')
            self.cbu.config(state = 'disable')
            self.balance.config(state = 'disable')
            self.disable_btn()
        
    def close_add_bank_acount(self):
        self.master.destroy()

    def update_bank_acount(self):
        iid = self.tree.item(self.tree.selection())['text']
        col = ['name', 'cbu', 'balance']
        query = fn.updateBD('bankacount', iid, col)
        parameters = (self.number.get(), self.cbu.get(), self.balance.get(), iid)
        fn.run_query(query, parameters)

        self.disable_edit()
        self.get_bank_acount()
        

    def copy_cbu(self, event):
        item_selected_id = self.tree.selection()
        list_item = self.tree.item(item_selected_id)['values']
        self.clipboard_clear()
        self.clipboard_append(list_item[3])

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

    def get_selected_item(self, event = None):
        ls_values = self.tree.item(self.tree.selection())['values']
        i = 0

        self.enable_edit()

        self.number.delete(0, tk.END)
        self.cbu.delete(0, tk.END)
        self.balance.delete(0, tk.END)

        self.number.insert(0, ls_values[0])

        for t in self.type['values']:
            if ls_values[1] == t:
                self.type.current(i)
                i = 0
                break
            i += 1

        for b in self.bank['values']:
            if ls_values[2] == b:
                self.bank.current(i)
                i = 0
                break
            i += 1

        self.cbu.insert(0, ls_values[3])
        self.balance.insert(0, ls_values[4])

        self.disable_edit()

    def enable_btn(self):
        self.update.config(state = 'normal')

    def disable_btn(self):
        self.update.config(state = 'disable')

        

if __name__ == "__main__":
    root = tk.Tk()
    app = BankAcount(master = root)
    app.mainloop()

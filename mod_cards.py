import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import fn as fn
import mod_add_card as mac
import mod_edit_card as mec

class CreditCards(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.title('Listado de tarjetas de crédito')
        self.master.geometry('565x270')
        self.master.config(bg = '#34378b')

        #Frame para visualizar los datos de las tarjetas de crédito
        frame = tk.LabelFrame(self.master, text = 'Tarjetas de Credito', bg = '#34378b', fg = '#ffffff')
        frame.place(x = 10, y = 10)

        #Creación del treeview y configuración de aspecto
        self.tree = ttk.Treeview(frame, height = 5, columns = ('#1','#2','#3','#4'))
        self.tree.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 4, sticky = 'ew')

        self.tree.column('#0', width = 50)
        self.tree.heading('#0', text = 'ID')
        self.tree.column('#1', width = 165)
        self.tree.heading('#1', text = 'Nombre')
        self.tree.column('#2', width = 100, anchor = 'center')
        self.tree.heading('#2', text = 'Cierre')
        self.tree.column('#3', width = 100, anchor = 'center')
        self.tree.heading('#3', text = 'Vencimiento')
        self.tree.column('#4', width = 100, anchor = 'e')
        self.tree.heading('#4', text = 'Total')

        tk.Label(frame, text = 'Total').grid(row = 1, column = 2, pady = 5, sticky = 'e')
        self.total = tk.Entry(frame, width = 15, justify = tk.CENTER)
        self.total.grid(row = 1, column = 3, padx = 8, pady = 5, sticky = 'e')
        
        #Creación de frame para contener los botones
        frameBtn = tk.LabelFrame(self.master, bg = '#34378b', fg = '#ffffff')
        frameBtn.place(x = 10, y = 210)

        tk.Button(frameBtn, text = 'Agregar', width = 17, command = self.open_add_card, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 0, column = 0, padx = 8, pady = 5)
        tk.Button(frameBtn, text = 'Editar', width = 17, command = self.open_edit_card, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 0, column = 1, padx = 7, pady = 5)
        tk.Button(frameBtn, text = 'Cerrar', width = 17, command = self.close_cards, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 0, column = 2, padx = 8, pady = 5)

        self.get_cards()

    #relleno los datos del treeview desde base de datos
    def get_cards(self):
        records = self.tree.get_children()
        for elements in records:
            self.tree.delete(elements)
        
        db_rows = fn.run_query(fn.selectDB('creditcards', 'DESC'))

        suma= 0

        for row in db_rows:
            id = row[0]
            name = row[1]
            deadline = fn.format_date(row[2])
            duedate = fn.format_date(row[3])
            balance = fn.format_currency(row[4])
            suma += row[4]

            xRow = [id, name, deadline, duedate,balance]
            self.tree.insert('', 0, text = xRow[0], values = xRow[1:])
        self.total.delete(0, tk.END)
        total = '{:.2f}'.format(suma)
        self.total.insert(0, fn.format_currency(total))

    def update_cards(self):
        if fn.validateDateFormat(self.deadline.get()) and fn.validateDateFormat(self.duedate.get()):
            iid = self.item('id')
            col = ['name', 'deadline', 'duedate', 'balance']
            query = fn.updateBD('creditcards', col)

            name = self.name.get()
            deadline = self.deadline.get()
            duedate = self.duedate.get()
            balance = self.balance.get()
            
            parameters = (name, deadline, duedate, balance, iid)
            fn.run_query(query, parameters)
            
            
            self.get_cards()
            # self.tree.selection_remove()
            self.disable_edit()
        else:
            messagebox.showerror(title = 'formato invalido', message = 'La fecha debe tener el formato aaaa-mm-dd')

        

    def open_add_card(self):
        top_level = tk.Toplevel(self)
        mac.AddCard(top_level)
        self.wait_window(top_level)
        self.get_cards()

    def open_edit_card(self):
        lsitem = self.tree.item(self.tree.selection())['values']

        if lsitem != '':
            top_level = Toplevel(self)
            i = 0
            name = lsitem[0]
            deadline = fn.format_date_db(lsitem[1])
            duedate = fn.format_date_db(lsitem[2])
            balance = lsitem[3]

            send = mec.EditCards(top_level)
            send.name.insert(0, name)
            send.deadline.insert(0, deadline)
            send.duedate.insert(0, duedate)
            send.balance.insert(0, balance)
            self.wait_window(top_level)
            self.get_cards()
        else:
            self.message()

    def close_cards(self):
        self.master.destroy()

    def message(self):
        msg = Toplevel(self)
        msg.geometry('300x100')
        msg.title('Error')
        msg.config(bg = '#34378b')
        label = tk.Label(msg, text = 'Debe seleccionar un item para editar', bg = '#34378b', fg = '#ffffff')
        label.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'ew')
        tk.Button(msg, text = 'Cerrar', command = msg.destroy).grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'ew')

if __name__ == "__main__":
    root = tk.Tk()
    app = CreditCards(master = root)
    app.mainloop()

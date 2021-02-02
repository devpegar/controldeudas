import tkinter as tk
from tkinter import messagebox
import fn as fn


class EditCards(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.title('Editar tarjeta de crédito')
        self.master.geometry('500x160')
        self.master.config(bg = '#34378b')


        frame = tk.LabelFrame(self.master, bg = '#34378b', fg = '#ffffff')
        frame.place(x = 10, y = 10)

        tk.Label(frame, text = 'Nombre', bg = '#34378b', fg = '#ffffff').grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.name = tk.Entry(frame, width = 20)
        self.name.grid(row = 0, column = 1, padx = 5, pady = 5)
        tk.Label(frame, text = 'Fecha Cierre', bg = '#34378b', fg = '#ffffff').grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.deadline = tk.Entry(frame, width = 10)
        self.deadline.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'w')
        tk.Label(frame, text = 'Fecha Vencimiento', bg = '#34378b', fg = '#ffffff').grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.duedate = tk.Entry(frame, width = 10)
        self.duedate.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'w')
        tk.Label(frame, text = 'Total', bg = '#34378b', fg = '#ffffff').grid(row = 3, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.balance = tk.Entry(frame, width = 10)
        self.balance.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = 'w')

        tk.Button(self.master, text = 'Actualizar', width = 15, height = 3, command = self.update_card, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').place(x = 340, y = 10)
        tk.Button(self.master, text = 'Cerrar', width = 15, height = 3, command = self.close_edit_card, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').place(x = 340, y = 80)

    def update_card(self):
        name = self.name.get()
        deadline = self.deadline.get()
        duedate = self.duedate.get()
        balance = self.balance.get()

        if name != '' and deadline != '' and duedate != '' and balance != '':
            iid = fn.get_id('creditcards', name)
            col = ['name', 'deadline', 'duedate', 'balance']
            query = fn.updateBD('creditcards', col)
            parameters = (name, deadline, duedate, balance, iid)
            fn.run_query(query, parameters)
            self.close_edit_card()
        else:
            messagebox.showerror(title = 'Error', message = 'No puede haber ningun dato vacio')

    def close_edit_card(self):
        self.master.destroy()
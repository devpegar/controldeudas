import tkinter as tk
from tkinter import ttk, Toplevel, messagebox
import fn as fn
import mod_add_expenses as mae
import mod_edit_expenses as mee

class Expenses(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.title('Listado de gastos')
        self.master.geometry('390x350')
        self.master.config(bg = '#34378b')

        frame = tk.LabelFrame(self.master, text = 'Gastos', bg = '#34378b', fg = '#ffffff')
        frame.place(x = 10, y = 10)

        self.tree = ttk.Treeview(frame, height = 10, columns = ('#1', '#2'))
        self.tree.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)

        self.tree.column('#0', width = 50)
        self.tree.heading('#0', text = 'ID')
        self.tree.column('#1', width = 150)
        self.tree.heading('#1', text = 'Nombre')
        self.tree.column('#2', width = 150)
        self.tree.heading('#2', text = 'Categoria')

        frame_btn = tk.LabelFrame(self.master, bg = '#34378b', fg = '#ffffff')
        frame_btn.place(x = 10, y = 280)

        tk.Button(frame_btn, text = 'Agregar', width = 10, command = self.open_add_expenses, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 0, column = 0, padx = 6, pady = 5)
        tk.Button(frame_btn, text = 'Editar', width = 10, command = self.edit_expenses, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 0, column = 1, padx = 7, pady = 5)
        tk.Button(frame_btn, text = 'Cerrar', width = 10, command = self.close_expenses, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 0, column = 2, padx = 6, pady = 5)

        self.get_expenses()

    def get_expenses(self):
        records = self.tree.get_children()
        for elements in records:
            self.tree.delete(elements)
        
        db_rows = fn.run_query(fn.selectDB('expenses', 'DESC'))

        for row in db_rows:
            iid = row[0]
            name = row[1]
            id_category = row[2]
            category = fn.get_name('category', id_category)

            xRow = [iid, name, category]
            self.tree.insert('', 0, text = xRow[0], values = xRow[1:])

    def open_add_expenses(self):
        top_level = tk.Toplevel(self)
        mae.AddExpenses(top_level)
        self.wait_window(top_level)
        self.get_expenses()

    def close_expenses(self):
        self.master.destroy()

    def edit_expenses(self):
        lsitems = self.tree.item(self.tree.selection())['values']
        top_level = tk.Toplevel(self)
        
        if lsitems != '':
            i = 0
            name = lsitems[0]
            category = lsitems[1]
            send = mee.EditExpenses(top_level)
            send.name.insert(0, name)
            
            for cat in send.category['values']:
                if cat == category:
                    send.category.current(i)
                    break
                i += 1
            self.wait_window(top_level)
            self.get_expenses()
        else:
            messagebox.showwarning(title = 'Atención', message = 'Debe seleccionar un item del listado antes de editarlo')

import tkinter as tk
from tkinter import ttk, Toplevel, messagebox
import fn as fn

class AddExpenses(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.title('Agregar subcategorias')
        self.master.geometry('300x150')
        self.master.config(bg = '#34378b')

        frame = tk.LabelFrame(self.master, bg = '#34378b', fg = '#ffffff')
        frame.place(x = 12, y = 10)

        tk.Label(frame, text = 'Nombre', width = 10, bg = '#34378b', fg = '#ffffff').grid(row = 0, column = 0, padx = 5, pady = 10)
        self.name = tk.Entry(frame, width = 17)
        self.name.grid(row = 0, column = 1, padx = 5, pady = 10)
        self.name.focus()

        tk.Label(frame, text = 'Categoria', width = 10, bg = '#34378b', fg = '#ffffff').grid(row = 1, column = 0, padx = 5, pady = 10)
        self.category = ttk.Combobox(frame, width = 15)
        self.category.grid(row = 1, column = 1, padx = 5, pady = 10)
        self.category['values'] = fn.get_names('category')

        tk.Button(frame, text = 'Agregar', width = 10, command = self.add_expense, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 2, column = 0, padx = 5, pady = 5)
        tk.Button(frame, text = 'Cancelar', width = 10, command = self.close_add_expenses, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'e')

    def add_expense(self):
        if self.name.get() != '' and self.category.get() != '':
            name = self.name.get()
            category = fn.get_id('category', self.category.get())

            query = fn.insertDB('expenses', 2)
            parameters = [name, category]

            fn.run_query(query, parameters)
            messagebox.showinfo(title = 'Éxito', message = 'La subcategoria a sido agregada con exito', parent = self.master)
            self.close_add_expenses()
        else:
            messagebox.showwarning(title = 'Atención!!!', message = 'Las entradas no pueden estar vacias')

    def close_add_expenses(self):
        self.master.destroy()


# if __name__ == '__main__':
#     root = tk.Tk()
#     app = AddExpenses(master=root)
#     app.mainloop()
import tkinter as tk
from tkinter import ttk, Toplevel, messagebox
import fn as fn

class EditExpenses(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.title('Editar subcategorias')
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

        tk.Button(frame, text = 'Actualizar', width = 10, command = self.update_expense, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 2, column = 0, padx = 5, pady = 5)
        tk.Button(frame, text = 'Cancelar', width = 10, command = self.close_edit_expenses, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'e')

    def update_expense(self):
        if self.name.get() != '' and self.category.get() != '':
            name = self.name.get()
            iid= fn.get_id('expenses', name)
            category = fn.get_id('category', self.category.get())
            col = ['name', 'id_category']
            query = fn.updateBD('expenses', col)
            parameters = [name, category, iid]

            fn.run_query(query, parameters)
            messagebox.showinfo(title = 'Éxito', message = 'La subcategoria a sido actualizada con exito', parent = self.master)
            self.close_edit_expenses()
        else:
            messagebox.showwarning(title = 'Atención!!!', message = 'Las entradas no pueden estar vacias')

    def close_edit_expenses(self):
        self.master.destroy()


# if __name__ == '__main__':
#     root = tk.Tk()
#     app = EditExpenses(master=root)
#     app.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import mod_category as cat
import fn as fn

class AddCategory(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.title('Agregar categoria')
        self.master.geometry('300x100')
        self.master.config(bg = '#34378b')

        frame = tk.LabelFrame(self.master, bg = '#34378b')
        frame.place(x = 10, y = 10)

        tk.Label(frame, text = 'Categoria', width = 10, bg = '#34378b', fg = '#ffffff').grid(row = 0, column = 0, padx = 5, pady = 10)
        self.category = tk.Entry(frame, width = 18)
        self.category.grid(row = 0, column = 1, padx = 5, pady = 10)
        self.category.focus()

        tk.Button(frame, text = 'Aceptar', width = 10, command = self.add_category, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 1, column = 0, padx = 5, pady = 5)
        tk.Button(frame, text = 'Cancelar', width = 10, command = self.close_add_category, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'e')

    def add_category(self):
        if self.category.get() != '':
            cat = self.category.get()
            query = fn.insertDB('category', 1)
            
            fn.run_query(query, parameters = (cat,))
            self.close_add_category()
        else:
            messagebox.showerror(title = 'Error', message = 'Casilla de texto no puede estar vacia')

    def close_add_category(self):
        self.master.destroy()






if __name__ == '__main__':
    root = tk.Tk()
    app = AddCategory(master = root)
    app.mainloop()

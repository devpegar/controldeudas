import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import fn as fn

class EditCategory(tk.Frame):
    def __init__(self, iid, master = None):
        super().__init__(master)
        self.master = master
        self.iid = iid
        self.master.title('Editar Categoria')
        self.master.geometry('320x100')
        self.master.config(bg = '#34378b')

        frame = tk.LabelFrame(self.master, bg = '#34378b', fg = '#ffffff')
        frame.place(x = 10, y = 10)

        tk.Label(frame, text = 'Categoria', width = 10, bg = '#34378b', fg = '#ffffff').grid(row = 0, column = 0, padx = 5, pady = 5)
        self.category = tk.Entry(frame, width = 20, justify = tk.CENTER)
        self.category.grid(row = 0, column = 1, padx = 5, pady = 5)
        self.update = tk.Button(frame, text = 'Actualizar', width = 10, command = self.update_category, bg = '#359f79', activebackground = '#309070', fg = '#ffffff')
        self.update.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.close = tk.Button(frame, text = 'Cerrar', width = 10, command = self.master.destroy, bg = '#359f79', activebackground = '#309070', fg = '#ffffff')
        self.close.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'e')

    def update_category(self):
        if self.category.get() != '':
            category = self.category.get()
            iid = self.iid
            col = ['name',]
            query = fn.updateBD('category',col)
            parameters = (category, iid)
            fn.run_query(query, parameters)
            messagebox.showinfo(title = 'Exito', message = 'La categoria ha sido actualizada')
            self.master.destroy()


if __name__== '__main__':
    root = tk.Tk()
    app = EditCategory(master = root)
    app.mainloop()
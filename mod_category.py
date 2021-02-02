import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import fn as fn
import mod_add_category as mc
import mod_edit_category as mec

class Category(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.title('Categorias')
        self.master.geometry('300x300')
        self.master.config(bg = '#34378b')

        frame = tk.LabelFrame(self.master, text = 'Listado de categorias', bg = '#34378b', fg = '#ffffff')
        frame.place(x = 10, y = 10)

        self.tree = ttk.Treeview(frame, height = 6, columns = ('#1'))
        self.tree.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)

        self.tree.column('#0', width = 50)
        self.tree.heading('#0', text = 'ID')
        self.tree.column('#1', width = 210)
        self.tree.heading('#1', text = 'Categoria')

        frame_btn = tk.LabelFrame(self.master, bg = '#34378b', fg = '#ffffff')
        frame_btn.place(x = 10, y = 200)

        tk.Button(frame_btn, text = 'Agregar', width = 12, command = self.open_add_category, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 0, column = 0, padx = 5, pady = 5)
        tk.Button(frame_btn, text = 'Editar', width = 12, command = self.open_edit_category, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 0, column = 1, padx = 6, pady = 5)
        tk.Button(frame_btn, text = 'Cerrar', width = 10, command = self.master.destroy, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = 'ew')

        self.get_category()

    def get_category(self):
        records = self.tree.get_children()
        for elements in records:
            self.tree.delete(elements)
        
        db_rows = fn.run_query(fn.selectDB('category', 'DESC'))

        for row in db_rows:
            self.tree.insert('', 0, text = row[0], values = row[1:])

    def open_edit_category(self):
        ls_items = self.tree.item(self.tree.selection())['values']
        iid = self.tree.item(self.tree.selection())['text']
        if ls_items != '':
            top_level = Toplevel(self)

            cat = ls_items[0]

            send = mec.EditCategory(iid, top_level)

            send.category.insert(0, cat)

            self.wait_window(top_level)
            self.get_category()
        else:
            messagebox.showwarning(message = 'Debe seleccionar un item')

    def open_add_category(self):
        top_level = Toplevel(self)
        mc.AddCategory(top_level)
        self.wait_window(top_level)
        self.get_category()

if __name__ == "__main__":
    root = tk.Tk()
    app = Category(master = root)
    app.mainloop()
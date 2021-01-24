import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import fn as fn
import mod_addcard

class CreditCards(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.title('Listado de tarjetas de crédito')
        self.master.geometry('565x320')
        self.master.config(bg = '#34378b')

        #Frame para visualizar los datos de las tarjetas de crédito
        frame = tk.LabelFrame(self.master, text = 'Tarjetas de Credito', bg = '#34378b', fg = '#ffffff')
        frame.place(x = 10, y = 10)

        #Creación del treeview y configuración de aspecto
        self.tree = ttk.Treeview(frame, height = 5, columns = ('#1','#2','#3','#4'))
        self.tree.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 2, sticky = 'ew')

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

        #Al seleccionar una fila del treeview se dispara una función
        self.tree.bind('<<TreeviewSelect>>', self.selectedItem)

        #Creación del frame para la edición del item seleccionado
        frame_edit = tk.LabelFrame(self.master, bg = '#34378b', fg = '#ffffff')
        frame_edit.place(x = 10, y = 180)

        tk.Label(frame_edit, text = 'Nombre', width = 10, bg = '#34378b', fg = '#ffffff').grid(row = 0, column = 0, padx = 5, pady = 5)
        self.name = tk.Entry(frame_edit, width = 15, state = 'disable')
        self.name.grid(row = 0, column = 1, padx = 5, pady = 5)
        
        tk.Label(frame_edit, text = 'Cierre', width = 10, bg = '#34378b', fg = '#ffffff').grid(row = 0, column = 2, padx = 5, pady = 5)
        self.deadline = tk.Entry(frame_edit, width = 10, state = 'disable')
        self.deadline.grid(row = 0, column = 3, padx = 5, pady = 5)

        self.update = tk.Button(frame_edit, text = 'Actualizar', width = 10, state = 'disable', command = self.update_cards, bg = '#359f79', activebackground = '#309070', fg = '#ffffff')
        self.update.grid(row = 0, column = 4, padx = 5, pady = 5, rowspan = 2, sticky = 'ns')

        tk.Label(frame_edit, text = 'Vencimiento', width = 10, bg = '#34378b', fg = '#ffffff').grid(row = 1, column = 0, padx = 5, pady = 5)
        self.duedate = tk.Entry(frame_edit, width = 10, state = 'disable')
        self.duedate.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'ew')

        tk.Label(frame_edit, text = 'Total', width = 10, bg = '#34378b', fg = '#ffffff').grid(row = 1, column = 2, padx = 5, pady = 5)
        self.balance = tk.Entry(frame_edit, width = 10, state = 'disable')
        self.balance.grid(row = 1, column = 3, padx = 5, pady = 5)
        
        #Creación de frame para contener los botones
        frameBtn = tk.LabelFrame(self.master, bg = '#34378b', fg = '#ffffff')
        frameBtn.place(x = 10, y = 260)

        tk.Button(frameBtn, text = 'Agregar', width = 17, command = self.open_addcard, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 0, column = 0, padx = 8, pady = 5)
        tk.Button(frameBtn, text = 'Editar', width = 17, command = self.enable_edit, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 0, column = 1, padx = 7, pady = 5)
        tk.Button(frameBtn, text = 'Cerrar', width = 17, command = self.close_cards, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 0, column = 2, padx = 8, pady = 5)

        self.get_cCards()

    #relleno los datos del treeview desde base de datos
    def get_cCards(self):
        records = self.tree.get_children()
        for elements in records:
            self.tree.delete(elements)
        
        db_rows = fn.run_query(fn.selectDB('creditcards', 'DESC'))

        for row in db_rows:
            id = row[0]
            name = row[1]
            deadline = row[2]
            duedate = row[3]
            balance = fn.format_currency(row[4])

            xRow = [id, name, deadline, duedate,balance]
            self.tree.insert('', 0, text = xRow[0], values = xRow[1:])

    def update_cards(self):
        iid = self.item('id')
        col = ['name', 'deadline', 'duedate', 'balance']
        query = fn.updateBD('creditcards', iid, col)
        parameters = (self.name.get(),self.deadline.get(),self.duedate.get(),self.balance.get(), iid)
        fn.run_query(query, parameters)
        
        self.disable_edit()
        self.get_cCards()

    def open_addcard(self):
        top_level = tk.Toplevel(self)
        mod_addcard.AddCard(top_level)


    def close_cards(self):
        self.master.destroy()

    
    def selectedItem(self, event = None):
        lsItem = self.item('value')

        self.enable_edit()

        self.name.delete(0, tk.END)
        self.deadline.delete(0, tk.END)
        self.duedate.delete(0, tk.END)
        self.balance.delete(0, tk.END)

        self.name.insert(0, lsItem[0])
        self.deadline.insert(0, lsItem[1])
        self.duedate.insert(0, lsItem[2])
        self.balance.insert(0, lsItem[3])

        self.disable_edit()

        


    def enable_edit(self):
        if (self.tree.selection()):
            self.name.config(state = 'normal')
            self.deadline.config(state = 'normal')
            self.duedate.config(state = 'normal')
            self.balance.config(state = 'normal')
            self.enable_btn()
        else:
            messagebox.showwarning(message = 'Debe seleccionar un item a editar', title = 'Advertencia')

    def disable_edit(self):
        self.name.config(state = 'disable')
        self.deadline.config(state = 'disable')
        self.duedate.config(state = 'disable')
        self.balance.config(state = 'disable')

        self.disable_btn()

    def enable_btn(self):
        self.update.config(state = 'normal')

    def disable_btn(self):
        self.update.config(state = 'disable')

    def item(self, dataget):
        if dataget == 'id':
            selItems = self.tree.selection()
            if selItems:
                selItem = selItems[0]
            iid = self.tree.item(selItem)['text']
            return iid
        elif dataget == 'value':
            selItems = self.tree.selection()
            if selItems:
                selItem = selItems[0]
            values = self.tree.item(selItem)['values']
            return values




if __name__ == "__main__":
    root = tk.Tk()
    app = CreditCards(master = root)
    app.mainloop()

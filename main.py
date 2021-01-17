import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import creditcards as cc
import fn as fn

class Mainapp:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Control gastos mensuales')
        self.wind.geometry('500x250')
        self.wind['bg'] = '#328be0'
        

        tk.Button(self.wind, text = 'Tarjetas de Credito', width = 20, height = 5,
        command = self.CreditCard, bg = '#ffb63e').grid(row = 1, column = 1)
    
    def CreditCard(self):
        self.cCard = Toplevel(window)
        self.cCard.title('Listado de Tarjetas de Credito')
        self.cCard.geometry('550x250')

        frame = tk.LabelFrame(self.cCard, text = 'Tarjetas de Credito')
        frame.place(x = 10, y = 10)

        self.tree = ttk.Treeview(frame, height = 5, columns = ('#1','#2','#3','#4'))
        self.tree.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 2, sticky = 'ew')

        self.tree.column('#0', width = 50)
        self.tree.heading('#0', text = 'ID')
        self.tree.column('#1', width = 150)
        self.tree.heading('#1', text = 'Nombre')
        self.tree.column('#2', width = 100)
        self.tree.heading('#2', text = 'Cierre')
        self.tree.column('#3', width = 100)
        self.tree.heading('#3', text = 'Vencimiento')
        self.tree.column('#4', width = 100)
        self.tree.heading('#4', text = 'Total')

        self.tree.bind('<<TreeviewSelect>>', self.selectedItem)

        frameBtn = tk.LabelFrame(self.cCard)
        frameBtn.place(x = 10, y = 200)

        tk.Button(frameBtn, text = 'Agregar', width = 17, command = self.addCard).grid(row = 0, column = 0, padx = 5)
        tk.Button(frameBtn, text = 'Editar', width = 17, command = self.editCard).grid(row = 0, column = 1, padx = 5)
        tk.Button(frameBtn, text = 'Cerrar', width = 17, command = self.cCard.destroy).grid(row = 0, column = 2, padx = 5)
            
        self.get_cCards()

    def addCard(self):
        self.addCard = Toplevel(self.cCard)
        self.addCard.title('Agregar Tarjeta de Credito')
        self.addCard.geometry('500x150')

        frame = tk.LabelFrame(self.addCard)
        frame.place(x = 10, y = 10)

        tk.Label(frame, text = 'Nombre').grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.addName = tk.Entry(frame, width = 20)
        self.addName.grid(row = 0, column = 1, padx = 5, pady = 5)
        tk.Label(frame, text = 'Fecha Cierre').grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.addDeadline = tk.Entry(frame, width = 10)
        self.addDeadline.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'w')
        tk.Label(frame, text = 'Fecha Vencimiento').grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.addDueDate = tk.Entry(frame, width = 10)
        self.addDueDate.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'w')
        tk.Label(frame, text = 'Total').grid(row = 3, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.addBalance = tk.Entry(frame, width = 10)
        self.addBalance.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = 'w')

        tk.Button(self.addCard, text = 'Aceptar', width = 15, height = 3, command = self.add_cCards).place(x = 340, y = 10)
        tk.Button(self.addCard, text = 'Cancelar', width = 15, height = 3, command = self.addCard.destroy).place(x = 340, y = 80)

    def editCard(self):
        self.editCard = Toplevel(self.cCard)
        self.editCard.title('Editar Tarjeta de Credito')
        self.editCard.geometry('500x150')

        frame = tk.LabelFrame(self.editCard)
        frame.place(x = 10, y = 10)

        tk.Label(frame, text = 'Nombre').grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.editName = tk.Entry(frame, width = 20)
        self.editName.grid(row = 0, column = 1, padx = 5, pady = 5)
        tk.Label(frame, text = 'Fecha Cierre').grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.editDeadline = tk.Entry(frame, width = 10)
        self.editDeadline.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'w')
        tk.Label(frame, text = 'Fecha Vencimiento').grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.editDueDate = tk.Entry(frame, width = 10)
        self.editDueDate.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'w')
        tk.Label(frame, text = 'Total').grid(row = 3, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.editBalance = tk.Entry(frame, width = 10)
        self.editBalance.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = 'w')

        tk.Button(self.editCard, text = 'Actualizar', width = 15, height = 3, command = self.update_cCard).place(x = 340, y = 10)
        tk.Button(self.editCard, text = 'Cancelar', width = 15, height = 3, command = self.editCard.destroy).place(x = 340, y = 80)

        selItem = self.selectedItem()
        
        self.editName.insert(0, selItem['values'][0])
        self.editDeadline.insert(0, selItem['values'][1])
        self.editDueDate.insert(0, selItem['values'][2])
        self.editBalance.insert(0, selItem['values'][3])


    def selectedItem(self, event = None):
        selItems = self.tree.selection()
        if selItems:
            selItem = selItems[0]
            lsItem = self.tree.item(selItem)

        return lsItem


    def get_cCards(self):
        records = self.tree.get_children()
        for elements in records:
            self.tree.delete(elements)
        
        db_rows = fn.run_query(fn.selectDB('creditcards'))

        for row in db_rows:

            self.tree.insert('', 0, text = row[0], values = row[1:])

    def add_cCards(self):
        if self.validar():
            # query = 'INSERT INTO creditcards VALUES(NULL, ?, ?, ?, ?)'
            if fn.validateDate(self.addDeadline.get()):
                if fn.validateDate(self.addDueDate.get()):
                    parameters = (self.addName.get(), self.addDeadline.get(), self.addDueDate.get(), self.addBalance.get())
                    fn.run_query(fn.insertDB(creditcards, 4), parameters)
                    messagebox.showinfo(title = 'Exito', message = 'Tarjeta agregada con éxito', parent = self.addCard)
                    self.addCard.destroy()
                    self.get_cCards()
                else:
                    messagebox.showerror(title = 'Error', message = 'Formato de fecha no admitido. Solo admite aaaa-mm-dd', parent = self.addCard)
            else:
                messagebox.showerror(title = 'Error', message = 'Formato de fecha no admitido. Solo admite aaaa-mm-dd', parent = self.addCard)
    
    def update_cCard(self):
        iid = self.selectedItem()['text']
        col = ['name', 'deadline', 'duedate', 'balance']
        query = fn.updateBD('creditcards', iid, col)
        parameters = (self.editName.get(), self.editDeadline.get(), self.editDueDate.get(), self.editBalance.get(), iid)
        fn.run_query(query, parameters)

    
    def validar(self):
        return len(self.addName.get()) !=0 and len(self.addDeadline.get()) !=0 and len(self.addDueDate.get()) !=0

if __name__ == "__main__":
    window = tk.Tk()
    application = Mainapp(window)
    window.mainloop()
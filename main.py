import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import creditcards as cc
import fn as fn

class Mainapp:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Control gastos mensuales')
        self.wind.geometry('500x250')

        tk.Button(self.wind, text = 'Tarjetas de Credito', width = 20, height = 5,
        command = self.CreditCard).grid(row = 1, column = 1)
    
    def CreditCard(self):
        self.cCard = Toplevel()
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

        frameBtn = tk.LabelFrame(self.cCard)
        frameBtn.place(x = 10, y = 200)

        tk.Button(frameBtn, text = 'Agregar', width = 50).grid(row = 0, column = 0)
        

        self.get_cCards()

    def get_cCards(self):
        records = self.tree.get_children()
        for elements in records:
            self.tree.delete(elements)
        
        query = 'SELECT * FROM creditcards ORDER BY id ASC'
        db_rows = fn.run_query(query)
        
        
        for row in db_rows:
        
            self.tree.insert('', 0, text = row[0], values = row[1:])



if __name__ == "__main__":
    window = tk.Tk()
    application = Mainapp(window)
    window.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import mod_cards as mc
import mod_bankacount as ba
import mod_category as cat
import mod_expenses as exp
import fn as fn

class Mainapp(tk.Frame):

    #Defino la ventana principal, su tamaño y color de fondo
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Control gastos mensuales')
        self.master.geometry('1024x600')
        self.master.config(bg='#34378b')
        
        frame = tk.LabelFrame(self.master, text = 'Cuentas', bg = '#34378b', fg = '#ffffff')
        frame.place(x = 10, y = 10)
        tk.Button(frame, text = 'Tarjetas de Credito', width = 20,
        command = self.open_cards, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 0, column = 0, padx = 5, pady = 5)
        tk.Button(frame, text= 'Cuentas bancarias', width = 20, bg = '#359f79', activebackground = '#309070', fg = '#ffffff', command = self.open_bank_acount).grid(row = 1, column = 0, padx = 5, pady = 5)

        frame2 = tk.LabelFrame(self.master, text = 'Gastos', bg = '#34378b', fg = '#ffffff')
        frame2.place(x = 10, y = 120)
        tk.Button(frame2, text = 'Categorias', width = 20, command = self.open_category, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 0, column = 0, padx = 5, pady = 5)
        tk.Button(frame2, text = 'Gastos', width = 20, command = self.open_expenses, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 1, column = 0, padx = 5, pady = 5)

    def open_cards(self):
        top_level = tk.Toplevel(self)
        mc.CreditCards(top_level)

    def open_bank_acount(self):
        top_level = Toplevel(self)
        ba.BankAcount(top_level)

    def open_category(self):
        top_level = Toplevel(self)
        cat.Category(top_level)

    def open_expenses(self):
        top_level = Toplevel(self)
        exp.Expenses(top_level)




if __name__ == "__main__":
    root = tk.Tk()
    app = Mainapp(master=root)
    app.mainloop()
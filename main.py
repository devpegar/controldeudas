import subprocess
import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import mod_cards as mc
import bankacount as ba
import fn as fn

class Mainapp(tk.Frame):

    #Defino la ventana principal, su tamaño y color de fondo
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.parent.title('Control gastos mensuales')
        self.parent.geometry('1024x600')
        self.parent.config(bg='#34378b')
        
        frame = tk.LabelFrame(self.parent, text = 'Cuentas', bg = '#34378b', fg = '#ffffff')
        frame.place(x = 10, y = 10)
        tk.Button(frame, text = 'Tarjetas de Credito', width = 20,
        command = self.open_cards, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').grid(row = 0, column = 0)
        tk.Button(frame, text= 'Cuentas bancarias', width = 20, bg = '#359f79', activebackground = '#309070', fg = '#ffffff', command = self.open_bank_acount).grid(row = 1, column = 0)

    def open_cards(self):
        top_level = tk.Toplevel(self)
        mc.CreditCards(top_level)

    def open_bank_acount(self):
        top_level = Toplevel(self)
        ba.BankAcount(top_level)



if __name__ == "__main__":
    root = tk.Tk()
    app = Mainapp(parent=root)
    app.mainloop()
import tkinter as tk
from tkinter import ttk, Toplevel, messagebox

class AddCard(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Agregar Tarjeta de Credito')
        self.master.geometry('500x160')
        self.master.config(bg = '#34378b')

        frame = tk.LabelFrame(self.master, bg = '#34378b', fg = '#ffffff')
        frame.place(x = 10, y = 10)

        tk.Label(frame, text = 'Nombre', bg = '#34378b', fg = '#ffffff').grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.addName = tk.Entry(frame, width = 20)
        self.addName.grid(row = 0, column = 1, padx = 5, pady = 5)
        tk.Label(frame, text = 'Fecha Cierre', bg = '#34378b', fg = '#ffffff').grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.addDeadline = tk.Entry(frame, width = 10)
        self.addDeadline.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'w')
        tk.Label(frame, text = 'Fecha Vencimiento', bg = '#34378b', fg = '#ffffff').grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.addDueDate = tk.Entry(frame, width = 10)
        self.addDueDate.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'w')
        tk.Label(frame, text = 'Total', bg = '#34378b', fg = '#ffffff').grid(row = 3, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.addBalance = tk.Entry(frame, width = 10)
        self.addBalance.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = 'w')

        tk.Button(self.master, text = 'Aceptar', width = 15, height = 3, command = self.add_cards, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').place(x = 340, y = 10)
        tk.Button(self.master, text = 'Cerrar', width = 15, height = 3, command = self.close_add_cards, bg = '#359f79', activebackground = '#309070', fg = '#ffffff').place(x = 340, y = 80)
    
    def close_add_cards(self):
        self.master.destroy()

    def add_cards(self):
        if self.validar():
        # query = 'INSERT INTO creditcards VALUES(NULL, ?, ?, ?, ?)'
            if fn.validateDate(self.addDeadline.get()):
                if fn.validateDate(self.addDueDate.get()):
                    parameters = (self.addName.get(), self.addDeadline.get(), self.addDueDate.get(), self.addBalance.get())
                    fn.run_query(fn.insertDB('creditcards', 4), parameters)
                    messagebox.showinfo(title = 'Exito', message = 'Tarjeta agregada con éxito', master = self.addCard)
                    self.addCard.destroy()
                    self.get_cCards()
                else:
                    messagebox.showerror(title = 'Error', message = 'Formato de fecha no admitido. Solo admite aaaa-mm-dd', master = self.addCard)
            else:
                messagebox.showerror(title = 'Error', message = 'Formato de fecha no admitido. Solo admite aaaa-mm-dd', master = self.addCard)
    
    def validar(self):
        return len(self.addName.get()) !=0 and len(self.addDeadline.get()) !=0 and len(self.addDueDate.get()) !=0


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = AddCard(master = root)
#     app.mainloop()
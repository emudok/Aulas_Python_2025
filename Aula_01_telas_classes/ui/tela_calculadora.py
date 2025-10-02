import tkinter as tk
from lib.calculadora import Calculadora

class TelaCalculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculadora') #titulo do programa
        self.geometry('400x300') #altura e largura
        self.resizable(False, False) #nao redimensioanar
        self.grid_columnconfigure(0, weight=200)
        self.grid_rowconfigure(1, weight=200)

        #VARIAVEIS
        #IntVar numeros inteiros
        #DoubleVar numeros com virgula
        #StringVar texto
        self.numero1 = tk.DoubleVar()
        self.numero2 = tk.DoubleVar()
        self.resultado = tk.DoubleVar()

        #CAMPOS
        #rg-> rgb (red, green, blue), vai de 00 até FF
        tk.Label(self, text="Calculadora", font=("Arial",20), fg= "#FF99E8").grid(row=0, padx=10, pady=10)


if __name__=='__main__':
    app = TelaCalculadora()
    app.mainloop()



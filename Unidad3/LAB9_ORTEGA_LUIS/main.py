
import tkinter as tk
from Views.login_view import LoginVentana


class Aplicacion:
    def __init__(self):
        self.root = tk.Tk()
        self.login = LoginVentana(self.root)

    def ejecutar(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()

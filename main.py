import tkinter as tk 
#el tkinter es una biblioteca de python que utilizaremos para crear la ventana flotante, donde el usuario podrá interactuar
from tkinter import messagebox 
#para que se pueda crear una ventana flotante donde el usuario pueda interactuar
import random 
#para utilizarlo luego y poder generar contraseñas aleatoria y seguras
import string
#para usar caracteres a la hora de crear las contraseñas


#comenzamos a crear el generador de contraseñas
def generate_password():
    try:
        length = int(entry_lenght.get()) #pedimos al usuario que introduzca la longitud que quiera para su contraseña
        if length <= 0:
            raise ValueError ("La longitud no puede ser 0, porfavor introduzca un numero valido")
            #salta un error ya que una contraseña no puede tener 0 caracteres, le pedimos que introduzca una longitud valida
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error",f"Entrada no valida: {e}")

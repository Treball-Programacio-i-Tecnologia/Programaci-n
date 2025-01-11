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

#funcion para comprobar la seguridad de una contraseña
def check_password():
    
    password = entry_password.get()
    # se obtiene la contraseña puesta por el usuario
    if len(password) < 8:
        # comprueba si la longitud de la contraseña es inferior a 8 caracteres
        # si es así , muestra un mensaje diciendo que la contraseña es débil
        messagebox.showinfo("Comprobación", "La contraseña es débil: menos de 8 caracteres.")
        
    elif not any(char.isdigit() for char in password):
        #comprueba si la contraseña no tienen ningun numero
        # verifica si al menos un carácter es un dígito
        # si no hay numeros, muestra un mensaje diciendo que la contraseña es débil
        messagebox.showinfo("Comprobación", "La contraseña es débil: no contiene números.")
        
    elif not any(char.isupper() for char in password):
        # comprueba si la contraseña no tiene mayusculas
        # verifica si al menos un caracter es una mayúscula
        # si no hay mayuscula, muestra un mensaje diciendo que la contraseña es débil
        messagebox.showinfo("Comprobación", "La contraseña es débil: no contiene letras mayúsculas.")
        
    elif not any(char in string.punctuation for char in password):
        # comprueba si la contraseña no tiene caracteres especiales
        # verifica si al menos un caracter de la contraseña  pertenece a 'string punctuation'
        # si no hay caracteres especiales, muestra un mensaje diciendo que la contraseña es débil
        messagebox.showinfo("Comprobación", "La contraseña es débil: no contiene caracteres especiales.")
        
    else:
        messagebox.showinfo("Comprobación", "La contraseña es segura.")
        # si la contraseña cumple con todos los requisitos (longitud minima, contiene numeros, letras mayusculas y caracteres especiales), es segura.
        # muestra un mensaje diciendo que la contraseña es segura

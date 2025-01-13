import tkinter as tk 
#el tkinter es una biblioteca de python que utilizaremos para crear la ventana flotante, donde el usuario podrá interactuar
from tkinter import messagebox 
#para que se pueda crear una ventana flotante donde el usuario pueda interactuar
import random 
#para utilizarlo luego y poder generar contraseñas aleatoria y seguras
import string
#para usar caracteres a la hora de crear las contraseñas


#comenzamos a crear el generador de contraseñas
def generador_contraseñas():
    try:
        length = int(entry_length.get()) #pedimos al usuario que introduzca la longitud que quiera para su contraseña
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
def comprobar_contraseña():
    
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


# Crear la ventana principal
ventana = tk.Tk()  # Inicializar la ventana principal
ventana.title("COBAMO: Gestor de contraseñas")  # Establecer el título de la ventana
ventana.geometry("400x300")  # Definir las dimensiones de la ventana (ancho x alto)
ventana.configure(bg="#2E3B4E")  # Establecer el color de fondo de la ventana

# Etiqueta y entrada para la longitud de la contraseña
label_length = tk.Label(  # Crear una etiqueta para indicar al usuario qué hacer
    ventana, 
    text="Longitud de la contraseña:",  # Texto de la etiqueta
    bg="#2E3B4E",  # Color de fondo de la etiqueta
    fg="white",  # Color del texto de la etiqueta
    font=("Arial", 12)  # Fuente y tamaño del texto
)
label_length.pack(pady=10)  # Agregar la etiqueta a la ventana con un margen vertical de 10 píxeles

entry_length = tk.Entry(  # Crear un campo de entrada para que el usuario introduzca la longitud de la contraseña
    ventana, 
    font=("Arial", 12),  # Establecer la fuente y el tamaño del texto
    justify="center",  # Alinear el texto al centro
    bg="#E8E8E8",  # Establecer el color de fondo del campo de entrada
    relief="flat"  # Estilo plano para el borde del campo
)
entry_length.pack(pady=5)  # Agregar el campo de entrada a la ventana con un margen vertical de 5 píxeles

# Botón para generar contraseña
btn_generate = tk.Button(  # Crear un botón para generar una contraseña
    ventana, 
    text="Generar Contraseña",  # Texto que aparece en el botón
    command=generador_contraseñas,  # Función que se ejecutará al hacer clic en el botón (debe estar definida)
    font=("Arial", 12),  # Fuente y tamaño del texto
    bg="#4CAF50",  # Color de fondo del botón
    fg="white",  # Color del texto del botón
    relief="flat",  # Estilo plano para el borde del botón
    activebackground="#45A049"  # Color de fondo del botón cuando está activo (clic o hover)
)
btn_generate.pack(pady=15)  # Agregar el botón a la ventana con un margen vertical de 15 píxeles

# Entrada para mostrar o introducir la contraseña
entry_password = tk.Entry(  # Crear un campo de entrada para mostrar o introducir la contraseña generada
    ventana, 
    width=30,  # Ancho del campo de entrada
    font=("Arial", 12),  # Fuente y tamaño del texto
    justify="center",  # Alinear el texto al centro
    bg="#E8E8E8",  # Establecer el color de fondo del campo de entrada
    relief="flat"  # Estilo plano para el borde del campo
)
entry_password.pack(pady=5)  # Agregar el campo de entrada a la ventana con un margen vertical de 5 píxeles

# Botón para comprobar la contraseña
btn_check = tk.Button(  # Crear un botón para comprobar la seguridad de la contraseña
    ventana, 
    text="Comprobar Contraseña",  # Texto que aparece en el botón
    command=comprobar_contraseña,  # Función que se ejecutará al hacer clic en el botón (debe estar definida)
    font=("Arial", 12),  # Fuente y tamaño del texto
    bg="#2196F3",  # Color de fondo del botón
    fg="white",  # Color del texto del botón
    relief="flat",  # Estilo plano para el borde del botón
    activebackground="#1E88E5"  # Color de fondo del botón cuando está activo (clic o hover)
)
btn_check.pack(pady=15)  # Agregar el botón a la ventana con un margen vertical de 15 píxeles

# Ejecutar la aplicación
ventana.mainloop()  # Iniciar el bucle principal de la aplicación para que la ventana sea interactiva

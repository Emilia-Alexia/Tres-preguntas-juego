# Módulos -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import tkinter as tk
import sqlite3

# Base de datos -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Creación del cursor
basedatos = sqlite3.connect('jugadores.db')
cursor = basedatos.cursor()

# Creamos la tabla
tabla = '''CREATE TABLE IF NOT EXISTS jugadores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            puntuacion INTEGER DEFAULT 0)'''
# Ejecuto la tabla y la confirmo
cursor.execute(tabla)
basedatos.commit()

# Función ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Función para comenzar el juego
def Comenzar_Juego():
    # Variable para almacenar el nombre
    nombre = label_entrada.get().strip() # El strip cogía elementos aun si tuviera espacios
    # Condicional para forzar la entrada
    if nombre:
        # Si existe lo almaceno
        cursor.execute('INSERT INTO jugadores(nombre,puntuacion) VALUES (?,?)',(nombre,0))
        basedatos.commit()
        # La siguiente ventana
        ventana_raiz.destroy()
    else:
        label_mensaje.config(text='Por favor, ingresa un nombre...')
    
# Programa ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Creamos y ajustamos la ventana
ventana_raiz = tk.Tk()
ventana_raiz.title('Login del Juego')
ventana_raiz.geometry('300x250')
ventana_raiz.configure(bg='red')

# Widgets
# Titulo
label_titulo = tk.Label(ventana_raiz,text='Introduzca su usuario',font=('Impact',15))
label_titulo.pack(pady=10)
# Entrada
label_entrada = tk.Entry(ventana_raiz,font=('Arial',12))
label_entrada.pack(pady=10)
# Botón
label_boton = tk.Button(ventana_raiz,border=0,bg='darkorchid',text='Comenzar', command=Comenzar_Juego)
label_boton.pack(pady=10)
# Creación de label por si no introduce un nombre
label_mensaje = tk.Label(ventana_raiz, text='',fg='red', font=('Arial',12))
label_mensaje.pack(pady=10)

# Mainloop
ventana_raiz.mainloop()

# Cierro conexión con la base de datos
cursor.close()
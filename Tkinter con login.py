# Módulos ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import tkinter as tk
import sqlite3
from PIL import ImageTk, Image

# Base de datos --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Creación de la Base de Datos
basedatos = sqlite3.connect('jugadores.db')
cursor = basedatos.cursor()
# Creación de las tablas
tabla = '''CREATE TABLE IF NOT EXISTS jugadores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            puntuacion INTEGER DEFAULT 0)'''
# Ejecutamos y hacemos commit
cursor.execute(tabla)
basedatos.commit()

# Programa -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Función para comenzar el juego
def Comenzar_Juego():
    # Valor del nombre
    nombre = label_entrada.get().strip()
    # Abro condicional, si acierta, se inserta el jugador a la base de datos
    if nombre:
        cursor.execute('INSERT INTO jugadores(nombre, puntuacion) VALUES (?, ?)', (nombre, 0))
        basedatos.commit()
        ventana_raiz.destroy()
        Cuestionario1(nombre)
    else:
        label_mensaje.config(text='Por favor, ingresa un nombre...')

# Función Pregunta 1
def Cuestionario1(nombre_jugador):
    # Creación de ventana
    ventana_secundaria = tk.Tk()
    ventana_secundaria.title('Pregunta 1')
    ventana_secundaria.geometry('300x200')
    # Respuestas
    opciones = {
        'A': 'Federico García Lorca',
        'B': 'Miguel de Cervantes',  # Correcta
        'C': 'Cristiano Ronaldo'
    }
    respuesta_correcta = 'B'

    # Función para responder
    def Responde(eleccion):
        if eleccion == respuesta_correcta:
            cursor.execute('UPDATE jugadores SET puntuacion = puntuacion + 100 WHERE nombre = ?', (nombre_jugador,))
            basedatos.commit()
        ventana_secundaria.destroy()
        Cuestionario2(nombre_jugador)

    # Label para la pregunta
    label_pregunta1 = tk.Label(ventana_secundaria, text='¿Quién escribió Don Quijote?', font=('Arial', 15))
    label_pregunta1.pack(pady=10)

    # Bucle para crear los botones
    for clave, valor in opciones.items():
        texto = f'{clave}. {valor}'
        tk.Button(ventana_secundaria, border=0, bg='gray30', text=texto,
                  command=lambda eleccion=clave: Responde(eleccion)).pack(pady=5)

# Función Pregunta 2
def Cuestionario2(nombre_jugador):
    # Creación de ventana
    ventana_terciaria = tk.Tk()
    ventana_terciaria.title('Pregunta 2')
    ventana_terciaria.geometry('300x200')
    # Respuestas
    opciones = {
        'A': 'Homero',  # Correcta
        'B': 'Platón',
        'C': 'Pitágoras'
    }
    respuesta_correcta = 'A'

    # Función para responder
    def Responde2(eleccion):
        if eleccion == respuesta_correcta:
            cursor.execute('UPDATE jugadores SET puntuacion = puntuacion + 100 WHERE nombre = ?', (nombre_jugador,))
            basedatos.commit()
        ventana_terciaria.destroy()
        Cuestionario3(nombre_jugador)

    # Label para la pregunta
    label_pregunta2 = tk.Label(ventana_terciaria, text='¿Quién escribió La Odisea?', font=('Arial', 15))
    label_pregunta2.pack(pady=10)

    # Bucle para crear los botones
    for clave, valor in opciones.items():
        texto = f'{clave}. {valor}'
        tk.Button(ventana_terciaria, border=0, bg='gray30', text=texto,
                  command=lambda eleccion=clave: Responde2(eleccion)).pack(pady=5)

# Función Pregunta 3
def Cuestionario3(nombre_jugador):
    # Creación de ventana
    ventana_cuarta = tk.Tk()
    ventana_cuarta.title('Pregunta 3')
    ventana_cuarta.geometry('300x200')
    # Respuestas
    opciones = {
        'A': 'Anna Freud',
        'B': 'Carl Gustav Jung',
        'C': 'Sigmund Freud'  # Correcta
    }
    respuesta_correcta = 'C'

    # Función para responder
    def Responde3(eleccion):
        if eleccion == respuesta_correcta:
            cursor.execute('UPDATE jugadores SET puntuacion = puntuacion + 100 WHERE nombre = ?', (nombre_jugador,))
            basedatos.commit()
        ventana_cuarta.destroy()

    # Label para la pregunta
    label_pregunta3 = tk.Label(ventana_cuarta, text='¿Quién es el padre del psicoanálisis?', font=('Arial', 15))
    label_pregunta3.pack(pady=10)

    # Bucle para crear los botones
    for clave, valor in opciones.items():
        texto = f'{clave}. {valor}'
        tk.Button(ventana_cuarta, border=0, bg='gray30', text=texto,
                  command=lambda eleccion=clave: Responde3(eleccion)).pack(pady=5)

# Programa ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ventana principal
ventana_raiz = tk.Tk()
ventana_raiz.title('Login del Juego')
ventana_raiz.geometry('300x250')

# Cargar imagen de fondo (Con try porque si no, no va)
try:
    imagen_fondo = Image.open("fondo.jpg")
except FileNotFoundError:
    imagen_fondo = Image.open(r'D:Semana del 19 al 23\Programación Prácticas\fondo.jpg')
fondo = ImageTk.PhotoImage(imagen_fondo)

# Colocamos la imagen de fondo
fondo_label = tk.Label(ventana_raiz, image=fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1) # Se usa el place para colocar la imagen de fondo en una posición exacta

# Título
label_titulo = tk.Label(ventana_raiz, text='Introduzca su usuario', font=('Impact', 15))
label_titulo.pack(pady=10)

# Entrada
label_entrada = tk.Entry(ventana_raiz, font=('Arial', 12))
label_entrada.pack(pady=10)

# Botón de comenzar
label_boton = tk.Button(ventana_raiz, border=0, bg='darkorchid', text='Comenzar', command=Comenzar_Juego)
label_boton.pack(pady=10)

# Mensaje para cuando la entrada de nombre este vacía
label_mensaje = tk.Label(ventana_raiz, text='', fg='red', font=('Arial', 12))
label_mensaje.pack(pady=10)

# Mainloop
ventana_raiz.mainloop()

cursor.close()
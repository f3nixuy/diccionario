#F3nix
import tkinter as tk
from tkinter import filedialog

# Función para procesar un archivo
def procesar_archivo(archivo):
    palabras = set()
    with open(archivo, 'r') as file:
        for line in file:
            palabras.update(line.split())
    return palabras

# Función para agregar archivos
def agregar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        archivos_seleccionados.append(archivo)
        archivos_seleccionados_label.config(text="Archivos seleccionados:\n" + "\n".join(archivos_seleccionados))

# Función para generar el resultado
def generar_resultado():
    palabras_unicas = set()
    for archivo in archivos_seleccionados:
        palabras_unicas.update(procesar_archivo(archivo))
    
    resultado = 'resultado.txt'
    with open(resultado, 'w') as file:
        file.write('\n'.join(palabras_unicas))

    resultado_label.config(text=f'Se han creado {len(palabras_unicas)} palabras únicas en {resultado}.')

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Unión de Diccionarios")

# Lista (array) para almacenar los archivos seleccionados
archivos_seleccionados = []

# Botones
agregar_button = tk.Button(ventana, text="Agregar Archivo", command=agregar_archivo)
agregar_button.pack()

generar_button = tk.Button(ventana, text="Generar Resultado", command=generar_resultado)
generar_button.pack()

# Etiqueta para mostrar los archivos seleccionados
archivos_seleccionados_label = tk.Label(ventana, text="Archivos seleccionados:")
archivos_seleccionados_label.pack()

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

ventana.mainloop()

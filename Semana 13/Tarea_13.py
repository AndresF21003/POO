import tkinter as tk
from tkinter import messagebox

# Botón "Agregar"
def agregar_dato():
    texto = entrada_texto.get()
    if texto:
        lista_datos.insert(tk.END, texto) # Agrega el texto
        entrada_texto.delete(0, tk.END)   # Limpia el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese algún dato.")

# Botón "Limpiar"
def limpiar_lista():
    lista_datos.delete(0, tk.END) # Borra t0do el contenido de la lista

# Crear la Ventana
ventana = tk.Tk()
ventana.title("Gestor de Datos Visual")
ventana.geometry("300x400")

# Etiquetas para instrucciones
etiqueta_instruccion = tk.Label(ventana, text="Ingrese un dato:")
etiqueta_instruccion.pack(pady=10)

# Entrada de datos
entrada_texto = tk.Entry(ventana)
entrada_texto.pack(pady=5)

# Botón "Agregar" con su evento
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar los datos
lista_datos = tk.Listbox(ventana)
lista_datos.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Botón "Limpiar" para borrar la lista
boton_limpiar = tk.Button(ventana, text="Limpiar Lista", command=limpiar_lista)
boton_limpiar.pack(pady=10)

ventana.mainloop()
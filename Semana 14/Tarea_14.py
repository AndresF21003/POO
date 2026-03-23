import tkinter as tk
from tkinter import ttk, messagebox

def agregar_evento():
    # Obtener los datos
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    desc = entry_desc.get()

    # Validar los campos
    if fecha and hora and desc:
        # Insertar los datos en el Treeview (Lista)
        tree.insert("", tk.END, values=(fecha, hora, desc))

        # Limpiar los campos
        entry_fecha.delete(0, tk.END)
        entry_hora.delete(0, tk.END)
        entry_desc.delete(0, tk.END)
    else:
        # Ventana si faltan datos
        messagebox.showwarning("Campos incompletos", "Por favor, llena todos los campos.")


def eliminar_evento():
    seleccion = tree.selection()

    if seleccion:
        # Ventana para confirmar la eliminación
        confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar el evento seleccionado?")
        if confirmar:
            # Eliminar el ítem
            for item in seleccion:
                tree.delete(item)
    else:
        # Advertencia si se intenta eliminar sin seleccionar nada
        messagebox.showinfo("Selección requerida", "Selecciona un evento de la lista para eliminar.")


# Ventana Principal

root = tk.Tk()
root.title("Agenda Personal")
root.geometry("600x600")

# 1. Panel para Controles de Entrada
panel_entrada = tk.Frame(root, borderwidth=2, relief="groove", bg="Light gray")
panel_entrada.pack(padx=10, pady=10, fill=tk.X)

titulo_entrada = tk.Label(panel_entrada, text="Agregar Nuevo Evento", bg="Light gray", font=("Arial", 12, "bold"))
titulo_entrada.pack(side=tk.TOP, fill=tk.X, pady=5)

# Metodo alternativo para DatePicker
tk.Label(panel_entrada, text="Fecha (DD/MM/AAAA):", bg="Light gray").pack(side=tk.TOP, fill=tk.X, padx=5)
entry_fecha = tk.Entry(panel_entrada)
entry_fecha.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

tk.Label(panel_entrada, text="Hora (HH:MM):", bg="Light gray").pack(side=tk.TOP, fill=tk.X, padx=5)
entry_hora = tk.Entry(panel_entrada)
entry_hora.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

tk.Label(panel_entrada, text="Descripción del evento:", bg="Light gray").pack(side=tk.TOP, fill=tk.X, padx=5)
entry_desc = tk.Entry(panel_entrada)
entry_desc.pack(side=tk.TOP, fill=tk.X, padx=5, pady=2)

# Botón vinculado a la función agregar_evento
btn_agregar = tk.Button(panel_entrada, text="Agregar Evento", command=agregar_evento)
btn_agregar.pack(side=tk.TOP, pady=10)

# 2. Panel para la Lista de Eventos
panel_lista = tk.Frame(root, borderwidth=2, relief="groove")
panel_lista.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

titulo_lista = tk.Label(panel_lista, text="Eventos Programados", font=("Arial", 12, "bold"))
titulo_lista.pack(side=tk.TOP, fill=tk.X, pady=5)

# Tree View (Árbol)
columnas = ("Fecha", "Hora", "Descripción")
tree = ttk.Treeview(panel_lista, columns=columnas, show="headings")

# Configurar las cabeceras de las columnas
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")

# Ancho de las columnas
tree.column("Fecha", width=100)
tree.column("Hora", width=100)
tree.column("Descripción", width=300)

tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# 3. Panel para Acciones Finales
panel_acciones = tk.Frame(root)
panel_acciones.pack(padx=10, pady=10, fill=tk.X)

# Botón para eliminar el evento
btn_eliminar = tk.Button(panel_acciones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.pack(side=tk.LEFT, padx=5)

# Botón para salir
btn_salir = tk.Button(panel_acciones, text="Salir", command=root.quit)
btn_salir.pack(side=tk.RIGHT, padx=5)

root.mainloop()
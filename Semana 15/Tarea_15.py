import tkinter as tk
from tkinter import messagebox

def anadir_tarea(event=None):
    tarea = entrada_tarea.get()
    if tarea != "":
        # Inserta la tarea al final del Listbox
        lista_tareas.insert(tk.END, tarea)
        # Limpia el campo de entrada
        entrada_tarea.delete(0, tk.END)
    else:
        # Alerta) si el campo está vacío
        messagebox.showwarning("Advertencia", "Por favor, escribe una tarea.")


def marcar_completada(event=None):
    try:
        # Obtener el índice de la tarea
        indice = lista_tareas.curselection()
        tarea = lista_tareas.get(indice)

        # Validación para no marcarla dos veces
        if not tarea.endswith(" (Completada)"):
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, tarea + " (Completada)")
            # Cambiar el color de la fuente
            lista_tareas.itemconfig(indice, {'fg': 'gray'})
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para completarla.")


def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()
        lista_tareas.delete(indice)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminarla.")

# Interfaz Gráfica de Usuario (GUI)

# Crear la ventana principal

root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x450")

# Campo de entrada
entrada_tarea = tk.Entry(root, width=40, font=("Arial", 12))
entrada_tarea.pack(pady=15)

# Registro y Vinculación de Eventos

# Relación directa entre un evento y el manejador

# Click de Mouse mediante 'command'
boton_anadir = tk.Button(root, text="Añadir Tarea", command=anadir_tarea, bg="lightblue")
boton_anadir.pack(pady=5)

boton_completar = tk.Button(root, text="Marcar como Completada", command=marcar_completada, bg="lightgreen")
boton_completar.pack(pady=5)

boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea, bg="lightcoral")
boton_eliminar.pack(pady=5)

# Componente para mostrar las tareas
lista_tareas = tk.Listbox(root, width=45, height=12, font=("Arial", 11))
lista_tareas.pack(pady=15)

# Pulsación de tecla 'Enter'

# Vincular el escuchador al campo de texto
entrada_tarea.bind('<Return>', anadir_tarea)

# Doble clic en un elemento de la lista
# Vincular el escuchador a la lista de tareas
lista_tareas.bind('<Double-Button-1>', marcar_completada)

root.mainloop()
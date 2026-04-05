import tkinter as tk


class GestorTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Pendientes")
        self.root.geometry("400x450")

        # Interfaz Gráfica
        # Entry
        self.entrada_tarea = tk.Entry(root, width=40)
        self.entrada_tarea.pack(pady=10)

        # Botón añadir
        self.btn_anadir = tk.Button(root, text='Añadir Tarea', command=self.anadir_tarea)
        self.btn_anadir.pack(pady=5)

        # Botón completar
        self.btn_completar = tk.Button(root, text='Marcar Completada', command=self.completar_tarea)
        self.btn_completar.pack(pady=5)

        # Botón eliminar
        self.btn_eliminar = tk.Button(root, text='Eliminar Tarea', command=self.eliminar_tarea)
        self.btn_eliminar.pack(pady=5)

        # Mostrar la lista
        self.lista_tareas = tk.Listbox(root, width=50, height=15)
        self.lista_tareas.pack(pady=10)

        # Vinculación de Eventos de Teclado
        # Se asocian teclas a sus respectivos eventos
        self.root.bind("<Return>", self.manejador_tecla_anadir)
        self.root.bind("<c>", self.manejador_tecla_completar)
        self.root.bind("<C>", self.manejador_tecla_completar)
        self.root.bind("<Delete>", self.manejador_tecla_eliminar)
        self.root.bind("<d>", self.manejador_tecla_eliminar)
        self.root.bind("<D>", self.manejador_tecla_eliminar)
        self.root.bind("<Escape>", self.cerrar_aplicacion)

    # Manejadores de Eventos
    def anadir_tarea(self):
        tarea = self.entrada_tarea.get()
        if tarea != "":
            self.lista_tareas.insert(tk.END, tarea)
            self.entrada_tarea.delete(0, tk.END)  # Limpia el campo

    def completar_tarea(self):
        try:
            # Indice de la tarea seleccionada
            indice = self.lista_tareas.curselection()[0]
            tarea_texto = self.lista_tareas.get(indice)

            # Gestión de estado y feedback al usuario
            if not tarea_texto.startswith("[✓]"):
                self.lista_tareas.delete(indice)
                self.lista_tareas.insert(indice, f"[✓] {tarea_texto}")
                self.lista_tareas.itemconfig(indice, {'fg': 'gray'})
        except IndexError:
            # Manejo por si no hay ninguna tarea
            pass

    def eliminar_tarea(self):
        try:
            indice = self.lista_tareas.curselection()[0]
            self.lista_tareas.delete(indice)
        except IndexError:
            pass

    # Wrappers
    # Funciones vinculadas con .bind() reciben un objeto 'event'
    def manejador_tecla_anadir(self, event):
        self.anadir_tarea()

    def manejador_tecla_completar(self, event):
        self.completar_tarea()

    def manejador_tecla_eliminar(self, event):
        self.eliminar_tarea()

    def cerrar_aplicacion(self, event):
        self.root.destroy()


if __name__ == "__main__":
    # Ventana principal
    ventana_principal = tk.Tk()
    app = GestorTareasApp(ventana_principal)
    # Ciclo de eventos
    ventana_principal.mainloop()
class Producto:

    def __init__(self, id_producto, nombre, cantidad, precio):
        # Constructor para inicializar los atributos
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos para obtener valores
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos para modificar valores
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        # Metodo auxiliar para mostrar el producto como texto legible
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"

class Inventario:

    def __init__(self):
        # Inicializamos una lista vacía
        self.productos = []

    def agregar_producto(self, nuevo_producto):
        # Añade un nuevo producto verificando que el ID sea único
        # Verificamos si el ID ya existe iterando la lista
        for p in self.productos:
            if p.get_id() == nuevo_producto.get_id():
                print(f"Error: El ID {nuevo_producto.get_id()} ya existe en el inventario.")
                return False

        # Si no existe, usamos .append() para añadir al final de la lista
        self.productos.append(nuevo_producto)
        print("Producto añadido exitosamente.")
        return True

    def eliminar_producto(self, id_producto):
        # Elimina un producto buscando por su ID
        for p in self.productos:
            if p.get_id() == id_producto:
                # Usamos .remove() para sacar el objeto de la lista
                self.productos.remove(p)
                print(f"Producto con ID {id_producto} eliminado.")
                return True
        print("Error: No se encontró un producto con ese ID.")
        return False

    def actualizar_producto(self, id_producto, nueva_cantidad, nuevo_precio):
        # Actualiza precio y cantidad buscando por ID
        for p in self.productos:
            if p.get_id() == id_producto:
                # Usamos los setters definidos en la clase Producto
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print(f"Producto {id_producto} actualizado correctamente.")
                return True
        print("Error: No se encontró el producto para actualizar.")
        return False

    def buscar_por_nombre(self, texto_busqueda):
        # Busca productos cuyo nombre contenga el texto ingresado
        encontrados = []
        for p in self.productos:
            # Convertimos a minúsculas para facilitar la búsqueda
            if texto_busqueda.lower() in p.get_nombre().lower():
                encontrados.append(p)

        if encontrados:
            print(f"--- Productos encontrados con '{texto_busqueda}' ---")
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        # Muestra todos los elementos presentes en la lista del inventario
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("--- Inventario Completo ---")
            # Iteración sobre la lista para mostrar cada elemento
            for p in self.productos:
                print(p)

# INTERFAZ DE USUARIO (CONSOLA)

def menu():
    mitienda = Inventario()

    while True:
        print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar producto por ID")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n-- Añadir Producto --")
            id_p = input("Ingrese ID único: ")
            nombre = input("Ingrese nombre: ")
            try:
                # Usamos float e int como tipos primitivos básicos
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                nuevo_prod = Producto(id_p, nombre, cantidad, precio)
                mitienda.agregar_producto(nuevo_prod)
            except ValueError:
                print("Error: La cantidad y el precio deben ser números.")

        elif opcion == "2":
            print("\n-- Eliminar Producto --")
            id_p = input("Ingrese el ID del producto a eliminar: ")
            mitienda.eliminar_producto(id_p)

        elif opcion == "3":
            print("\n-- Actualizar Producto --")
            id_p = input("Ingrese el ID del producto a actualizar: ")
            try:
                cant_input = input("Nueva cantidad (presione Enter para no cambiar): ")
                prec_input = input("Nuevo precio (presione Enter para no cambiar): ")

                # Mantener valores anteriores si el usuario no escribe nada
                nueva_cant = int(cant_input) if cant_input else None
                nuevo_prec = float(prec_input) if prec_input else None

                mitienda.actualizar_producto(id_p, nueva_cant, nuevo_prec)
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")

        elif opcion == "4":
            print("\n-- Buscar Producto --")
            nombre = input("Ingrese el nombre a buscar: ")
            mitienda.buscar_por_nombre(nombre)

        elif opcion == "5":
            mitienda.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
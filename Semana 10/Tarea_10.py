# Clase de la estructura de datos del producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        # Formato para guardar en el archivo de texto
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"


class Inventario:
    def __init__(self, nombre_archivo="inventario.txt"):
        self.archivo = nombre_archivo
        self.productos = {}
        # Al instanciar, cargamos los datos existentes
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        try:
            # Apertura y cierre automático
            with open(self.archivo, 'r') as f:
                for linea in f:
                    partes = linea.strip().split(',')
                    if len(partes) == 4:
                        id_p, nom, cant, pre = partes
                        self.productos[id_p] = Producto(id_p, nom, int(cant), float(pre))
        except FileNotFoundError:
            # Si el archivo no existe, se notifica y se crea uno nuevo
            print(f"Aviso: El archivo '{self.archivo}' no existe. Se creará al añadir productos.")
        except Exception as e:
            # Captura de errores inesperados
            print(f"Ocurrió un error al cargar los datos: {e}")

    def guardar_en_archivo(self):
        try:
            # Sobrescribir el contenido existente
            with open(self.archivo, 'w') as f:
                for p in self.productos.values():
                    f.write(str(p) + "\n")[cite: 66]
        except PermissionError:
            # Manejo de error de permisos
            print("Error: No se tienen permisos de escritura sobre el archivo.")
        except Exception as e:
            print(f"Error al guardar: {e}")

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: El ID ya existe en el sistema.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_en_archivo()
            print(f"Éxito: Producto '{producto.nombre}' guardado en el archivo.")

    def actualizar_producto(self, id_producto, nueva_cantidad):
        if id_producto in self.productos:
            self.productos[id_producto].cantidad = nueva_cantidad
            self.guardar_en_archivo()  # Actualización persistente [cite: 71]
            print("Actualización realizada y guardada exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado y archivo actualizado.")
        else:
            print("Error: No se encontró el producto para eliminar.")


def menu():
    inventario_app = Inventario()

    while True:
        print("\n--- MENÚ DE GESTIÓN DE INVENTARIOS (Persistencia en Archivos) ---")
        print("1. Añadir Producto")
        print("2. Actualizar Cantidad")
        print("3. Eliminar Producto")
        print("4. Mostrar Todo el Inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        # Manejar errores de entrada
        try:
            if opcion == "1":
                id_p = input("Ingrese ID único: ")
                nom = input("Ingrese Nombre: ")
                cant = int(input("Ingrese Cantidad: "))  # Lanzar ValueError
                pre = float(input("Ingrese Precio: "))
                inventario_app.agregar_producto(Producto(id_p, nom, cant, pre))

            elif opcion == "2":
                id_p = input("Ingrese el ID del producto: ")
                cant = int(input("Nueva cantidad: "))
                inventario_app.actualizar_producto(id_p, cant)

            elif opcion == "3":
                id_p = input("Ingrese ID a eliminar: ")
                inventario_app.eliminar_producto(id_p)

            elif opcion == "4":
                print("\n--- CONTENIDO DEL INVENTARIO ---")
                if not inventario_app.productos:
                    print("El inventario está vacío.")
                for p in inventario_app.productos.values():
                    print(f"ID: {p.id_producto} | Nombre: {p.nombre} | Stock: {p.cantidad} | Precio: ${p.precio}")

            elif opcion == "5":
                print("Cerrando el sistema. ¡Hasta luego!")
                break
            else:
                print("Opción inválida, intente de nuevo.")

        except ValueError:
            # Error específico para tipos de datos incorrectos
            print("Error: La cantidad debe ser un entero y el precio un número decimal.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
        finally:
            print("-" * 40)

if __name__ == "__main__":
    menu()
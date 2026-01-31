import os
import subprocess


class GestorDeArchivos:

    def leer_archivo(self, ruta_script):
        """
        Lee y devuelve el contenido de un archivo dado.
        """
        ruta_script_absoluta = os.path.abspath(ruta_script)
        try:
            with open(ruta_script_absoluta, 'r') as archivo:
                return archivo.read()
        except FileNotFoundError:
            return None
        except Exception as e:
            return f"Error leyendo archivo: {e}"

    def ejecutar_archivo(self, ruta_script):
        """
        Ejecuta el script de Python en una nueva terminal según el sistema operativo.
        """
        try:
            if os.name == 'nt':  # Windows
                subprocess.Popen(['cmd', '/k', 'python', ruta_script])
            else:  # Unix-based systems
                subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
        except Exception as e:
            print(f"Ocurrió un error al ejecutar el código: {e}")


class MenuDashboard:

    def __init__(self):
        # Inicializamos el gestor de archivos (Composición)
        self.gestor = GestorDeArchivos()
        # Define la ruta base donde se encuentra el dashboard.py
        self.ruta_base = os.path.dirname(__file__)
        self.unidades = {
            '1': 'Unidad 1',
            '2': 'Unidad 2'
        }

    def mostrar_menu_principal(self):
        """
        Muestra el menú principal de unidades.
        """
        while True:
            print("\n--- Menu Principal - Dashboard ---")
            for key in self.unidades:
                print(f"{key} - {self.unidades[key]}")
            print("0 - Salir")

            eleccion = input("Elige una unidad o '0' para salir: ")

            if eleccion == '0':
                print("Saliendo del programa...")
                break
            elif eleccion in self.unidades:
                ruta_unidad = os.path.join(self.ruta_base, self.unidades[eleccion])
                self.mostrar_submenu_carpetas(ruta_unidad)
            else:
                print("Opción no válida. Intente de nuevo.")

    def mostrar_submenu_carpetas(self, ruta_unidad):
        """
        Muestra las subcarpetas dentro de una unidad seleccionada.
        """
        # Validación simple para asegurar que la ruta existe
        if not os.path.exists(ruta_unidad):
            print(f"La ruta {ruta_unidad} no existe.")
            return

        sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

        while True:
            print("\n--- Submenú: Selecciona una subcarpeta ---")
            for i, carpeta in enumerate(sub_carpetas, start=1):
                print(f"{i} - {carpeta}")
            print("0 - Regresar al menú principal")

            eleccion = input("Elige una opción: ")

            if eleccion == '0':
                break

            try:
                indice = int(eleccion) - 1
                if 0 <= indice < len(sub_carpetas):
                    ruta_subcarpeta = os.path.join(ruta_unidad, sub_carpetas[indice])
                    self.mostrar_menu_scripts(ruta_subcarpeta)
                else:
                    print("Opción fuera de rango.")
            except ValueError:
                print("Opción no válida.")

    def mostrar_menu_scripts(self, ruta_sub_carpeta):
        """
        Muestra los scripts disponibles y permite verlos o ejecutarlos.
        """
        scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

        while True:
            print("\n--- Scripts Disponibles ---")
            for i, script in enumerate(scripts, start=1):
                print(f"{i} - {script}")
            print("0 - Regresar al submenú anterior")
            print("9 - Regresar al menú principal")

            eleccion = input("Elige una opción: ")

            if eleccion == '0':
                break
            if eleccion == '9':
                # Retornamos al menú principal rompiendo el flujo actual,
                # Usamos un break o simplemente dejamos que el usuario
                # navegue hacia atrás con 0 en el bucle superior, 0
                return "salir_a_principal"

            try:
                indice = int(eleccion) - 1
                if 0 <= indice < len(scripts):
                    nombre_script = scripts[indice]
                    ruta_script = os.path.join(ruta_sub_carpeta, nombre_script)
                    self._manejar_script(ruta_script, nombre_script)
                else:
                    print("Opción fuera de rango.")
            except ValueError:
                print("Opción no válida.")

    def _manejar_script(self, ruta_script, nombre_script):
        """
        Método auxiliar para manejar la lógica de visualización y ejecución de un script específico.
        Encapsula la lógica de interacción final[cite: 87].
        """
        codigo = self.gestor.leer_archivo(ruta_script)

        if codigo:
            print(f"\n--- Código de {nombre_script} ---\n")
            print(codigo)
            print("\n---------------------------------")

            ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
            if ejecutar == '1':
                self.gestor.ejecutar_archivo(ruta_script)
            elif ejecutar == '0':
                print("No se ejecutó el script.")
            else:
                print("Opción no válida.")

            input("\nPresiona Enter para volver al menú de scripts.")
        else:
            print("No se pudo leer el archivo.")


# Bloque principal de ejecución
if __name__ == "__main__":
    # Instanciamos la clase principal que orquesta la aplicación
    dashboard = MenuDashboard()
    dashboard.mostrar_menu_principal()
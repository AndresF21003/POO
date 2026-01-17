# Definición de la Clase Base
class DispositivoElectronico:
    def __init__(self, marca, modelo):
        # Atributos
        self.marca = marca
        self.modelo = modelo
        # Encapsulación
        self.__estado = "apagado"

    # Getter
    def obtener_estado(self):
        return self.__estado

    # Polimorfismo
    def encender(self):
        self.__estado = "encendido"
        print("El dispositivo se está encendiendo")

# Definición de la Clase Derivada
class Telefono(DispositivoElectronico):
    def __init__(self, marca, modelo, numero_serie):
        # Constructor de la clase padre
        super().__init__(marca, modelo)
        self.numero_serie = numero_serie

    # Polimorfismo de Sobreescritura
    def encender(self):
        print(f"El teléfono {self.marca} {self.modelo} está iniciando su sistema operativo...")

    # Polimorfismo con argumentos múltiples
    def realizar_llamada(self, contacto, mensaje=None):
        if mensaje:
            print(f"Enviando mensaje a {contacto}: {mensaje}")
        else:
            print(f"Llamando a {contacto}...")

# Programa

# Creación de un objeto de la clase derivada
mi_telefono = Telefono("Xiaomi", "POCO", "X7 Pro")

# Metodos
print(f"Dispositivo: {mi_telefono.marca} {mi_telefono.modelo}")

# Sobreescritura
mi_telefono.encender()

# Polimorfismo con argumentos múltiples
mi_telefono.realizar_llamada("Andrés")
mi_telefono.realizar_llamada("Rosario", "Hola, cómo estás?")

# Encapsulación
print(f"Estado actual: {mi_telefono.obtener_estado()}")
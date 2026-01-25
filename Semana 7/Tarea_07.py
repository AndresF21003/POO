class PacienteVeterinaria:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        # El objeto empieza con un estado definido y consistente
        print(f"[CONSTRUCTOR]: Registrando a {self.nombre} ({self.especie}), edad: {self.edad} años.")

    def mostrar_info(self):
        print(f"Paciente: {self.nombre} | Especie: {self.especie} | Edad: {self.edad}")

    def __del__(self):
        print(f"[DESTRUCTOR]: Cerrando historial médico de {self.nombre}. Recursos liberados.")

# --- APLICACIÓN PRÁCTICA ---

def gestionar_emergencia():
    print("\n--- INICIO DE ATENCIÓN DE EMERGENCIA ---")
    # Este objeto nace aquí. El parámetro 'self' representa esta instancia
    paciente_temp = PacienteVeterinaria("Luna", "Perro", 4)
    paciente_temp.mostrar_info()
    print("--- FIN DE LA ATENCIÓN ---")
    # Al terminar la función, paciente_temp pierde su última referencia y se destruye.

# Creamos un paciente en el programa principal (fuera de la función)
# El constructor asegura que el objeto esté en un estado válido antes de usarse
paciente1 = PacienteVeterinaria("Lili", "Gato", 5)

# Ejecutamos la función de emergencia
gestionar_emergencia()

# Finalización
print("\nFinalizando programa...")
# Al terminar el programa, todas las referencias se eliminan
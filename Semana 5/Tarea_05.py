"""
Registro de Información Básica de un Perrito
Calculo de la edad estimado en años humanos
"""

def registrar_paciente_canino():
    # ENTRADA DE DATOS

    # Secuencia de caracteres para nombres
    nombre_perro = "Luna"

    # Número para la edad
    edad_perro = 5

    # Número para el peso
    peso_perro = 12.5

    # Valor de verdad para el estado del perro
    tiene_vacunas = True
    if tiene_vacunas==True:
        tiene_vacunas2 = ("Sí")

    # Calculamos una edad estimada
    edad_estimada = edad_perro * 7

    # SALIDA DE DATOS
    print("--- FICHA DE REGISTRO VETERINARIO ---")
    print("Nombre del paciente:", nombre_perro)
    print("Edad cronológica:", edad_perro, "años")
    print("Edad estimada en años humanos:", edad_estimada, "años")
    print("Peso del perrito:", peso_perro, "kg")
    print("¿Cuenta con vacunas al día?:", tiene_vacunas2)

# Ejecución del programa
if __name__ == "__main__":
    registrar_paciente_canino()
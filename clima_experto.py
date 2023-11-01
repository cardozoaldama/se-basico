# Definición de la base de conocimiento inicial (reglas)
reglas = [
    {"if": ["llueve", "frío"], "then": "Está lloviendo y hace frío"},
    {"if": ["llueve", "templado"], "then": "Está lloviendo y hace un clima agradable"},
    {"if": ["llueve", "calor"], "then": "Está lloviendo, pero hace calor"},
    {"if": ["soleado", "frío"], "then": "Hace sol, pero hace frío"},
    {"if": ["soleado", "templado"], "then": "Hace un hermoso día soleado"},
    {"if": ["soleado", "calor"], "then": "Hace sol y calor"},
    {"if": ["nublado", "frío"], "then": "Está nublado y hace frío"},
    {"if": ["nublado", "templado"], "then": "Está nublado, pero con un clima agradable"},
    {"if": ["nublado", "calor"], "then": "Está nublado y hace calor"}
]

# Pedir al usuario que ingrese reglas adicionales
print("¿Deseas agregar reglas adicionales a la base de conocimiento?")
print("Ingresa 'si' para agregar reglas o 'no' para continuar sin cambios.")
respuesta = input("Respuesta: ").lower()

while respuesta == 'si':
    condiciones = input("Condiciones (e.g., soleado, frío): ").split(',')
    resultado = input("Resultado (e.g., Hace sol, pero hace frío): ")
    
    # Agregar la nueva regla a la base de conocimiento
    regla = {"if": [condicion.strip() for condicion in condiciones], "then": resultado}
    reglas.append(regla)
    
    respuesta = input("¿Deseas agregar otra regla? (si/no): ").lower()

# Pedir al usuario que ingrese hechos iniciales
print("Por favor, ingresa los hechos iniciales uno por uno (presiona Enter después de cada uno).")
hechos = []
while True:
    hecho = input("Hecho inicial (o presiona Enter para finalizar): ")
    if not hecho:
        break
    hechos.append(hecho)

# Motor de inferencia
def inferir_clima(reglas, hechos):
    clima_inferido = []

    for regla in reglas:
        if all(condicion in hechos for condicion in regla["if"]):
            clima_inferido.append(regla["then"])

    return clima_inferido

try:
    # Ejecución del motor de inferencia
    resultados = inferir_clima(reglas, hechos)

    # Resultado
    if resultados:
        print("Los resultados posibles del clima actual son:")
        for resultado in resultados:
            print("- " + resultado)
    else:
        print("No se pudo determinar el clima actual.")
except Exception as e:
    print("Error inesperado:", e)
# Definición de la base de conocimiento (reglas)
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

# Pedir al usuario que ingrese hechos iniciales
print("Por favor, ingresa los hechos iniciales uno por uno (presiona Enter después de cada uno).")
hechos = []
while True:
    hecho = input("Hecho inicial (o presiona Enter para finalizar): ")
    if not hecho:
        break
    hechos.append(hecho)

# Motor de inferencia (sin cambios)
def inferir_clima(reglas, hechos):
    clima_inferido = []

    for regla in reglas:
        if all(condicion in hechos for condicion in regla["if"]):
            clima_inferido.append(regla["then"])

    return clima_inferido

# Ejecución del motor de inferencia
clima_actual = inferir_clima(reglas, hechos)

# Resultado
if clima_actual:
    print("El clima actual es:", ", ".join(clima_actual))
else:
    print("No se pudo determinar el clima actual.")
# Definición de la base de conocimiento (reglas)
reglas = [
    {"if": ["llueve"], "then": "Está lloviendo"},
    {"if": ["soleado"], "then": "Hace sol"},
    {"if": ["nublado"], "then": "Está nublado"},
    {"if": ["llueve", "frío"], "then": "Está lloviendo y hace frío"},
    {"if": ["soleado", "calor"], "then": "Hace sol y hace calor"}
]

# Hechos iniciales (input del usuario)
hechos = ["llueve", "frío"]

# Motor de inferencia
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


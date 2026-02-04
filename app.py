
# Online Python - IDE, Editor, Compiler, Interpreter

# Solicitar nombre del estudiante
nombre = input("Ingrese su nombre: ")

# Mensaje de bienvenida
print("\n--------------------------------")
print(f"Bienvenido/a {nombre} 👋")
print("Resuelve el examen, lee las opciones y selecciona la opción correcta.")
print("--------------------------------")

# Lista de preguntas, opciones y respuesta correcta
preguntas = [
    {
        "pregunta": "1. ¿Qué se entiende por productividad en una línea de producción?",
        "opciones": {
            "A": "La cantidad de horas trabajadas por los operarios",
            "B": "La relación entre la cantidad producida y los recursos utilizados",
            "C": "El número total de máquinas en la planta"
        },
        "respuesta": "B"
    },
    {
        "pregunta": "2. ¿Cuál es el objetivo principal del estudio de tiempos?",
        "opciones": {
            "A": "Aumentar el número de trabajadores",
            "B": "Determinar el tiempo estándar para realizar una tarea",
            "C": "Reducir la calidad del producto"
        },
        "respuesta": "B"
    },
    {
        "pregunta": "3. ¿Qué es el tiempo ciclo en una línea de producción?",
        "opciones": {
            "A": "El tiempo total de descanso del operario",
            "B": "El tiempo que tarda una estación en completar una unidad",
            "C": "El tiempo perdido por fallas de maquinaria"
        },
        "respuesta": "B"
    },
    {
        "pregunta": "4. ¿Cuál de los siguientes factores afecta directamente la productividad?",
        "opciones": {
            "A": "El color de las máquinas",
            "B": "La eficiencia del operario",
            "C": "La ubicación geográfica de la empresa"
        },
        "respuesta": "B"
    },
    {
        "pregunta": "5. ¿Qué ocurre cuando una estación de trabajo es más lenta que las demás?",
        "opciones": {
            "A": "Aumenta la productividad total",
            "B": "Se genera un cuello de botella",
            "C": "Se reduce el tiempo ciclo"
        },
        "respuesta": "B"
    },
    {
        "pregunta": "6. ¿Qué es un cuello de botella en una línea de producción?",
        "opciones": {
            "A": "Un exceso de inventario terminado",
            "B": "Una etapa que limita la capacidad total del sistema",
            "C": "Un error de calidad en el producto"
        },
        "respuesta": "B"
    },
    {
        "pregunta": "7. ¿Para qué se utiliza el balanceo de línea?",
        "opciones": {
            "A": "Para aumentar el número de tareas",
            "B": "Para distribuir equitativamente el trabajo entre estaciones",
            "C": "Para eliminar a los operarios menos productivos"
        },
        "respuesta": "B"
    },
    {
        "pregunta": "8. ¿Qué indicador se usa comúnmente para medir productividad?",
        "opciones": {
            "A": "Producción / Recursos utilizados",
            "B": "Recursos utilizados / Producción",
            "C": "Tiempo muerto / Tiempo total"
        },
        "respuesta": "A"
    },
    {
        "pregunta": "9. ¿Qué es el tiempo muerto en una línea de producción?",
        "opciones": {
            "A": "El tiempo dedicado al mantenimiento preventivo",
            "B": "El tiempo en que no se realiza trabajo productivo",
            "C": "El tiempo necesario para fabricar un producto"
        },
        "respuesta": "B"
    },
    {
        "pregunta": "10. ¿Cuál es una ventaja de mejorar los tiempos de producción?",
        "opciones": {
            "A": "Incrementar los costos operativos",
            "B": "Disminuir la capacidad de producción",
            "C": "Reducir costos y aumentar la eficiencia"
        },
        "respuesta": "C"
    }
]

# Inicializar puntaje
puntaje = 0

# Recorrer preguntas
for p in preguntas:
    print("\n" + p["pregunta"])
    for opcion, texto in p["opciones"].items():
        print(f"{opcion}) {texto}")

    respuesta_usuario = input("Tu respuesta (A, B o C): ").upper()

    if respuesta_usuario == p["respuesta"]:
        print("✅ Respuesta correcta")
        puntaje += 1
    else:
        print(f"❌ Respuesta incorrecta. La correcta era {p['respuesta']}")

# Resultado final
print("\n--------------------------------")
print(f"{nombre}, tu puntaje final es: {puntaje} / {len(preguntas)}")

if puntaje >= 7:
    print("🎉 ¡Aprobado!")
else:
    print("📘 No aprobado. Sigue estudiando.")

import time
from datetime import datetime, timedelta
import pytz



# Definir la lista de nombres y sus horarios de entrada, almuerzo y salida
nombres = [
    {"nombre": "Diana Carolina Parrado", "entrada": "10:00 am", "almuerzo": "1:00 pm", "salida": "8:00 pm"},
    {"nombre": "Oscar Rodriguez", "entrada": "7:00 am", "almuerzo": "12:00 pm", "salida": "4:00 pm"},
    {"nombre": "Kadir Alistarco Cuenca Sandoval", "entrada": "8:00 am", "almuerzo": "12:00 pm", "salida": "5:00 pm"},
    {"nombre": "Ivan Dario Avellaneda Galvez", "entrada": "8:00 am", "almuerzo": "1:00 pm", "salida": "5:00 pm"},
    {"nombre": "Javier Forero Cruz", "entrada": "7:00 am", "almuerzo": "12:00 pm", "salida": "4:00 pm"},
    {"nombre": "Juan Camilo Guzman Osorio", "entrada": "7:00 am", "almuerzo": "12:00 pm", "salida": "4:00 pm"},
    {"nombre": "Jairo Alexis Castañeda", "entrada": "11:00 am", "almuerzo": "1:00 pm", "salida": "8:00 pm"},
    {"nombre": "Alexander Loaiza", "entrada": "7:00 am", "almuerzo": "12:00 pm", "salida": "4:00 pm"},
    {"nombre": "Hector Morales", "entrada": "8:00 am", "almuerzo": "12:00 pm", "salida": "5:00 pm"},
    {"nombre": "Hernan Losada", "entrada": "11:00 am", "almuerzo": "1:00 pm", "salida": "8:00 pm"}
]




# Obtener la hora actual en Colombia
def obtener_hora_colombia():
    zona_horaria_colombia = pytz.timezone("America/Bogota")
    hora_actual = datetime.now(zona_horaria_colombia)
    return hora_actual.strftime("%I:%M:%S %p")

# Obtener los nombres correspondientes al rango de horas actual para cada grupo
def obtener_nombres_en_rango_grupo1(hora_actual):
    nombres_en_rango_grupo1 = []
    for persona in nombres:
        if persona["nombre"] in ["Diana Carolina Parrado", "Oscar Rodriguez", "Kadir Alistarco Cuenca Sandoval", "Ivan Dario Avellaneda Galvez", "Javier Forero Cruz", "Juan Camilo Guzman Osorio", "Jairo Alexis Castañeda"]:
            hora_entrada = datetime.strptime(persona["entrada"], "%I:%M %p")
            hora_salida = datetime.strptime(persona["salida"], "%I:%M %p")
            hora_almuerzo = datetime.strptime(persona["almuerzo"], "%I:%M %p")
            if hora_actual >= hora_entrada and hora_actual <= hora_salida and (hora_actual < hora_almuerzo or hora_actual >= hora_almuerzo + timedelta(hours=1)):
                nombres_en_rango_grupo1.append(persona["nombre"])
    return nombres_en_rango_grupo1

def obtener_nombres_en_rango_grupo2(hora_actual):
    nombres_en_rango_grupo2 = []
    for persona in nombres:
        if persona["nombre"] in ["Diana Carolina Parrado", "Oscar Rodriguez", "Kadir Alistarco Cuenca Sandoval", "Ivan Dario Avellaneda Galvez"]:
            hora_entrada = datetime.strptime(persona["entrada"], "%I:%M %p")
            hora_salida = datetime.strptime(persona["salida"], "%I:%M %p")
            hora_almuerzo = datetime.strptime(persona["almuerzo"], "%I:%M %p")
            if hora_actual >= hora_entrada and hora_actual <= hora_salida and (hora_actual < hora_almuerzo or hora_actual >= hora_almuerzo + timedelta(hours=1)):
                nombres_en_rango_grupo2.append(persona["nombre"])
    return nombres_en_rango_grupo2

def obtener_nombres_en_rango_grupo3(hora_actual):
    nombres_en_rango_grupo3 = []
    for persona in nombres:
        if persona["nombre"] in ["Hector Morales", "Alexander Loaiza", "Hernan Losada"]:
            hora_entrada = datetime.strptime(persona["entrada"], "%I:%M %p")
            hora_salida = datetime.strptime(persona["salida"], "%I:%M %p")
            hora_almuerzo = datetime.strptime(persona["almuerzo"], "%I:%M %p")
            if hora_actual >= hora_entrada and hora_actual <= hora_salida and (hora_actual < hora_almuerzo or hora_actual >= hora_almuerzo + timedelta(hours=1)):
                nombres_en_rango_grupo3.append(persona["nombre"])
    return nombres_en_rango_grupo3

# Asignar casos a cada persona según las reglas establecidas
hora_actual = obtener_hora_colombia()

# Imprimir mensaje de bienvenida
print("¡Bienvenido! A continuación, te indicaré a quién debes asignar el caso.")
print("Hora actual en Colombia:", hora_actual)

# Obtener los nombres dentro del rango de horas actual para cada grupo
nombres_en_rango_grupo1 = obtener_nombres_en_rango_grupo1(datetime.strptime(hora_actual, "%I:%M:%S %p"))
nombres_en_rango_grupo2 = obtener_nombres_en_rango_grupo2(datetime.strptime(hora_actual, "%I:%M:%S %p"))
nombres_en_rango_grupo3 = obtener_nombres_en_rango_grupo3(datetime.strptime(hora_actual, "%I:%M:%S %p"))

# Mostrar el siguiente nombre al ingresar "vip", "vip3" o presionar Enter
indice_grupo_1 = 0
indice_grupo_2 = 0
indice_grupo_3 = 0

while True:
    opcion = input("\nIngresa 'vip' para mostrar el siguiente nombre del grupo 2, 'vip3' para mostrar el siguiente nombre del grupo 3 o presiona Enter para mostrar el siguiente nombre del grupo 1: ")

    if opcion.lower() == "vip":
        if nombres_en_rango_grupo2:
            siguiente_nombre_grupo2 = nombres_en_rango_grupo2[indice_grupo_2 % len(nombres_en_rango_grupo2)]
            indice_grupo_2 += 1
            print("Siguiente nombre del grupo 2:", siguiente_nombre_grupo2, "| Hora:", obtener_hora_colombia())
        nombres_en_rango_grupo2 = obtener_nombres_en_rango_grupo2(datetime.strptime(obtener_hora_colombia(), "%I:%M:%S %p"))

    elif opcion.lower() == "vip3":
        if nombres_en_rango_grupo3:
            siguiente_nombre_grupo3 = nombres_en_rango_grupo3[indice_grupo_3 % len(nombres_en_rango_grupo3)]
            indice_grupo_3 += 1
            print("Siguiente nombre del grupo 3:", siguiente_nombre_grupo3, "| Hora:", obtener_hora_colombia())
        nombres_en_rango_grupo3 = obtener_nombres_en_rango_grupo3(datetime.strptime(obtener_hora_colombia(), "%I:%M:%S %p"))

    else:
        if nombres_en_rango_grupo1:
            siguiente_nombre_grupo1 = nombres_en_rango_grupo1[indice_grupo_1 % len(nombres_en_rango_grupo1)]
            indice_grupo_1 += 1
            print("Siguiente nombre del grupo 1:", siguiente_nombre_grupo1, "| Hora:", obtener_hora_colombia())
        nombres_en_rango_grupo1 = obtener_nombres_en_rango_grupo1(datetime.strptime(obtener_hora_colombia(), "%I:%M:%S %p"))

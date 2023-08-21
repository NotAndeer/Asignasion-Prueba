# Asignasion-Prueba
Este código es un programa en Python que se ejecuta en la consola y realiza un seguimiento de los nombres de personas y sus horarios de trabajo en tres grupos diferentes. Está diseñado para mostrar el siguiente nombre de cada grupo en función de la hora actual en Colombia y algunas condiciones específicas de horario de trabajo. El programa sigue una lógica de asignación de casos a personas en diferentes grupos, y permite al usuario mostrar el siguiente nombre en los grupos utilizando comandos específicos.

Aquí está una descripción detallada del funcionamiento del código:

Importación de módulos:

El código importa los módulos necesarios: time, datetime, timedelta y pytz para trabajar con fechas y tiempos, así como para manejar zonas horarias.
Definición de la lista de nombres y horarios:

Se define una lista llamada nombres, que contiene diccionarios con la información de diferentes personas, incluyendo sus nombres, horarios de entrada, almuerzo y salida.
Función obtener_hora_colombia():

Define una función que utiliza la biblioteca pytz para obtener la hora actual en Colombia y formatearla en un formato legible.
Funciones obtener_nombres_en_rango_grupo1(), obtener_nombres_en_rango_grupo2() y obtener_nombres_en_rango_grupo3():

Estas funciones toman la hora actual como entrada y devuelven una lista de nombres de personas dentro de los grupos correspondientes, según sus horarios de trabajo.
Impresión de mensaje de bienvenida y hora actual:

Imprime un mensaje de bienvenida junto con la hora actual en Colombia.
Obtención de nombres dentro del rango de horas actual para cada grupo:

Utiliza las funciones mencionadas anteriormente para obtener los nombres de las personas dentro del rango horario para cada grupo.
Bucle principal:

Inicia un bucle infinito que permite al usuario ingresar comandos para mostrar el siguiente nombre en diferentes grupos.
El usuario puede ingresar "vip" para mostrar el siguiente nombre del grupo 2, "vip3" para el grupo 3 o simplemente presionar Enter para el grupo 1.
El código comprueba las condiciones y muestra el siguiente nombre de acuerdo con el comando ingresado y el grupo correspondiente.
Las listas de nombres se actualizan utilizando las funciones de obtención de nombres en cada iteración del bucle.

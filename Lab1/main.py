import os
from datetime import datetime

from Trig import Trig

fecha_actual = datetime.now()
# Crear una instancia de la clase Trig
trig_instance = Trig()


while True:
    # Pedir al usuario qué valor desea consultar o si desea salir
    opcion = input("¿Qué valor deseas consultar? (seno, coseno, tangente) o escribe 'salir' para terminar: ")

    if opcion == "salir":
        # Si el usuario escribe 'salir', terminar el bucle
        break

    # Validar la opción ingresada por el usuario
    if opcion == "seno":
        resultado = trig_instance.sin_pi()
    elif opcion == "coseno":
        resultado = trig_instance.cos_pi()
    elif opcion == "tangente":
        resultado = trig_instance.tan_pi()
    else:
        resultado = "Opción inválida"

    # Obtener la fecha y hora actual
    fecha_actual = datetime.now()

    # Mostrar el resultado
    print(f"El resultado de {opcion} de pi es:", resultado)

    # se escribe  la fecha y hora en el archivo log.txt ya creado previamente y se escribe "a" para agregar el contenido al final del archivo
    with open("log.txt", "a") as archivo_log:
        archivo_log.write(f"Operación '{opcion}' realizada el {fecha_actual}\n")
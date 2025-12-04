from multiprocessing import Pool
import time
import os
import random

# Función que ejecutará cada proceso
def tarea(nombre):
    duracion = random.randint(1, 4)
    print(f" Proceso {nombre} (PID={os.getpid()}) inició, durará {duracion}s")
    time.sleep(duracion)
    return f" Proceso {nombre} completado en {duracion}s (PID={os.getpid()})"

if __name__ == "__main__":
    # Crear un pool de 3 procesos
    with Pool(processes=3) as pool:
        nombres = [f"P{i}" for i in range(1, 7)]  # 6 tareas
        # Ejecutar las tareas en paralelo
        resultados = pool.map(tarea, nombres)

    # Mostrar resultados
    print("\n Resultados finales:")
    for r in resultados:
        print(r)
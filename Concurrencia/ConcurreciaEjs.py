import numpy as np
from multiprocessing import Process, Array
from math import ceil
#importes de librerias necesariaas

def Concu(arr, inic, fin):
    #arr: objeto multiprocessing .Array compartido
    #inic y fin son los indices, inic comienza en 0 y fin es el numero final al que debe llegar

    arr[inic:fin] = np.random.randint(0, 1000000, size=(fin-inic,))
    #Genera números aleatorios y los asigna en la porción compartida

if __name__ == "__main__":
    N = 1_000_000 #Esta es la longitud del vector a rellenas
    nproc = 8  # Número de procesos que crearemos
    vector = Array('i', N)  # Array compartido con la N cantidad de elementos

    bsize = ceil(N / nproc) #cuantos elementos maneja cada proceso
    procs = [] #lista para guardar los objetos

    #Creamos y arrancamos procesos
    for i in range(nproc):
        inic = i * bsize
        fin = min((i + 1) * bsize, N) #este se asegura que no pase el ultimo N (1.000.000)
        p = Process(target=Concu, args=(vector, inic, fin))
        p.start() #iniciamos procesos hijo
        procs.append(p)

    #Esperamos que terminen los procesos
    for p in procs:
        p.join()

    
    print(list(vector))  # lo pasamos a lista y mostramos el vector
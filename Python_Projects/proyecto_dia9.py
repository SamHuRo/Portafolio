import os
import math
import re
import time
import datetime

from pathlib import Path


contador = 0
patron = r'N\D{3}-\d{5}'
fecha_hoy = datetime.datetime.now().strftime('%d/%m/%y')
ruta = '/Users/samuel/Documents/Cursos/Python/CursoPython/Dia9/Proyecto_Dia9/Mi_Gran_Directorio'


os.system('clear')
print('-' * 50)
print(f'Fecha de búsqueda: {fecha_hoy}')
print('ARCHIVO       \tNRO. SERIE')
print('--------      \t--------')

inicio = time.time()

#Ciclo for para recorrer la carpeta
for carpeta, subcarpeta, archivo in os.walk(ruta):
    for arch in archivo:
        if(arch.endswith('txt')):
            ruta_archivo = carpeta + '/' + arch
            archivo = open(ruta_archivo, 'r')
            texto = archivo.read()
            verificar = re.search(patron, texto)
            if verificar != None:
                print(f'{arch}  \t{verificar.group()}')
                contador += 1
            archivo.close()

final = time.time()
duracion = final - inicio

print(f'Números encontrados: {contador}')
print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')
print('-' * 50)

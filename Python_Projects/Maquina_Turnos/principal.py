'''
En esta parte se van a  escribir las funciones encargadas de administrar el funcionamiento
del programa.
'''
import numeros
from os import system


def generar_tiquete():
    while True:
        try:
            opcion = numeros.opciones().upper()
            ['P', 'C', 'F'].index(opcion)
        except: 
            print('¡¡¡ Esa opción no existe elija otra !!!')
        else:
            break
    numeros.mostrar_mensaje(opcion)


def inicio():
    system('clear')
    opcion_si = True
    while True:
        try:
            if(opcion_si):
                generar_tiquete()
            otro_turno = input('¿Quieres otro turno? [S]/[N]: ').upper()
            ['S', 'N'].index(otro_turno)
        except:
            opcion_si = False
            print('¡¡¡ Esa opción no existe elija otra !!!')
        else:
            if(otro_turno == 'N'):
                print('¡¡¡ Gracias por su visita !!!')
                break
            else:
                opcion_si = True


inicio()
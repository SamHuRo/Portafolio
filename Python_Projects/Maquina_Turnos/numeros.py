'''
Modulo donde se encuentran las funciones y generadores de escribir el mensaje del turno.
Funciones:
    - mensaje_turno(): se encarga de escribir el mensaje que aparece en el tiquete
    - opiones(): se enarga de mostrar el menu de las areas
    - mostrar_mensaje(): se encarga de mostrar el mensaje que aparece en el turno

Generadores:
    - perfumeria(): almacena los turnos generados para el area de perfumeria
    - farmacia(): almacena los turnos generados para el area de farmacia
    - cosmeticos(): almacena los turnos generados para el area de cosmeticos
'''


#Funcion que muestra las opciones del programa
def opciones():
    separacion = '=' * 90

    print(separacion)
    print('¿A que area quieres ir?:')
    #Opciones que tiene el programa
    print('[C]: Cosmeticos.')
    print('[F]: Farmacia.')
    print('[P]: Perfumeria.')
    opcion = input('¿Cual es tu opción?: ')
    print('\n')
    return opcion


#Funcion para escribir texto en el turno
def mensaje_turno(turno):
    print('Tu turno es el:')
    print(turno)
    print('Aguarde y sera atendido\n')


#Generadores: se van a crear tres generadores los cuales representan las areas de atencion, las cuales son:
#   - Perfumeria
#   - Farmacia
#   - Cosmeticos
def perfumeria():
    turno = 0
    while True:
        texto = f'P-{turno}'
        turno += 1
        yield texto


def farmacia():
    turno = 0
    while True:
        texto = f'F-{turno}'
        turno += 1
        yield texto


def cosmeticos():
    turno = 0
    while True:
        texto = f'C-{turno}'
        turno += 1
        yield texto


turno_cosmetico = cosmeticos()
turno_farmacia = farmacia()
turno_perfumeria = perfumeria()

def mostrar_mensaje(opcion):
    if(opcion == 'C'):
        mensaje_turno(next(turno_cosmetico))
    elif(opcion == 'F'):
        mensaje_turno(next(turno_farmacia))
    elif(opcion == 'P'):
        mensaje_turno(next(turno_perfumeria))

from os import system

#Crear la clase persona
#   Atributos:
#       - Nombre y Apellido
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

#Crear la clase cliente, la cual va a heredar los atributos de la clase persona
#   Atributos:
#       - Numero de cuenta y balance
#   Metodos:
#       - imprimir la información del cliente, depositar (cuanto dinero quiere agregar a su cuenta), retirar (cuanto dinero quiere sacar de su cuenta)
class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        texto = f'El nombre del cliente: {self.nombre} {self.apellido}\nEl numero de cuenta es: {self.numero_cuenta}\nEl saldo de la cuenta es: ${self.balance}\n'
        return texto

    #Metodo para agregar dinero a la cuenta
    def depositar(self, agregar_dinero):
        self.balance += agregar_dinero
        texto = f'La cantidad de dinero depositado es de: ${agregar_dinero}\nEl saldo total de la cuenta es: ${self.balance}'
        print(texto)

    #Metodo para retirar dinero de la cuenta
    def retirar(self, cantidad_transferir):
        if(self.balance >= cantidad_transferir):
            self.balance -= cantidad_transferir
            texto = f'La cantidad de dinero retirado es de: ${cantidad_transferir}\nEl saldo total de la cuenta es: ${self.balance}'
            print(texto)
        else:
            print('¡¡¡ No tienes el suficiente dinero para realizar el retiro !!!')


#Función para crear un cliente
def crear_cliente(nombre, apellido, numero_cuenta, balance):
    cliente = Cliente(nombre, apellido, numero_cuenta, balance)
    return cliente

#Funcion ue muestra las opciones del programa
def opciones():
    separacion = '=' * 100

    print(separacion)
    print('Escoge alguna de las opciones')
    #Opciones que tiene el programa
    print('[1]: Depositar en tu cuenta.')
    print('[2]: Retirar dinero de tu cuenta.')
    #Opcion para salir del programa
    print('[q]: Finalizar programa.')
    opcion = input('¿Cual es tu opción?: ')
    return opcion

#Función para iniciar el programa
def inicio():
    system('clear')
    print()
    print('¡¡¡ Bienvenido al programa de la cuenta bancaria !!!')
    print()
    print('Por favor ingrese la siguiente información\n')
    nombre_cliente = input('Ingrese el nombre del cliente: ')
    apellido_cliente = input('Ingrese el apellido del cliente: ')
    numero_cuenta_cliente = input('Ingrese el numero de cuenta: ')
    balance_cliente = int(input('Ingrese el saldo de la cuenta: '))

    system('clear')
    cliente_creado = crear_cliente(nombre_cliente, apellido_cliente, numero_cuenta_cliente, balance_cliente)
    print('¡¡¡ Felicidades el cliente ha sido creado !!!')
    print(cliente_creado)

    fin_programa = True
    while fin_programa:
        opcion = opciones()
        if(opcion == 'q'):
            fin_programa = False
        elif(opcion == '1'):
            depositar_dinero = int(input('¿Cuanto dinero quiere consignar?: '))
            cliente_creado.depositar(depositar_dinero)
        elif (opcion == '2'):
            retirar_dinero = int(input('¿Cuanto dinero deseas retirar?: '))
            cliente_creado.retirar(retirar_dinero)
        else:
            print('¡¡¡ Opción incorrecta, escoja una de las opciones mostradas !!!')
    
    print('¡¡¡ Finalizando programa !!!')


inicio()











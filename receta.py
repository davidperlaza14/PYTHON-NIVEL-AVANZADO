'''receta.py

Modelo sencillo de una receta de cocina.
atributos:
     ingrediente. --Lista de ingredienetes para la receta
     pasos        --Lista de pasos o instrucciones para la receta
     nombre       --Nombre de la receta    
comportamientos
    menu          --Menu de operaciones
    agregar_ingredientes --Permite agregar ingredientes a la receta
    consultar_ingredientes --Permite consultar los ingredientes 
    agregar_paso --Permite agregar pasos a la receta 
    consultar_pasos --Permite consultar los pasos para la receta.  
'''

from ingrediente import Ingrediente
import os


class Receta:

    OPC_AGREGAR_INGREDIENTE = 1
    OPC_CONSULTAR_INGREDIENTES = 2
    OPC_AGREGAR_PASOS = 3
    OPC_CONSULTAR_PASOS = 4
    OPC_SALIR = 0

    def __init__(self, nombre=''):
        self._nombre = nombre
        self._ingredientes = []
        self._pasos = []
        
    def __str__(self):
        s = f'                      {self.nombre}\n'
        s += 'Ingredientes: \n'
        for ingrediente in self.ingredientes:
            s += f'{ingrediente}\n'
        s += '\nPasos: \n'
        for i, paso in enumerate(self.pasos):
            s += f'{i+1}. {paso}\n'
        return s

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
    @nombre.deleter
    def nombre(self):
        del self._nombre

    @property
    def ingredientes(self):
        return self._ingredientes
    @ingredientes.setter
    def ingredientes(self, valor):
        self._ingredientes = valor
    @ingredientes.deleter
    def ingredientes(self):
        del self._ingredientes
    
    @property
    def pasos(self):
        return self._pasos
    @pasos.setter
    def pasos(self, valor):
        self._pasos = valor
    @pasos.deleter
    def pasos(self):
        del self._pasos

    def menu(self):
        continuar = True
        while continuar:
            os.system('clear')
            print(f'''                   {self.nombre}
{self.OPC_AGREGAR_INGREDIENTE}) Agregar Ingrediente
{self.OPC_CONSULTAR_INGREDIENTES}) Consultar Ingredientes
{self.OPC_AGREGAR_PASOS}) Agregar Pasos
{self.OPC_CONSULTAR_PASOS}) Consultar Pasos
{self.OPC_SALIR}) Salir ''')
            opc = int(input('Selecciona un opcion:'))
            if opc == self.OPC_AGREGAR_INGREDIENTE:
                self.agregar_ingrediente()
            elif opc == self.OPC_CONSULTAR_INGREDIENTES:
                self.consultar_ingredientes()
            elif opc == self.OPC_AGREGAR_PASOS:
                self.agregar_pasos()
            elif opc == self.OPC_CONSULTAR_PASOS:
                self.consultar_pasos()
            elif opc == self.OPC_SALIR:
                continuar = False
            else:
                print('Opcion no valida...')
            input('Presiona enter para continuar...')
        print('Nos vemos')

    def agregar_ingrediente(self):
        continuar = True
        while continuar:
            os.system("clear")
            print('                         Agregar Ingrediente')
            nombre = input('Nombre: ')
            cantidad = -1
            while cantidad <= 0:
                cantidad = input('Cantidad: ')
                try:
                    cantidad = float(cantidad)
                except:
                    cantidad = 0
            unidad = input('Unidad de medida: ')
            ingrediente = Ingrediente(nombre, cantidad, unidad)
            self.ingredientes.append(ingrediente)
            respuesta = input('Desea agregar otro ingrediente? (s/n): ')
            if respuesta != 's' and respuesta != 'S':
                continuar = False

    def consultar_ingredientes(self):
        os.system("clear")
        print('                         Ingredientes')
        if len(self.ingredientes) == 0:
            print('No hay ingredientes registrados.')
        else:
            for ingrediente in self.ingredientes:
                print(f'{ingrediente}')

    def agregar_pasos(self):
        continuar = True
        while continuar:
            os.system("clear")
            print('                         Agregar Paso')
            paso = input("Pasos: ")
            self.pasos.append(paso)
            respuesta = input('Desea agregar otro paso? (s/n): ')
            if respuesta != 's' and respuesta != 'S':
                continuar = False
            
    def consultar_pasos(self):
        os.system("clear")
        print('                             Pasos')
        if len(self.pasos) <= 0:
            print('No hay pasos registrados')
        else:
            for i, paso in enumerate(self.pasos):
                print(f'{i+1}. {paso}')


    
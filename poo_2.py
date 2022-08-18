"""
Script en Python que implemente una clase Persona con las siguientes propiedades:
    nombre
    edad
Ademas se debera agregar los comportamientos:
hablar(mensaje) - mensaje: el mensaje que dira la persona.
comer(alimento) - alimento: el alimento que consume la persona.
"""

class Persona:
    def __init__(self):
        self._nombre = ''
        self._edad = None

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
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        self._edad = valor

    @edad.deleter
    def edad(self):
        del self._edad
    
    def hablar(self, mensaje):
        print(f'{self.nombre}: {mensaje}')
    def comer(self, alimento):
        print(f'{self.nombre} esta comiedo {alimento}')


def main():
    persona_1 = Persona()
    persona_2 = Persona()

    persona_1. nombre = 'Pedro Navajas'
    persona_1.edad = 33

    persona_2. nombre = 'Susana Sonido'
    persona_2.edad = 33

    print('Datos de la primera persona')
    print(f'Nombre {persona_1.nombre}')
    print(f'Edad: {persona_1.edad}')

    print('Datos de la segunda persona')
    print(f'Nombre {persona_2.nombre}')
    print(f'Edad: {persona_2.edad}')

    persona_1.hablar(f'Hola {persona_2.nombre} como estas?')
    persona_2.hablar(f'Hey {persona_1.nombre} que gusto verte.')

    persona_1.comer('Esquites')
    persona_2.comer('Tamales')

if __name__ == '__main__':
    main()
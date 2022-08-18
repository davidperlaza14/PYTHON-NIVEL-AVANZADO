'''
Modelo sencillo de un deportista.Hereda de la clase Persona.
atributos:
    deporte -- Deporte que practica la persona
comportamientos:
    entrenar -- Entrena el deporte asignado.
'''
from persona import Persona

class Deportista(Persona):
    def __init__(self, nombre='', edad=None, deporte=''):
        super().__init__(nombre, edad)
        self._deporte = deporte

    @property
    def deporte(self):
        return self._deporte
    @deporte.setter
    def deporte(self, valor):
        self._deporte = valor
    @deporte.deleter
    def deporte(self):
        del self._deporte

    def entrenar(self):
        print(f'{self.nombre} esta entrenando {self.deporte}')

    def __str__(self):
        return f'''Nombre: {self.nombre}
Edad: {self.edad}
Deporte: {self.deporte}'''

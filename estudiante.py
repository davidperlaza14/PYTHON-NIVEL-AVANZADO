'''
Modelo sencillo de un estudiante. Hereda de la clase Persona.
Atributos:
    promedio 
    codigo
Comportamiento:
    estudiar
'''

from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre='', edad=None, promedio=None, codigo=''):
        super().__init__(nombre, edad)
        self._promedio = promedio
        self._codigo =codigo

    @property
    def promedio(self):
            return self._promedio

    @promedio.setter
    def promedio(self, valor):
        self._promedio = valor
    
    @promedio.deleter
    def promedio(self):
        del self._promedio

    @property
    def codigo(self):
            return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor < 0.0:
            self._promedio = None
        else:
            self._codigo = valor

    @codigo.deleter
    def codigo(self):
        del self._codigo
    
    def estudiar(self, materia):
        print(f'{self.nombre} se encuentra estudiando {materia}')
    
    def __str__(self):
         return f'''{super().__str__()}
Promedio: {self.promedio}
Codigo: {self.codigo}'''
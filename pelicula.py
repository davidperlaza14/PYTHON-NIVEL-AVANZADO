class Pelicula:
    def __init__(self, titulo='', director='', año=None, duracion=None):
        self._titulo = titulo
        self._director = director
        self._año = año
        self._duracion = duracion
    
    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self,valor):
        self._titulo = valor
    @titulo.deleter
    def titulo(self):
        del self._titulo

    @property
    def director(self):
        return self._director
    @director.setter
    def director(self,valor):
        self._director = valor
    @director.deleter
    def director(self):
        del self._director
    
    @property
    def año(self):
        return self._año
    @año.setter
    def año(self,valor):
        self._año = valor
    @año.deleter
    def año(self):
        del self._año
    
    @property
    def duracion(self):
        return self._duracion
    @duracion.setter
    def duracion(self,valor):
        self._duracion = valor
    @duracion.deleter
    def duracion(self):
        del self._duracion

    def __str__(self):
        ESPACIOS = 10
        return f'''{"Titulo:" : <{ESPACIOS}}{self.titulo}
{"Director:" : <{ESPACIOS}}{self.director}
{"Año:" : <{ESPACIOS}}{self.año}
{"Duracion:" : <{ESPACIOS}}{self.duracion} min'''

    def __lt__(self, otro):
        return self.titulo < otro.titulo
    
    def __eq__(self, otro):
        return self.titulo == otro.titulo and self.año == otro.año

    def __le__(self, otro):
        return self < otro or self == otro
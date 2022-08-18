'''
                            Clases

                            class Identificador:
                                instrucciones

'''

# CREAR CLASE
"""
script en Python que implemente una clase Figura que como atributo tenga la cantidad de lados.

Una vez creada la clase crear dos figuras (objetos) y mostrar su cantidad de lados.

"""

class Figura:
    def __init__(self):
        self._lados = None

    @property # Getter : Regresa el valor asociaddo a la cantidad de lados
    def lados(self):
        return self._lados

    @lados.setter #setter: Permite asignar valor a la propiedad o atributo a lados
    def lados(self, valor):
        self._lados = valor
    
    @lados.deleter
    def lados(self):
        del self._lados

def main():
    triangulo = Figura()
    cuadrado = Figura()

    triangulo.lados = 3
    cuadrado.lados = 4
    
    print(f"El triangulo tiene {triangulo.lados} lados.")
    print(f"El cuadrado tiene {cuadrado.lados} lados.")

if __name__ == "__main__":
    main()
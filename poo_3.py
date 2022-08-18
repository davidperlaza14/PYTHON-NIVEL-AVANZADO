# Clase como  un Modulo y una Funcion __str__
"""
Script de Python que importe la clase Prenda para despues crear dos objetos e imprimir su informacion en pantalla.
"""

from prenda import Prenda

def main():
    playera = Prenda()
    
    playera.tipo = 'Playera con estampado'
    playera.talla = 'M'

    print(playera)

if __name__ == '__main__':
    main()
'''
Composicion entre Clases

script de Python que cree y asigne un valor a los atributos de un objeto tipo RECETA  Los ingredientes seran modelados dentro de una clase en un modulo separado y tendran los siguientes atributos:

    - nombre
    - cantidad
    - unidad de medida

La clase Receta ademas de contener un menu y una lista ingredientes  debera tener una numbre y una lista de pasos o instrucciones asi como los siguienetes comportamientos:
    - Agregar ingrediente
    - Consultar ingredientes 
    - Agregar Paso
    - Consultar Pasos 
'''

from receta import Receta

def main():
    receta = Receta('Pizza') 

    receta.menu()
    print(receta)

if __name__ == '__main__':
    main()
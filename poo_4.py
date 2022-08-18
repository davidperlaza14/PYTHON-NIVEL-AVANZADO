'''
__init__ 
Constructor de Clase


poo_4.py
script de Python que cree y asigne un valor a los atributos de un objeto tipo Ingrediente.  Los ingredientes seran modelados dentro de una clase en un modulo separado y tendran los siguientes atributos:

    - nombre
    - cantidad
    - unidad de medida

Ademas la clase ingrediente podraa recibir como argumentos los valors iniciales para sus atributos a traves del metodo constructor.

'''

from ingrediente import Ingrediente

def main():
    ingrediente = Ingrediente('Papa', 3, 'Kilos')

    print(ingrediente)


if __name__ == '__main__':
    main()
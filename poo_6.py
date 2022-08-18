'''
Herencia

class Derivado(Base_1, ..., Base_n):
    instrucciones
'''
'''
poo_6.py
script en Python que cree e imprima la informacion de un objeto de tipo Persona y de otro de tipo Deportista.
La clase Deportista heredara de la clase Persona, es decir que sera un tipo particular de persona.
'''
from persona import Persona
from deportista import Deportista

def main():
    per_1 = Persona('Hector tuga', 44) 
    deportista = Deportista('Pepe Nava', 33, 'Basketball')

    print(f'''Datos de la persona:
{per_1}''')
    print('-'*30)
    print(f'''Datos de la deportista:
{deportista}''')

    deportista.entrenar()
    deportista.hablar("Listo para ganar una medalla.")
    

if __name__ == '__main__':
    main()
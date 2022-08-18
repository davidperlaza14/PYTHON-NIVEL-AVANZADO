'''
herencia_e.py
script en Python que solicite la informacion de un objeto de tipo estudiante e imprima en pantalla sus datos.La clase estudiante heredara de la clase Persona, es decir que sera un tipo particular de persona. Tendra como atributos un promedio y un codigode estudiante  y como comportamiento podra estudiar una materia. Finalmente hacer que el estudiante ejecute el comportamiento "estudiar"
'''
from estudiante import Estudiante

def main():
    nombre = input('Nombre del estudiante: ')
    edad = input('Edad del estudiante: ')
    promedio = float(input('Promedio: '))
    codigo = input('codigo: ')

    estudiante = Estudiante(nombre, edad, promedio, codigo)
    print(f'''Los datos del estudiante son: 
{estudiante}''')
    print('-'*30)
    estudiante.estudiar('Quimica')
    estudiante.estudiar('Fisica')


if __name__ == '__main__':
    main()
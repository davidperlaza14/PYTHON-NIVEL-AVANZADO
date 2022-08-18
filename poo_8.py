'''
poo_8.py
script en python que tenga una lista de objetos tipo Pelicula. la lista debera ser ordenada segun el nombre de las peliculas, una vez ordenada se mostrara la lista adamas del menor y mayor dentro de la coleccion.
'''

from pelicula import Pelicula 

def main():
    peliculas = []
    peliculas.append(Pelicula('El padrino', 'Francis Ford Coppola', 1972, 175))
    peliculas.append(Pelicula('Sueño de fuga', 'Frank Darabont', 1994, 142))
    peliculas.append(Pelicula('La lista de schindler', 'Steven Spielberg', 1993, 195))
    peliculas.append(Pelicula('Toro', 'Martin Scorsese', 1980, 129))
    peliculas.append(Pelicula('Casablanca', 'Michael Curtiz', 194, 102))

    peliculas.sort()


    for pelicula in peliculas:
        print(pelicula)
        print('-'*32) 
    
    print(f'Menor pelicula en la coleccion:\n {min(peliculas)}')
    print(f'\nMayor pelicula en la coleccion:\n {min(peliculas)}')


if __name__ == '__main__':
    main()
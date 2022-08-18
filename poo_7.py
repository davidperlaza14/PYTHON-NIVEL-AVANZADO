'''
poo_7.py
script en Python que simule  un personaje  y un grupo de enemigos que podran
atacar al personaje principal de forma especial segun su naturaleza.
Los enemigos seran modelados con clases y se hara uso de polimorfismo para permitirles atacar de manera personalizada.
'''

import os
import random
import enemigo


def main():
    enemigos = []
    for i in range(5):
        tipo_enemigo = random.randint(0, len(enemigo.tipos)-1)
        if tipo_enemigo == enemigo.MOMIA:
            enemigos.append(enemigo.Momia())
        elif tipo_enemigo == enemigo.ZOMBI:
            enemigos.append(enemigo.Zombi())
        else:
            enemigos.append(enemigo.Vampiro())
    
    personaje = {'energia':100, 'fuerza': 6}
    GANANCIA_ENERGIA= 5
    INCREMENTO_FUERZA = 4

    while personaje['energia'] > 0 and len(enemigos) > 0:
        while personaje['energia'] > 0 and enemigos[0].energia > 0:
            os.system("clear")
            print(f'Energia: {personaje["energia"]} {enemigos[0].tipo}: {enemigos[0].energia}.')
            enemigos[0].atacar()
            personaje['energia'] -= enemigos[0].fuerza
            if personaje['energia'] > 0:
                print(f'Has atacado a {enemigos[0].tipo} y causaste {personaje["fuerza"]} de daño.')
                enemigos[0].energia -= personaje['fuerza']
                input('Continuar batalla...')
        if personaje['energia'] > 0:
            os.system("clear")
            print(f'Energia: {personaje["energia"]}     {enemigos[0].tipo}: {enemigos[0].energia}')
            print(f"Has derrotado a {enemigos[0].tipo}")
            print(f"Has recuperado {GANANCIA_ENERGIA} de energia")
            print(f"Tu fuerza a aumentado {INCREMENTO_FUERZA}")
            personaje['energia'] += GANANCIA_ENERGIA
            personaje['fuerza'] += INCREMENTO_FUERZA
            enemigos.pop(0)
            input('Continuar aventura.')
    if personaje['energia'] > 0:
        print("Has vencido a todos tus rivales.")
    else:
        print('Has sido vencido X.X')
 
if __name__ == '__main__':
    main()
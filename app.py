from os import system, name
import time
import sys

#################################################################################
#######################       FUNCTIONS        ##################################
#################################################################################

def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def tam_precio(tam):
    if tam == 't':
        return 580
    elif tam == 'd':
        return 430
    elif tam == 'i':
        return 280

def precio_ing(ing):
    if ing == 'ja':
        return 40
    elif ing == 'cha':
        return 35
    elif ing == 'pi':
        return 30
    elif ing == 'dq':
        return 40
    elif ing == 'ac':
        return 57.5
    elif ing == 'pp':
        return 38.5
    elif ing == 'sa':
        return 62.5

def opciones (nro):
    flag_tam = False
    flag_ing = False
    list_ing = []
    tamano = ''
    precio_total = 0.0
    print("Opciones: ")
    while flag_tam is False:
        tamano = str(input(f'Tamaño del Sandwich {nro}: Triple (t) Doble (d) Individual (i): ')).lower()
        if tamano == 't' or tamano == 'd' or tamano == 'i':
            flag_tam=True
        else:
            print('Debe seleccionar el tamaño correcto!!')
            
    precio_total += tam_precio(tamano)
    
    print("""Ingredientes:\n
          Jamon          (ja)
          Champi;ones    (cha)
          Pimenton       (pi)
          Doble Queso    (dq)
          Aceitunas      (ac)
          Pepperoni      (pp)
          Salchichon     (sa)\n""")
    
    precio_ingr = 0.0
    
    while flag_ing is False:
            ingrediente = str(input(f'Ingrediente del Sandwich {nro} (enter para finalizar):  ')).lower()
            if ingrediente == 'ja' or ingrediente == 'cha' or ingrediente == 'pi' or ingrediente == 'dq' or ingrediente == 'ac' or ingrediente == 'pp' or ingrediente == 'sa':
               list_ing.append(ingrediente)
               precio_ingr += precio_ing(ingrediente)
            elif ingrediente == "":
                break
            else:
               print('Debe seleccionar un ingrediente correcto!!')
    
    precio_total += precio_ingr
               
    sub_total(tamano,list_ing,precio_total)
    time.sleep(2)
    clear()
    return precio_total

##############################################################################
#########################       MAIN        ##################################
##############################################################################

logo = """******************************************
*          SANDWICHES UCAB               *
******************************************"""
print(logo)
nro_sandwiches = int(input('\n Numero de sandwiches que desea ordenar: '))
total = 0.0
for i in range(1,nro_sandwiches + 1):
   total += opciones(i) 

print(f'El pedido tiene un total de {nro_sandwiches} sandwich(es) por un monto de: {total} ')
print('Gracias por su compra regrese pronto!')
time.sleep(5)
sys.exit
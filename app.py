from functions import *

##############################################################################
#########################       MAIN        ##################################
##############################################################################

def main():
    logo = """******************************************
    *          SANDWICHES UCAB               *
    ******************************************"""
    print(logo)
    sandwiches_comprados = list()
    valor = str(input('\n Numero de sandwiches que desea ordenar: '))
    validar =valor.isdigit()
    if not validar:
        print('Ingrese nuevamente el numero de sandwiches sin letras\n'
              'El numero de Sandwiches no puede ser mayor a 10\n\n')
        main()
    else:
        nro_sandwiches = int(valor)
        total = 0.0
        for i in range(1,nro_sandwiches + 1):
           total += opciones(i,sandwiches_comprados)

        verificacion_total(nro_sandwiches,sandwiches_comprados,total)

main()
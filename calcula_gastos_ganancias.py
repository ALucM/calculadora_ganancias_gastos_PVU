import time
import msvcrt

menuinicio = """
#############################
#############################
#############################
######## Calculadora ########
####  Gastos & Ganancias ####
########## En PVU  ##########
#############################
### Pulse 1 para comenzar ###
#### Pulse 2  para salir ####
########## V: 0.7 ###########
"""

menucantidad = """
##############################
##############################
##############################
####  Gastos & Ganancias #####
########## En PVU  ###########
##############################
##############################
# Cuantas plantas compraste? #
##############################
##############################
"""

menuvalorv1 = """
#############################
#############################
#############################
####  Gastos & Ganancias ####
########## En PVU  ##########
#############################
######## 1- LE  #############
#############################
#############################
#############################
"""

menuplantasv2 = """
#############################
#############################
#############################
####  Gastos & Ganancias ####
########## En PVU  ##########
#############################
######## 1- LE  ###########
#############################
####### 2- PVU Token  #######
#############################
"""


menutipoplantas = """
#############################
#### Que tipo de plantas ####
######## compraste?  ########
#############################
###  1- Sunflower Sapling ###
#############################
##### 2- Sunflower Mama #####
#############################
"""


def main():
    opcionMenuInicio = int(input(menuinicio))

    if opcionMenuInicio == 1:
        opcionMenuValorv1 = int(input(menuvalorv1))

        if opcionMenuValorv1 == 1:
            opcionMenuCantidad = int(input(menucantidad))

            if opcionMenuCantidad >= 1:
                cantidad_plantas = opcionMenuCantidad
                opcionMenuTipoPlantas = int(input(menutipoplantas))

                if opcionMenuTipoPlantas:
                    tipo_plantas = ["", 0]
                    tipo_plantas[1] = opcionMenuTipoPlantas

                    if tipo_plantas[1] == 1:
                        tipo_plantas[0] = "Sunflower Sapling"
                        valor_plantas = cantidad_plantas * 100
                        valor_macetas = cantidad_plantas * 50
                        valor_agua = 50
                        ganancia_per_planta = 250
                        ganancia_total = ganancia_per_planta * cantidad_plantas - \
                        valor_plantas - valor_macetas - valor_agua

                        print("Estos son los valores estimados de gasto en " +
              str(cantidad_plantas) + " plantas " + str(tipo_plantas[0]))
                        print("El valor de las plantas es: " + str(valor_plantas) + "LE")
                        print("El valor de las macetas es: " + str(valor_macetas) + "LE")
                        print("El valor del agua es: " + str(valor_agua) + "LE")
                        print("Y la ganancia total es de " + str(ganancia_total) + " LE")

                    time.sleep(2)

                    print("\nPresione una tecla para continuar...")
                    msvcrt.getch()

                    if tipo_plantas[1] == 2:
                        tipo_plantas[0] = "Sunflower Mama"
                        valor_plantas = cantidad_plantas * 200
                        valor_macetas = cantidad_plantas * 100
                        valor_agua = 50
                        ganancia_per_planta = 850
                        ganancia_total = ganancia_per_planta * cantidad_plantas - \
                        valor_plantas - valor_macetas - valor_agua

                        print("\nEstos son los valores estimados de gasto en " +
              str(cantidad_plantas) + " plantas " + str(tipo_plantas[0]))
                        print("El valor de las plantas es: " + str(valor_plantas) + "LE")
                        print("El valor de las macetas es: " + str(valor_macetas) + "LE")
                        print("El valor del agua es: " + str(valor_agua) + "LE")
                        print("Y la ganancia total es de " + str(ganancia_total) + " LE")

                        time.sleep(2)

                        print("\nPresione una tecla para continuar...")
                        msvcrt.getch()

                    else:
                        print("Selecione La opcion correcta \n \n \n")
                        main()
                else:
                        print("Selecione una cantidad por encima de 1 \n  \n \n")
                        main()
            else:
                        print("Selecione La opcion correcta \n  \n \n")
                        main()
        else:
                        print("Selecione La opcion correcta \n  \n \n")
                        main()
    else:
                        print("\nPresione una tecla para continuar...")
                        msvcrt.getch()
                        


if __name__ == "__main__":
    main()

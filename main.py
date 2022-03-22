
from clases.Inmortal import *
from clases.AlterHerenciaMultiple import *

def eleccion():
    variable = int(input("Por favor, introduzca qué ejercicio desea realizar: \n 1: El día siguiente\n 2: Inmortal\n 3: Alternativa a la herencia múltiple\n"))
    if variable == 1:
        import clases.Edificios
    elif variable == 2:
        Inmortal.ejecucion()
    elif variable == 3:
        Interfaz_Cristal().Paredes(['NORTE', 'SUR', 'ESTE', 'OESTE'])
        print()
        Interfaz_Cristal().Paredes(['NORTE', 'SUR', 'ESTE', 'OESTE'])
        print()
        Interfaz_Cristal().ParedCortina('NORTE', 4)
        print()
        Interfaz_Cristal().Superficie()
        print()
        Interfaz_Cristal().ComprobarProteccion('NORTE')
    else:
        print("Sólo son válidos los valores 1,2 y 3.\n")
        eleccion()
eleccion()
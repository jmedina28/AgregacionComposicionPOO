<h1 align="center">Agregación y composición</h1>

<h3 align="center">Autores de este proyecto:</h3>

1. [@jmedina28](https://github.com/jmedina28)

---
En este [repositorio](https://github.com/jmedina28/AgregacionComposicionPOO) quedan resueltos los ejercicios de agregación y composición para POO. Para llevar a cabo el proyecto me he documentado a través de la teoría que se encuentra en el campus virtual y de diversas fuentes que he encontrado.
***
## Índice
1. [El día siguiente.](#id1)
3. [Inmortal.](#id2)
3. [Alternativa a la herencia múltiple.](#id3)

***

## Ejercicio 1: El día siguiente<a name="id1"></a>

En este ejercicio...

El código empleado para resolverlo es el siguiente:

```python

class Edificio:
    def __init__(self, ubicacion, empresa, empleado, estado):
        self.ubicacion = ubicacion
        self.empresa = empresa
        self.empleado = empleado
        self.estado = estado

    def catastrofe(self):
        self.estado = "Destruido"
        self.empleado = "Fallecidos"

    def caracteristicas():
        print("\nEl edificio A tiene las siguientes características:\n1. Ubicación: "+str(A.ubicacion) +
              "\n2. Empresa: "+str(A.empresa)+"\n3. Empleado: "+str(A.empleado)+"\n4. Estado: "+str(A.estado))
        print("\nEl edificio B tiene las siguientes características:\n1. Ubicación: "+str(B.ubicacion) +
              "\n2. Empresa: "+str(B.empresa)+"\n3. Empleado: "+str(B.empleado)+"\n4. Estado: "+str(B.estado))
        print("\nEl edificio C tiene las siguientes características:\n1. Ubicación: "+str(C.ubicacion) +
              "\n2. Empresa: "+str(C.empresa)+"\n3. Empleado: "+str(C.empleado)+"\n4. Estado: "+str(C.estado))


A = Edificio("Nueva York", "YooHoo!", "Sr. Martin", "Bueno")
B = Edificio("Nueva York", "YooHoo!", "Sr. Salim", "Bueno")
C = Edificio("Los Ángeles", "YooHoo!", "Sra. Xing", "Bueno")

print("Ha elegido ejecutar el ejercicio 1, A continuación se le van a mostrar los datos de 3 edificaciones.")
Edificio.caracteristicas()


variable = int(input(
    "\nSi desea provocar una catástrofe en Nueva York pulse 1, si desea provocarla en Los Ángeles pulse cualquier otra tecla: "))
if variable == 1:
    Edificio.catastrofe(A), Edificio.catastrofe(B)
    Edificio.caracteristicas()
    variable2 = int(input(
        "\nSi desea provocar el Apocalipsis pulse 1, en caso contrario pulse cualquier otro valor y se finalizará con la ejecución del programa: "))
    if variable2 == 1:
        Edificio.catastrofe(C)
    else:
        Edificio.caracteristicas()
        exit()
else:
    Edificio.catastrofe(C)
    Edificio.caracteristicas()
    variable2 = int(input(
        "\nSi desea provocar el Apocalipsis pulse 1, en caso contrario pulse cualquier otro valor y se finalizará con la ejecución del programa: "))
    if variable2 == 1:
        Edificio.catastrofe(A), Edificio.catastrofe(B)
    else:
        Edificio.caracteristicas()
        exit()
Edificio.caracteristicas()

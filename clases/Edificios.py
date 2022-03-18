
class Edificio:
    def __init__(self, ubicacion, empresa, empleado, estado):
        self.ubicacion = ubicacion
        self.empresa = empresa
        self.empleado = empleado
        self.estado = estado

    def catastrofe(self):
        if self.ubicacion == "Nueva York":
            self.estado = "Destruido"
            self.empleado = "Fallecidos"


A = Edificio("Nueva York", "YooHoo!", "Sr. Martin", "Bueno")
B = Edificio("Nueva York", "YooHoo!", "Sr. Salim", "Bueno")
C = Edificio("Los Ángeles", "YooHoo!", "Sra. Xing", "Bueno")

print("Ha elegido ejecutar el ejercicio 1, A continuación se le van a mostrar los datos de 3 edificaciones.")
print("\nEl edificio A tiene las siguientes características:\n1. Ubicación: "+str(A.ubicacion) +
      "\n2. Empresa: "+str(A.empresa)+"\n3. Empleado: "+str(A.empleado)+"\n4. Estado: "+str(A.estado))
print("\nEl edificio B tiene las siguientes características:\n1. Ubicación: "+str(B.ubicacion) +
      "\n2. Empresa: "+str(B.empresa)+"\n3. Empleado: "+str(B.empleado)+"\n4. Estado: "+str(B.estado))
print("\nEl edificio C tiene las siguientes características:\n1. Ubicación: "+str(C.ubicacion) +
      "\n2. Empresa: "+str(C.empresa)+"\n3. Empleado: "+str(C.empleado)+"\n4. Estado: "+str(C.estado))


variable = int(input(
    "Si desea provocar una catástrofe en Nueva York pulse 1, en caso contrario pulse cualquier otro valor: "))
if variable == 1:
    Edificio.catastrofe(A)
    Edificio.catastrofe(B)
else:
    exit()

print("\nEl edificio A tiene las siguientes características:\n1. Ubicación: "+str(A.ubicacion) +
      "\n2. Empresa: "+str(A.empresa)+"\n3. Empleado: "+str(A.empleado)+"\n4. Estado: "+str(A.estado))
print("\nEl edificio B tiene las siguientes características:\n1. Ubicación: "+str(B.ubicacion) +
      "\n2. Empresa: "+str(B.empresa)+"\n3. Empleado: "+str(B.empleado)+"\n4. Estado: "+str(B.estado))
print("\nEl edificio C tiene las siguientes características:\n1. Ubicación: "+str(C.ubicacion) +
      "\n2. Empresa: "+str(C.empresa)+"\n3. Empleado: "+str(C.empleado)+"\n4. Estado: "+str(C.estado))

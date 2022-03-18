
class Edificio:
    def __init__(self, ubicacion, empresa, empleado, estado):
        self.ubicacion = ubicacion
        self.empresa = empresa
        self.empleado = empleado
        self.estado = estado
    
    def catastrofe(self):
        if self.ubicacion == "Nueva York":
            self.estado = "Destruido"
        

A = Edificio("Nueva York", "YooHoo!", "Sr. Martin", "Bueno")
B = Edificio("Nueva York", "YooHoo!", "Sr. Salim", "Bueno")
C = Edificio("Los Ángeles", "YooHoo!", "Sra. Xing", "Bueno")


print(A.ubicacion, A.empresa, A.empleado, A.estado, sep="\n")

A.catastrofe()

print(A.ubicacion, A.empresa, A.empleado, A.estado)


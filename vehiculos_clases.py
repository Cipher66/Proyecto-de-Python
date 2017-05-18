class Vehiculo():
    def __init__(self, nombre, faccion, tipo):
        self.nombre = nombre
        self.faccion = faccion
        self.tipo = tipo
    
    def __str__(self):
        return "Nombre: faccion: %s, tipo: %s" % (self.nombre, self.faccion)
"""
class Caza(Vehiculo):
    def __init__(self, nombre):
        super().__init__(nombre, faccion, tipo)

    def caza(self):
        return(self.nombre + "is searching. " + self.faccion +" es de la OTAN "+ self.tipo+" y es un caza multirol")
"""

my_vehicle = Vehiculo("FV-720", "AAF", "Vehiculo de Combate de Infatería")

print(my_vehicle)

#print(Caza('F/A-181', 'OTAN', 'polivalente'))

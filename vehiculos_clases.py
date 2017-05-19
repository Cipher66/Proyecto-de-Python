class Vehiculo():
    def __init__(self, nombre, faccion, tipo):
        self.nombre = nombre
        self.faccion = faccion
        self.tipo = tipo
    
    def __str__(self):
        return "Nombre: %s, faccion: %s, tipo: %s" % (self.nombre, self.faccion, self.tipo)
"""
class Caza(Vehiculo):
    def __init__(self, nombre):
        super().__init__(nombre, faccion, tipo)

    def caza(self):
        return(self.nombre + "is searching. " + self.faccion +" es de la OTAN "+ self.tipo+" y es un caza multirol")
"""

class Vehiculo():
    def __init__(self, nombre, faccion, tipo):
        self.nombre = nombre
        self.faccion = faccion
        self.tipo = tipo

class Caza(Vehiculo):
    def __init__(self, nombre):
        super().__init__(nombre, faccion, tipo)

    def caza(self):
        print(self.nombre + "is searching. " + self.faccion +" es de la OTAN "+ self.tipo+" y es un caza multirol")

print(Caza('F/A-181'))

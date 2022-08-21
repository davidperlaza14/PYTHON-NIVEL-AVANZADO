'''Herencia'''

class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color,ruedas)
        # Vehiculo.__init__(self,color,ruedas)
        # self.color = color
        # self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return super().__str__() + ", {}km/h, {} cc ".format(self.color, self.velocidad, self.ruedas, self.cilindrada )
        # return Vehiculo.__str__(self) + ", {}km/h, {} cc ".format(self.color, self.velocidad, self.ruedas, self.cilindrada )
        # z = "Color {}, {}km/h, {} ruedas, {} cc"

# x = Vehiculo("Negro", 4)
# print(x)

Y = Coche("Negro", 4, 120, 1500)
print(Y)
        
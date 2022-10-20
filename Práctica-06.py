
""""Escribir una clase en python que contenga un método que convierta un
número entero en su cubo."""


class Círculo:

    def __init__(self,radio):
        self.radio = radio

    def calcular_radio(self):
        self.radio=(self.radio*self.radio)*3.14

    def mostrar(self):
        print("El radio del círculo es: {}".format(self.radio))

circulo1=Círculo(int(input("Ingrese el radio del círculo: ")))
circulo1.calcular_radio()
circulo1.mostrar()





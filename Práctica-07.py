""""Crear una clase Persona que contenga dos atributos: nombre y edad.
Nombre y edad se ingresarán por teclado en el constructor.
Declarar una segunda clase llamada Empleado que herede de la clase
Persona y agregue un atributo sueldo y muestre si debe pagar
impuestos (10% de su sueldo) (sueldo superior a 4000)
Instanciar la clase Empleado, mostrar el sueldo del empleado y cuánto
debe pagar de impuesto."""



class persona:
    def __init__(self):
        self.nombre=input("Ingrese su nombre: ")
        self.edad=int(input("Ingrese su nombre: "))

    def imprimir(self):
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad))


class empleado(persona):
    def __init__(self,sueldo):
        self.sueldo=sueldo

    def pagar_impuestos(self):
        if self.sueldo>4000:
            self.sueldo=self.sueldo*0.10
            print("Usted necesita pagar el 10% de su sueldo")
        else:
            self.sueldo = self.sueldo*0
            print("Usted no necesita pagar el 10% de su sueldo")

    def mostrar(self):
        print("El pago total es: {}".format(self.sueldo))

empleado1=empleado(int(input("Ingrese el monto de su sueldo: ")))
empleado1.pagar_impuestos()
empleado1.mostrar()

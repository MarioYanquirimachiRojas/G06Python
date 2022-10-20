
"Factorial"

numero=int(input("Ingrese el numero: "))
a=1
resultado_factorial=1

while a<numero:
        resultado_factorial=resultado_factorial*(a+1)
        a=a+1

print("El factorial es: {}".format(resultado_factorial))


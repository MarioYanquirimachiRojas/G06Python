"""Ejercicios de práctica"""

edad=int(input("Estimado usuario ingrese su edad: "))


if 0<edad<18:
    print("Usted es menor de edad")
elif 18<=edad<65:
    print("Usted es mayor de edad")
elif 65<=edad<=100:
    print("Usted es de tercera edad")
else:
    print("Usted ingresó una edad errónea")
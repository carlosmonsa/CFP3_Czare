#EJERCICIO 1
# meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre" ]
# print(meses)

# #EJERCICIO 2
# #  Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

# palabra = input ("Ingrese una palabra: ")
# print(palabra * 10)
# #salto de linea
# print("hola/n pedro")

#EJERCICO 3
#  Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar

# numero =int(input("ingrerse un numero: "))
# if numero % 2 ==0: # PARA SABER SI ES PAR O IMPAR
#     print(f"{numero} es par.")
# else:
#     print(f"{numero} es impar.")    

 #EJERCICO 4
#  Para pagar un determinado impuesto se debe ser mayor de 18 años y tener un ingreso mensual igual o mayor
# a $200.000. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por
#  pantalla si el usuario debe pagar el impuesto o no.

# edad =int(input("Ingrese su edad:"))
# sueldo = int(input("ingrese su sueldo":))
# if edad >= 18 and sueldo >= 200000:
#     print("El usuario debe abonar el impuesto")
# else:
#     print("El usuario no debe abonar el impusto")    

#EJERCICIO 5
# Escribir un programa para una empresa de juegos para todas las edades y quiere calcular de forma
# automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario 
# la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, 
# si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.

edad = int(input("Ingrese su edad: "))

if edad < 4: 
    print("Cliente puede entrar gratis")
elif edad > 4 and edad <= 18:
    print("El precio de la entrada es $500.")
elif edad > 18:
    print("El precio de la entrada es $1000.")    


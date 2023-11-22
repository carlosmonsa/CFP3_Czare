#EJ:1 crea dos variables, num 1 y num2, e imprime la suma, resta, multiplicacion y division de ambas.

# num1 = int(input("ingrese un numero: "))
# num2= int(input("ingrese otro numero: "))

# suma = num1 + num2
# resta = num1 - num2
# multi = num1 * num2
# div = num1 / num2

# print(f"la suma de ambos es {suma} y su resta es: {resta}. la division es {div} y la multiplicacion {multi}")

#EJ2: 
#Ingrese un numero y verifique si es positivo, negativo o cero e imprime un mensaje correspondiente

# num = int(input("Ingrese un numero"))

# if num > 0: 
#     print(f"{num} es positivo")
# elif num < 0:
#     print(f"{num} es negativo")
# else:
#     print(f"{num} es igual a 0")

# #EJ3:Utiliza un bucle while para imprimir los números del 1 al 10.
# contador = 0
# while contador <=10:
#    contador = contador+1
#    print(contador)


# #EJ4:Dada la siguiente lista lista_num = [1,3,4,2,1,5,8,7,9,2,3,4,3,6], 
# Calcular la suma y el promedio de sus elementos.

# lista_num = [1,3,4,2,1,5,8,7,9,2,3,4,3,6]
# suma_lista = 0

# for i in lista_num:
#     suma_lista += i
# print(suma_lista)
# promedio = suma_lista / (len(lista_num))
# print(round(promedio,2))



# #EJ5:Teniendo en cuenta la lista anterior eliminar los elementos duplicados y mostrar la lista final.
# (Para este ejercicio se pide no usar funciones propias de listas)

lista_num = [1,3,4,2,1,5,8,7,9,2,3,4,3,6]
lista_sin_dupli =[]
for i in lista_num:
    if i not in lista_sin_dupli:
         lista_sin_dupli.append(i)
print(lista_sin_dupli)



#EJ6:

# nombres = ("carlos","juan","tomas","mariano")
# cont = 0
# for i in nombres:
#     print(nombres[cont])
#     cont = cont + 1

#EJ7:

# set1 = {"a","b","c","d","e"}
# set2 = {"d","e","f","g","l"}

# print(set2.union(set1))
# print(set2.intersection(set1))
# print(set2.difference(set1))

#EJ8:
# diccionario de productos y sus precios, imprimir la lista de productos, los precios y producto-precio

# comida = {
#     "pizza1":5500,
#     "pizza2":5000,
#     "limonada": 1100,
#     "coca":1000,
# }

# for clave in comida.keys():
#     print(clave)
# for clave in comida.values():
#     print(clave)
# for clave in comida.items():
#     print(clave)



#EJ9:

# alumnos =["Claudio","Maria","Jose","pedro","a"]
# contador = len(alumnos)
# contador = contador - 1
# # print(contador)
# while contador >= 0:
#     print(alumnos[contador])
#     contador = contador - 1

#EJ10:
#frase = input("ingrese una frase:")
# vocales = 0
# cantidad = len(frase)
# for i in range(cantidad):
#     if frase[i] == "a":
#         vocales = vocales + 1
#     if frase[i] == "e":
#         vocales = vocales + 1
#     if frase[i] == "i":
#         vocales = vocales + 1
#     if frase[i] == "o":
#         vocales = vocales + 1
#     if frase[i] == "u":
#         vocales = vocales + 1
# print(vocales)
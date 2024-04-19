# num =10
# def doblar_numero(num):
#     num *=2
#     return num

# resultado = doblar_numero(num)
# print(resultado)
# print(num)

# def doblar_lista(lista):
#     for i in range(len(lista)):
#         lista[i] *= 2
#     return lista

# lista =[10,20,30]
# copia_lista = lista[:] # mantener lista original
# resultado = doblar_lista(copia_lista)
# print(resultado)
# print(lista)


# def suma_args(*args):# el asterisco(*) define el codigo
#     resultado = 0
#     for i in args:
#         resultado += i
#     return resultado

# resultado = suma_args(20,40,10,5,20,30,40,70,50,15,60)
# print(resultado)

# CREAR UNA FUNCION QUE CALCULE EL PERIMETRO 

# def calcular_perimetro(*args):
#         resultado = 0
#         for i in args:
#             resultado += i
#         return resultado

# resultado = calcular_perimetro(10,20,30,40)
# print(resultado)


# EFICIENCIA DE EJECUCION
# def suma_for(lista):
#     suma = 0
#     for i in lista:
#         suma += i
#     return suma(lista)

# lista = [1,2,3,4,5,6,7]
# resultado_for = suma_for(lista)
# resultado_suma = suma_sum(lista)


#crear una funcion que acepte como argumentos un numermo indefinido de string
# y devuelva una cadena que contenga todo los argunmentos en una sola cadena
#separada por un separador opcional, si no se proporciona un separador
#la funcion debe utilizar un espacio en blanco por default.


def concatenar(*args,separador= ' '):
    return separador.join(args)

resultado = concatenar("milagros","Davis","Jessica",separador="_")
print(resultado)

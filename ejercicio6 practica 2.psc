Algoritmo ejercicio6
	Definir i , f, ff,vector , temp Como Entero
	Dimension  vector[10]
	temp = 0
	f = 0
	ff = 0
	Para i = 0  Hasta 10 - 1  Con Paso 1 Hacer
		Imprimir " ingrese el  numero "
		º
		Para f = 0 Hasta i Con Paso 1 Hacer
			Para ff = f  Hasta i Con Paso 1 Hacer
				Si vector[f] > vector[ff] Entonces
					tem = vector[f]
					vector[f] = vector[ff]
					vector[ff] = temp
				Fin Si
			Fin Para
		Fin Para
	Fin Para
	Para i = 0  Hasta 10 - 1  Con Paso 1 Hacer
		Imprimir vector[1]
	Fin Para
FinAlgoritmo

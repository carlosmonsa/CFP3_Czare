Algoritmo ejercicio_2
	Definir dimensionArreglo , valoresArreglo Como Entero
	Imprimir " ingrese la dimension del arreglo: "
	Leer  dimensionArreglo
	Dimension valoresArreglo[dimensionArreglo]
	Para i = 0  Hasta dimensionArreglo Con Paso 1 Hacer
		Imprimir " ingrese los numeros del arreglo: "
		leer valoresArreglo[i]
	Fin Para
	mayor  = valoresArreglo[0]
	menor  = valoresArreglo[0]
	Para i = 1  Hasta dimensionArreglo -1 Con Paso 1 Hacer
		si valoresArreglo[i] > mayor Entonces
			mayor = valoresArreglo[i]
		SiNo
			si valoresArreglo[i] < menor Entonces
				menor = valoresArreglo[1]
			FinSi
		FinSi
	Fin Para
	Imprimir " El numero mayor es: " mayor
	Imprimir " El numero menor es: " menor
FinAlgoritmo

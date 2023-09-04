Algoritmo OperacionesNumericas
	// solicito el 1er numero
	Escribir 'ingrese el 1er numero: '
	Leer num1
	// solicito el 2do numero
	Escribir 'ingrese 2do numero: '
	Leer num2
	// calculos
	suma <- num1+num2
	resta <- num1-num2
	multi <- num1*num2
	// muestre los resaultadosde las operaciones
	Escribir 'la suma de los numeros es: ', suma
	Escribir 'la resta de los numeros es: ', resta
	Escribir 'la multiplicacion de los numeros : ', multi
	Si num2<>0 Entonces
		division <- num1/num2

		Escribir 'la division de los numeros es: ', division
	
	SiNo
		Escribir ' no se puede dividir por 0: '
	FinSi
	
FinAlgoritmo

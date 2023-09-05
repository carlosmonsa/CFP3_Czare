Algoritmo dolar
	//  Desarrollar un programa que al comenzar, imprima por terminal el mensaje "Bienvenido al conversor de pesos a dólares!"
	//, luego, el programa deberá mostrar otro mensaje que diga "Ingrese el monto en pesos para convertirlo a dólares: ", y se deberá quedar
	//esperando a que el usuario ingrese el valor. Luego el programa deberá imprimir por terminal el mensaje
	//"Su equivalente en dólares es: <resultado> dólares" donde <resultado> debe ser el valor que resulte de la 
	//conversión. Ej: Si el usuario ingresa "183", el mensaje final será "Su equivalente en dólares es: 1 dolares"
	Definir montoPesos, montoDolar Como real;
	Escribir "bienvenido al conversor de pesos a dolares: " ;
	Escribir "ingrese monto en pesos para convertirlo a dolares: " ;
	Leer montoPesos;
	montoDolar=montoPesos/570 ;
	Escribir "equivalente en dolares es: ", montoDolar; 
	
FinAlgoritmo

Algoritmo dolar
	//  Desarrollar un programa que al comenzar, imprima por terminal el mensaje "Bienvenido al conversor de pesos a d�lares!"
	//, luego, el programa deber� mostrar otro mensaje que diga "Ingrese el monto en pesos para convertirlo a d�lares: ", y se deber� quedar
	//esperando a que el usuario ingrese el valor. Luego el programa deber� imprimir por terminal el mensaje
	//"Su equivalente en d�lares es: <resultado> d�lares" donde <resultado> debe ser el valor que resulte de la 
	//conversi�n. Ej: Si el usuario ingresa "183", el mensaje final ser� "Su equivalente en d�lares es: 1 dolares"
	Definir montoPesos, montoDolar Como real;
	Escribir "bienvenido al conversor de pesos a dolares: " ;
	Escribir "ingrese monto en pesos para convertirlo a dolares: " ;
	Leer montoPesos;
	montoDolar=montoPesos/570 ;
	Escribir "equivalente en dolares es: ", montoDolar; 
	
FinAlgoritmo

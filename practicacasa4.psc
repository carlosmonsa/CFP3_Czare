Algoritmo calificaciones
	//Escribe un programa que pida al usuario ingresar una calificaci�n num�rica entre 0 y 10. Luego, el programa debe verificar
	//si la calificaci�n est� dentro del rango de aprobaci�n (por ejemplo, entre 6 y 10) y debe mostrar un mensaje que diga "Aprobado".
	//En caso contrario, debe mostrar "Reprobado".
	Definir nota Como Entero;
	Escribir "ingrese calificacion numerica entre 0 y 10: ";
	Leer nota;
	Si nota >= 0 & nota <=10 Entonces
		Si nota >=6 & nota <= 10; Entonces
			Escribir "Aprobado"; 
		SiNo 
			Escribir "Desaprobado";
		FinSi
	SiNo
		Escribir "Nota fuera de rango, reintente nuevamente.";
	FinSi
FinAlgoritmo

import funciones as fn

while True:
        condicion=input(
"""Por favor ingrese la opcion que desee utilizar
        1. Suma
        2. Resta
        3. Multiplicacion
        4. Division
        5. Salir
Numero: """)
    
        if condicion =="1":   
            a,b = fn.pedir_numeros()
            fn.suma(a,b)
            
        elif condicion =="2":   
            a,b = fn.pedir_numeros()
            fn.resta(a,b)
           
        elif condicion =="3":   
            a,b = fn.pedir_numeros()
            fn.multiplicacion(a,b)

        elif condicion =="4":   
            a,b = fn.pedir_numeros()
            fn.division(a,b)
        elif condicion =="5":   
            print("Gracias por utilizar esta calculadora! Hasta luego!")
            break
        else:
            print("No ingreso una opcion correcta")
        
 
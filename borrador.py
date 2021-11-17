def nombre_chofer(Taxis):
    while True:
                opcion = input(
                """Por favor, elija una opcion:
                1- Auto 1
                2- Auto 2
                3- Auto 3
                4-Salir
                Numero """)

                if opcion == "1":
                    nombre_1 = input("Ingrese el nombre del chofer: ")
                    if nombre_1.isalpha():
                        for i in range(len(Taxis)):
                            if Taxis[1][0] == "chofer_1":
                               Taxis[1][0] = nombre_1
                            print(f"El nombre del chofer del Auto 1 es {Taxis[1][0]}")
                        
                elif opcion == "2":
                    nombre_2 = input("Ingrese el nombre del chofer: ")
                    if nombre_2.isalpha():
                        for i in range(len(Taxis)):
                            if Taxis[1][1] == "chofer_1":
                               Taxis[1][1] = nombre_2
                            print(f"El nombre del chofer del Auto 2 es {Taxis[1][1]}")

                elif opcion == "3":
                    nombre_3 = input("Ingrese el nombre del chofer: ")
                    if nombre_3.isalpha():
                        for i in range(len(Taxis)):
                            if Taxis[1][2] == "chofer_1":
                               Taxis[1][2] = nombre_3
                            print(f"El nombre del chofer del Auto 3 es {Taxis[1][2]}")
                elif opcion =="4":   
                    break
                else:
                    print("No ingreso una opcion correcta")

def modificar_recorrido(Taxis):
  while True:
                opcion = input(
                """Por favor, elija una opcion:
                1- Auto 1
                2- Auto 2
                3- Auto 3
                4-Salir
                Numero """)

                if opcion == "1":
                    recorrido_1 = int(input("Ingrese el recorrido que desea cambiar: "))
                    for i in range(len(Taxis)):
                        if Taxis[2][0] == 45:
                            Taxis[2][0] = recorrido_1
                            print(f"El nuevo recorrido del auto 1 es de {Taxis[2][0]} kilometros")

                elif opcion == "2":
                    recorrido_2 = int(input("Ingrese el recorrido que desea cambiar: "))
                    for i in range(len(Taxis)):
                        if Taxis[2][1] == 30:
                            Taxis[2][1] = recorrido_2
                            print(f"El nuevo recorrido del auto 2 es de {Taxis[2][1]} kilometros")
                elif opcion == "3":
                    recorrido_3 = int(input("Ingrese el recorrido que desea cambiar: "))
                    for i in range(len(Taxis)):
                        if Taxis[2][2] == 50:
                            Taxis[2][2] = recorrido_3
                            print(f"El nuevo recorrido del auto 3 es de {Taxis[2][2]} kilometros")
                elif opcion =="4":   
                    break
                else:
                    print("No ingreso una opcion correcta")

def choferes_recorridos(Taxis):
    print(f"  AUTO  -  CHOFER  - RECORRIDO MÁX.")
    for i in range(len(Taxis[0])):
        print(f"{Taxis[0][i]} - {Taxis[1][i]} - {Taxis[2][i]}")

#Taxis=[["auto_1","auto_2","auto_3"],["chofer_1","chofer_2","chofer_3"],[45,30,50]]
#choferes_recorridos(Taxis)
while True:
    try:
        año = int(input("Por favor ingrese el año de la pelicula: "))
        if año <=0:
            print("El año de la película debe ser mayor de cero")
        elif (año >= 1930) and (año <= 2021):
            break
        else:
            print("El año debe ser mayor a a 1930 y menor o igual a 2021")
    except:
        print("ERROR.")

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 1], [2, 2], [3, 3]])
print(a.dot(b))
[[14 14]
 [32 32]]

print(a.T)
[[1 4]
 [2 5]
 [3 6]]

 Matriz_de_salarios
[[176.   301.   340.  ]
 [191.4  333.   343.2 ]
 [213.6  313.28 333.  ]]
Salario_Máximo:  343.2

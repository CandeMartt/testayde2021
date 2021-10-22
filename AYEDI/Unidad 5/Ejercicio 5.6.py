"""
##**Ejercicio 5.6 (Programa de Inventario de verduleria)**
Crear un programa que debe:
*    Contar con un stock de frutas y otro de verduras (El stock indica si venden o 
no esa fruta o verdura, no la cantidad) - dos listas que inician vacias
*    Contar con un menu y 3 funciones

      1. Agregar frutas o verduras al correspondiente stock (verificando que que sean nuevas)
      2. Consultar el stock de frutas o verduras
      3. Eliminar un elemento del stock
"""
#Agregar frutas o verduras segun corresponda
def agregar_productos():
    while True:
                opcion = input(
                """Por favor, elija una opcion:
                1- Agregar FRUTA al stock actual
                2- Agregar VERDURAS al stock actual
                3- Salir
                Numero """)

                if opcion == "1":
                    agregar_prod = input("Ingrese el producto que desee agregar: ")
                    if agregar_prod.isalpha():
                        if agregar_prod not in frutas:
                            frutas.append(agregar_prod)
                            print(f"Usted agregó {frutas}")
                        elif agregar_prod in frutas:
                            print("Esa fruta ya se encuentra en su stock") 
                elif opcion == "2":
                    agregar_prod = input("Ingrese el producto que desee agregar: ")
                    if agregar_prod.isalpha():
                       if agregar_prod not in verduras:
                            verduras.append(agregar_prod)
                            print(f"Usted agregó {verduras}") 
                       elif agregar_prod in verduras:
                            print("Esa verdura ya se encuentra en su stock") 
                elif opcion =="3":   
                    break
                else:
                    print("No ingreso una opcion correcta")

#Consultar stock de frutas o verduras
def consultar_stock():
    while True:
                opcion = input(
                """Por favor, elija una opcion:
                1- Consultar stock actual de FRUTA
                2- Consultar stock actual de VERDURA
                3- Salir
                Numero """)

                if opcion == "1":
                    print(frutas)
                elif opcion == "2":
                    print(verduras)
                elif opcion =="3":   
                    break
                else:
                    print("No ingreso una opcion correcta")

#Eliminar elemento del stock de frutas o verduras 
def eliminar_elemento_stock():
     while True:
                opcion = input(
                """Por favor, elija una opcion:
                1- Eliminar elemento del stock actual de FRUTA
                2- Eliminar elemento del stock actual de VERDURA
                3- Salir
                Numero """)

                if opcion == "1":
                    producto_eliminar = input("Ingrese el producto a eliminar: ")
                    if producto_eliminar in frutas:
                        frutas.remove(producto_eliminar)
                        print(f"Su stock actual seria: {frutas}")
                    elif producto_eliminar not in frutas:
                        print("Este producto no se encuentra en el stock actual")
                elif opcion == "2":
                    producto_eliminar = input("Ingrese el producto a eliminar: ")
                    if producto_eliminar in verduras:
                        verduras.remove(producto_eliminar)
                        print(f"Su stock actual seria: {verduras}")
                    elif producto_eliminar not in verduras:
                        print("Este producto no se encuentra en el stock actual")
                elif opcion =="3":   
                    break
                else:
                    print("No ingreso una opcion correcta")

frutas = []
verduras = []

while True:
    cant_stock_fruta = input("Ingrese cuantos productos distintos de fruta vende: ")
    contador = 1
    for i in range(int(cant_stock_fruta)):
        stock_frutas = input(f"Ingrese el producto numero {contador + i} de frutas:")
        if stock_frutas.isalpha():
            frutas.append(stock_frutas)
            print(f"En su stock actual hay {frutas}")
    cant_stock_ver = input("Ingrese cuantos productos distintos de verdura vende: ")
    for i in range(int(cant_stock_ver)):
        stock_verduras = input(f"Ingrese  el producto numero {contador + i} de verduras:")
        if stock_verduras.isalpha():
            verduras.append(stock_verduras)
            print(f"En su stock actual hay {verduras}")
       
    while True:
        condicion=input(
            """Por favor ingrese la opcion que desee utilizar
                1. Agregar fruta o verdura
                2. Consultar stock
                3. Eliminar elemento del stock
                4. Salir
            Numero: """)
        
        if condicion == "1": 
           agregar_productos()
        elif condicion =="2": 
           consultar_stock()
        elif condicion =="3": 
            eliminar_elemento_stock()
        elif condicion =="4":   
                print("Gracias por utilizar este programa! Hasta luego!")
                break
        else:
            print("No ingreso una opcion correcta")
    break



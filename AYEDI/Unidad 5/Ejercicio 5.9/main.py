#23/09/2021
'''
##**Ejercicio 5.9 (Empresa de Taxis)**
El programa debe:
*   Simular una empresa de taxis que cuente con tres Autos con sus respectivos choferes
```
Taxis=[["auto_1","auto_2","auto_3"],["chofer_1","chofer_2","chofer_3"],[45,50,30]]
```
    *  Cada auto cuenta con un chofer y no hace recorridos mayores a lo q se le indica
*   Contar con 6 funciones disponibles en el menu:
    1. Preguntar al usuario el recorrido del viaje e indicar posibles autos y choferes
    2. Modificar nombre chofer segun el nombre del auto.
        auto_1 -> "federico"
    3. Modificar el recorrido segun el nombre del auto.
        auto_1 -> 60
    4. Agregar nuevo auto a la empresa de Taxis, indicando auto, nombre chofer y recorrido maximo -> ULTIMO
    5. Observar una lista de autos choferes y recorrido maximo con el siguiente formato:
    6. Observar informacion de un chofer, verificando su existencia previamente

```
AUTO    -    CHOFER    -   RECORRIDO
auto_1  -   chofer_1   -   45
auto_2  -   chofer_1   -   50
```
    
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''
Taxis=[["auto_1","auto_2","auto_3"],["chofer_1","chofer_2","chofer_3"],[45,30,50]]
import funciones as fn

while True:
                opcion = input(
                """Por favor, elija una opcion:
                1- Recorrido que realizará el usuario
                2- Modificar nombre del chofer
                3- Modificar recorrido
                4- Agregar nuevo trabajador a la empresa
                5- Observar la lista completa de empleados
                6- Informacion de choferes
                7- Salir
                Numero """)

                if opcion == "1":
                   fn.recorrido_viaje(Taxis)           
                elif opcion == "2":
                   Taxis = fn.nombre_chofer(Taxis)
                elif opcion == "3":
                   Taxis = fn.modificar_recorrido(Taxis)
                elif opcion == "4":
                   Taxis = fn.nuevo_trabajador(Taxis)
                elif opcion == "5":
                   fn.choferes_recorridos(Taxis)
                elif opcion == "6":
                   Taxis = fn.informacion_chofer(Taxis)
                elif opcion =="7":   
                    break
                else:
                    print("No ingreso una opcion correcta")
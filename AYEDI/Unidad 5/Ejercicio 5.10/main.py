"""
##**Ejercicio 5.10 (Conversión de alfabeto)**
El programa debe:
*   Simular la conversion de un alfabeto a otro: Por ejemplo el moorse 
    (NO ES ESTRICTAMENTE NECESARIO USAR ESTE ALFABETO, PUEDE SER INVENTADO)

```
 alfabeto_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 alfabeto_b = ['.-' ,'-...' , '-.-.' ,'-..' ,'.', '..-.','--.', '....','..' ,'.---' , '-.-', '.-..','--' ,'-.' ,'---' ,'.--.','--.-' , '.-.' ,'...' ,'-','..-' ,'...-','.--','-..-' , '-.--' , '--..' ]
```

*   Contar con 6 funciones disponibles en el menu:
    1. Mostrar el alfabeto A
    2. Mostrar el alfabeto B
    3. Modificar una letra del Alfabeto A y el alfabeto B (debe ser la misma)
    4. Conversion de alfabeto A a alfabeto B: ejemplo **abc --> .--...-.-.**
    5. Conversion de alfabeto B a alfabeto A: ejemplo **.--...-.-. --> abc**
    6. Verificacion de existencia de una letra del alfabeto (debe seleccionar A o B)

*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
    """
import funciones as fn
alfabeto_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabeto_b = ['.-' ,'-...' , '-.-.' ,'-..' ,'.', '..-.','--.', '....','..' ,'.---' , '-.-', '.-..','--' ,'-.' ,'---' ,'.--.','--.-' , '.-.' ,'...' ,'-','..-' ,'...-','.--','-..-' , '-.--' , '--..' ]


while True:
                opcion = input(
                """Por favor, elija una opcion:
                1. Mostrar el alfabeto A
                2. Mostrar el alfabeto B
                3. Modificar una letra del Alfabeto A y el Alfabeto B 
                4. Conversion de alfabeto A a alfabeto B
                5. Conversion de alfabeto B a alfabeto A
                6. Verificar la existencia de una letra del alfabeto A
                7. Verificar la existencia de una letra del alfabeto B
                8- Salir
                Numero """)

                if opcion == "1":
                    fn.alfabeto(alfabeto_a)
                elif opcion == "2":
                    fn.alfabeto_moorse(alfabeto_b)
                elif opcion == "3":
                    alfabeto_a,alfabeto_b = fn.modificar_letras(alfabeto_a,alfabeto_b)
                elif opcion == "4":
                    alfabeto_a,alfabeto_b = fn.convertir_alfabeto_A(alfabeto_a,alfabeto_b)
                elif opcion == "5":
                    alfabeto_a,alfabeto_b = fn.convertir_alfabeto_B(alfabeto_a,alfabeto_b)
                elif opcion == "6":
                    fn.verificar_letras_a(alfabeto_a)
                elif opcion == "7":
                    fn.verificar_letras_b(alfabeto_b)
                elif opcion =="8":   
                    break
                else:
                    print("No ingreso una opcion correcta")

       
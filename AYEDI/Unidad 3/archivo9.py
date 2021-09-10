#18/08/2021
"""
El programa debe:

- pedir el ingreso de un número positivos al usuario y almacenar la respuesta en la variable numero.
- Verificar que se trate de un numero entero y sino mostrar un error
- Comprobar si el número es negativo. Si lo es, el programa debe avisa que no era eso lo que se había pedido. (si no hay error)
- Finalmente imprimir siempre el valor introducido por el usuario.(si no hay error)
"""
try:
    numero = int(input("por favor ingrese un numero: "))
    if numero < 0: #ya que los numero menores a cero no son enteros
        print("Pedi un numero positivo!")
    else: print("Soy un numero positivo")  
    print(f"El numero  que usted ingreso es {numero}")
except:
    print("No ingreso un numero entero")
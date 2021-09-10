"""
Pedir un dato dato_numerico
Imprimir la tabla del numero de 1 al 10
no deben aparecer errores.

"""

flag = True
while flag:
    try: 
        dato_numerico = int(input("Ingrese un numero"))
        flag = False
    except:
        print("ERROR.")
multiplicador = 1
while multiplicador <= 10:
    print(f"{multiplicador} x {dato_numerico} = {multiplicador * dato_numerico}")
    multiplicador+=1

#26/08/2021
"""
-Preguntar al usuario por una frase y una letra
-
"""
frase = input("Por favor ingrese una frase: ")
letra = input("Por favor ingrese la frase que euiere contar: ")
contador = 0

for i in frase:
    if i == letra:
        contador+=1
    
print(f"El numero de veces de la letra: {letra} es {contador}")
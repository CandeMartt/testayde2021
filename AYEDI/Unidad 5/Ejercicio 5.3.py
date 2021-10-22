"""
##**Ejercicio 5.3**
Crear una funcion que debe:

*    Pedir al usuario 5 materias (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
*    Verficiar que sea un nombre correcto
*    Almacenar los nombres en una lista
*    Mostrar las materias en orden alfabetico
*    No deben aparecer y se deben tener en cuenta todos los posibles errores
"""
def ordenamiento_palabras():
    lista_materias = []
    for i in range(5):
        while True:
            materia = input("Ingrese una materia: ")
            if materia.isalpha():
                lista_materias.append(materia)
                lista_materias.sort() #Puede ir por fuera, justo adentro del For
                print(f"Su materias son: {lista_materias}")
                break
            else:
                print("Por favor ingrese una palabra.")
    

ordenamiento_palabras()


        
       
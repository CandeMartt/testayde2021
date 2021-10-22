"""
Crear una funcion que debe: (usar diccionario)

Guardar en un diccionario los precios de las frutas de la tabla.
Preguntar al usuario por una fruta, un número de kilos y 
mostrar por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje informando ERROR.
"""

frutas = {
    "Banana":50, 
    "Manzana": 80
    }

def ver_frutas(): 
    fruta = input("Ingrese la fruta que desee ver: ").casefold().capitalize()
    valor = frutas.get(fruta,"No existe") #devuelve el valor, por ejemplo 50
    print(f"{fruta} :  $ {valor} por kilo")
    if fruta in frutas:
        while True:
            try:
                kilos = int(input("Ingrese cuantos kilo desea comprar: "))
                precio = valor*kilos
                print(f"El precio es $ {precio}")
                break
            except:
                print("ERROR.")

ver_frutas()

diccionario_frutas={    
    "Pera": 110,
    "Manzana": 90,
    "Naranja": 80
}

def venta_de_fruta():
    fruta=input("Ingrese la fruta que desea: ").capitalize()
    if fruta in diccionario_frutas:
        while True:
            try:
                cantidad=float(input("Ingrese la cantidad de kilos: "))
                precio=(diccionario_frutas.get(fruta))*cantidad
                print(f"Por {cantidad}Kg. de {fruta} debe pagar: {precio}")
                return
            except:
       
                print("Cantidad Erronea.")
    else:
        print("La fruta no existe")
venta_de_fruta()



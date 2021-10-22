#30/09/2021
datos_persona = {}
def datos_de_persona():
    nombre = input("Por favor ingrese el nombre: ").capitalize()
    datos_persona.update({"Nombre": nombre})
    while True:
        try:
            edad =int(input("Por favor ingrese su edad: "))
            datos_persona.update({"Edad": edad})
            break        
        except:
            print("ERROR.")
    direccion = input("Por favor ingrese la direccion: ").capitalize()
    datos_persona.update({"Direccion": direccion})
    while True:
        try:
            telefono =int(input("Por favor ingrese su telefono ej (3541384764): "))
            datos_persona.update({"Telefono": telefono})
            break        
        except:
            print("ERROR.")
    
    print(datos_persona)
    print(f"{nombre} tiene {edad} años, vive en {direccion} y su telefono es {telefono}")
    print(f"{datos_persona.get('Nombre')} tiene {datos_persona.get('Edad')} años, vive en {datos_persona.get('Direccion')} y su telefono es {datos_persona.get('Telefono')}")

datos_de_persona()
dinero_disponible = 50000.0 #esta es mi variable global

"""Ingresa dinero al sistema y actualiza el saldo"""

def ingresar_y_actualizar():
    global dinero_disponible
    while True:
        try:
            dinero_ingresar = float(input("Ingrese dinero a depositar: "))
            if dinero_ingresar > 0 :
                break
            else:
                print("Por favor ingrese una suma positiva ")
        except:
            print("ERROR. Ingrese un valor numérico")
       
    dinero_disponible += dinero_ingresar
    return dinero_disponible

#print(f"Nuevo Monto= {ingresar_y_actualizar()}")

"""Retirar dinero del sistema y actualizar saldo"""
def retirar_y_actualizar():
    global dinero_disponible
    while True:
        try:
            retirar_dinero = float(input("Ingrese el monto que desea retirar: "))
            if retirar_dinero > 0 and retirar_dinero <= dinero_disponible:
                break
            else:
                print("Por favor ingrese una suma positiva o menor al dinero disponible")
        except:
            print("ERROR. Ingrese un valor numérico")
       
    dinero_disponible -= retirar_dinero
    return dinero_disponible

def consultar_saldo():
    global dinero_disponible
    print(f"Su saldo disponible es {dinero_disponible}")

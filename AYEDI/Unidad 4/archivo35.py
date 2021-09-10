#Actividad Nº 4:
"""
*   Contar con 4 funciones:
  1.  Conversor de Grados Celcius a Fahrenheit(temperatura en °C).(buscar regla)
  2.  Conversor de cm3 a litros (cantidad de cm3)
  3.  Conversor de litros a cm3 (cantidad de litros)
  4.  Pesos a Dolares (pesos)
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los parametros y devolver el resultado al usuario
*   Gestionar posibles errores
"""

def conversor_grados():
  while True:
    try:
      celcius = float(input("Por favor ingrese los grados Celcius: "))
      fahrenheit = ( celcius * 1.8 ) + 32
      print(f"{celcius} grados celcius en Fahrenheit son: {fahrenheit}")
      break
    except:
      print("ERROR. Por favor ingrese un valor numérico.")

def conversor_medicion():
  while True:
    try:
      cm3 = float(input("Por favor ingrese el valor en cm3: "))
      litros = cm3 / 1000
      print(f"{cm3} cm3 son {litros} litros.")
      break
    except:
      print("ERROR. Por favor ingrese un valor numérico.")


def conversor_liquidos():
  while True:
    try:
      litros = float(input("Por favor ingrese el valor en litros: "))
      cm3 = litros * 1000
      print(f"{litros} litros son {cm3} cm3.")
      break
    except:
      print("ERROR. Por favor ingrese un valor numérico.")


def conversor_dinero():
  while True:
    try:
      pesos = float(input("Ingrese el valor en pesos: "))
      dolares = pesos / 182
      print(f"{pesos} pesos son {dolares} dolares.")
      break
    except:
      print("ERROR. Por favor, ingrese un valor numérico.")

while True:
      condicion=str(input(
        """Por favor ingrese la opcion que desee utilizar
            1. Conversor de grados Celcius a Fahrenheit
            2. Conversor de cm3 a litros
            3. Conversor de litros a cm3
            4. Conversor de cm3 a litros
            5. Salir
        Numero: """))
    
      if condicion == "1":   
        conversor_grados()
      elif condicion =="2":   
        conversor_medicion() 
      elif condicion =="3":   
        conversor_liquidos()
      elif condicion =="4":   
        conversor_dinero()
      elif condicion =="5":   
            print("Gracias por utilizar este conversor! Hasta luego!")
            break
      else:
          print("No ingreso una opcion correcta")
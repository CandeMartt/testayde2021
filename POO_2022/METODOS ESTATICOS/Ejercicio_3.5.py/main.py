from libreria import Persona as pe

try:
  peso = int(input("ingrese el peso: "))
  estatura = int(input("ingrese su estatura: "))
except:
  print("Error")

print(f"El IMC = {pe.calcular_IMC(peso,estatura)}")

try:
  fecha_nacimiento = input("Ingrese su fecha de nacimiento: ")
except:
  print("Error")

print(f"Edad = {pe.calcular_edad(fecha_nacimiento)}")
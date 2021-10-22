#30/09/2021
monedas = {
    "Peso":"$", 
    "Dolar": "USD",
    "Euro":  "€"
    }

def obtener_simbolo_2():
  moneda = input("Ingrese que tipo de moneda desea saber el simbolo: ").casefold().capitalize()
  valor = monedas.get(moneda,"No existe")
  print(f"El simbolo de {moneda} : {valor}")

obtener_simbolo_2()
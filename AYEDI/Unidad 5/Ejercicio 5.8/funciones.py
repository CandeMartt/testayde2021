#imprime la tabla con codigo, producto, precio, stock
def imprimir_matriz(base_productos):  
  print(f"C - Producto - Pr - Stock")
  for i in range(len(base_productos[0-1])):
    print(f"{base_productos[0][i]} - {base_productos[1][i]} - {base_productos[2][i]} - {base_productos[3][i]}")

def imprimir_matriz2(base_productos):
  print(f"--------------PRODUCTOS--------------")
  print(f"C \t PRODUCTO \t Pr$ \tStock")
  for i in range(len(base_productos)-1):
    if i !=0:
      print("")
    for j in range(len(base_productos)):
      print(f"{base_productos[j][i]}",end='\t')
  print("") 

#imprime el codigo del producto
def imprimir_codigo_producto(base_productos):
  print(f"--------------PRODUCTOS--------------")
  print(f"C \t PRODUCTO")
  for i in range(len(base_productos)-1):
    if i !=0:
      print("")
    for j in range(2):
      print(f"{base_productos[j][i]}",end='\t')
  print("") 

#funcion forma de pago (solo menu)
def forma_pago():
  while True:
      try:
          forma_pago = input("""Por favor ingrese su forma de pago:
            1. Credito
            2. Debito
            3. Efectivo
            Opcion: """)
          if forma_pago =="1":
            return "credito"
          elif forma_pago =="2":
            return "debito"
          elif forma_pago =="3":
            return "efectivo"
          else:
            print("Opcion incorrecta")
      except:
        print("ERROR.")

#funcion pago con credito
def pago_con_credito(base_productos):
  imprimir_matriz(base_productos)
  print(f"--------------PAGO CON CREDITO--------------")
  while True:
      try:
            print(f"Que producto desea vender:")
            for i in range(len(base_productos[1])):
              print(f"{base_productos[0][i]}  {base_productos[1][i]}")
            producto=input("--> ")
            if producto =="1":
              if(base_productos[3][0]>0):
                base_productos[3][0] = base_productos[3][0]-1 #resto stock
                print(f"El comprador debe pagar: {base_productos[2][0]*1.1}")
                return base_productos
              else:
                print("no hay stock")
            elif producto =="2":
              if(base_productos[3][1]>0):
                base_productos[3][1] = base_productos[3][1]-1 #resto stock
                print(f"El comprador debe pagar: {base_productos[2][1]*1.1}")
                return base_productos
              else:
                print("no hay stock")
            elif producto =="3":
              if(base_productos[3][2]>0):
                base_productos[3][2] = base_productos[3][2]-1 #resto stock
                print(f"El comprador debe pagar: {base_productos[2][2]*1.1}")
                return base_productos
              else:
                print("no hay stock")
            else:
              print("Opcion incorrecta")
      except:
        print("ERROR.")

#funcion pago con debito
def pago_con_debito(base_productos):
  imprimir_matriz(base_productos)
  print(f"--------------PAGO CON DÉBITO--------------")
  while True:
      try:
          print(f"Que producto desea vender:")
          for i in range(len(base_productos[1])):
            print(f"{base_productos[0][i]}  {base_productos[1][i]}")
          producto=input("--> ")
          if producto =="1":
            if(base_productos[3][0]>0):
              base_productos[3][0] = base_productos[3][0]-1 #resto stock
              print(f"El comprador debe pagar: {base_productos[2][0]}")
              return base_productos
            else:
              print("no hay stock")
          elif producto =="2":
            if(base_productos[3][1]>0):
              base_productos[3][1] = base_productos[3][1]-1 #resto stock
              print(f"El comprador debe pagar: {base_productos[2][1]}")
              return base_productos
            else:
              print("no hay stock")
          elif producto =="3":
            if(base_productos[3][2]>0):
              base_productos[3][2] = base_productos[3][2]-1 #resto stock
              print(f"El comprador debe pagar: {base_productos[2][2]}")
              return base_productos
            else:
              print("no hay stock")
          else:
            print("Opcion incorrecta")
      except:
        print("ERROR.")

#funcion pago con efectivo
def pago_con_efectivo(base_productos):
  imprimir_matriz(base_productos)
  print(f"--------------PAGO CON EFECTIVO--------------")
  while True:
      try:
          print(f"Que producto desea vender:")
          for i in range(len(base_productos[1])):
            print(f"{base_productos[0][i]}  {base_productos[1][i]}")
          producto=input("--> ")
          if producto =="1":
            if(base_productos[3][0]>0):
              base_productos[3][0] = base_productos[3][0]-1 #resto stock
              base_productos[2][0] -= base_productos[2][0]*0.1
              print(f"El comprador debe pagar: {base_productos[2][0]}")
              return base_productos
            else:
              print("no hay stock")
          elif producto =="2":
            if(base_productos[3][1]>0):
              base_productos[3][1] = base_productos[3][1]-1 #resto stock
              base_productos[2][1] -= base_productos[2][1]*0.1
              print(f"El comprador debe pagar: {base_productos[2][1]}")
              return base_productos
            else:
              print("no hay stock")
          elif producto =="3":
            if(base_productos[3][2]>0):
              base_productos[3][2] = base_productos[3][2]-1 #resto stock
              base_productos[2][2] -= base_productos[2][2]*0.1
              print(f"El comprador debe pagar: { base_productos[2][2]}")
              return base_productos
            else:
              print("no hay stock")
          else:
            print("Opcion incorrecta")
      except:
        print("ERROR.")

#consultar stock
def consultar_stock(base_productos):
  print(f"Producto  - Stock")
  for i in range(len(base_productos[0])):
    print(f"{base_productos[1][i]} - {base_productos[3][i]}")
  

#agregar stock
def agregar_stock(base_productos):
  consultar_stock(base_productos)
  try:
      producto = input("Indique cual es el producto: ")
      stock_nuevo = int(input("Agregar stock: "))
      if producto in base_productos[1]:
        base_productos[3][base_productos[1].index(producto)] += stock_nuevo
        print(f"Usted agregó {base_productos}")
      elif producto not in base_productos:
          print("Este producto no está disponible")
  except:
    print("ERROR.")
  return base_productos

#modificar precios de los productos
def modificar_precios(base_productos):
  while True:
      try:
          imprimir_matriz(base_productos)
          indicar_producto = input("Nombre del producto a modificar: ")
          precio_nuevo = input("Ingrese el nuevo precio: ")
          if indicar_producto in base_productos[1]:
              base_productos[2][base_productos[1].index(indicar_producto)] = precio_nuevo
              print(f"El nuevo precio de {indicar_producto} es {base_productos[2][base_productos[1].index(indicar_producto)]}")
              imprimir_matriz(base_productos)
              break
          else:
              print("Este auto no trabaja en esta empresa")
      except:
        print("ERROR.")
  return base_productos




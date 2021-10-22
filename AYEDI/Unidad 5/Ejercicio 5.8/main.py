'''
##**Ejercicio 5.8 (Programa de ventas)**
El programa debe:
*   Simular un programa que venda 3 productos
Codigo      Nombre     Precio Stock
    1     & producto1  & 300   & 5
    2     & producto2  & 400   & 4
    3     & producto3  & 500   & 7

*   El menu debe mostrar los productos a comprar. ->LISTO
*   Luego se debe contar con un menu de si se pagara en efectivo o tarjeta credito o debito -> LISTO
*   Contar con 7 funciones disponibles en el menu:
  1.  Ver menu de productos (Formato: codigo - producto) ->LISTO
  2.  Pagar con tarjeta credito (Se debe cobrar 10% mas y se debe descontar el stock) -> LISTO
  3.  Pagar con tarjeta debito (se debe descontar el stock)
  4.  Pagar con efectivo (Se debe cobrar 10% menos y se debe descontar el stock)
  5.  Consultar productos y stock
  6.  Agregar stock a los productos
  7.  Cambiar el precio a los productos
  
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''
import funciones as fn
base_productos = [[1,2,3],["producto1","producto2","producto3"],[300,400,500],[5,4,7]]

fn.imprimir_matriz2(base_productos)
while True:
   opcion = input(
    """Por favor, elija una opcion:
        1- Ver menú de productos
        2- Pagar con tarjeta de Credito
        3- Pagar con tarjeta de Débito
        4- Pagar con efectivo
        5- Consultar productos y stock
        6- Agregar stock a los productos
        7- Cambiar el precio a los productos
        8- Salir
      Número """)

   if opcion == "1":
      fn.imprimir_codigo_producto(base_productos)
   elif opcion == "2":
      base_productos = fn.pago_con_credito(base_productos)
   elif opcion == "3":
      base_productos = fn.pago_con_debito(base_productos)
   elif opcion == "4":
      base_productos = fn.pago_con_efectivo(base_productos)
   elif opcion == "5":
      fn.consultar_stock(base_productos)
   elif opcion == "6":
      base_productos = fn.agregar_stock(base_productos)
   elif opcion =="7":   
      base_productos = fn.modificar_precios(base_productos)
   elif opcion == "8":
      break
   else:
     print("No ingreso una opcion correcta")

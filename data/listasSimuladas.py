# rutina par simular un set de datos
# uttlizaremos listas y diccionarios

import random
from datetime import datetime, timedelta
def generar_ventas(numeroVentas):

 productos = [
    { "nombre" : "camiseta polo", "precio": 150000},
    { "nombre" : "pantalon ", "precio": 350000},
    { "nombre" : "jean ajustado", "precio": 250000},
    { "nombre" : "camisa leñadora", "precio": 200000},
    { "nombre" : "falda", "precio": 120000}
 ]

 tallas =["s","m","l","38","40","42"]

 vendedores = ["Ana","Andres","juan","miguel"]

 ventas =[]

#  fechaInicio = datetime(2025,1,1)
 fechaInicio = datetime(2024,12,1)

 for _ in range(numeroVentas):
  producto = random.choice(productos) 
  cantidad = random.randint(1,5)
  fecha = fechaInicio+timedelta(days=random.randint(0,90))
  ventas.append(
   {
    "fecha":fecha.strftime("%Y-%m-%d"),
    "producto":producto["nombre"],
    "precioUnitario": producto ["precio"],
    "talla": random.choice(tallas),
    "cantidad":cantidad,
    "vendedor":random.choice(vendedores),
    "total":producto["precio"]*cantidad
   }
  )

 return ventas

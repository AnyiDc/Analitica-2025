#Traer un registro de N ventas para analizar con pandas
#Primeros pasos con pandas

from data.listasSimuladas import generar_ventas
from notebook.graficarBarras import generarBarra
from notebook.generarReportes import crearTabla
import pandas as pd
import matplotlib.pyplot as plt

datos_simulados=generar_ventas(100)

#Organizando la fuente de datos con pandas
tablaOrdenada=pd.DataFrame(datos_simulados)

#1. Obtener la informacion general de la fuente de datos
#print(tablaOrdenada.info())

#2. Obtener la informacion estadistica basica (descriptiva) de la fuente de datos
#print(tablaOrdenada.describe())

#3. Obtener la informacion de los primeros N registros de la fuente de datos
#print(tablaOrdenada.head(20))

#4. Obtener la informacion de los ultimos N registros de la fuente de datos
#print(tablaOrdenada.tail(20))

#5. Acceder a una columna (Seleccionar) en especifico
#print(tablaOrdenada["vendedor"])

#6. TAREA como hago para acceder a varias columnas al mismo tiempo

#7. PUEDO APLICAR AGRUPACIONES (AGRUPAR DATOS NUMERICOS Y STRING)
#print(tablaOrdenada.groupby("producto")["total"].sum())
#print(tablaOrdenada.groupby("vendedor")["total"].sum())
#print(tablaOrdenada.groupby("fecha")["total"].sum().head(31))


##################################################################################
#TRANSFORMANDO DATOS CON PANDAS 
#APLICANDO FILTROS O DATA QUERIES

#PROFE
#Yo puedo obtener de los datos las ventas realizadas en enero de 2025?
queryUno=tablaOrdenada.query("fecha >= '2025-01-01' and fecha <= '2025-01-31' ")
crearTabla(queryUno,"reportes/tablaUno.html","Ventas de enero",200)

#Yo como adminsitrador del PV puedo ver la cantidad mayor o iguales 3?
queryDos=tablaOrdenada.query("cantidad >= 3")

#Yo como administrador del PV puedo ver cuales fueron las ventas del producto JEAN AJUSTADO
queryTres=tablaOrdenada.query("producto == 'jean ajustado' ")
crearTabla(queryTres,"reportes/tablaDos.html","Ventas jean ajustado",20)
#Yo puedo puedo obtener las ventas de tallas M O L
tallasFiltradas=['M','L']
queryCuatro=tablaOrdenada.query("talla.isin(@tallasFiltradas)")
#Yo como lider de bodega puedo acceder a los productos cuyo preciounitario  entre los 150k y 300k
queryCinco=tablaOrdenada.query("precioUnitario >=150000 and precioUnitario<= 300000")
#Yo puedo ver las ventas que hizo Juan Jose Gallego
querySeis=tablaOrdenada.query("vendedor == 'Juan Jose Gallego' ")

#Yo puedo obtener las ventas de los fines de semana
#Cree una columna con el numero del dia de la semana Lunes=0, Domingo=6
tablaOrdenada["fecha"]=pd.to_datetime(tablaOrdenada["fecha"])
tablaOrdenada["dia_semana"]=tablaOrdenada["fecha"].dt.day_of_week
queriSiete=tablaOrdenada.query("dia_semana == 5 and dia_semana == 6")
#Yo puedo ver ventas cuyo total sea mayor a 1Millon
queryOcho=tablaOrdenada.query("total > 1000000 ")
#Yo quiero ver todas las ventas de todos los prductos excluyendo las faldas
queryNueve=tablaOrdenada.query("producto!='Falda'")
crearTabla(queryNueve,"reportes/tablaTres.html","ventas por producto",20)
#yo puedo ver las ventas entre dos fechas especificas
queryDiez=tablaOrdenada.query("fecha >= '2025-01-01' and fecha <= '2025-01-31' ")

#les toca a ustedes
# 10. Ventas con cantidad > 3 y total > 600K
queryOnce = tablaOrdenada.query("cantidad > 3 and total > 600000")

# print(queryOnce)

# Ventas de productos que contengan la palabra "Camisa"
queryDoce = tablaOrdenada.query("producto.str.contains('Camisa', case=False)")
# print(queryDoce)

# Ventas de vendedores cuyo nombre contiene "Juan"
queryTrece = tablaOrdenada.query("vendedor.str.contains('Juan', case=False)")
# print(queryTrece)

# Ventas con precio unitario mayor al promedio general
promedio_precio = tablaOrdenada["precioUnitario"].mean()
queryCatorce = tablaOrdenada.query("precioUnitario > @promedio_precio")

# print(queryCatorce)

# Ventas con total mayor al doble del precio unitario
queryQuince = tablaOrdenada.query("total > 2 * precioUnitario")
# print(queryQuince)

# Ventas de tallas numéricas
queryDieciseis = tablaOrdenada.query("talla.str.isnumeric()")
# print(queryDieciseis)

# Ventas de Pantalón o Jean Ajustado con cantidad >= 2
queryDiecisiete = tablaOrdenada.query("(producto == 'Pantalón' or producto == 'Jean ajustado') and cantidad >= 2")
# print(queryDiecisiete)

#  Ventas >400K y talla no numérica
queryDieciocho = tablaOrdenada[(tablaOrdenada["total"] > 400000) & (~tablaOrdenada["talla"].str.isnumeric())]
# print(queryDieciocho)


# Ventas de todos menos las de Raúl
queryDiecinueve = tablaOrdenada.query("vendedor != 'Raul'")

# print(queryDiecinueve)

# Ventas ordenadas por total descendente
queryVeinte = tablaOrdenada.sort_values("total", ascending=False)
# print(queryVeinte)



#GRAFICAS A GENERAR
# total de ventas por producto
generarBarra(tablaOrdenada,"producto","total","Ventas totales por producto")
# total de ventas con cantidad >=3
filtroUno=tablaOrdenada.query("cantidad >= 3")
generarBarra(filtroUno,"producto","total","Ventas > 3 productos")
#total de ventas por vendedor
generarBarra(tablaOrdenada,"vendedor","total","Desempeño de vendedores en la tienda san diego")
 
#ESTE QUEDA DE TAREA (buscar como guardar)


#total de ventas de productos caros (>200k)
filtroCaros = tablaOrdenada.query("precioUnitario > 200000")
generarBarra(filtroCaros,"producto","total","Ventas de productos caros (>200000)")


#GRAFICAR LAS VENTAS DE ENERO
filtroEnero = tablaOrdenada.query("fecha >= '2025-01-01' and fecha <= '2025-01-31'")
generarBarra(filtroEnero,"producto","total","Ventas del mes de enero")



#GRAFICAR LAS VENTAS DE JEANS AJUSTADOS POR VENDEDOR
filtroJeans = tablaOrdenada.query("producto == 'jean ajustado'")
generarBarra(filtroJeans,"vendedor","total","Ventas de Jeans Ajustados por vendedor")



#UNIDADES VENDIDAS DE TALLA XL
filtroXL = tablaOrdenada[tablaOrdenada["talla"].isin(["42", "xl", "XL"])]
generarBarra(filtroXL,"producto","cantidad","Unidades vendidas de talla XL")
#propuesta


#Ventas de diciembre
filtroDiciembre = tablaOrdenada.query("fecha >= '2024-12-01' and fecha <= '2024-12-31'")
ventasPorVendedorDic = filtroDiciembre.groupby("vendedor")["total"].sum().reset_index()
generarBarra(
    ventasPorVendedorDic,
    "vendedor",
    "total",
    "Vendedor que más vendió en diciembre de 2024"
)


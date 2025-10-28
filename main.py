# traer un registro de n ventas pata analizar con pandas 

from data.listasSimuladas import generar_ventas
import pandas as pd


datos_simulados = generar_ventas(100)
# organizando la fuente de datos
tablaOrdenada = pd.DataFrame(datos_simulados)
print(tablaOrdenada)

# obtener informacion general de los datos
# print(tablaOrdenada.info())

# # obtener la informacion descriptiva 
# print(tablaOrdenada.describe())


# # obtener la informacion de los primeros n registros
# print(tablaOrdenada.head(20))

# # obtener la informacion de los ultimos n registros
# print(tablaOrdenada.tail(20))

# # seleccionar una columna en especifico
# print(tablaOrdenada["vendedor"])
 
 # acceder a mas de una columa, tarea

# print(tablaOrdenada["vendedor" + "producto"])
# aplicar agrupaciones
print(tablaOrdenada.groupby("producto")["total"].sum())


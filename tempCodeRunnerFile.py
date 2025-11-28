filtroCaros = tablaOrdenada.query("precioUnitario > 200000")
generarBarra(filtroCaros,"producto","total","Ventas de productos caros (>200000)")
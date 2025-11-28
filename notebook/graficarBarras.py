import matplotlib.pyplot as plt
import os
import re

def generarBarra(tablaOrdenada, columnaX, columnaY, titulo):
    # Crear carpeta "graficos" si no existe
    os.makedirs("graficos", exist_ok=True)

    colores=[
        "#8258C7",
        "#58C783",
        "#80C758",
        "#C7C758",
        "#C7585A"
    ]

    agrupacionDatos = tablaOrdenada.groupby(columnaX)[columnaY].sum()
    
    plt.figure(figsize=(10,5))
    plt.bar(agrupacionDatos.index, agrupacionDatos.values, color=colores)
    plt.title(titulo)
    plt.xlabel(columnaX)
    plt.ylabel(columnaY)

    # LIMPIAR NOMBRE DEL ARCHIVO → quitar caracteres inválidos en Windows
    nombre_archivo = titulo.lower().replace(" ", "_")
    nombre_archivo = re.sub(r'[<>:"/\\|?*]', "", nombre_archivo)  # <-- limpia
    nombre_archivo += ".png"

    ruta = os.path.join("graficos", nombre_archivo)

    plt.savefig(ruta, bbox_inches='tight')
    plt.show()
    
    print(f"✔ Gráfico guardado en: {ruta}")

import os
bootstrap = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"


def crearTabla(tablaOrdenada, archivo_html, titulo, filas_maximas):

    os.makedirs(os.path.dirname(archivo_html), exist_ok=True)

    dataFrame_vista = tablaOrdenada.head(filas_maximas)

    tabla_html = dataFrame_vista.to_html(
        classes="table table-striped table-bordered",
        index=False, justify="left"

    )

    html = f"""

        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{titulo}</title>
            <link rel="stylesheet" href="{bootstrap}">
        </head>
        <body>
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-8">
                        <h3>{titulo}</h3>
                        <div class="table-responsive">
                            {tabla_html}
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
    """

    with open(archivo_html, "w", encoding="utf-8") as archivo:
        archivo.write(html)
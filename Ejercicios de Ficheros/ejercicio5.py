import csv

def ejercicio5_diccionario_del_fichero(fichero):
    datos = {
        "Nombre": [],
        "Final": [],
        "Máximo": [],
        "Mínimo": [],
        "Volumen": [],
        "Efectivo": [],
    }

    with open(fichero, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f, delimiter=";")
        for fila in lector:
            datos["Nombre"].append(fila["Nombre"])
            for columna in ["Final", "Máximo", "Mínimo", "Volumen", "Efectivo"]:
                
                valor_str = (
                    fila[columna].replace(".", "").replace(",", ".")
                )
                datos[columna].append(float(valor_str))

    return datos

def ejercicio5_fichero_en_formato_csv(diccionario_datos, fichero_salida="fichero_resumido.csv"):
    columnas_numericas = ["Final", "Máximo", "Mínimo", "Volumen", "Efectivo"]

    with open(fichero_salida, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f, delimiter=";")

        escritor.writerow(["Columna", "Mínimo", "Máximo", "Media"])

        for col in columnas_numericas:
            valores = diccionario_datos[col]
            minimo = min(valores)
            maximo = max(valores)
            media = sum(valores) / len(valores)

            escritor.writerow(
                [col, f"{minimo:.2f}", f"{maximo:.2f}", f"{media:.2f}"]
            )

    print(f"Fichero creado en: {fichero_salida}")

# Ejemplos:
# datos = ejercicio5_diccionario_del_fichero(fichero='cotización.csv')
# ejercicio5_fichero_en_formato_csv(diccionario_datos=datos)
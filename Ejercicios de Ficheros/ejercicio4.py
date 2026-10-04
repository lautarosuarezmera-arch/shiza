from urllib.request import urlopen


def ejercicio4(url):
    try:
        with urlopen(url) as respuesta:
            contenido = respuesta.read().decode("utf-8")
            palabras = contenido.split()
            print(
                f"El fichero en la URL tiene la cantidad de: {len(palabras)} palabras."
            )
    except Exception as e:
        print(f"Error al acceder a la URL: {e}")

#ejemplo de url:
ejercicio4("https://www.gutenberg.org/cache/epub/174/pg174.txt")
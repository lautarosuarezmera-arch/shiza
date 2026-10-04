def ejercicio2():
    n = int(input("Introduce un número entero entre 1 y 10: "))
    if 1 <= n <= 10:
        nombre_fichero = f"tabla-{n}.txt"
        try:
            with open(nombre_fichero, "r") as f:
                print(f.read())
        except FileNotFoundError:
            print(f"El fichero {nombre_fichero} no existe.")
    else:
        print("El número debe estar entre 1 y 10.")

ejercicio2()
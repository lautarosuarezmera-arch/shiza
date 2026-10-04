def ejercicio1():
    n = int(input("Introduce un número entero entre 1 y 10: "))
    if 1 <= n <= 10:
        nombre_fichero = f"tabla-de-{n}.txt"
        with open(nombre_fichero, "w") as f:
            for i in range(1, 11):
                f.write(f"{n} x {i} = {n * i}\n")
        print(f"Tabla de {n} guardada en {nombre_fichero}")
    else:
        print("El número debe estar entre 1 y 10.")
        
ejercicio1()
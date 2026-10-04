def ejercicio3():
    n = int(input("Introduce el valor de n entre 1 y 10: "))
    m = int(input("Introduce el valor de m entre 1 y 10: "))

    if 1 <= n <= 10 and 1 <= m <= 10:
        nombre_fichero = f"tabla-{n}.txt"
        try:
            with open(nombre_fichero, "r") as f:
                lineas = f.readlines()
                
                print(lineas[m - 1].strip())
        except FileNotFoundError:
            print(f"El fichero {nombre_fichero} no existe.")
    else:
        print("Ambos números deben estar entre 1 y 10.")
        
ejercicio3()
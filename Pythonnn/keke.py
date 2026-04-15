def eje1():
    n1 = int(input("Ingresar un número"))
    n2 = int(input("Ingresar otro número"))
    resultado=n1+n2
    print("El resultado es: ", resultado)
#eje1()

def eje2():
    n1 = int(input("Ingresar un número"))
    n2 = int(input("Ingresar un segundo número"))
    n3 = int(input("Ingresar un tercer número"))
    n4 = int(input("Ingresar un cuarto número"))
    resultado=n1+n2+n3+n4
    print("El resultado es: ", resultado)
#eje2()

def eje3():
    lado1 = int(input("Ingresar un lado"))
    lado2 = int(input("Ingresar otro lado"))

    if(lado1==lado2):
        print("Eso no es un rectángulo...")

    else:
        superficie=lado1*lado2

        print("La superficie del rectángulo es: ", superficie)

#eje3()

def eje4():
    lado1 = float(input("Ingresar un lado con decimales"))
    superficie = lado1*lado1

    print("la superficie es ", superficie)

#eje4

def eje5():
    horas = float(input("Ingresar unas horas"))
    minutos = float(input("Ingresar unos minutos"))
    segundos = int(input("Ingresar unos segundos"))

    h = horas*3600
    m = minutos*60

    resultadoEnSegundos = h+m+segundos

    print("el resultado expresado en segundos es: ", resultadoEnSegundos)

#eje5()

def eje6():
    altura=float(input("Ingresar unas horas"))
    base=float(input("Ingresar unas horas"))

    superficie= (altura*base) /2
    print("la superficie es ", superficie)

#eje6()

def eje7():
    arr=[]
    for i in range(6):
        arr.append(int(input("Ingresar un número ")))

    promedio=sum(arr)/6
    print("el promedio es ", promedio)

#eje7()

def eje8():
    n1 = int(input("Ingresar un número"))
    n2 = float(input("Ingresar otro número"))
    porcentaje=float(n1/n2)*100
    print("el porcentaje es ", porcentaje)

#eje8()

def eje9():
    fecha = int(input("Ingrese alguna fecha en formato numérico"))



#eje9()


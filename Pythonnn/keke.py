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
    n1 = int(input("Ingresar fecha en formato númerico (DDMMAAAA): "))
    m = n1 % 1000000
    meses = int(m//10000)  
    dias = int(n1//1000000)
    años = n1 % 10000
    print("La fecha es : ", "Dia : ", dias, "Mes :", meses ,"Año : ", años)
    print(dias,meses,años)
#eje9()

def eje10():
    EP = int(input("Ingrese su nota de Exámenes Parciales"))
    TP = int(input("Ingrese su nota de Trabajos Prácticos"))
    EI = int(input("Ingrese su nota del Exámen Integrador"))

    REP = EP*0.3
    RTP = TP*0.2
    REI = EI*0.5
    NotaFinal = REP+RTP+REI

    if(NotaFinal>10):
        print("El resultado es incorrecto, ingrese las notas exactas")

    else:
        print("Su Nota Final es: ", NotaFinal)
    
#eje10()

def eje11():
    AutosVendidos = int(input("Ingrese la cantidad de autos vendidos"))
    i=0
    Precios=[]
    while i < AutosVendidos:
        Precios.append(float(input(f"Ingrese el precio del auto n°{i + 1}: ")))
        Adicional = Precios[i] * 0.05
        print("megustanlosquesosapestosos")
    Comision=(AutosVendidos * 200)

    SalarioTotal = 5500 + Comision + Adicional
    print("Su salario total es de: ", SalarioTotal)

eje11()

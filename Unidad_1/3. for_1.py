def ejercicio1():
    num = int(input("ingrese un numero: "))
    suma = 0
    resta = 0
    mult = 1
    for i in range(1,num+1):
        print(i)
        suma = suma + i
        resta = resta - i
        mult = mult * i
    
    print("la suma de los numeros es: " + str(suma))
    print("la resta de los numeros es: " + str(resta))
    print("la multiplicacion de los numeroes es: " + str(mult))

def ejercicio2():
    i = 0
    j = 0
    for x in range(1, 11):

        x = int(input("ingrese un numero "))

        if x > 0:
            i+=1
        else:
            j+=1
    
    print(str(i) + "numeros son  mayores a 0")
    print(str(j) + "numeros son menores a 0")
    
def ejercicio3():
    i = 0
    j = 0

    can = int(input("ingrese la cantidad de pesos: "))

    for x in range(can):
        peso = float(input("ingrese el peso de la persona: "))

        if peso > 80:
            i += 1
        else:
            j += 1
    
    print("la cantidad de personas que pesan mas de 80 es:", i)
    print("la cantidad de personas que pesan menos de 80 es", j)

def ejercicio4():

    x = int(input("ingrese el primer numero: "))
    y = int(input("ingrese el segundo numero: "))
    z = int(input("ingrese el tercer numero: "))

    for i in range(x+1, y):
        if i == z:
            print("el tercer numero pertenece al intervalo")
            i = y
    if i != y:
        print("el tercer numero no pertenece al intervalo")

def ejercicio5():
    x = int(input("ingrese el primer numero: "))
    y = int(input("ingrese el segundo numero: "))

    total = 0
    par = 0
    impar = 0

    for i in range(x+1, y):
        if i % 2 == 0:
            par += 1
        else:
            impar += 1
        total += 1
    
    print("hay un total de " + str(total) + " numeros")
    print(par, "son pares")
    print(impar, "son impares")

def ejercicio6():
    prom = 0
    dm = 0
    dn = 0
    for i in range(1, 32):
        x = float(input("ingrese la cantidad de agua en milimetros: "))
        if i == 1:
            mayor = x
            menor = x

        if x > mayor:
            mayor = x
            dm = i
        if x < menor:
            menor = x
            dn = i
        
        prom = prom + x

    print("el dia de mayor lluvia fue:", dm)
    print("el dia de menor lluvia fue:", dn)
    print("el promedio de lluva en milimetros es", prom/31)

ejercicio1()
ejercicio2()
ejercicio3()
ejercicio4()
ejercicio5()
ejercicio6()
    

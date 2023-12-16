def ejercicio1():
    total = 0
    mensaje = " "
    print("""
    Ingrese el platillo:
    1. Lomo Saltado  S/10.00
    2. Ceviche       S/13.00
    3. Estofado      S/ 9.00
    4. Salir
""")
    op = int(input())

    if op == 1: 
        total += 10
        mensaje = "lomo saltado con "
    elif op == 2:
        total += 13
        mensaje = "ceviche con "
    elif op == 3:
        total += 9
        mensaje = "estofado con "
    else:
        return
    
    cant = int(input("ingrese la cantidad"))

    total *= cant

    print("""
    Ingrese la bebida:
    1. Agua
    2. Jugo       
    3. Gaseosa      
""")
    beb = int(input())

    if beb == 1:
        mensaje += "agua"
    elif beb == 2:
        mensaje += "jugo"
    elif beb == 3:
        mensaje += "gaseosa"
    else:
        mensaje += "agua"
    
    print("usted a pedido " + str(cant) + " platos de " + mensaje)
    print("el precio total mas igv es: ",total + total*0.1)


def ejercicio2():
    nac= input("ingrese su fecha de nacimiento: ")
    fec = input("ingrese la fecha actual: ")

    nac = nac.split('/')
    fec = fec.split('/')
    
    year = int(fec[2]) - int(nac[2])
    mont = (year*12) + (int(fec[1]) - int(nac[1]) )
    days = (mont*30) +  (int(fec[0]) - int(nac[0]))

    if fec[1] < nac[1]:
        print("años:", year - 1)
    else:
        print("años:", year)
    
    print("meses:", mont)
    print("dias:", days)
    
    if int(nac[1]) == 4:
        if int(nac[0]) >= 20:
            print("Tauro")
        else:
            print("Aries")
    elif int(nac[1]) == 5:
        if int(nac[0]) > 21:
            print("Geminis")
        else:
            print("Tauro")
    elif int(nac[1]) == 6:
        if int(nac[0]) >= 21:
            print("Cancer")
        else:
            print("Geminis")
    elif int(nac[1]) == 7:
        if int(nac[0]) >= 23:
            print("Leo")
        else:
            print("Cancer")
    elif int(nac[1]) == 8:
        if int(nac[0]) >= 23:
            print("Virgo")
        else:
            print("Leo")
    elif int(nac[1]) == 9:
        if int(nac[0]) >= 23:
            print("Libra")
        else:
            print("Virgo")
    elif int(nac[1]) == 10:
        if int(nac[0]) >= 23:
            print("Escorpio")
        else:
            print("Libra")
    elif int(nac[1]) == 11:
        if int(nac[0]) >= 22:
            print("Sagitario")
        else:
            print("Escorpio")
    elif int(nac[1]) == 12:
        if int(nac[0]) >= 22:
            print("Capricornio")
        else:
            print("Sagitario")
    elif int(nac[1]) == 1:
        if int(nac[0]) >= 20:
            print("Acuario")
        else:
            print("Capricornio")
    elif int(nac[1]) == 2: 
        if int(nac[0]) >= 19:
            print("Piscis")
        else:
            print("Acuario")
    else:
        if int(nac[0]) >= 21:
            print("Aries")
        else:
            print("Piscis")

def ejercicio3():
    num = 11
    sum = 0
    lista = []

    while num >= 10:
        num = int(input("ingrese un numero: "))
        lista.append(num)
    
    print("ingreso el numero ",num)

    for x in lista:
        sum = sum + x

    print("la suma de los numeros es ",sum - num)

def ejercicio4():
    sum = 0
    
    while sum < 100:
        num = int(input("ingrese un numero: "))       
        sum += num
    
    print("la suma total es " + str(sum))



ejercicio2()


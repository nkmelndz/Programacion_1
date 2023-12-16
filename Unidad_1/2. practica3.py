def ejercicio1():
    km= float(input("Ingrese la cantidad de kilometrosrecorridos: "))
    if km <= 300:
        print("el monto a pagar es 300")
    elif km <= 1000:
        x = 300 + (50 * (km-300))
        print("el monto a pagar es: " + str(x))
    else:
        x = 300 + (50 * 700) + (100 * (km - 1000))
        print("el monto a pagar es: " + str(x))

def ejercicio2():
    
    gasto = float(input("Ingrese la cantidad que a gastado: "))

    if gasto <= 100:    
        print("pago con dinero en efectivo un monto de", gasto)
    elif gasto <= 300:
        print("pago con tarjeta de debito un monto de", gasto - (gasto * 0.1))
    else:
        print("pago con tarjeta de credito un monte de", gasto - (gasto * 0.1))

def ejercicio3():
    
    can1 = int(input("ingrese la primera cantidad: "))
    can2 = int(input("ingrese la segunda cantidad: "))
    can3 = int(input("ingrese la tercera cantidad: "))

    if can1 < can2 and can1 < can3:
        print("el menor numero es: ", can1)
    elif can2 < can1 and can2 < can3:
        print("el menor numero es: ", can2)
    elif can3 < can1 and can3 < can2:
        print("el menor numero es ", can3)
    else:
        print("todos los numeros son iguales")

def ejercicio4():

    niños = int(input("Ingrese la cantidad de niños: "))
    niñas = int(input("Ingrese la cantidad de niñas: "))

    total = niñas + niños

    por1 = (niños/total)*100
    por2 = (niñas/total)*100

    print("el porcentaje de niños es:", por1)
    print("el porcentaje de niñas es:", por2)
    
def ejercicio5():
    
    nombre = input("Ingres el nombre del alumno: ")
    p1 = int(input("Ingrese la nota de la parte practica: "))
    p2 = int(input("Ingrese la nota de la parte de problemas: "))
    p3 = int(input("Ingrese la nota de la parte de teorica: "))

    total = (p1 * 0.1) + (p2 * 0.5) + ( p3 * 0.4)

    if total <= 10:
        print(nombre + " esta desaprobado")
    elif total <= 16:
        print(nombre + " esta aprobado")
    else: 
        print(nombre + "es destacado")

def ejercicio6():
    juan = int(input("Ingresa la edad de Juan: "))
    mario = int(input("Ingresa la edad de Mario: "))
    pedro = int(input("Ingresa la edad de Pedro: "))

    if juan == mario: 
        print("Juan y Mario son contemporaneos")
    elif mario == pedro:
        print("Mario y Pedro son contemporaneos")
    elif juan == pedro:
        print("Juan y Pedro son contemporaneos")
    elif juan == pedro and pedro == mario: 
        print("Los tres son contemporaneos")
    else:
        print("Ninguno es contemporaneo")


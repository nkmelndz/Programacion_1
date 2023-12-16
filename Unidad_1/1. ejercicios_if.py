
from operator import truediv
from re import T
from ssl import cert_time_to_seconds


def ejercicio1():
    a = int(input("Ingresa un numero entero: "))
    if a > 0 and a % 2 == 0 :
        print("El numero es positivo y par")
    elif a > 0 and a % 2 != 0:
        print("El numero es positivo e impar")
    elif a < 0 and a % 2 == 0 :
        print("El numero es negativo y par")
    elif a < 0 and a % 2 != 0:
        print("El numero es negativo e impar")
    else:
        print("El numero es cero")

def ejercicio2():
    sueldo = float(input("Ingrese el sueldo de un empleado: "))

    if sueldo > 600:
        sueldo = sueldo + sueldo * 0.1
        print("Su nuevo sueldo sera "  + str(sueldo))
    else:
        print("Su sueldo es mayor a 600 por lo tanto no recibira aumento")
    
def ejercicio3():
    horas = int(input("ingrese la cantidad de horas trabajadas: "))
    pago = float(input("ingres el pago que recibe por hora trabajada: "))

    if horas > 48:
        total = ((pago * 2)* 8) + ((pago*3)*(horas-48))
        print("el pago total por las horas extras trabajadas sera: " + str(total))
    elif horas > 40:
        total = ((pago*2)*(horas-40))
        print("el pago total por las horas extras trabajadas sera: " + str(total))
    else:
        print("no excede las 40 horas")

def ejercicio4():
    año = int(input("ingrese el año: "))

    if año % 4 == 0:
        print("el año es bisiesto")
    else:
        print("el año no es bisiesto")

def ejercicio5():

    saldo = float(input("ingrese la cantidad a depositar: "))
    retirar = float(input("ingrese la cantidad a retirar: "))

    if retirar > saldo:
        print("la cantidad de dinero que desea retirar excede su saldo")
    elif retirar <= saldo:
        restante = saldo - retirar
        print("la cantidad de dinero que queda en su cuenta es", restante)

def ejercicio6():
    
    x = 0

    res1 = input("¿Tiene usted dolor de garganta?(s/n) ")

    if res1 == 's':
        x+=1
    
    res2 = input("¿Tiene usted tos persistente?(s/n) ")

    if res2 == 's':
        x+=2
    
    res3 = input("¿Tiene usted fiebre?(s/n) ")
    
    if res3 == 's':
        x+=3
    
    res4 = input("¿Tiene usted dolor de pecho?(s/n) ")

    if res4 == 's':
        x+=4
    
    res5 = input("Tiene usted dificultad al respirar?(s/n) ")

    if res5 == 's':
        x+=5

    if x == 0:
        print("Usted no tiene covid-19")
    elif x < 4:
        print("Usted debe entrar a observacion")
    elif x < 9:
        print("Usted debe entrar a hospitalizacion")
    else:
        print("Usted debe entrar a UCI")

def ejercicio7():


    a = input("¿Aprobo el examen medico?(s/n): ")
    b = float(input("Puntaje del examen de reglas de transito: "))
    c = float(input("Puntaje del examen de manejo: "))

    if a == 's':
        x = True
    else:
        x = False
    
    if b >= 70:
        y = True
    else:
        y = False

    if c >= 85:
        z = True
    else:
        z = False
    
    if x == True and z == True and y == False:
        print("Tienes una segunda oportunidad de dar el examen fallido")
    elif x == True and y == False and z == False:
        print("Tienes una penalidad de 6 meses para volver a dar el examen")
    elif x == False and y == True and z == True:
        print("Obtienes una licencia temporal por 1 año")
    elif x == True and y == True and z == False:
        print("No obtienes la licencia")
    elif x == True and y == True and z == True:
        print("Obtienes la licencia por 10 años")

def ejercicio8():

    ciclo = int(input("Ingrese el ciclo en el que se encuentra: "))
    creditos = int(input("Ingrese la cantidad de creditos: "))

    if ciclo >= 6:
        x = 35
    elif ciclo >= 2:
        x = 36
    else:
        x = 40
    
    if creditos < 12:
        y = 12 * x
        print("La cantidad que debe pagar es:", y)
    elif creditos < 18:
        y = 18 * x
        print("La cantidad que debe pagar es:", y)
    else:
        y = creditos * x
        print("La cantidad que debe pagar es:", y)

ejercicio1()
ejercicio2()
ejercicio3()
ejercicio4()
ejercicio5()
ejercicio6()
ejercicio7()
ejercicio8()
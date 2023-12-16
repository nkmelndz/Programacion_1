def ejercicio1():
    sum = 0
    n = int(input("ingrese un numero: "))
    
    while n != 0:
        sum += n
        n = int(input("ingrese un numero: "))
    
    print("la suma de los numeros es " + str(sum))
    
def ejercicio2():
    a = 0; b = 0;c = 0; d = 0; e = 0
    ans = input("desea realizar la votacion?(s/n)\n")
    while ans == 's':
        edad = int(input("ingrese su edad: "))
        if edad < 18:
            print("usted es menor de edad por lo tanto no puede votar")
            ans = input("desea realizar la votacion?(s/n)\n")
            break
        vot = input("""
Elija una opcion:
a. candidato 1
b. candidato 2
c. candidato 3
d. blanco
""")
        if vot == 'a':
            a += 1
        elif vot == 'b':
            b += 1
        elif vot == 'c':
            c += 1
        elif vot == 'd':
            d += 1
        else:
            e += 1
        ans = input("desea realizar la votacion?(s/n)\n")
    
    print("candidato1: ", a)
    print("candidato2: ", b)
    print("candidato3: ", c)
    print("votos en blanco: ", d)
    print("votos nulos: ", e)
        
def ejercicio3():
    
    i = 3
    a = "nkmelndz"
    b = "123"
    
    while i > 0:
        
        usuario = input("ingrese el usuario: ")
        contraseña = input("ingrese contraseña: ")
        
        if usuario != a and contraseña != b:
            i -= 1
            print("contraseña incorrecta") 
            print("le quedan " + str(i) + " intentos")
             
        else:
            print("contraseña correcta") 
            break
    
        
def ejercicio4():
    
    ans = "si"
    can = 0
    promt = 0
    
    while ans == "si":
        nom = input("ingrese el nombre: ")
        cal1 = float(input("calificacion 1: "))
        cal2 = float(input("calificacion 2: "))
        cal3 = float(input("calificacion 3: "))
        prom = ((cal1 + cal2 +cal3)/3)
        print("el promedio es: ", prom)
        promt += prom
        can += 1
        ans = input("desea ingresar otro? ")
        
    print("se ingresaron ", can, " estudiantes")
    print("el promedio total es: ", promt/can)

def ejercicio5():
    
    din = 0
    ans = ''
    op = ''
    
    while ans != "no" or op == 'c':
        
        op = input("""
    a. Retirar
    b. Depositar
    c. Salir
    Ingrese una opcion: 
""")
        if op == 'a':
            mon = int(input("ingrese el monto: "))
            if mon > din: 
                print("el monto ingresado supera la cantidad de dinero disponible")
                print("saldo disponible: ", din)
            else:
                din =  din - mon
                print("saldo disponible ", din)
        elif op == 'b':
            mon = int(input("ingrese el monto: "))
            din = din + mon
            print("saldo disponible: ", din)
        else:
            break
        ans = input("desea realizar otra transaccion? ").lower
    
ejercicio5()

    
        
    
            
        
            
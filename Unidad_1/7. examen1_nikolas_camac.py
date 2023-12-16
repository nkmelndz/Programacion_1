    
def ejercicio4():
    
    suma = 0
    can = 0
    
    es = int(input("ingrese la edad del estudiante (si marca 0 se detine el programa)"))
    
    mayor = es
    menor = es
    
    while es != 0:
        can += 1
        suma += es
        
        if es < menor:
            menor = es 
        if es > mayor:
            mayor = es
        
        if es < 14:
            print("se encuentra en la niñez")
        elif es < 18:
            print("se encuentra en la adolescencia")
        elif es < 36:
            print("se encuentra en adultos jovenes")
        elif es < 65:
            print("se encuentra en adultos")
        else:
            print("se encuentra en la tercera edad")
        
        es = int(input("ingrese la edad del estudiante (si marca 0 se detine el programa)"))
    
    print("el promedio de alumnos es: ", suma/can )
    print("el mayor estudiante tiene ", mayor)
    print("el menor estudiante tiene: ", menor)
    

def ejercicio2():
    for i in range(2, 12, 2):
        print(i, "-", i*i*i)
    
    n = int(input("que tabla de multiplicar desea? "))
    
    for i in range(13):
        print(n,"x",i,"=", n * i)
        
    
def ejercicio1():

    ans = 's'
    
    while ans == 's':
        nombre = input("ingrese el nombre del docente: ")
        apellido = input("ingrese el apellido del docente: ")
        
        codigo = nombre[0] + nombre[1] + apellido[0] + apellido[1]
            
        cursos = int(input("ingrese la cantidad de cursos: "))
        horas = int(input("ingrese la cantidad de horas por cursos: "))
        
        bruto = (horas * cursos) * 18.50 
        
        if bruto > 850:
            afp = bruto * 0.13
            sueldo = bruto - afp
            
            salud = sueldo * 0.09
            sueldo = sueldo - salud
            
            print("nombre: " + nombre)
            print("apellido: " + apellido)
            print("codigo: " + codigo)
            print("cantidad cursos:", cursos)
            print("cantidad de horas mensuales: ", cursos * horas)
            print("sueldo bruto: ", bruto)
            print("descuento afp: ", afp)
            print("descuento essalud: ", salud)
            print("sueldo neto: ", sueldo)
        else:
            salud = bruto * 0.09
            sueldo = bruto - salud
            
            print("nombre: " + nombre)
            print("apellido: " + apellido)
            print("codigo: " + codigo)
            print("cantidad cursos:", cursos)
            print("cantidad de horas mensuales: ", cursos * horas)
            print("sueldo bruto: ", bruto)
            print("descuento essalud: ", salud)
            print("sueldo neto: ", sueldo)
            
        ans = input("desea continuar?(s/n) ")
        print("")

        
def ejercicio3():
    op = 'a'
    total = 0
    while op != 'c':
        op = input("""
Ingrese una opcion:
a. consultar transaccion 
b. registrar transaccion
c. salir
""")
        if op == 'a':
            mon = int(input("ingrese el monto: "))
            dolar = mon * 3.45
            euro = mon * 3.83
            print ("dolares: ", dolar)
            print ("euros: ", euro)  
            
        
        elif op == 'b':
            mon = int(input("ingrese el monto: "))
            dolar = mon * 3.45
            euro = mon * 3.83
            
            total += mon
            
            print ("transaccion exitosa") 
            print ("dolares: ", dolar)
            print ("euros: ", euro)  
            
    
    print("monto total en transacciones: ", total)
    
ejercicio3()
        
        
    
    

    

        
        
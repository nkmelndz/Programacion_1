def ejercicio7():

    for i in range(5):
        x = int(input(str(i)+ ": "))
        if i == 0:
            m = x
            n = x
        else:
            if x > m:
                m = x
            if x < n:
                n = x
    
    print("el mayor numero es:", m)
    print("el menor nu mero es:", n)

def ejercicio8():
    sum = 0
    mult = 1
    print("imprima 10 numeros")
    for i in range(1, 11):
        x = int(input(str(i) + ": "))
        if i <= 5:
            sum = sum + x
        else:
            mult = mult * x
        
    print("La suma de los 5 primeros es:", sum)
    print("la multiplicacion de los 5 ultimos es:", mult)

def ejercicio9():
    eq = 0
    iso = 0
    es = 0
    for i in range(5):
        x = int(input("primer lado: "))
        y = int(input("segundo lado: "))
        z = int(input("tercer lado: "))

        if x == y and y == z:
            print("el triangulo es equilatero")
            eq += 1
        elif x == y or y == z or x == z:
            print("el triangulo es isosceles")
            iso += 1
        else:
            print("el triangulo es escaleno")
            es += 1
    print("equilatero:", eq)
    print("isosceles: ", iso)
    print("escaleno:", es)
        
        
def ejercicio10():
    sum = 0
    x = input("ingrese un numero: ")
    for i in x:
        sum = sum + int(i) 

    print("la suma es", sum)




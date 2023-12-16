
def ejercicio1():
    class Personaje():
        def __init__(self,  nombre, fuerza, inteligencia, defensa, vida):
            self.nombre = nombre
            self.fuerza = fuerza
            self.inteligencia = inteligencia
            self.defensa = defensa
            self.vida = vida
            self.nivel = 0
        
        def subir_nivel(self):
            self.nivel += 1
        
        def verificar_vida(self):
            print("Vida: ",self.vida)

            if self.vida > 0:
                print("ESTA VIVO")
            else:
                print("ESTA MUERTO")
        
        def morir(self):
            self.vida = 0

    personaje1 = Personaje("Anderson", 20, 30, 40, 100)

    personaje1.subir_nivel()

    print("Nivel: ",personaje1.nivel)

    personaje1.verificar_vida()

    personaje1.morir()

    personaje1.verificar_vida()

def ejercicio2():
    class Cuenta():
        def __init__(self, titular):
            self.titular = titular
            self.__dinero = 0
            self.__movimiento = 0

        def depositar(self):
            monto = float(input("Ingrese el monto a depositar: "))
            self.__movimiento = self.__dinero + monto
            self.__movimiento = self.__movimiento - self.__dinero
            self.__dinero += monto
        
        def retirar(self):
            monto = float(input("Ingrese el monto a retirar: "))
            self.__movimiento = self.__dinero - monto
            self.__movimiento = self.__movimiento - self.__dinero
            self.__dinero -= monto
            

        def imprimir_movimiento(self):
            print("Movimiento: ",self.__movimiento)
            print("Dinero: ",self.__dinero)
    
    cuenta1 = Cuenta("nikolas")

    print("Cuenta de " + cuenta1.titular)
    cuenta1.depositar()
    cuenta1.imprimir_movimiento()
    cuenta1.retirar()
    cuenta1.imprimir_movimiento()

        

def ejercicio3():
    class Vehiculo():
        def __init__(self, marca, modelo):
            self.marca = marca
            self.modelo = modelo
    
    class Coche(Vehiculo):
        def __init__(self, marca, modelo, puertas):
            super().__init__(marca, modelo)
            self.puertas = puertas
        
    coche1 = Coche("Toyota", "Yaris", 4)

    print("Marca: " + coche1.marca)
    print("Modelo: " + coche1.modelo)
    print("Puertas: " + str(coche1.puertas))

ejercicio2()
from ClaseConjunto import Conjunto

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3
                            }

    def opcion(self,op,Manejador):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=='3':
            func(Manejador)
        else:
            func()

    def opcion1(self,Manejador):
        x=int(input('Elija el primer Conjunto (1 al 5): '))
        y=int(input('Elija el segundo Conjunto (1 al 5): '))
        C3=Manejador[x-1]+Manejador[y-1]
        print(f'El resultado de la suma entre los conjuntos {Manejador[x-1]} + {Manejador[y-1]} es: {C3}')
        pass

    def opcion2(self,Manejador):
        x=int(input('Elija el primer Conjunto (1 al 5): '))
        y=int(input('Elija el segundo Conjunto (1 al 5): '))
        C3=Manejador[x-1]-Manejador[y-1]
        print(f'El resultado de la diferencia entre los conjuntos {Manejador[x-1]} - {Manejador[y-1]} es: {C3}')
        pass

    def opcion3(self,Manejador):
        x=int(input('Elija el primer Conjunto (1 al 5): '))
        y=int(input('Elija el segundo Conjunto (1 al 5): '))
        resultado=Manejador[x-1]==Manejador[y-1]
        print(f'¿Los conjuntos C1= {Manejador[x-1]} y C2= {Manejador[y-1]} son iguales?: {resultado}')
        pass
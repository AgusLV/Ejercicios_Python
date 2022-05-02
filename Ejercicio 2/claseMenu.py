from claseViajero import ViajeroFrecuente

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            }

    def opcion(self,op,Viajero):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=='3':
            func(Viajero)
        else:
            func()

    def opcion1(self,Viajero):
        cant= Viajero.cantidadTotalMillas()
        print(f'Cantidad de millas: {cant}')

    def opcion2(self,Viajero):
        cant=int(input('Ingrese las Millas Recorridas: '))
        print(f'Millas Acumuladas: {Viajero.acumularMillas(cant)}')

    def opcion3(self,Viajero):
        cant=(int(input('Ingrese la cantidad de millas a canjear: ')))
        print(f'Millas restantes: {Viajero.canjearMillas(cant)}')
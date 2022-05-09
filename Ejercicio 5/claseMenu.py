from clasePlanAhorro import PlanAhorro

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4
                            }

    def opcion(self,op,manejador):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=='3' or op=='4':
            func(manejador)
        else:
            func()

    def opcion1 (self,manejador):
        manejador.actualizarListaValores()

    def opcion2 (self,manejador):
        valor=float(input('Ingrese un valor: '))
        manejador.mostrarInferior(valor)

    def opcion3 (self,manejador):
        manejador.mostrarMonto()

    def opcion4 (self,manejador):
        manejador.modificaCantCuotas()
from claseManejadorLista import ManejadorPlanes

from clasePlanAhorro import PlanAhorro

from claseMenu import Menu

def test():
    objetoPrueba=PlanAhorro(130, 'Corolla', 'Cross XEI CVT',4177000)
    print(objetoPrueba)


if __name__=='__main__':
    test()
    mp=ManejadorPlanes()
    mp.testLista()
    menu= Menu()
    print('MENU DE OPCIONES')
    print('1 - Actualizar el valor de vehículo para cada plan.')
    print('2 - Ingresar valor y mostrar info de las cuotas inferiores.')
    print('3 - Mostrar monto para licitar el vehículo.')
    print('4 - Modificar cantidad de cuotas a licitar.')
    print('5 - Salir.')
    opcion = (input('Opcion: '))
    while opcion!='5':
        menu.opcion(opcion,mp)
        opcion = (input('Opcion (Ingrese 5 para salir): '))
    print("Usted salió del programa")
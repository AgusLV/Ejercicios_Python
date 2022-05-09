from ClaseConjunto import Conjunto

from claseMenu import Menu

def test():
    objPrueba= Conjunto([1,2,3,4,5,6])
    print(objPrueba)

if __name__ == '__main__':
    test()
    A=Conjunto([2,9,3,5,4])
    B=Conjunto([7,12,4,9,6])
    C=Conjunto([1,21,3,17])
    D=Conjunto([3,21,14,6])
    E=Conjunto([3,21,14,6])
    Manejador=[A,B,C,D,E]
    menu= Menu()
    print('MENU DE OPCIONES')
    print('1 - Union de dos Conjuntos.')
    print('2 - Diferencia de dos Conjuntos.')
    print('3 - Verificar si dos Conjuntos son iguales.')
    print('4 - Salir.')
    opcion = (input('Opcion: '))
    while opcion!='4':
        menu.opcion(opcion,Manejador)
        opcion = (input('Opcion (Ingrese 4 para salir): '))
    print("Usted salió del programa")
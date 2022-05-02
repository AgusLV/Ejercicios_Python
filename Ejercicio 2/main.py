import csv

from claseMenu import Menu

from claseViajero import ViajeroFrecuente

#Funcion test para verificar la creacion de objetos
def test():
    objPrueba=ViajeroFrecuente(741,44127766,'Agustín','Astudillo',400)
    print(f"----PRUEBA----\n{objPrueba}")

def BuscarNumero(num,list):
    indice=0
    bandera=False
    while indice < len(lista) and bandera==False:
        if list[indice].getNumero() == num:
            bandera=True
        else:
            indice+=1
    return (bandera,indice)

if __name__=="__main__":
    test()
    lista=[]
    archivo=open("Viajeros.csv")
    reader= csv.reader(archivo, delimiter=',')
    for line in reader:
        obj=ViajeroFrecuente(int(line[0]),line[1],line[2],line[3],int(line[4]))
        lista.append(obj)
    numero=int(input("Ingrese un numero de Viajero Frecuente: "))
    Datos=BuscarNumero(numero,lista)
    if Datos[0]==True:
        menu=Menu()
        print('Elija una opcion:')
        print('1 - Consultar cantida de millas.')
        print('2 - Acumular millas.')
        print('3 - Canjear millas')
        print('4 - Salir del programa')
        opcion=(input("Opcion: "))
        while opcion!='4':
            menu.opcion(opcion,lista[Datos[1]])
            opcion = (input('Opcion: '))
        print("Usted salió del programa")
    else: 
        print(f"El numero de viajero {numero} no se ha encontrado")
    archivo.close()

''' LOTE DE PRUEBAS
328
1
2
130
3
500
'''

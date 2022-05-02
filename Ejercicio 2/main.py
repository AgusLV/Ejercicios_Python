import csv
from claseViajero import ViajeroFrecuente

def test():
    objPrueba=ViajeroFrecuente(741,44127766,'Agustín','Astudillo',400)
    print("----PRUEBA----\n{}".format(objPrueba.mostrar()))

if __name__=="__main__":
    test()
    lista=[]
    
    '''APERTURA DEL ARCHIVO PENDIENTE
    archivo=open("Viajeros.csv")
    reader= csv.reader(archivo, delimiter=",")
    for line in archivo:
        line=
    '''

    numero=int(input("Ingrese un numero de Viajero Frecuente: "))
    opcion=None
    indice=0
    while indice!= len(lista) and lista[indice].get:
        if(lista[indice])

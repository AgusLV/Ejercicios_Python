import csv

from claseViajero import ViajeroFrecuente

if __name__=="__main__":
    #Crea una lista de viajeros con los datos del archivo Viajeros.csv
    lista=[]
    archivo=open("Viajeros.csv")
    reader= csv.reader(archivo, delimiter=',')
    for line in reader:
        obj=ViajeroFrecuente(int(line[0]),line[1],line[2],line[3],int(line[4]))
        lista.append(obj)
    archivo.close()

#Compara la cantidad de millas acumuladas entre los viajeros a y b
    print('\n-----COMPARAR-----')
    a= lista[0]
    igual= a==500
    print(f'{a.cantidadTotalMillas()} es igual a 500: {igual}')
    igual= 100==a
    print(f'100 es igual a {a.cantidadTotalMillas()}: {igual}')

#Acumula las millas del viajero c
    print('\n-----ACUMULAR-----')
    c=lista[1]
    print(f'Millas acumuladas antes de acumular: {c.cantidadTotalMillas()}')
    c= 100+c
    print(f'Millas acumuladas después de acumular: {c.cantidadTotalMillas()}')

#Canjea las millas del viajero d
    print('\n-----CANJEAR-----')
    d= lista[3]
    print(f'Millas acumuladas antes de canjear: {d.cantidadTotalMillas()}')
    d = 100-d
    print(f'Millas acumuladas después de canjear: {d.cantidadTotalMillas()}\n')
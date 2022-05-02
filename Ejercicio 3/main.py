from ClaseRegistro import Registro

from claseMenu import Menu

import csv

'''def mostrar_mayorTemp(lista):
    max_t = -1
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j].get_temperatura() > max_t:
                max_t = lista[i][j].get_temperatura() 
                hora = i
                dia = j
    print(f"Dia:{dia+1}\t Hora:{hora}")

def mostrar_menorTemp(lista):
    min_t= 1000
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j].get_temperatura() < min_t:
                min_t = lista[i][j].get_temperatura() 
                hora = i
                dia = j
    print(f"Dia:{dia+1}\t Hora:{hora}")

def mostrar_mayorPres(lista):
    max_p = -1
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j].get_presion() > max_p:
                max_p = lista[i][j].get_presion() 
                hora = i
                dia = j
    print(f"Dia:{dia+1}\t Hora:{hora}")

def mostrar_menorPres(lista):
    min_p= 10000
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j].get_presion() < min_p:
                min_p= lista[i][j].get_presion() 
                hora = i
                dia = j
    print(f"Dia:{dia+1}\t Hora:{hora}")

def mostrar_mayorHum(lista):
    max_h = -1
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j].get_humedad() > max_h:
                max_h = lista[i][j].get_humedad() 
                hora = i
                dia = j
    print(f"Dia:{dia+1}\t Hora:{hora}")

def mostrar_menorHum(lista):
    min_h = 10000
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j].get_humedad() < min_h:
                min_h = lista[i][j].get_humedad() 
                hora = i
                dia = j
    print(f"Dia:{dia+1}\t Hora:{hora}")
'''

'''def temp_prom_hora(lista):
    print("___TEMPERATURA PROMEDIO___")
    for i in range(len(lista)):
        suma = 0
        for j in range(len(lista[i])):
            suma += int(lista[i][j].get_temperatura())
        prom = suma/dias
        print(f"Hora:{i}\t Promedio:{prom}")
'''

'''def listar_variables(lista):
    print('Ingrese dia para listar')
    dia = int(input('Dia: '))
    for i in range(len(lista)):
        print(lista[i][dia - 1])
'''

'''def menu(lista):

    print('Elija una opcion:')
    print('1 - Mostrar para cada variable el día y hora de menor y mayor valor. ')
    print('2 - Indicar la temperatura promedio mensual por cada hora.')
    print('3 - listar los valores de las tres variables para cada hora del día dado')

    opcion = int(input('Opcion: '))

    match opcion:
        case 1:
            print(f"TEMPERATURA MAXIMA")
            mostrar_mayorTemp(lista)
            print(f"TEMPERATURA MINIMA")
            mostrar_menorTemp(lista)
            print(f"PRESION MAXIMA")
            mostrar_mayorPres(lista)
            print(f"PRESION MINIMA")
            mostrar_menorPres(lista)
            print(f"HUMEDAD MAXIMA")
            mostrar_mayorHum(lista)
            print(f"HUMEDAD MINIMA")
            mostrar_menorHum(lista)

        case 2:
            temp_prom_hora(lista)
        case 3:
            listar_variables(lista)
        case _:
            print('opcion incorrecta')
'''

if __name__ == '__main__':
    dias = 30
    horas = 24
    lista = []
    for i in range(horas):
        lista.append([0] * dias)
    
    archivo = open('enero.csv')
    reader = csv.reader(archivo, delimiter = ';')
    for linea in reader:
        dia = int(linea[0])
        hora = int(linea[1])
        temp = linea[2]
        humedad = linea[3]
        presion = linea[4]
        lista[hora][dia - 1] = Registro(temp, humedad, presion)
    
    menu= Menu()
    print('Elija una opcion:')
    print('1 - Mostrar para cada variable el día y hora de menor y mayor valor. ')
    print('2 - Indicar la temperatura promedio mensual por cada hora.')
    print('3 - listar los valores de las tres variables para cada hora del día dado')
    print('4 - Salir del programa')
    opcion = (input('Opcion: '))
    while opcion!='4':
        menu.opcion(opcion,lista)
        opcion = (input('Opcion: '))
    print("Usted salió del programa")
    archivo.close()
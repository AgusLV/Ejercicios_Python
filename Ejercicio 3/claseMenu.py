from ClaseRegistro import Registro

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            }

    def opcion(self,op,lista):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1' or op=='2' or op=='3':
            func(lista)
        else:
            func()

    def opcion1(self,lista):
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

    def opcion2(self,lista):
        print("___TEMPERATURA PROMEDIO___")
        for i in range(len(lista)):
            suma = 0
            for j in range(len(lista[i])):
                suma += int(lista[i][j].get_temperatura())
            prom = suma/30
            print(f"Hora:{i}\t Promedio:{prom}")

    def opcion3(self,lista):
        print('Ingrese dia para listar')
        dia = int(input('Dia: '))
        for i in range(len(lista)):
            print(lista[i][dia - 1])

def mostrar_mayorTemp(lista):
    max_t=-1
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
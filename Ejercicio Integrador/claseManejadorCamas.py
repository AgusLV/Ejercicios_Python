import numpy as np

import csv

from claseCama import Cama

class ManejadorCamas:
    __cantidad=0
    __dimension=0
    __incremento=1

    def __init__(self,dimension=1,incremento=1):
        self.__arrCamas= np.empty(dimension,dtype=Cama)
        self.__cantidad=0
        self.__dimension=dimension
        self.__incremento=incremento
        pass

    def agregarCama(self,obj):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arrCamas.resize(self.__dimension)
        self.__arrCamas[self.__cantidad] = obj
        self.__cantidad += 1

    def testCamas(self):
        archivo = open('camas.csv')
        reader = csv.reader(archivo,delimiter=';')
        next(reader)
        for fila in reader:
            id = int(fila[0])
            habitacion = int(fila[1])
            estado = bool(fila[2])
            AyN = fila[3]
            diagnostico = fila[4]
            F_Intern = fila[5]
            F_Alta = fila[6]
            self.agregarCama(Cama(id,habitacion,estado,AyN,diagnostico,F_Intern,F_Alta))

    def buscaPaciente(self,AyN):
        paciente=None
        i=0
        band=False
        while i<self.__arrCamas.size and not band:
            if self.__arrCamas[i].getNom() == AyN:
                band=True
                paciente = self.__arrCamas[i]
            else: i += 1
        return paciente

    def buscaPaciente_Diagnostico(self,diagnostico):
        pacientes=[]
        for i in range(self.__cantidad):
            if self.__arrCamas[i].getEstado() == True:
                if diagnostico == self.__arrCamas[i].getDiagnostico():
                    pacientes.append(self.__arrCamas[i])
        return pacientes

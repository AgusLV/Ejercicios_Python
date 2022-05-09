import csv

from claseMedicamento import Medicamento

class ManejadorMedicamentos:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def agregarMedicamento(self,obj):
        self.__lista.append(obj)
        pass

    def testMedicamentos(self):
        archivo=open('medicamentos.csv')
        reader=csv.reader(archivo,delimiter=';')
        next(reader)
        for fila in reader:
            idCama=int(fila[0])
            idMedicamento=int(fila[1])
            nom_com=fila[2]
            monodroga=fila[3]
            presentacion=fila[4]
            cantidad=fila[5]
            precio=float(fila[6])
            self.agregarMedicamento(Medicamento(idCama,idMedicamento,nom_com,monodroga,presentacion,cantidad,precio))

    def buscaMed(self,id):
        Lista_MedPaciente=[]
        for i in range(len(self.__lista)):
            if(id==self.__lista[i].getIdCama()):
                Lista_MedPaciente.append(self.__lista[i])
        return Lista_MedPaciente


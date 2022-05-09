import csv

from clasePlanAhorro import PlanAhorro

class ManejadorPlanes:
    __lista=[]
    def __init__(self):
        self.__lista=[]    

    def agregarPlan(self,unPlan):
        self.__lista.append(unPlan)

    def actualizarListaValores(self):
        for plan in self.__lista:
            plan.mostrarInfo()
            plan.actualizarValor()

    def mostrarInferior(self,valor):
        for plan in self.__lista:
            valor_cuota=(plan.getValor()/PlanAhorro.getCuotasPlan()) + plan.getValor() * 0.10
            print(valor_cuota)
            if valor_cuota < valor:
                plan.mostrarInfo()

    def mostrarMonto(self):
        for plan in self.__lista:
            valor_cuota=(plan.getValor()/PlanAhorro.getCuotasPlan()) + plan.getValor() * 0.10
            monto=plan.calculaMonto(valor_cuota)
            print(f"Monto para licitar el vehículo {plan.getModelo()} {plan.getVersion()}: {monto}")

    def modificaCantCuotas(self):
        PlanAhorro.modificaCuotasLicitar()
        print(PlanAhorro.getCuotasLicitar())

    def testLista(self):
        archivo=open('planes.csv')
        reader= csv.reader(archivo, delimiter=';')
        for line in reader:
            unPlan=PlanAhorro(int(line[0]),line[1],line[2],float(line[3]))
            self.agregarPlan(unPlan)
        archivo.close()
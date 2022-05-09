class PlanAhorro:
    __code=0
    __modelo=''
    __valor = 0.0
    __version=''
    __cuotasPlan=60
    __cuotasLicitar=10
    def __init__(self,cod,modelo,version,val):
        self.__code=cod
        self.__modelo=modelo
        self.__version=version
        self.__valor = val

    def __str__(self):
        return f'Codigo: {self.__code} Modelo: {self.__modelo} Version: {self.__version}\n Valor: {self.__valor} Cuotas Plan: {self.__cuotasPlan} Cuotas para Licitar: {self.__cuotasLicitar}'

    def getValor(self):
        return float(self.__valor)

    def getModelo(self):
        return self.__modelo

    def getVersion(self):
        return self.__version

    def mostrarInfo(self):
        return print(f'Codigo: {self.__code}\t Modelo: {self.__modelo} \tVersion: {self.__version}')

    def actualizarValor(self):
        self.__valor = float(input('Ingrese el valor actual del vehículo: '))
        print('Se modificó el valor del vehículo')

    def calculaMonto(self,valor_cuota):
        return self.__cuotasLicitar*valor_cuota

    @classmethod
    def getCuotasLicitar(cls):
        return int(cls.__cuotasLicitar)

    @classmethod
    def getCuotasPlan(cls):
        return int(cls.__cuotasPlan)

    @classmethod
    def modificaCuotasLicitar(cls):
        cls.__cuotasLicitar=int(input("Ingrese cantidad de cuotas para licitar: "))
class ViajeroFrecuente:
    __num_viajero=0
    __dni=''
    __nombre=''
    __apellido=''
    __millas_acum=0

    def __init__(self,num,nom,apellido,dni,millas):
        self.__num_viajero=num
        self.__dni=dni
        self.__nombre=nom
        self.__apellido=apellido
        self.__millas_acum=millas

    def __str__(self):
        return (f'N° Viajero: {self.__num_viajero} Nombre: {self.__nombre} Apellido: {self.__apellido}\nDNI: {self.__dni} Cantidad de Millas: {self.__millas_acum}')

    def getNumero(self):
        return self.__num_viajero

    def cantidadTotalMillas(self):
        return self.__millas_acum

    def acumularMillas(self,cantRecorr):
        self.__millas_acum += cantRecorr
        return self.__millas_acum

    def canjearMillas(self,cantCanj):
        if cantCanj <= self.__millas_acum:
            self.__millas_acum -= cantCanj
            print("Millas canjeadas")
        else: 
            print("Error")
        return self.__millas_acum

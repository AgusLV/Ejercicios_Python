class ViajeroFrecuente:
    __num_viajero=0
    __dni=''
    __nombre=''
    __apellido=''
    __millas_acum=0

    def __init__(self,num,dni,nom,apellido,millas):
        self.__num_viajero=num
        self.__dni=dni
        self.__nombre=nom
        self.__apellido=apellido
        self.__millas_acum=millas

    def getNumero(self):
        return self.__num_viajero

    def cantidadTotalMillas(self):
        return self.__millas_acum

    def acumularMillas(self,cantRecorr):
        return(self.__millas_acum + cantRecorr)

    def canjearMillas(self,cantCanj):
        if cantCanj <= self.__millas_acum:
            self.__millas_acum-=cantCanj
            print("Millas canjeadas")
        else: print("Error")
        return self.__millas_acum

    def mostrar(self):
        return self.__num_viajero + " " + self.__nombre + " " + self.__apellido + " " + self.__dni + " " + self.__millas_acum
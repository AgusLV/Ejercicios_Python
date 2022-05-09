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

    def __gt__(self,otro):
        if (self.__millas_acum) > (otro.__millas_acum):
            mayor = self
        else: mayor = otro
        return mayor

    def __add__ (self,millas):
        return ViajeroFrecuente(self.__num_viajero,self.__nombre,self.__apellido,self.__dni,self.__millas_acum + millas)

    def __sub__(self,millas):
        calculo=self.__millas_acum
        if (calculo>=millas):
            calculo = calculo - millas
        else: print("\t---ERROR---")
        return ViajeroFrecuente(self.__num_viajero,self.__nombre,self.__apellido,self.__dni,calculo)
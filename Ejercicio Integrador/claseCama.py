class Cama:
    __id=0
    __habitacion=0
    __estado=False
    __NomyAp=None
    __diagnostico=''
    __F_Intern=''
    __F_Alta=''
    
    def __init__(self,id,hab,estado,NyA,diagn,Fi,Fa):
        self.__id=id
        self.__habitacion=hab
        self.__estado=estado
        self.__NomyAp=NyA
        self.__diagnostico=diagn
        self.__F_Intern=Fi
        self.__F_Alta=Fa

#    def cambiaEstado(self,band):
#        self.__estado=band

    def getNom(self):
        return self.__NomyAp

    def getId(self):
        return self.__id

    def getHabitacion(self):
        return self.__habitacion

    def getDiagnostico(self):
        return self.__diagnostico

    def getFecha_Internacion(self):
        return self.__F_Intern

    def getFecha_Alta(self):
        return self.__F_Alta

    def __str__(self):
        return(f'ID: {self.__id}\nHabitacion: {self.__habitacion}\nPaciente: {self.__NomyAp}\nEstado: {self.__estado}\nDiagnostico: {self.__diagnostico}\nFecha Internacion: {self.__F_Intern}\nFecha Alta: {self.__F_Alta}')

#    def setFecha_Alta(self):
#        self.__F_Alta=input('Fecha de Alta: ')
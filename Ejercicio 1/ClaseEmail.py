class Email:
    __idCuenta = ''
    __Dominio = ''
    __TipoDominio = ''
    __Contraseña = ''
    def __init__(self,id = '',dom = '',tipoD = '',contr = ''):
        self.__idCuenta = id
        self.__Dominio = dom
        self.__TipoDominio = tipoD
        self.__Contraseña = contr
    
    def retornaEmail(self):
        return(self.__idCuenta + '@' + self.__Dominio + '.' + self.__TipoDominio)
    
    def getDominio(self):
        return(self.__Dominio)
    
    def getId(self):
        return(self.__idCuenta)
    
    def crearCuenta(self,direc):
        if (direc.find ('@')):
            x=direc.split('@')
            xid=x[0]
            if (x[1].find ('.')):
                y=x[1].split('.')
                xdom=y[0]
                xtipoD=y[1]
                contra= input("Ingrese una contraseña: ")
                self.__init__(xid,xdom,xtipoD,contra)
                print("La cuenta se ha creado con éxito")
            else: print("La direccion de correo no tiene un '.'")
        else: print("La direccion de correo no tiene '@'")
    
    def modContraseña(self):
        auxiliar = input("Ingrese la Contraseña actual: ")
        while (auxiliar != self.__Contraseña):
            print("La contraseña ingresada no es correcta")
            auxiliar = input("Ingrese la Contraseña actual: ")
        else: self.__Contraseña=input("Ingrese la nueva Contraseña: ")
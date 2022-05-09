class Medicamento:
    __idCama=0
    __idMedicamento=0
    __nom_com=''
    __monodroga=''
    __presentacion=''
    __cantidad=''
    __precio=0.0

    def __init__(self,idCama,idMed,nom,monodroga,present,cant,precio):
        self.__idCama=idCama
        self.__idMedicamento=idMed
        self.__nom_com=nom
        self.__monodroga=monodroga
        self.__presentacion=present
        self.__cantidad=cant
        self.__precio=precio
        pass

    def getIdCama(self):
        return self.__idCama

    def getPrecio(self):
        return self.__precio

    def getNombre_Comercial(self):
        return self.__nom_com

    def getMonodroga(self):
        return self.__monodroga

    def getPresentacion(self):
        return self.__presentacion

    def getCantidad(self):
        return self.__cantidad
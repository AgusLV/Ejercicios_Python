class Conjunto:
    __lista=[]
    def __init__(self,obj=[]):
        self.__lista=obj
    
    def __str__(self):
        return (f'{self.__lista}')
    
    def __add__(self,otro):
        self.__lista.sort()
        otro.__lista.sort()
        a=len(self.__lista)
        b=len(otro.__lista)
        i=0
        j=0
        nuevo=[]
        while i<a and j<b:
            if self.__lista[i] < otro.__lista[j]:
                nuevo.append(self.__lista[i])
                i+=1
            elif self.__lista[i] > otro.__lista[j]:
                nuevo.append(otro.__lista[j])
                j+=1
            else:
                nuevo.append(self.__lista[i])
                i+=1
                j+=1
        if i<a:
            while i<a:
                nuevo.append(self.__lista[i])
                i+=1
        if j<b:
            while j<b:
                nuevo.append(otro.__lista[j])
                j+=1
        return Conjunto(nuevo)
    
    def __sub__(self,otro):
        self.__lista.sort()
        otro.__lista.sort()
        nuevo=self.__lista.copy()
        i=0
        while i<len(nuevo):
            if nuevo[i] in otro.__lista:
                nuevo.pop(i)
            else:
                i+=1
        return Conjunto(nuevo)
    
    def __eq__(self,otro):
        band=True
        if(len(self.__lista)== len(otro.__lista)):
            i=0
            while i<len(self.__lista) and band:
                if self.__lista[i] in otro.__lista:
                    i+=1
                else:
                    band=False
        else: band=False
        return band

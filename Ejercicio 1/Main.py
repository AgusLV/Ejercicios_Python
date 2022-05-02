import csv

from ClaseEmail import Email

def test():
    objPrueba= Email('ejemplo123','gmail','com',789456)
    print(f'-------- EMAIL --------: {objPrueba.retornaEmail()}')

def cargaDatos():
    print("\n1- Proceso de creacion de cuenta")
    nom = input('\tIngrese Nombre: ')
    id = input('\tId: ')
    dom = input('\tDominio: ')
    tipo = input('\tTipo: ')
    contr = input('\tContraseña: ')
    nuevo = Email(id,dom,tipo,contr)
    print(f'Estimado {nom} te enviaremos tus mensajes a la direccion {nuevo.retornaEmail()}')
    return nuevo

def repetido():
    indice= 0
    cont=0
    while indice < len(lista) and cont<2 :
        if id == lista[indice].getId():
            cont=cont+1
        indice+=1
    return cont

if __name__ == '__main__':
    test()
    unEmail = cargaDatos()
    print("\n2- CAMBIO DE CONTRASEÑA")
    unEmail.modContraseña()
    
    print("\n3- Crear cuenta a partir de un correo")
    otroEmail = Email()
    otroEmail.crearCuenta(input('\nIngrese una dirección de Correo: '))
    
    print("\n4- Trabajar con Archivo CSV")
    lista=[]
    archivo= open('Correos.csv')
    reader= csv.reader(archivo,delimiter=';')
    
    for line in reader:
        for correo in line:
            new_account = Email()
            print(f"\n{correo}")
            new_account.crearCuenta(correo)
            lista.append(new_account)
    archivo.close()
    id=input("\nIngrese un Id a buscar: ")
    
    cont=repetido()
    if cont==2:
        print(f"El Id {id} está repetido")
    elif cont==1 :
        print(f"El Id {id} no está repetido")
    else: print(f"El Id {id} no está en la lista") 

''' LOTE DE PRUEBAS
Agustín Astudillo
aguastudillo
gmail
com
123456
123456
826454
leonomia126@hotmail.com
789456
123
456
789
dsad
fghfhgf
oiewa
KJDFKLJ
kdjaskljd
rytjoyuirwe
utykjxad
meitrumauddauxa-1675
'''
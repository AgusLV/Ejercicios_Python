import csv
import email

from ClaseEmail import Email

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

if __name__ == '__main__':
    
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
    busca=input("\nIngrese un Id a buscar: ")
    cont=0
    for cuenta in lista:
        if busca == cuenta.getId():
            cont+=1
        if cont >= 2:
            print(f"El Id{busca} está repetido.")

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
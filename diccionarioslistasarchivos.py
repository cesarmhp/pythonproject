def menu():
    print("******** Inventario**********")
    print("0. Salir")
    print("1. Imprimir inventario")
    print("2. Agregar articulos")
    print("3. Eliminar articulos")
    print("4. Generar archivo")

def seleccion():
    while True:
        try:
            opcion=int(input("Que opción eliges: "))
            if opcion<0 or opcion>4:
                print("Debes elegir solo entre 0 y 4")
            else:
                break
        except ValueError:
            print("Solo utiliza numeros")
    return opcion
    
lista=[]
diccionario={}

while True:
    menu()
    opcion=seleccion()
    if opcion == 0:
        break

    if opcion == 1:
        print("ARTICULO\t\tCANTIDAD")
        for i in lista:
            print(i,"\t\t",diccionario[i])

    if opcion == 2:
        articulo=input("Que articulo deseas agregar: ")
        if articulo in lista:
            print("Hay: ",diccionario[articulo]," articulo(s) de: ",articulo)
            while True:
                try:
                    cantidad=int(input("Cuantos mas deseas agregar: "))
                    diccionario[articulo]=diccionario[articulo]+cantidad
                    break
                except ValueError:
                    print("Utiliza solo numeros")
        else:
            while True:
                desicion=input("no existe el articulo deseas agregarlo al invnetario (s/n)")
                if desicion != 's' and desicion != 'n':
                    print("Solo puedes escribir s ó n minusculas")
                else:
                    if desicion == 's':
                        lista.append(articulo)
                        diccionario[articulo]=0
                        cantidad=int(input("Cuantos hay: "))
                        diccionario[articulo]=cantidad
                        break
                    if desicion == 'n':
                        break
    
    if opcion == 3:
        articulo=input("Que articulo deseas eliminar: ")
        if articulo in lista:
            print("Hay: ",diccionario[articulo]," articulo(s) de: ",articulo)
        
        
        
                        
                        
            
        
        
                     
        
        

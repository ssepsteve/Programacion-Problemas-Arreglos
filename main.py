#Punto 1 
def promedio(lista):
    suma = 0
    try:
        for i in lista:
            suma += i
        cantidad = len(lista)
        prom = suma / cantidad
            
    except:
        print("Hay elementos que no son numeros")
    else:
        return prom
print(f"el promedio de la lista es: {promedio([1,2,3,4,5,6,7])}")

#Punto 2
def productoPuntoDosArreglos(Arreglo1:list,Arreglo2:list):
    print(f"Los Arreglos son: {Arreglo1} y {Arreglo2}")
    productoPunto = 0
    if len(Arreglo1) == len(Arreglo2):
        Arreglo1Tipos = []
        Arreglo2Tipos = []
        for i in range(0,len(Arreglo1)):
            Arreglo1Tipos.append(str(type(Arreglo1[i])))
            Arreglo2Tipos.append(str(type(Arreglo1[i])))
        if str(type(True)) in Arreglo1Tipos or str(type(True)) in Arreglo2Tipos:
            print("Hay valores booleanos en el arreglo")
            productoPunto = None
        elif str(type("String")) in Arreglo1Tipos or str(type("String")) in Arreglo2Tipos:
            print("Hay caracteres en el arreglo")
            productoPunto = None
        else:
            for v,w in zip(Arreglo1,Arreglo2):
                productoPunto += v*w
    else:
        print("Los arreglos son de diferente longitud")
        productoPunto = None
    return productoPunto

print(productoPuntoDosArreglos([1,2,3,4,5],[2,3,4,5,6]))




#Punto 3
tupla1 = (43, 15, 7, 8, 7, 34, 76,12)
tupla2 = (5, 6, 2, "a", 9, 2, 5, 6)
def productos_directos(arr1, arr2):
    #define los 2 arreglos iniciales

    if len(tupla1)  == len(tupla2): #confirma que tienen la cantidad de elementos

        productos = []
        for i in range(len(tupla1)): #recorre la tupla por indices
                
            if type(tupla2[i]) == int and type(tupla1[i]) == int: #confirma que ambos elementos sean enteros        
                punto = tupla1[i] * tupla2[i] #multiplica por el elemento del mismo indice en la otra tupla
                productos.append(punto)
                
            else: 
                print(f"Se encuentro un valor no entero, por lo tanto se salto la columna {i+1}")
                pass

        print("El conjunto de los productos directos es", productos)

    else:
        print("los arreglos deben tener la misma cantidad de elementos")

productos_directos(tupla1, tupla2)

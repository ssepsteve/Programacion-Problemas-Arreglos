#Punto 1 


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

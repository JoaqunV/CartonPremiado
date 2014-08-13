def leerArchivo():
    archivo= open("sorteos del kino.txt","r")
    sorteo= archivo.readlines()
    archivo.close()
    return sorteo


def crearListaDelSorteo(sorteo):
    lista=[]
    
    for elemento in sorteo:
        elemento= elemento.rstrip()
        elemento= elemento.split(" ")
        lista.append(elemento)
    return lista


def crearDiccionario(lista):
    diccionario=dict(lista)
    return diccionario



cartones={'1':[1,3,5,7],'2':[2,4,6,8],'3':[9,11,13,15],'4':[10,12,14,28]}
listaGanadora= [3,8,14,28]

def compararNumeros(cartones,listaGanadora):
    result={}
    number=cartones.keys()
    juegos=cartones.values()
    posic=0
    for carton in juegos:
        cont=0
        print carton
        for elemento in carton:
            if elemento in listaGanadora:
                cont+=1
            else:
                pass
        a=number[posic]
        result[a]=cont
        posic+=1
    return result



sorteo= leerArchivo()
listadosDelSorteo= crearListaDelSorteo(sorteo)
Diccionario=crearDiccionario(listadosDelSorteo)
resultado= compararNumeros(cartones,listaGanadora)
print resultado
print ""
print ""

print sorteo
print ""
print ""
print ""
print listadosDelSorteo
print""
print crearDiccionario(listadosDelSorteo)

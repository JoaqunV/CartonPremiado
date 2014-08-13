#Importacion modulo Random
import random

def leerArchivoSorteo(numero):
    Archivo= open("Sorteo-%s.txt"%(numero),"r") # al imprimir en pantalla
    Cartones=Archivo.readlines()
    Archivo.close()
    return Cartones

def leerArchivoCartones(numero):
    Archivo= open("Cartones-%s.txt"%(numero),"r") # al imprimir en pantalla
    Cartones=Archivo.readlines()
    Archivo.close()
    return Cartones
#al retornar cartones, se convertirá la lista de lineas en una matriz donde en la posicion [0] se encuetran
#los numeros de los cartones y en la posicion[1] son las jugadas
def convertirSorteoALista(Cartones):
    #creo una lista vacía para numeros cartones y jugadas
    aciertos=[]
    montos=[]
    #leemos cada elemento que se encuentra en la lista llamada cartones
    for elemento in Cartones:
        #para la linea leida separo los elementos con un ':'
        elemento=elemento.strip()
        elemento = elemento.split(" ")
        # los numeros de los cartones quedan en la posicion [0]
        aciertos.append(elemento[0])
        #las jugadas quedan en la posicion [1]
        montos.append(elemento[1])
        #creo una matriz donde guardo los numeros de cartones y las jugadas (son dos listas dentro de una lista)
    matriz = [aciertos, montos]
    #retorno la matriz obtenida para luego ser utilizada en la funcion siguiente
    return matriz

def convertirCartonALista(Cartones):
    #creo una lista vacía para numeros cartones y jugadas
    listaCartones=[]
    listaJuego=[]
    #leemos cada elemento que se encuentra en la lista llamada cartones
    for elemento in Cartones:
        #para la linea leida separo los elementos con un ':'
        elemento=elemento.strip()
        elemento = elemento.split(" ")
        # los numeros de los cartones quedan en la posicion [0]
        listaCartones.append(elemento[0].strip(":"))
        #las jugadas quedan en la posicion [1]
        listaJuego.append(elemento[1])
        #creo una matriz donde guardo los numeros de cartones y las jugadas (son dos listas dentro de una lista)
    matriz1 = [listaCartones, listaJuego]
    #retorno la matriz obtenida para luego ser utilizada en la funcion siguiente
    return matriz1
    
def consultarCarton(carton, matriz):
    cont = 0
    #el id(identificador) sirve para comparar al final de la funcion, si el carton indicado existe o no
    id = False
    #utilizamos un while para iterar y comparar que el carton indicado se encuentre dentro de los registros en matriz
    while cont <= len(matriz[0])-1:
        if carton == matriz[0][cont]:
            return matriz[1][cont]
    #si el id no es falso pasa sobre el while y se crea una condicion negacion para que retorne un False
    if not(id):
        return False

#esta funcion se puede ocupar para ambos archivos de entradas
def crearDiccionario(lista):
    diccionario= {}
    cont=0
    while cont<len(lista[0]):
        diccionario[lista[0][cont]]=lista[1][cont]
        cont=cont+1
    return diccionario

def cambiarValoresALista(diccionario):
    listaDeValores={}
    llaves=diccionario.keys()
    for elementos in llaves:
        lista=diccionario[elementos].split(",")
        listaDeValores[elementos]=lista
    return listaDeValores
    



#def generarArchivo(numeroSorteo, lista):
    #nombreArchivo = "Sorteo-"+str(numeroSorteo)+".txt"
    #archivo = open(nombreArchivo,"w")
    #archivo.write(lista)
    #archivo.close()


def generarSorteo():
    listaNumGanadores = []
    while len(listaNumGanadores)<=14:
        numero = random.randint(1,25)
        if not(numero in listaNumGanadores):
            listaNumGanadores.append(numero)
        #Genera los numeros ganadores, comparando que el numero no se repita.
    #Ordeno de los numeros con la funcion sort
    listaNumGanadores.sort()
    #retorno lista de numeros ganadores
    return listaNumGanadores
    
def compararNumeros(cartones,listaNumGanadores):
    result={}
    number=cartones.keys()
    juegos=cartones.values()
    posic=0
    for carton in juegos:
        cont=0
        for elemento in carton:
            elemento= int(elemento)
            if elemento in listaGanadora:
                cont+=1
            else:
                pass
        a=number[posic]
        result[a]=cont
        posic=posic+1
    return result

def indicarMontoObtenido(aciertos, montos):
    cartones = aciertos.keys()
    aciertosCarton = aciertos.values()
    aciertosDeMontos = montos.keys()
    montoAsociado = montos.values()
    
    cont = 0
    cartonYAciertos = {}
    while cont < len(cartones):
        pos = 0
        while pos < len(aciertosDeMontos):
            if str(aciertosCarton[cont])==str(aciertosDeMontos[pos]):
                cartonYAciertos[cartones[cont]] = montoAsociado[pos]
            else:
                pass
            pos+=1
        #End while    
        cont+=1
    #End while
    return cartonYAciertos

def formato(numero):
    cont=0
    primero=""
    final=""
    num = str(numero)
    while(cont< len(num)):
        primero = primero + num[-1]
        cont+=1
    j=0
    while(j<len(primero)):
        if(cont%3==0):
            primero=primero +"."
        j+=1
    i= 0
    while(i<len(primero)):
          final = final + primero[-1]
          i+=1
    return final



def escribirResumenDelSorteo(montos, sorteados, ganadores, numero, aciertos):
    lineaSeparadora="====================================================================\n"
    archivo = open ("Resumen_Sorteo-"+str(numero)+".txt", "w")
    #
    archivo.write(lineaSeparadora)
    #
    linea = "SORTEO N° " + str(numero)+"\n"
    archivo.write(lineaSeparadora+linea)
    cantidadCartonesJugados = len(aciertos.keys())
    linea = "SE JUGARON "+ str(cantidadCartonesJugados) + " CARTONES\n"
    archivo.write(linea+lineaSeparadora)
    linea = "RESULTADOS:\n"+str(sorteados)+"\n"
    archivo.write(linea+lineaSeparadora)
    linea = "CATEGORIA     TOTAL CATEGORIA     N GANADORES     PREMIO POR GANADOR"+"\n"
    archivo.write(linea)
    if ganadores[0] == 0:
        linea = "14 ACIERTOS   $"+str(montos['14'])+"          "+str(ganadores[0])+"              $"+montos['14']+"\n"
    else:
        linea = "14 ACIERTOS   $"+str(montos['14'])+"   "+str(ganadores[0])+"                     $"+str(int(montos['14'])/ganadores[0])+"\n"
    archivo.write(linea)
    if ganadores[1] == 0:
        linea = "13 ACIERTOS   $"+str(montos['13'])+"             "+str(ganadores[1])+"             $"+montos['13']+"\n"
    else:
        linea = "13 ACIERTOS   $"+str(montos['13'])+"             "+str(ganadores[1])+"             $"+str(int(montos['13'])/ganadores[1])+"\n"
    archivo.write(linea)
    if ganadores[2] == 0:
        linea = "12 ACIERTOS   $"+str(montos['12'])+"            "+str(ganadores[2])+"             $"+montos['12']+"\n"
    else:
        linea = "12 ACIERTOS   $"+str(montos['12'])+"            "+str(ganadores[2])+"              $"+str(int(montos['12'])/ganadores[2])+"\n"
    archivo.write(linea)
    if ganadores[3] == 0:
        linea = "11 ACIERTOS   $"+str(montos['11'])+"            "+str(ganadores[3])+"              $"+montos['11']+"\n"
    else:
        linea = "11 ACIERTOS   $"+str(montos['11'])+"            "+str(ganadores[3])+"              $"+str(int(montos['11'])/ganadores[3])+"\n"
    archivo.write(linea)
    if ganadores[4] == 0:
        linea = "10 ACIERTOS   $"+str(montos['10'])+"            "+str(ganadores[4])+"               $"+montos['10']+"\n"
    else:
        linea = "10 ACIERTOS   $"+str(montos['10'])+"            "+str(ganadores[4])+"               $"+str(int(montos['10'])/ganadores[4])+"\n"
    archivo.write(linea)
    return True

                  
def escribirCartonesPremiados( diccionario, montos, aciertos, Resultado, numero):
    lineaSeparadora="====================================================================\n"
    listaNumeroGanadores=[]
    archivo = open ("Cartones_Premiados-"+str(numero)+".txt", "w")
    #
    archivo.write(lineaSeparadora)
    #
    lineaAciertoYMonto14 = "14 ACIERTOS, PREMIO TOTAL A REPARTIR ES DE $" + montos['14']+"\n"
    archivo.write(lineaAciertoYMonto14)
    archivo.write(lineaSeparadora)
    cartones = Resultado.keys()
    aciertosCarton = Resultado.values()
    a = aciertos.keys()
    b = aciertos.values()
    cont = 0
    cantidadGanadores = 0
    while cont < len(cartones):

        if str(b[cont])=='14':
            linea = cartones[cont] + ":" + diccionario[cartones[cont]] + "\n"
            archivo.write(linea)
            cantidadGanadores+=1
        else:
            pass
        cont+=1
    if cantidadGanadores == 0:
        cantidadGanadores2=1
    else:
        linea = "Total Ganadores: " + str(cantidadGanadores)+"\n" + "QUEDANDO UN TOTAL PARA CADA GANADOR DE: " + str(int(montos['14'])/cantidadGanadores)+"\n"
        archivo.write(linea)

    listaNumeroGanadores.append(cantidadGanadores)
    archivo.write(lineaSeparadora)
    #
    
    lineaAciertoYMonto13 = "13 ACIERTOS, PREMIO TOTAL A REPARTIR ES DE $" + montos['13']+"\n"
    archivo.write(lineaAciertoYMonto13)
    archivo.write(lineaSeparadora)
    cartones = Resultado.keys()
    aciertosCarton = Resultado.values()
    cont = 0
    cantidadGanadores = 0
    while cont < len(cartones):
        if str(b[cont])=='13':
            linea = cartones[cont] + ":" + diccionario[cartones[cont]] + "\n"
            archivo.write(linea)
            cantidadGanadores+=1
        else:
            pass
        cont+=1
    if cantidadGanadores == 0:
        cantidadGanadores2=1
    else:
        linea = "Total Ganadores: " + str(cantidadGanadores)+"\n" + "QUEDANDO UN TOTAL PARA CADA GANADOR DE: " + str(int(montos['13'])/cantidadGanadores)+"\n"
        archivo.write(linea)

    listaNumeroGanadores.append(cantidadGanadores)
    archivo.write(lineaSeparadora)
    #
    
    lineaAciertoYMonto12 = "12 ACIERTOS, PREMIO TOTAL A REPARTIR ES DE $" + montos['12']+"\n"
    archivo.write(lineaAciertoYMonto12)
    archivo.write(lineaSeparadora)
    cartones = Resultado.keys()
    aciertosCarton = Resultado.values()
    cont = 0
    cantidadGanadores = 0
    while cont < len(cartones):
        if str(b[cont])=='12':
            linea = cartones[cont] + ":" + diccionario[cartones[cont]] + "\n"
            archivo.write(linea)
            cantidadGanadores+=1
        else:
            pass
        cont+=1
    if cantidadGanadores == 0:
        cantidadGanadores2=1
    else:
        linea = "Total Ganadores: " + str(cantidadGanadores)+"\n" + "QUEDANDO UN TOTAL PARA CADA GANADOR DE: " + str(int(montos['12'])/cantidadGanadores)+"\n"
        archivo.write(linea)
    listaNumeroGanadores.append(cantidadGanadores)
    archivo.write(lineaSeparadora)
    #
    
    lineaAciertoYMonto11 = "11 ACIERTOS, PREMIO TOTAL A REPARTIR ES DE $" + montos['11']+"\n"
    archivo.write(lineaAciertoYMonto11)
    archivo.write(lineaSeparadora)
    cartones = Resultado.keys()
    aciertosCarton = Resultado.values()
    cont = 0
    cantidadGanadores = 0
    while cont < len(cartones):
        if str(b[cont])=='11':
            linea = cartones[cont] + ":" + diccionario[cartones[cont]] + "\n"
            archivo.write(linea)
            cantidadGanadores+=1
        else:
            pass
        cont+=1
    if cantidadGanadores == 0:
        cantidadGanadores2=1
    else:
        linea = "Total Ganadores: " + str(cantidadGanadores)+"\n" + "QUEDANDO UN TOTAL PARA CADA GANADOR DE: " + str(int(montos['11'])/cantidadGanadores)+"\n"
        archivo.write(linea)
    listaNumeroGanadores.append(cantidadGanadores)
    archivo.write(lineaSeparadora)
    #
    
    lineaAciertoYMonto10 = "10 ACIERTOS, PREMIO TOTAL A REPARTIR ES DE $ " + montos['10']+"\n"
    archivo.write(lineaAciertoYMonto10)
    archivo.write(lineaSeparadora)
    cartones = Resultado.keys()
    aciertosCarton = Resultado.values()
    cont = 0
    cantidadGanadores = 0
    while cont < len(cartones):
        if str(b[cont])==str(10):
            linea = cartones[cont] + ":" + diccionario[cartones[cont]] + "\n"
            archivo.write(linea)
            cantidadGanadores+=1
        else:
            pass
        cont+=1
    if cantidadGanadores == 0:
        cantidadGanadores2=1
    else:
        linea = "Total Ganadores: " + str(cantidadGanadores)+"\n" + "QUEDANDO UN TOTAL PARA CADA GANADOR DE: " + str(int(montos['10'])/cantidadGanadores)+"\n"
        archivo.write(linea)
    listaNumeroGanadores.append(cantidadGanadores)
    archivo.write(lineaSeparadora)
    #
    archivo.close()
    return listaNumeroGanadores


n=input("ingrese: ")
Sorteos= leerArchivoSorteo(n)
Cartones= leerArchivoCartones(n)
listaDelSorteo=convertirSorteoALista(Sorteos)
listaDeCartones= convertirCartonALista(Cartones)
diccionarioDeCartones=crearDiccionario(listaDeCartones)
diccionarioDelSorteo=crearDiccionario(listaDelSorteo)
listaDeCartones1= cambiarValoresALista(diccionarioDeCartones)
listaGanadora= generarSorteo()
Aciertos= compararNumeros(listaDeCartones1,listaGanadora)
resultado = indicarMontoObtenido(Aciertos, diccionarioDelSorteo)


listaDeGanadoresCategorias = escribirCartonesPremiados(diccionarioDeCartones,diccionarioDelSorteo, Aciertos, resultado, n)
if escribirResumenDelSorteo(diccionarioDelSorteo, listaGanadora, listaDeGanadoresCategorias, n, Aciertos):
    print "Se han generado los archivos referentes al sorteo"
else:
    print "Error inesperado..."



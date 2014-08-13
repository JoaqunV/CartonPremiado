import random
#cLANR= CREAR lista aleatoria no repetitiva

def cLANR(largo,ini,fin):
    fila=[]
    i=0
    while i< largo:
        numero= random.randrange(ini,fin+1)
        numero= str(numero)
        if numero in fila:
            pass
        else:
            fila.append(numero)
            i=i+1
    return fila



#cM= crea matriz
def cM(f,c,ini,fin):
    matriz=[]
    j=0
    while j< f:
        fila= cLANR(c,ini,fin)# c= columna, ini= inicio,fin= final
        matriz.append(fila)
        j=j+1
    return matriz

numeros = cLANR(15,100,200)
numeros.sort()
print numeros
print "###"
matrizPrueba = cM(5,5,1,100)
print matrizPrueba
print "###"



archivoM= open("matriz.txt","w")

for i in matrizPrueba:
    fila= "\t".join(i)
    fila= fila+ "\n"
    print fila
    archivoM.write(fila)
archivoM.close()









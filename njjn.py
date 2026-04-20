import random
from collections import Counter
def generador(nombre:list, numeros:list):
    #CONSTRUYO EL DICT
    dic = {}
    for i in range(len(nombre)):
        dic[nombre[i]] = numeros.copy()
    for i in range(len(numeros)):
        dic[numeros[i]] = nombre.copy()
    
    for x in range(len(nombre)):
        permitidos = []
        for j in range(len(nombre)):
            if (x == len(nombre)-1 and (nombre[j] != nombre[x])):
                permitidos.append(nombre[j])
                
            else:
                if (nombre[j] != nombre[x+1]) and (nombre[j] != nombre[x]):
                    permitidos.append(nombre[j])
        dic[nombre[x]] += permitidos
    print(dic)
    for y in range(len(numeros)):
        permitidos = []
        for j in range(len(numeros)):
            if numeros[j] != numeros[y+1]:
                permitidos.append(numeros[j])
        dic[numeros[x]] += permitidos

generador(["h","o","l"],[1,4,6,4,1,3])


    
    
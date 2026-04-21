def primos2_modificado(limite):
    lista = []
    n = 2
    while (n < limite):
        m = int((n)**0.5)
        while (m > 0):
            if (m == 1): 
                lista.append(n)
                m = 0
                n += 1
            elif ((n % m) == 0):
                n += 1
                m = 0
            else:
                m -= 1
    return lista
print(primos2_modificado(1000))
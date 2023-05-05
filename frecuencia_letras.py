def indice_de_coincidencia(fn,grupo):
    f = open(fn)
    texto = f.read()
    indices = []
    indice = ""
    for letra in grupo:
        indices.append(indice)
        indice = []
        rep = texto.count(letra)
        IoC = (26*(rep*(rep-1)))/(len(texto)*(len(texto)-1))
        indice.append(IoC)
    indices.append(indice)
    indices.remove("")
    return indices
    suma = []
    longitud = []
    for i in lista:
        longitud.append(len(i))
    longitud = sum(longitud)
    for i in indices:
        suma.append(sum(i))
    promedio = (sum(suma)/longitud)
    print("Promedio:",promedio)
    f.close()
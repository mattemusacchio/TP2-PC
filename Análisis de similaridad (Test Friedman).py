def indice_de_coincidencia(fn,k):
    texto = fn
    texto = texto.lower()
    texto = texto.split(" ")
    texto = "".join(texto)
    lista = []
    grupo = ""
    for i in range(k):
        lista.append(grupo)
        contador = -1
        contador += 1
        grupo = []
        grupo.append(texto[i])
        conti = i
        while contador < (len(texto)/k):
            contador += 1
            conti = conti + (k)
            if conti >= len(texto):
                continue
            elif texto[conti].isalpha() == False:
                continue
            else:
                grupo.append(texto[conti])
    lista.append(grupo)
    lista.remove("")
    print(lista)
    indices = []
    indice = ""
    for grupo in lista:
        indices.append(indice)
        indice = []
        for i in grupo:
            rep = texto.count(i)
            IoC = (26*(rep*(rep-1)))/(len(texto)*(len(texto)-1))
            indice.append(IoC)
    indices.append(indice)
    indices.remove("")
    print(indices)
    suma = []
    longitud = []
    for i in lista:
        longitud.append(len(i))
    longitud = sum(longitud)
    for i in indices:
        suma.append(sum(i))
    promedio = (sum(suma)/longitud)
    print("Promedio:",promedio)
print(indice_de_coincidencia("Hello' and 'hallo' are the same word. 'Hallo' is simply an alternative way of writing 'hello'. It's quite old-fashioned and rarely used these days. Nowadays, almost everyone writes it 'hello'.",5))
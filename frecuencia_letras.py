def indice_de_coincidencia(grupo):
    grupo = "".join(grupo)
    indices = []
    indice = ""
    for letra in grupo:
        indices.append(indice)
        rep = grupo.count(letra)
        IoC = (26*(rep*(rep-1)))/(len(grupo)*(len(grupo)-1))
        indice = IoC
    indices.append(indice)
    indices.remove("")
    return indices
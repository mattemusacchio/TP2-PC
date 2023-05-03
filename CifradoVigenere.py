def cifrado(msg,clave):
    longitud = len(msg)
    clave_repetida = []
    contador = -1
    while len(clave_repetida) < longitud:
        for i in msg:
            if i == " ":
                clave_repetida.append(" ")
            x = i.isalpha()
            if x == False:
                continue
            else:
                contador += 1
                if contador >= len(clave):
                    contador = 0
                clave_repetida.append(clave[contador])
    diccionario = {
        "a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25
    }
    clave_final = []
    clave_repetida = "".join(clave_repetida)
    msg = msg.lower()
    for m,j in (msg,clave_repetida):
        num = diccionario[m]+diccionario[j]
        clave_final.append(diccionario[num])
    return clave_repetida
print(cifrado("Este es un mensaje super secreto","clavesecreta"))
print("Este es un mensaje super secreto")

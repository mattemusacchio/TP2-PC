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
    clave_final = []
    clave_repetida = "".join(clave_repetida)
    msg = msg.lower()
    contador = -1
    for m in msg:
        contador += 1
        if m == " ":
            valor = " "
        else:
            j = clave_repetida[contador]
            num = ord(m) + ord(j)
            valor = chr(num)
        clave_final.append(valor)
    clave_final = "".join(clave_final)
    return clave_final
print(cifrado("Este es un mensaje super secreto","clavesecreta"))

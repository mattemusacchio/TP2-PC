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
                longitud = longitud - 1
                continue
            else:
                contador += 1
                if contador >= len(clave):
                    contador = 0
                clave_repetida.append(clave[contador])
    diccionario = {
        "a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25
    }
    diccionario2 = {
        0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z",26:"a",27:"b",28:"c",29:"d",30:"e",31:"f",32:"g",33:"h",34:"i",35:"j",36:"k",37:"l",38:"m",39:"n",40:"o",41:"p",42:"q",43:"r",44:"s",45:"t",46:"u",47:"v",48:"w",49:"x",50:"y",51:"z"
    }
    clave_final = []
    clave_repetida = "".join(clave_repetida)
    msg = msg.lower()
    contador = -1
    for m in msg:
        if m == " ":
            valor = " "
            contador += 1
        if m.isalpha() == False:
            valor = m
        else:
            contador += 1
            j = clave_repetida[contador]
            num = diccionario[m]+diccionario[j]
            valor = diccionario2[num]
        clave_final.append(valor)
    clave_final = "".join(clave_final)
    return clave_final
print(cifrado("Este es un mensaje super secreto.","clavesecreta"))

def grupos(fn,k):
    f = open(fn,"r")
    texto = f.read()
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
        try:
            grupo.append(texto[i])
        except:
            grupo.append("0")
        count = i
        while contador < (len(texto)/k):
            contador += 1
            count = count + (k)
            if count >= len(texto):
                continue
            elif texto[count].isalpha() == False:
                continue
            else:
                grupo.append(texto[count])
    lista.append(grupo)
    lista.remove("")
    return lista
def getMedium(text):
    everyLetter = list(map(chr, range(97, 123)))
    countLetter = {}
    top = 0
    amount = 0
    for letra in text:
     if letra in countLetter:
        countLetter[letra] += 1
     else: 
       countLetter[letra] = 1
    for letrasEncontradas in countLetter:
       amount += countLetter[letrasEncontradas]
       top += countLetter[letrasEncontradas] * (countLetter[letrasEncontradas] - 1)
    try:
      return(top / (amount * (amount - 1)))
    except:
       return 0
def valores():
   ratiofinal = []
   for k in range(1,31):
      i = grupos("plain.txt",k)
      ratio = []
      for j in i:
         ratio.append(getMedium(j))
      ratiofinal.append(sum(ratio)/len(ratio))
   diccionario = {}
   contador = 0
   for i in ratiofinal:
      contador += 1
      diccionario[contador] = i
   return diccionario



ratio  = (getMedium("esnsst") + getMedium("susueo") + getMedium("tnapc") + getMedium("emjer") + getMedium("eeere")) / 5



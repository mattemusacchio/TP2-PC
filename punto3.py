import numpy as np
import matplotlib.pyplot as plt

archivo = input("Ingrese nombre del archivo: ")
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

def getIoC(text):
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
      i = grupos(archivo,k)
      ratio = []
      for j in i:
         ratio.append(getIoC(j))
      ratiofinal.append(sum(ratio)/len(ratio))
   diccionario = {}
   contador = 0
   for i in ratiofinal:
      contador += 1
      diccionario[contador] = i
   return diccionario

def frecuencia(grupo):
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

def grafico(data,title,xlabel,ylabel):
    # creating the dataset
    courses = list(data.keys())
    values = list(data.values())
    
    fig = plt.figure(figsize = (10, 5))

    # creating the bar plot
    plt.bar(courses, values, color ='steelblue',
            width = 0.8)
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

###########################################################

# 1. Dividir el texto en grupos
valor_de_k = int(input("Ingrese valor de k: "))
print(grupos(archivo,valor_de_k))

# 2. Calcular el IoC de cada uno de estos grupos
resultados = []
for i in grupos(archivo,valor_de_k):
   resultados.append(getIoC(i))
print(resultados)

# 3. Promediar estos resultados.
promedio = sum(resultados)/len(resultados)
print(promedio)

# Gráfico de barras del IoC en función del posible largo de la clave, para longitudes de entre 1 y 30.
grafico(valores(),"IoC en función del posible largo de la clave","Largo de la clave","Indice de coincidencia")

#La frecuencia de las letras en el idioma inglés.
ENGLISH_LETTERS_FRECUENCIES = {
    "a": 0.08167, "b": 0.01492, "c": 0.02782, "d": 0.04253, "e": 0.12702, "f": 0.02228,
    "g": 0.02015, "h": 0.06094, "i": 0.06966, "j": 0.00153, "k": 0.00772, "l": 0.04025,
    "m": 0.02406, "n": 0.06749, "o": 0.07507, "p": 0.01929, "q": 0.00095, "r": 0.05987,
    "s": 0.06327, "t": 0.09056, "u": 0.02758, "v": 0.00978, "w": 0.02360, "x": 0.00150,
    "y": 0.01974, "z": 0.00075
}
grafico(ENGLISH_LETTERS_FRECUENCIES,"Inglés","","Frecuencia")

#La frecuencia de las letras que están en las posiciones 0, 5, 10, 15 … del mensaje en encrypted.txt.
m = 0
contador = 0
for i in grupos(archivo,5):
    m += 1
    count = -1
    diccionario = {
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0,  "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
    }
    contador += 1
    ioc = frecuencia(i)
    for item in i:
        count += 1
        diccionario[item] = ioc[count]
    grafico(diccionario,f"Letra {m} de la clave","","Frecuencia")
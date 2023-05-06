import numpy as np
import matplotlib.pyplot as plt

archivo = input("Ingrese nombre del archivo: ")
def DivideText(f, length):
    text = open(f,"r",encoding='utf-8')
    text = text.read()
    textDivided = []
    count = 0
    newText = text.casefold()
    for i in range(0, length):
        textDivided.append([])
    for letter in newText:
       if(letter.isalpha()):
        textDivided[count].append(letter)
        if(length -1 == count):
            count = 0
        else:
            count += 1
    return textDivided

def getIoC(List):
    countLetter = {}
    top = 0
    amount = 0
   
    for letra in List:
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
    diccionario = {}
    for k in range(1,31):
        resultados = []
        for i in DivideText(archivo,k):
            resultados.append(getIoC(i))
        promedio = sum(resultados)/len(resultados)
        diccionario[k] = promedio
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

    ypoints = np.array([0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385,0.0385])
    plt.plot(ypoints, linestyle = "dashed", color="black")
    ypoints = np.array([0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686,0.0686])
    plt.plot(ypoints, linestyle = "dashed", color="black")

    plt.show()

def graficos():
    fig = plt.figure(figsize = (16,9))

    ENGLISH_LETTERS_FRECUENCIES = {
    "a": 0.08167, "b": 0.01492, "c": 0.02782, "d": 0.04253, "e": 0.12702, "f": 0.02228,
    "g": 0.02015, "h": 0.06094, "i": 0.06966, "j": 0.00153, "k": 0.00772, "l": 0.04025,
    "m": 0.02406, "n": 0.06749, "o": 0.07507, "p": 0.01929, "q": 0.00095, "r": 0.05987,
    "s": 0.06327, "t": 0.09056, "u": 0.02758, "v": 0.00978, "w": 0.02360, "x": 0.00150,
    "y": 0.01974, "z": 0.00075
}
    x = np.array(list(ENGLISH_LETTERS_FRECUENCIES.keys()))
    y = np.array(list(ENGLISH_LETTERS_FRECUENCIES.values()))

    plt.subplot(2, 3, 1)
    plt.bar(x, y, color ='steelblue', width = 0.8)
    plt.title("Inglés")
    plt.ylabel("Frecuencia")

    x = np.array([0, 1, 2, 3])
    y = np.array([10, 20, 30, 40])

    m = 0
    contador = 0
    for i in DivideText(archivo,5):
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
        x = np.array(list(diccionario.keys()))
        y = np.array(list(diccionario.values()))
        plt.subplot(2,3,m+1)
        plt.bar(x, y, color ='steelblue', width = 0.8)  
        plt.title(f"Letra {m} de la clave")
        plt.ylabel("Frecuencia")
    plt.show()

###########################################################

# 1. Dividir el texto en DivideText
valor_de_k = int(input("Ingrese valor de k: "))
print(DivideText(archivo,valor_de_k))

# 2. Calcular el IoC de cada uno de estos DivideText
resultados = []
for i in DivideText(archivo,valor_de_k):
   resultados.append(getIoC(i))
print(resultados)

# 3. Promediar estos resultados.
promedio = sum(resultados)/len(resultados)
print(promedio)

# Gráfico de barras del IoC en función del posible largo de la clave, para longitudes de entre 1 y 30.
grafico(valores(),"IoC en función del posible largo de la clave","Largo de la clave","Indice de coincidencia")

# Genere una figura que contenga 6 gráficos
graficos()
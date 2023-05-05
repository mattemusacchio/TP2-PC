import numpy as np
import matplotlib.pyplot as plt
from TestNew_3 import valores,grupos,getMedium
from frecuencia_letras import indice_de_coincidencia
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

#IoC en función del posible largo de la clave, para longitudes de entre 1 y 30.
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
print(grupos("encrypted.txt",5))
m = 0
contador = 0
for i in grupos("encrypted.txt",5):
    m += 1
    count = -1
    diccionario = {
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0,  "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
    }
    contador += 1
    ioc = indice_de_coincidencia("encrypted.txt",i)
    for item in i:
        count += 1
        diccionario[item] = ioc[count]
    print(ioc)
    grafico(diccionario,f"Letra {m} de la clave","","Frecuencia")

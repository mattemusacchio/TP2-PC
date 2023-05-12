import numpy as np
import matplotlib.pyplot as plt

# Tomamos informacion del usuario, para saber que texto encriptado hay que analizar.
archivo = input("Ingrese nombre del archivo encriptado: ")
def DivideText(f:str, length:int) -> list:
    """ Devuelve una lista de listas de: el texto encriptado dividido en distintos grupos de letras, separadas por (length - 1) letras entre sí.

    Toma como argumentos:
    f = file name, nombre del archivo encriptado. (str) 
    length = k, longitud de la clave a analizar (int)
    """
    valuesPerLetter = list(map(chr, range(97, 123))) * 2
    text = open(f,"r",encoding='utf-8')
    text = text.read()
    textDivided = []
    count = 0
    newText = text.casefold()
    for i in range(0, length):
        textDivided.append([])
    for letter in newText:
       if letter in valuesPerLetter:
        textDivided[count].append(letter)
        if(length -1 == count):
            count = 0
        else:
            count += 1
    return textDivided

def getIoC(grupo:list) -> float:
    """ Devuelve el Indice de Coincidencia de un determinado grupo de letras.

    Toma como argumentos:
    grupo = grupo de letras (list) 
    """
    countLetter = {}
    top = 0
    amount = 0
   
    for letra in grupo:
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
    """ Calcula el promedio usando el IoC en función del posible largo de la clave, para longitudes de entre 1 y 30.
    """
    diccionario = {}
    for k in range(1,61):
        resultados = []
        for i in DivideText(archivo,k):
            resultados.append(getIoC(i))
        promedio = sum(resultados)/len(resultados)
        diccionario[k] = promedio
    return diccionario    
    
           

def frecuencia(grupo:list) -> list:
    """ Devuelve una lista con la frecuencia de cada letra en un respectivo grupo de letras.

    Toma como argumentos:
    grupo = grupo de letras (list) 
    """
    grupo = "".join(grupo)
    indices = []
    frequency = ""
    for letra in grupo:
        indices.append(frequency)
        rep = grupo.count(letra)
        frequency = (rep/len(grupo))
    indices.append(frequency)
    indices.remove("")
    return indices

def longitud_de_clave(diccionario):
    """ Devuelve la longitud de la clave
    
    Toma como argumento:
    diccionario = diccionario con el promedio usando el IoC en función del posible largo de la clave para las longitudes entre 1 y 30 (dict)
    """
    longitud = 1
    for i in diccionario.values():
        # tomamos cualquier punto mas grande que 0.062 como el primer pico de la funcion, es decir la longitud de la clave.
        if i > 0.062:
            return longitud
        longitud += 1

def grafico(data,title,xlabel,ylabel):
    """ Genera un gráfico de barras del IoC en función del posible largo de la clave, para longitudes de entre 1 y 30 con una linea horizontal en 6.86% y otra en 3.85%

    Toma como argumentos:
    data = diccionario con la informacion a graficar (dict)
    title = titulo para el grafico (str)
    xlabel = titulo para el eje x del grafico (str)
    ylabel = titulo para el eje y del grafico (str)
    """

    # crea el dataset usando la informacion de el diccionario data
    x = list(data.keys())
    y = list(data.values())
    
    fig = plt.figure(figsize = (10, 5))

    # crea el grafico de barras
    plt.bar(x, y, color ='steelblue',
            width = 0.8)
    
    # asigna los titulos respectivos
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    # grafica las lineas horizontales en 6.86 % y 3.85%
    plt.axhline(y=0.0686,color="black", linestyle="dashed")
    plt.axhline(y=0.0385,color="black", linestyle="dashed")

    # muestra el resultado (grafico de barras)
    plt.show()

def graficos(fig,data,k):
    """ Genera graficos de barras

    Toma como argumentos:
    fig = comando para programar el grafico.
    data = diccionario con la informacion a graficar (dict).
    k = longitud de la clave. (int)
    """

    # Formulamos el tamaño de la grilla en funcion del largo de la clave. Para que la grilla tenga el tamaño mas adecuado posible
    grilla = 0
    filas = 1
    columnas = 1
    while grilla < (k+1):
        if filas == columnas:
            filas += 1
        else:
            columnas += 1
        grilla = filas*columnas
    
    # Tomamos informacion del diccionario data para poder graficar.
    x = np.array(list(data.keys()))
    y = np.array(list(data.values()))

    # Programamos los graficos como subplots, usando la grilla que calculamos anteriormente para que aparezcan todos en la misma ventana y asignamos los titulos y cada grafico de barras.
    plt.subplot(filas, columnas, 1)
    plt.bar(x, y, color ='steelblue', width = 0.8)
    plt.title("Inglés")
    plt.ylabel("Frecuencia")

    # A continuación vamos a usar un for loop para programar cada grafico del subplot
    clave = []
    m = 0
    contador = 0

    # el for itera sobre cada grupo de letras, usando la funcion DivideText.
    for i in DivideText(archivo,k):
        valuesPerLetter = list(map(chr, range(97, 123))) * 2
        m += 1
        count = -1
        diccionario = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0,  "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
        }
        contador += 1

        # usando la funcion frecuencia, calculamos la frecuencia de cada letra del grupo i
        freq = frecuencia(i)

        # con la informacion de freq, asignamos la frecuencia por letra a un diccionario
        for item in i:
            if item in valuesPerLetter:
                count += 1
                diccionario[item] = freq[count]
            else:
                continue
        # este diccionario es el que usaremos para tomar la informacion a usar el grafico

        # buscamos el valor maximo en el diccionario, es decir el valor con mas frecuencia, el cual PROBABLEMENTE sea la "e", ya que sabemos que es la letra en ingles con mas frecuencia en general.
        values = list(diccionario.values())
        maximo = values.index(max(diccionario.values()))

        # Sabiendo que el maximo PROBABLEMENTE sea "e" desplazado x lugares por la encriptacion, podemos restarle 4 al valor de "e" (porque la "a" esta a 4 lugares de la "e"), lo cual nos dejaría con el valor de la letra en ese lugar de la clave. Todo esto asumiendo que el caracter que mas se repite es la "e"
        letra = valuesPerLetter[maximo-4]
        clave.append(letra)

        # y utilizando el diccionario que conseguimos mostrando la frecuencia de cada letra, aplicamos esta informacion al grafico.
        x = np.array(list(diccionario.keys()))
        y = np.array(list(diccionario.values()))
        plt.subplot(filas,columnas,m+1)
        barlist = plt.bar(x, y, color ='steelblue', width = 0.8)  
        barlist[maximo-4].set_color("g")
        plt.title(f"Letra {m} de la clave")
        plt.ylabel("Frecuencia")
        fig.tight_layout(pad=1.0)
        
        # una vez que encontramos la letra en esa posicion de la clave, la printeamos.
        print(f"--> {letra}")

    # mostramos la posible clave de la encriptación al usuario.
    clave = "".join(clave)
    print(clave)
    plt.show()

    # la cual si el usuario considera que no es correcta, se puede utilizar un algoritmo que busca mas coincidencias que el anterior para intentar optimizarlo a una clave mas cercana a la correcta.
    optimizar = int(input("""Desea optimizar la clave?
    1. Si 
    0. No 
    """))

    # si se desea optimizar
    if optimizar == 1:
            clave = []
            m = 0
            contador = 0
            # se usa el mismo loop que antes
            for i in DivideText(archivo,k):
                valuesPerLetter = list(map(chr, range(97, 123))) * 2
                m += 1
                count = -1
                diccionario = {
                "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0,  "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
                }
                contador += 1
                freq = frecuencia(i)
                for item in i:
                    if item in valuesPerLetter:
                        count += 1
                        diccionario[item] = freq[count]
                    else:
                        continue
                values = list(diccionario.values())

                # aca es donde cambia el algoritmo, que en vez de buscar el punto maximo asumiendo que es la letra "e", se asegura de que ese punto que elegimos sea la "e", es decir. Si encuentra un maximo, pero el valor minimo no se encuentra a una distancia de 5,6,12,19 o 21, NO considera ese punto maximo como la "e". Esto es porque no sabemos cual es el punto maximo ni el minimo, pero sabemos que la "e" tiende a ser el maximo, y pusimos 5 candidatos a ser el minimo, "j","k","v","x","z", que estan a distancias 5,6,9,12,19,21 de la "e". Entonces si encontramos un maximo, pero el minimo no se encuentra a esta distancia, podemos deducir que este maximo, no es la "e", y pasamos a probar el proximo maximo y probar el mismo algoritmo, hasta encontrar un maximo que tenga a esta distancia el minimo, y si tenemos suerte ese maximo es la letra "e". y usando el mismo algoritmo de antes de restarle 4, deberiamos sacar la letra correspondiente a la clave.
                while True:
                    maximo = values.index(max(values))
                    if values[maximo-4] > values[maximo-3] and values[maximo-4] > values[maximo-2] and values[maximo-4] > values[maximo-1] and values[maximo-4] < values[maximo] and values[maximo-5] < values[maximo-6]:
                        letra = valuesPerLetter[maximo-4]
                        clave.append(letra)
                        print(f"--> {letra}")
                        # y utilizando el diccionario que conseguimos mostrando la frecuencia de cada letra, aplicamos esta informacion al grafico.
                        x = np.array(list(diccionario.keys()))
                        y = np.array(list(diccionario.values()))
                        plt.subplot(filas,columnas,m+1)
                        barlist = plt.bar(x, y, color ='steelblue', width = 0.8)  
                        barlist[maximo-4].set_color("g")
                        plt.title(f"Letra {m} de la clave")
                        plt.ylabel("Frecuencia")
                        fig.tight_layout(pad=1.0)
                        break
                    elif values[maximo] == 0:
                        values = list(diccionario.values())
                        maximo = values.index(max(values))
                        letra = valuesPerLetter[maximo-4]
                        clave.append(letra)
                        print(f"--> {letra}")
                        x = np.array(list(diccionario.keys()))
                        y = np.array(list(diccionario.values()))
                        plt.subplot(filas,columnas,m+1)
                        barlist = plt.bar(x, y, color ='steelblue', width = 0.8)  
                        barlist[maximo-4].set_color("g")
                        plt.title(f"Letra {m} de la clave")
                        plt.ylabel("Frecuencia")
                        fig.tight_layout(pad=1.0)
                        break
                    else:
                        values[maximo] = 0
                        continue
    plt.show()
    
    # mostrar la clave
    clave = "".join(clave)
    return f"Clave ---> {clave}"

###########################################################

# 1. Dividir el texto en grupos
valor_de_k = int(input("Ingrese valor de k: "))
DivideText(archivo,valor_de_k)

# 2. Calcular el IoC de cada uno de estos grupos
resultados = []
for i in DivideText(archivo,valor_de_k):
   resultados.append(getIoC(i))
#print(resultados)

# 3. Promediar estos resultados.
promedio = sum(resultados)/len(resultados)
#print(promedio)

# Gráfico de barras del IoC en función del posible largo de la clave, para longitudes de entre 1 y 30.
grafico(valores(),"IoC en función del posible largo de la clave","Largo de la clave","Indice de coincidencia")

# Genere una figura que contenga 6 gráficos

ENGLISH_LETTERS_FRECUENCIES = {
    "a": 0.08167, "b": 0.01492, "c": 0.02782, "d": 0.04253, "e": 0.12702, "f": 0.02228,
    "g": 0.02015, "h": 0.06094, "i": 0.06966, "j": 0.00153, "k": 0.00772, "l": 0.04025,
    "m": 0.02406, "n": 0.06749, "o": 0.07507, "p": 0.01929, "q": 0.00095, "r": 0.05987,
    "s": 0.06327, "t": 0.09056, "u": 0.02758, "v": 0.00978, "w": 0.02360, "x": 0.00150,
    "y": 0.01974, "z": 0.00075
}

#graficos(plt.figure(figsize = (12,6)),ENGLISH_LETTERS_FRECUENCIES,5)

print("---------------")

print(graficos(plt.figure(figsize = (12,6)),ENGLISH_LETTERS_FRECUENCIES,longitud_de_clave(valores())))

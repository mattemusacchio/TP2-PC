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
    valuesPerLetter = list(map(chr, range(97, 123))) * 2 # Usando chr() se obtiene el abecedario y se multiplica por 2 para no tener problemas a la hora de sumar diferentes letras.
    text = open(f,"r",encoding='utf-8')
    text = text.read() # Se lee el archivo 
    textDivided = []
    count = 0
    newText = text.casefold()
    # Se inicia un loop del largo de la clave
    for i in range(0, length):
        textDivided.append([])
         # Generar un la cantidad necesaria de [] vacios. Se genera un loop del
         # largo de la clave y se separa el texto en cada []

    # Se inicia un loop del texto y se va
    for letter in newText:
       if letter in valuesPerLetter:
        # Pushear cada letra del texto en un index de la lista, basado en que
        # index de la letra esta el contador.
        textDivided[count].append(letter)
        if(length -1 == count):
            count = 0
            # Chequear si el largo de la clave - 1 es igual al contador, en caso
            # que sea asi, resetear el contador.

        else:
            count += 1
    return textDivided

def getIoC(grupo:list) -> float:
    """ Devuelve el Indice de Coincidencia de un determinado grupo de letras.

    Toma como argumentos:
    grupo = grupo de letras (list) 
    """
    countLetter = {} # Declarar un diccionario vacio
    top = 0
    amount = 0
    
    # Rellenar el diccionario por cada letra en el grupo pasado como pametro.
    for letra in grupo:
         # Si la letra ya se encuentra en el diccionario agregar 1, en caso
         # contrario, declararlo con valor inicial 1.
         if letra in countLetter:
          countLetter[letra] += 1
         else: 
             countLetter[letra] = 1

    # Hacer un loop en cada letra encontrada y finalmente calcular el IoC 
    for letrasEncontradas in countLetter:
          amount += countLetter[letrasEncontradas] # La cantidad de veces que aparece una letra
          top += countLetter[letrasEncontradas] * (countLetter[letrasEncontradas] - 1) # Se le suma a la variable top += n * (n - 1)
    try:
        return(top / (amount * (amount - 1))) # Finalmente se calcula la suma de todos las letras calculadas como n(n - 1) dividido por la formula del denominador.
    except:
        return 0
def valores():
    """ Calcula el promedio usando el IoC en función del posible largo de la clave, para longitudes de entre 1 y 30.
    """
    diccionario = {} # Se declara un diccionario vacio.

    # Se genera un loop 30 veces y se calcula el IoC en diferentes largos de
    # clave (Rango de longitud entre 1 - 30)
    for k in range(1,31):
        resultados = []
        # Posteriormente se vuelve a
        # generar un loop dentro del anterior pero esta vez es sobre cada lista
        # del texto dividido.
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
    grupo = "".join(grupo) # Juntamos todas las letras en un texto
    indices = []  # Declaramos el indice para luego pushear 
    frequency = "" 
    # Se genera un loop en cada letra, se calcula el indice de frecuencia de la misma y posteriormente se pushea a indices.
    for letra in grupo:
        rep = grupo.count(letra)
        frequency = (rep/len(grupo)) 
        indices.append(frequency)

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
            return longitud # Si encuentra el valor, devuelve la longitud de la clave
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

def graficos(size_x,size_y,data,k):
    """ Genera graficos de barras y calcula la clave del texto encriptado.

    Toma como argumentos:
    size_x = tamaño en eje x de la ventana de los graficos
    size_y = tamaño en eje y de la ventana de los graficos
    data = diccionario con la informacion a graficar (dict).
    k = longitud de la clave. (int)
    """

    fig = plt.figure(figsize = (size_x,size_y))
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

        # usamos este diccionario vacio para agregar las frecuencias de cada letra del grupo.
        diccionario = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0,  "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
        }
        contador += 1

        # usando la funcion frecuencia, calculamos la frecuencia de cada letra del grupo i
        freq = frecuencia(i)

        # con la informacion de freq, asignamos la frecuencia por letra al diccionario. Este diccionario es el que usaremos para tomar la informacion a usar el grafico
        for item in i:
            if item in valuesPerLetter:
                count += 1
                diccionario[item] = freq[count]
            else:
                continue

        # tomamos los valores de este diccionario
        values = list(diccionario.values())

        # usamos el siguiente algoritmo para encontrar cada letra de la clave.
        while True:
                    maximo = values.index(max(values)) # Buscamos el valor maximo siguiendo los patrones de frecuencia de letras en ingles, entendemos que el mas propenso a ser el maximo es la "e", pero para confirmar eso usamos el siguiente if.

                    if values[maximo-4] > values[maximo-3] and values[maximo-4] > values[maximo-2] and values[maximo-4] > values[maximo-1] and values[maximo-4] < values[maximo] and values[maximo-5] < values[maximo-6]:
                    # asumiendo que el maximo es la "e", el maximo - 4 sería la "a" pero movida hasta la letra que buscamos. Para confirmar que el maximo es la "e", nos fijamos en los patrones de los graficos, y nos damos cuenta que la "a" siempre es mas grande que los 3 que estan a su derecha ([maximo - 4] > [maximo - 3 , -2 y -1]) pero tambien sabemos que el valor de "a" sea menor que el de "e" ([maximo - 4] < [maximo]) y tambien si el maximo - 4 es la "a", el maximo - 5 deberia ser la "z", por lo que nos fijamos que la "z" < "y" ([maximo-5] < [maximo-6]). Con estos algoritmos, nos dariamos cuenta que el pico que nos dio, es verdaderamente nuestra "e" y no otro punto que de casualidad es mas alto. Por lo que maximo - 4, nos daria la supuesta "a" que en realidad es esa letra escondida que buscamos para nuestra clave.

                        # buscamos esa "a" que ahora va a ser otra letra, y la sumamos a la clave.
                        letra = valuesPerLetter[maximo-4]
                        clave.append(letra)
                        print(f"--> {letra}") # vamos mostrando cada letra de la clave.

                        # y utilizando el diccionario que conseguimos mostrando la frecuencia de cada letra, aplicamos esta informacion al grafico. El cual nos ayuda a entender mejor todavía el proceso de encontrar la letra de la clave.
                        x = np.array(list(diccionario.keys()))
                        y = np.array(list(diccionario.values()))
                        plt.subplot(filas,columnas,m+1)
                        barlist = plt.bar(x, y, color ='steelblue', width = 0.8)

                        # marcamos la "a" de otro color
                        barlist[maximo-4].set_color("mediumseagreen")

                        # titulos y  espaciado
                        plt.title(f"Letra {m} de la clave")
                        plt.ylabel("Frecuencia")
                        fig.tight_layout(pad=0.75)
                        break

                    # en caso de que el algoritmo anterior no funcione, es decir que haya una medida imprevista en la cual no se cumpla el patron. Y en caso de que tampoco encuentre ninguna letra que cumpla ese patron, para que no se quede buscando para siempre una letra que no va a encontrar, le asignamos que simplemente tome el valor maximo, como la "e" y prosiga. En caso de entrar a este if, la letra posiblemente sea erronea, pero es solo para prevenir que se quede buscando para siempre en el if de arriba. 
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
                        barlist[maximo-4].set_color("mediumseagreen")
                        plt.title(f"Letra {m} de la clave")
                        plt.ylabel("Frecuencia")
                        fig.tight_layout(pad=0.75)
                        break

                    # si encuentra un valor maximo que no cumple las condiciones del primer if, le asignamos que ese valor pase a ser 0 para que vuelva y pruebe con el proximo maximo. 
                    else:
                        # asignar este valor a 0 no cambia nada el valor del grafico, porque esta cambiando la informacion de la lista con los valores, no del diccionario en si.
                        values[maximo] = 0
                        continue

    # mostramos la posible clave de la encriptación al usuario y mostramos el grafico.
    clave = "".join(clave)
    plt.show()
    return f"Clave ---> {clave}"

###########################################################
"""
# 1. Dividir el texto en grupos
valor_de_k = int(input("Ingrese valor de k: "))
DivideText(archivo,valor_de_k)

# 2. Calcular el IoC de cada uno de estos grupos
resultados = []
for i in DivideText(archivo,valor_de_k):
   resultados.append(getIoC(i))
print(resultados)

# 3. Promediar estos resultados.
promedio = sum(resultados)/len(resultados)
print(promedio)
"""

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

# corremos la funcion graficos
print(graficos(12,6,ENGLISH_LETTERS_FRECUENCIES,longitud_de_clave(valores())))

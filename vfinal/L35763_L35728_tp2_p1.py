def cifrado(msg:str, clave:str) -> str:
  """ Convierte un mensaje desencriptado en un mensaje encriptado.

  Toma como argumentos:
  msg: el texto desencriptado (str)
  clave: la clave que se quiere usar para encriptar el texto (str)
  """

  # ValuesPerLetter es una lista de la A a la Z * 2, osea una lista con rango 0 - 51 que en 0 vale a, en 25 vale z, en 26 vale a y en 51 vale z. Esto es para evitar problemas cuando sumamos los valores de las letras
  valuesPerLetter = list(map(chr, range(97, 123))) * 2
  
  # usamos encryptedValue como una lista para almacenar cada letra encryptada
  encryptedValue = []
  indexEncrypted = 0
  
  # Convertimos todo el texto en minuscula
  newClave = clave.casefold()
  newMensaje = msg.casefold()

  # loop para asginar cada letra encriptada al nuevo texto encriptado
  for letter in newMensaje:
     
     # si ord(letter) se encuentra entre la A y la Z, le asignamos a encryptedValue la letra encriptada, usando la formula de Xi + Ki 
     # Siendo Xi el número correspondiente a la i-ésima letra del mensaje, y  Ki el número correspondiente a la i-ésima letra de la clave
     if(ord(letter) in range(97,123)):
       encryptedValue.append(valuesPerLetter[(ord(letter) - ord("a")) + (ord(newClave[indexEncrypted]) - ord("a"))])
       if(len(newClave) - 1 == indexEncrypted):
        indexEncrypted = 0
       else: 
        indexEncrypted += 1

    # Si la letra no se encuentra entre la A y la Z, la asignamos asi como esta a encryptedValue, es decir que caracteres especiales permanecen como estaban.    
     else: 
      encryptedValue.append(letter)

# transformamos la lista en un string, y ya tendríamos el texto encriptado listo.
  result = "".join(encryptedValue)
  return result

# tomamos datos del usuario
print("≡≡Encriptador de Cifrado de Vigenère≡≡")
filename = input("Ingrese nombre del archivo en texto plano: ")
key = input("Ingrese la clave: ")
encryptedfile = input("Ingrese nombre del archivo para la encripción: ")

# usamos este while para verificar que el archivo exista
f = 0
while f == 0:
  try:
    f = open(filename,"r", encoding='utf-8')
  except:
    print("Archivo Inexistente, por favor ingrese de nuevo.")
    filename = input("Ingrese nombre del archivo en texto plano: ")

# usamos la variable mensaje para almacenar el texto del archivo como un string
mensaje = f.read()

# usamos este ciclo para verificar que el archivo de texto no se ecuentre vacio
vacio = True
while vacio == True:
  for i in mensaje:
    # vamos probando letra por letra hasta encontrar alguna letra alfanumerica
    if i.isalpha() == True:
      vacio = False
      break
  
  # si en este punto el ciclo no se freno, significa que el archivo esta vacio, entonces le pedimos al usuario que ingrese otra vez
  if mensaje == "" or vacio == True:
    print("El archivo de texto plano se encuentra vacio o no contiene caracteres legibles. Por favor ingrese el nombre del archivo de nuevo")
    filename = input("Ingrese nombre del archivo en texto plano: ")
    f = open(filename,"r", encoding='utf-8')
    mensaje = f.read()
  else:
    vacio = False

# usamos este while para verificar que la clave no contenga numeros o caracteres especiales, ademas de transformarla en minuscula.
caracterfalso = False
while caracterfalso == False:
  caracterfalso = True
  key = key.casefold()
  valuesPerLetter = list(map(chr, range(97, 123)))
  for i in key:
    if i in valuesPerLetter:
      continue
    else:
      print("La clave no puede contener caracteres especiales o numeros. Por favor ingrese de nuevo la clave. ")
      key = input("Ingrese la clave: ")
      caracterfalso = False
      break

# usamos la funcion cifrado para encriptarlo
f.close()
mensaje_cifrado = cifrado(mensaje,key)

# almacenamos el texto cifrado en un archivo dictado por el usuario.
file = open(encryptedfile,"w", encoding='utf-8')
file.write(mensaje_cifrado)
file.close()
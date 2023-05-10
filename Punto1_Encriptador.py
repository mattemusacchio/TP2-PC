def cifrado(msg:str, clave:str):
  """
  cifrado toma un mensaje y una clave, y convierte el mensaje en un mensaje encriptado, utilizando la clave dada.
  """
  valuesPerLetter = list(map(chr, range(97, 123))) * 2 
  encryptedValue = []
  indexEncrypted = 0
  newClave = clave.casefold()
  newMensaje = msg.casefold()
  for letter in newMensaje:
     if(ord(letter) in range(97,123)):
       encryptedValue.append(valuesPerLetter[(ord(letter) - ord("a")) + (ord(newClave[indexEncrypted]) - ord("a"))])
       if(len(newClave) - 1 == indexEncrypted):
        indexEncrypted = 0
       else: 
        indexEncrypted += 1
     else: 
      encryptedValue.append(letter)

  result = "".join(encryptedValue)
  return result

print("≡≡Encriptador de Cifrado de Vigenère≡≡")
filename = input("Ingrese nombre del archivo en texto plano: ")
key = input("Ingrese la clave: ")
encryptedfile = input("Ingrese nombre del archivo para la encripción: ")
try:
  f = open(filename,"r", encoding='utf-8')
except:
  exit("Archivo inexistente")
mensaje = f.read()
f.close()
mensaje_cifrado = cifrado(mensaje,key)
file = open(encryptedfile,"w", encoding='utf-8')
file.write(mensaje_cifrado)
file.close()
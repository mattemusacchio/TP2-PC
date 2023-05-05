def decifrado(msg, clave):
  valuesPerLetter = list(map(chr, range(97, 123))) * 2
  encryptedValue = []
  indexEncrypted = 0
  newClave = clave.casefold()
  newMensaje = msg.casefold()
  for letter in newMensaje:
     if(ord(letter) in range(97,123)):
       encryptedValue.append(valuesPerLetter[(ord(letter) - ord("a")) - (ord(newClave[indexEncrypted]) - ord("a"))])
       if(len(newClave) - 1 == indexEncrypted):
        indexEncrypted = 0
       else: 
        indexEncrypted += 1
     else: 
      encryptedValue.append(letter)

  result = "".join(encryptedValue)
  return result
print("≡≡Desencriptador de Cifrado de Vigenère≡≡")
filename = input("Ingrese nombre del archivo encriptado: ")
key = input("Ingrese la clave: ")
encryptedfile = input("Ingrese nombre del archivo para la desencripción: ")
f = open(filename,"r")
mensaje = f.read()
f.close()
mensaje_cifrado = decifrado(mensaje,key)
file = open(encryptedfile,"w")
file.write(mensaje_cifrado)
file.close()
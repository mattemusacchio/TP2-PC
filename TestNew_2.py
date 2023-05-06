def Descifrar(msg, clave):
  valuesPerLetter = list(map(chr, range(97, 123))) * 2
  encryptedValue = []
  indexEncrypted = 0
  newClave = clave.casefold()
  newMensaje = msg.casefold()
  for letter in newMensaje:
     if(letter.isalpha()):
       encryptedValue.append(valuesPerLetter[(ord(letter) - ord("a")) - (ord(newClave[indexEncrypted]) - ord("a"))])
       if(len(newClave) - 1 == indexEncrypted):
        indexEncrypted = 0
       else: 
        indexEncrypted += 1
     else: 
      encryptedValue.append(" ")

  result = "".join(encryptedValue)
  print(result)    


Descifrar("gdtz ik yp digscue nyhit jivrgeo", "clavesecreta")
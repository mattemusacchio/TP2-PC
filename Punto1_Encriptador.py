"""Se debe escribir un programa que le pida al usuario el path a un archivo en texto plano, por ejemplo plain.txt y, con una clave solicitada al usuario, encripte el texto mediante cifrado de Vigenère y lo guarde en un nuevo archivo elegido por el usuario, por ejemplo encrypted.txt. Todos los caracteres especiales y números deben quedar como estaban en el texto plano. Las mayúsculas deben convertirse en minúsculas antes de encriptar, el texto encriptado estará entonces todo en minúscula. En este caso encriptaremos sólo las 26 letras del alfabeto inglés. El programa no debe fallar catastróficamente ante entradas insperadas del usuario, archivos vacíos o inexistentes, etc."""
from CifradoVigenere import cifrado

print("≡≡Encriptador de Cifrado de Vigenère≡≡")
filename = input("Ingrese nombre del archivo en texto plano: ")
key = input("Ingrese la clave: ")
encryptedfile = input("Ingrese nombre del archivo para la encripción: ")
f = open(filename,"r")
mensaje = f.read()
f.close()
mensaje_cifrado = cifrado(mensaje,key)
file = open(encryptedfile,"w")
file.write(mensaje_cifrado)
file.close()
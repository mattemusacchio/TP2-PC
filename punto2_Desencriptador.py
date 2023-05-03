"""Se debe escribir un programa que le pida al usuario el path al archivo encriptado, por ejemplo llamado encrypted.txt, le solicite al usuario una clave y luego desencripte el texto con Cifrado de Vigenère y lo guarde en un nuevo archivo elegido por el usuario, por ejemplo llamado decrypted.txt."""
from decifradorVigenere import decifrado

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
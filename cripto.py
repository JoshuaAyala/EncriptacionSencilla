#!/usr/bin/python
#coding: utf-8

# Filename  : PyMath.py
# Autor     : Joshua Ayala
# Website   : https://github.com/JoshuaAyala/PyMath
# pep8: 100%

#-----importaciones-----
import random

mensajeEncriptado = str(input("+- Bienvenido -+\n\n Introduce el mensaje a encriptar:\n>: ")) # Se inserta el mensaje a encriptar
mensajeEncriptadoSplit = list(mensajeEncriptado) 											  # Se divide el mensaje en una lista
mensajeDesencriptado = "" 
mensajeDesencriptadoCode = ""

op = int(input("[1] Valor aleatorio.\n[2] Introducir valor.\n>: "))

if(op==1):
	for i in mensajeEncriptadoSplit:
		x = random.randint(1, 10)											# Se genera un número aleatorio del 1 al 10
		letraCode = ord(i)													# Se toma el valor unicode de los caracteres
		letra = chr(letraCode+x)											# Se suma el valor aleatorio y se pasa a char
		mensajeDesencriptadoCode = mensajeDesencriptadoCode + letraCode		# Se unen los valores
elif(op==2):
	x = int(input("Introduce un valor:\n>: "))
	for i in mensajeEncriptadoSplit:
		letraCode = ord(i)													# Se toma el valor unicode de los caracteres
		letra = chr(letraCode+x)											# Se suma el valor aleatorio y se pasa a char
		mensajeDesencriptadoCode = mensajeDesencriptadoCode + letra			# Se unen los valores

for i in mensajeDesencriptadoCode:
	mensajeDesencriptado = mensajeDesencriptado + int 						# Se unen los valores a cadena de texto




print("[!] Mensaje Encriptado:",mensajeEncriptado)
print("[-] Mensaje Desencriptado:",mensajeDesencriptado)
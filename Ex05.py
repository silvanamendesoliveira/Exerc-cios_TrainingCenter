#!/usr/bin/python3
import random, string

caracteres = string.ascii_uppercase 

letra1 = input("Insira a primeira Letra \n").upper()
letra2 = input("Insira a segunda Letra \n").upper()

posicao1 = caracteres.find(letra1) 
posicao2 = caracteres.find(letra2) 

posicaoLetraEncontrada = (posicao1 + posicao2)/2 

if posicao1 > posicao2:
 posicaoLetraEncontrada = posicaoLetraEncontrada + 0.5
 print ("A letra que fica no meio das letras que inseriu é a letra", caracteres[int(posicaoLetraEncontrada)])
else:
 print ("A letra que fica no meio das letras que inseriu é a letra", caracteres[int(posicaoLetraEncontrada)])
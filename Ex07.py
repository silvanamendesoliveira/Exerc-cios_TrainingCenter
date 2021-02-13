#!/usr/bin/python3

import random, string

caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation 
tamanho = 0 
password = "" 

file = open("passwords_geradas.txt","a") 
file.write("PASSWORDS GERADAS \n") 

while tamanho < 8 or tamanho > 32: 
    tamanho = int(input("Entre 8 e 32 caracteres, introduza o número de caracteres que deseja para a sua password?\n"))
    if tamanho < 8 or tamanho > 32:
        print("Tamanho de password fora dos parâmetros!")
    else: 
        print("Tamanho de password dentro dos parâmetros.")
        for x in range (tamanho):
            password += random.choice(caracteres)
        print ("A sua password é: ", password, sep="")
        file.write(password)

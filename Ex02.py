#!/usr/bin/python3
import collections

#solicitar ao utilizador que introduza os valores
valor1 = int(input("Introduza o 1º valor: "))
valor2 = int(input("Introduza o 2º valor: "))
valor3 = int(input("Introduza o 3º valor: "))
valor4 = int(input("Introduza o 4º valor: "))

#Dizer quantos números são pares ou ímpares

lista = [valor1, valor2, valor3, valor4]

contar_pares = 0
contar_impares = 0

for i in lista:
    if i % 2 == 0:
        contar_pares += 1
    else:
        contar_impares += 1

# Dizer quantos números são diferentes

diferentes = collections.Counter(lista).items()

print("Números diferentes:", len(diferentes)," Números pares:", contar_pares, " Números ímpares:", contar_impares, sep="")


 
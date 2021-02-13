#!/usr/bin/python3

from math import gcd

#encontrar o mínimo múltiplo comum entre 1 e 20

def mmc(numeros):
    x = 1
    for n in numeros:
        x = x * n // gcd(x, n)
    return x

numeros = range(1, 21)
print("O número mais pequeno que é divisível por todos os números de 1 até 20 é o", mmc(numeros)) 




#!/usr/bin/python3

def soma_multiplos(limite):
    sum = 0
    for i in range(limite):
        if i%3 == 0 or i%5 == 0:
            sum += i
    return sum

print( "A soma de todos os múltiplos de 3 e 5 abaixo de 1000 é:", soma_multiplos (1000) )
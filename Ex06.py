#!/usr/bin/python3

def soma_multiplos_abaixo_de(limite):
    return sum([i for i in range(limite) if i%3 == 0 or i%5 == 0])

print( "A soma de todos os múltiplos de 3 e 5 abaixo de 1000 é:", soma_multiplos_abaixo_de(1000))

#!/usr/bin/python3

seg = int(input("Introduza os segundos que deseja converter: "))

horas = int(seg / 3600)
seg_restantes = int(seg % 3600)
minutos = int(seg_restantes / 60)
seg_restantes_final = int(seg_restantes % 60)

if seg > 3600:
    horas 
elif seg > 60:
    minutos 
else:
    seg_restantes_final
print (seg, " segundos é igual a ", horas, ":", minutos, ":", seg_restantes_final, sep="")


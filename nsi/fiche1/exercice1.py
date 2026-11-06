#!/usr/bin/env python

nombre = int(input("Saisir un nombre : "))
print(f"Table de multiplication de {nombre} :")
for i in range(11):
    print(f"{nombre} x {i} = {nombre*i}")

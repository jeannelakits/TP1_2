#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 09:45:10 2025

@author: jeanne
"""


### EXO 5
# (a) Somme des n premiers entiers
def somme_entiers(n):
    # Formule : n*(n+1)/2
    return n * (n + 1) // 2

# (b) Factorielle n!
def factorielle(n):
    if n == 0 or n == 1:
        return 1
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat

# (c) Puissance x^n
def puissance(x, n):
    resultat = 1
    for _ in range(n):
        resultat *= x
    return resultat

print(somme_entiers(5))   # 1+2+3+4+5 = 15
print(factorielle(5))     # 5! = 120
print(puissance(2, 10))   # 2^10 = 1024


### EXO 6
def echange_positions(t, i, j):
    t[i], t[j] = t[j], t[i]

def position_plus_petit(t, p):
    pos_min = p
    for i in range(p + 1, len(t)):
        if t[i] < t[pos_min]:
            pos_min = i
    return pos_min

def tri_selection(t):
    n = len(t)
    for p in range(n - 1):  # jusqu'à l'avant-dernier élément
        h = position_plus_petit(t, p)
        if h != p:  # échange seulement si nécessaire
            echange_positions(t, p, h)
    return t

t = [12, 1, 5, 26, 7, 14, 3, 7, 2]
print(tri_selection(t))  
# Résultat attendu : [1, 2, 3, 5, 7, 7, 12, 14, 26]

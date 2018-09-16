#!/usr/bin/env/python3.4

# -*- coding:utf8 -*-

# TODO -----------------
# TODO docstring 
# TODO ask at the end of the program if user wants to continue with new equation 
# TODO offer the possibility to have coefficients in file in order to resolve multiple equations 
# TODO implement gui in order to be more user-friendly 
# TODO ------------------

"""
a*x**2 + b*x +c = 0
delta = b**2 - 4*a*c
if delta > 0
x1 = (-b - (Delta ** 0.5)) / (2*a)
x2 = (-b + (Delta ** 0.5)) / (2*a)
if delta == 0
x0 = -(b/(2*a))
if delta <0
x1 = (-b - j*(abs(Delta)**0.5)) / (2*a)
x2 = (-b + j*(abs(Delta)**0.5)) / (2*a)
"""

print("-----------------------------------------------------------------------------------------------")
print("Programme qui résoud les équations du second degrés sous la forme : a*x**2 + b*x + c = 0")
print("\n")
while True:
  try:
    a = int(input("Veuillez saisir la valeur de a : "))
  except ValueError:
    print("Erreur => vous n'avez pas saisi un entier")
    continue
    #exit(1)
  else:
    break
while True:
  try:
    b = int(input("Veuillez saisir la valeur de b : "))
  except ValueError:
    print("Erreur => vous n'avez pas saisi un entier")
    continue
    #exit(1)
  else:
    break
while True:
  try:
    c = int(input("Veuillez saisir la valeur de c : "))
  except ValueError:
    print("Erreur => vous n'avez pas saisi un entier")
    continue
    #exit(1)
  else:
    break

print("a = %d" % a)
print("b = %d" % b)
print("c = %d" % c)
print("équation : %dx**2 + %dx + %d = 0" % (a,b,c))
print("Calcul du discriminant : b**2 - 4*a*c")
delta = b**2 - 4 *a*c
print("Discriminant = %d " % delta)
print("--------------------------------------solution : ----------------------------")
if delta > 0:
  print("Discriminant positif")
  print("L'équation possède donc deux solutions x1 et x2")
  x1 = (-b - (delta ** 0.5)) / (2*a)
  x2 = (-b + (delta ** 0.5)) / (2*a)
  print("x1 = %f" % x1)
  print("x2 = %f" % x2)
elif delta == 0:
  print("Discriminant égal à 0")
  print("L'équation possède donc une solution x1")
  x1 = -(b/(2*a))
  print("x1 = %f" % x1)
else:
  print("Discriminant négatif")
  print("L'équation possède donc deux solutions complexes et conjuguées x1 et x2")
  x1 = complex(-b/(2*a),-abs(delta)**0.5/(2*a))
  x2 = complex(-b/(2*a),abs(delta)**0.5/(2*a))
  print("x1 = %0.4f + %0.4fi" % (x1.real,x1.imag))
  print("x2 = %0.4f + %0.4fi" % (x2.real,x2.imag))


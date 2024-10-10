#Ejercicio 4

import numpy as np

a = int(input("Ingrese un entero positivo a: "))
b = int(input("Ingrese un entero positivo b: "))

c = a
d = b

#Se verifica que los valores ingresados sean positivos
if a <= 0 or b <= 0:
   print("Los valores ingresados tienen que ser positivos")
   exit()

#Matriz identidad
m = np.array([
      [1,0],
      [0,1]
])
q = 0

#Se intercambian los valores si a < b
if a < b:
   a, b = b,a
   print("Se han intercambiado los valores: ahora a = " + str(a) + " y b = " + str(b))

#Algoritmo de bezout 

while b != 0:  # Mientras b no sea 0 se ejecuta el ciclo
   q = a // b  # Se calcula el cociente de la división de a entre b
   r = a % b # Se calcula el residuo de la división de a entre b
   print(a, "=", b, "(", q, ")", "+", r)
   a = b # Se asigna el valor de b a a
   print("a = ", a)
   b = r # Se asigna el valor de r a b
   print("b = ", b)
   
   #Multiplicadores de matrices
   Q1 = np.array([
      [0,1],
      [1,-q]
   ])

   m= Q1@m

x = m[0,0]
y = m[0,1]
print(f"Los coeficientes de Bezout son x = {x}, y = {y}")
print(f"Entonces {c}({x}) + {d}({y}) = {c * x + d * y}")
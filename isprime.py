import math
#Ejercicio 1
# Función para generar números primos hasta un límite usando la criba de Eratóstenes
def Primos_N(n):
    if n < 2:
        return

    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for p in range(2, int(math.sqrt(n)) + 1):
        if prime[p]:
            # Marcar los múltiplos de p como no primos, comenzando desde p^2.
            for i in range(p * p, n + 1, p):
                prime[i] = False

    # Imprimir los números primos
    primes = [p for p in range(2, n + 1) if prime[p]]
    print(*primes)
    
#Ejercicio 2
# Función para determinar si un número n es primo utilizando la criba
def is_prime(N):
    if N < 2:
        return False

    # Inicializamos una lista de booleanos para los números desde 0 hasta N.
    prime = [True] * (N + 1)
    prime[0] = prime[1] = False

    # Criba de Eratóstenes
    for p in range(2, int(math.sqrt(N)) + 1):
        if prime[p]:
            for i in range(p * p, N + 1, p):
                prime[i] = False

    # El valor de prime[N] nos indicará si N es primo
    return prime[N]

# Función principal para probar con varios números
def main():
    A = 0
   
    A = int(input("ingrese Número de ejecución deseado: 1. lista de primos entre 0 y N | 2. Si N es primo o no"))
    if A == 1:
        try:
            n = int(input("Ingrese un entero positivo n (o -1 para salir): "))
            if n == -1:
                exit
            print(Primos_N(n))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
    if A == 2:
        try:
            n = int(input("Ingrese un entero positivo n (o -1 para salir): "))
            if n == -1:
                exit
            print(is_prime(n))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
    else:
        exit

# Ejecutar las pruebas
main()


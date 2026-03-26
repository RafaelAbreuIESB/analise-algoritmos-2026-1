import math

def F(n):
    if n == 1:
        return 2
    else:
        return 2 * F(n - 1) + int(math.pow(n, 2))


n = int(input("Digite um valor para n: "))

if n < 1:
    print("Digite um número inteiro maior ou igual a 1.")
else:
    resultado = F(n)
    print(f"F({n}) = {resultado}")


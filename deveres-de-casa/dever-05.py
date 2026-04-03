
import math

# Merge Sort - O(n log n)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])

    return merge(esquerda, direita)


def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado


# Multiplicacao de matrizes - O(n^3)

def multiplicar_matrizes(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


# Recorrencias

def mostrar_recorrencias():
    print("Recorrencia: T(n) = 2T(n/4) + sqrt(n)")
    print("Complexidade: O(sqrt(n) log n)")

    print("Recorrencia 2: T(n) = 2T(n/4) + n")
    print("Complexidade: O(n)\n")

    print("Recorrencia: T(n) = 16T(n/4) + n^2")
    print("Complexidade: O(n^2 log n)")


# Testes
if __name__ == "__main__":
    # Teste Merge Sort
    vetor = [38, 27, 43, 3, 9, 82, 10]
    print("Vetor original:", vetor)
    print("Merge Sort:", merge_sort(vetor))
    print("Complexidade: O(n log n)\n")

    # Teste multiplicação de matrizes
    A = [
        [1, 2],
        [3, 4]
    ]

    B = [
        [5, 6],
        [7, 8]
    ]

    print("Resultado da multiplicacao de matrizes:")
    for linha in multiplicar_matrizes(A, B):
        print(linha)
    print("Complexidade: O(n^3)\n")

    # Mostrar recorrências
    mostrar_recorrencias()

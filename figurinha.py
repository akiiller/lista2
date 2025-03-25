def mdc(a, b):
    # Algoritmo de Euclides para calcular o MDC
    while b != 0:
        a, b = b, a % b
    return a

# Número de casos de teste
N = int(input())
F1 = []
F2 = []
resultado = []

# Processar cada caso de teste
for i in range(N):
    r, v = map(int, input().split())
    F1.append(r)
    F2.append(v)

for i in range(N):
    # Calcular o MDC de F1 e F2
    resultado.append(mdc(F1[i], F2[i]))
    # Imprimir o resultado
    print(resultado[i])
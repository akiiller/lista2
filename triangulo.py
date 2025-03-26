# # Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
# sides = list()
#
# sides = input().split(" ",3 )
#
#
# sides.sort()
#
#
#
# # se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
#
# if float(sides[2]) >= float(sides[1]) + float(sides[0]) :
#     print('NAO FORMA TRIANGULO')
#
# # se A2² = B2² + C2², apresente a mensagem: TRIANGULO RETANGULO
# if (float(sides[2])**2) == (float(sides[1])**2) + (float(sides[0])**2) :
#     print('TRIANGULO RETANGULO')
# # se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
# if (float(sides[2])**2) > (float(sides[1])**2) + (float(sides[0])**2) :
#     print('TRIANGULO OBTUSANGULO')
# # se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
# if (float(sides[2])**2) < (float(sides[1])**2) + (float(sides[0])**2) :
#     print('TRIANGULO ACUTANGULO')
# # se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
# if float(sides[2]) == float(sides[1]) and float(sides[2]) == float(sides[0]) and float(sides[1]) == float(sides[0]) :
#     print('TRIANGULO EQUILATERO')
#
# # se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
# if float(sides[2]) == float(sides[1]) or float(sides[2]) == float(sides[0]) or float(sides[1]) == float(sides[0]) :
#     print('TRIANGULO ISOSCELES')
# Função principal
def classificar_triangulo(A, B, C):
    # Ordenar os lados em ordem decrescente
    lados = sorted([A, B, C], reverse=True)
    A, B, C = lados  # A é o maior lado

    # Verificar se forma um triângulo
    if A >= B + C:
        print("NAO FORMA TRIANGULO")
        return

    # Classificar o tipo de triângulo com base nos ângulos
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    # Classificar o tipo de triângulo com base nos lados
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or B == C or A == C:
        print("TRIANGULO ISOSCELES")


# Entrada dos valores
A, B, C = map(float, input().split())

# Chamar a função para classificar o triângulo
classificar_triangulo(A, B, C)
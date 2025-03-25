# Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
sides = list()

sides = input().split(" ",3 )


sides.sort()



# se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO

if float(sides[2]) >= float(sides[1]) + float(sides[0]) :
    print('NAO FORMA TRIANGULO')

# se A2² = B2² + C2², apresente a mensagem: TRIANGULO RETANGULO
if (float(sides[2])**2) == (float(sides[1])**2) + (float(sides[0])**2) :
    print('TRIANGULO RETANGULO')
# se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
if (float(sides[2])**2) > (float(sides[1])**2) + (float(sides[0])**2) :
    print('TRIANGULO OBTUSANGULO')
# se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
if (float(sides[2])**2) < (float(sides[1])**2) + (float(sides[0])**2) :
    print('TRIANGULO ACUTANGULO')
# se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
if float(sides[2]) == float(sides[1]) and float(sides[2]) == float(sides[0]) and float(sides[1]) == float(sides[0]) :
    print('TRIANGULO EQUILATERO')

# se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
if float(sides[2]) == float(sides[1]) or float(sides[2]) == float(sides[0]) or float(sides[1]) == float(sides[0]) :
    print('TRIANGULO ISOSCELES')
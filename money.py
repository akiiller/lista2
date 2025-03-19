# -*- coding: utf-8 -*-

value = int(input())

# print orignal value
print(value)

# nota(s) de R$ 100,00
nota100 = value // 100
print("{} nota(s) de R$ 100,00".format(nota100))

# nota(s) de R$ 50,00
value %= 100
nota50 = value // 50
print("{} nota(s) de R$ 50,00".format(nota50))

# nota(s) de R$ 20,00
value %= 50
nota20 = value // 20
print("{} nota(s) de R$ 20,00".format(nota20))

# nota(s) de R$ 10,00
value %= 20
nota10 = value // 10
print("{} nota(s) de R$ 10,00".format(nota10))

#nota(s) de R$ 5,00
value %= 10
nota5 = value // 5
print("{} nota(s) de R$ 5,00".format(nota5))

# nota(s) de R$ 2,00
value %= 5
nota2 = value // 2
print("{} nota(s) de R$ 2,00".format(nota2))

# nota(s) de R$ 1,00
value %= 2
print("{} nota(s) de R$ 1,00".format(value))

while True:
    # Leitura das coordenadas
    X1, Y1, X2, Y2 = map(int, input().split())

    # Condição de parada
    if X1 == 0 and Y1 == 0 and X2 == 0 and Y2 == 0:
        break

    # Verifica se a posição inicial e final são iguais
    if X1 == X2 and Y1 == Y2:
        print(0)
    # Verifica se está na mesma linha, coluna ou diagonal
    elif X1 == X2 or Y1 == Y2 or abs(X1 - X2) == abs(Y1 - Y2):
        print(1)
    # Caso contrário, são necessários 2 movimentos
    else:
        print(2)
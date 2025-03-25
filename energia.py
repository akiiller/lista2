
def find_min_m(N, target=13):
    # Função para simular o desligamento das regiões
    def simulate(m):
        regions = list(range(1, N + 1))  # Lista de regiões ativas
        index = 0  # Começamos na região 1 (índice 0)

        while len(regions) > 1:
            # Remove a região atual
            regions.pop(index)
            # Calcula o próximo índice usando o salto m
            index = (index + m - 1) % len(regions)

        # Retorna a última região restante
        return regions[0]

    # Testa valores de m começando de 1
    m = 1
    while True:
        if simulate(m) == target:
            return m
        m += 1


# Leitura da entrada e processamento
answer = []
while True:
    N = int(input())
    if N == 0:
        break
    answer.append(find_min_m(N))
for e in answer:
    print(e)
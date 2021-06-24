GRAFO = {
    'Arad': {'Sibiu': 140, 'Zerind': 75, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
    'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}


def bfs_algo(origem, destino, path=None):
    if path is None:
        path = [origem]
    if origem == destino:
        yield path
    for prox_no in set(GRAFO[origem].keys()) - set(path):
        yield from bfs_algo(prox_no, destino, path + [prox_no])

def ucs(origem, destino):
    from queue import PriorityQueue
    priority_queue, noVisitado = PriorityQueue(), {}
    priority_queue.put((0, origem, [origem]))
    noVisitado[origem] = 0
    while not priority_queue.empty():
        (custo, vertex, path) = priority_queue.get()
        if vertex == destino:
            return custo, path
        for proxNo in GRAFO[vertex].keys():
            custoX = custo + GRAFO[vertex][proxNo]
            if not proxNo in noVisitado or noVisitado[proxNo] >= custoX:
                noVisitado[proxNo] = custoX
                priority_queue.put((custoX, proxNo, path + [proxNo]))
def main():
    print('Digite a origem :', end=' ')
    origem = input().strip()
    print('Digite o destino :', end=' ')
    destino = input().strip()
    if origem not in GRAFO or destino not in GRAFO:
        print('Erro: Esta cidade não existe.')
    else:
        print('\nCaminhos possíveis:')
        paths = bfs_algo(origem, destino)
        for path in paths:
            print(' -> '.join(cidade for cidade in path))
        custo, melhorCaminho = ucs(origem, destino)
        print('\nCaminho com menos custos:')
        print(' -> '.join(cidade for cidade in melhorCaminho))
        print('Custo deste caminho total =', custo)

if __name__ == '__main__':
    main()

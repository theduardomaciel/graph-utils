import random

def generate_graph_with_negative_cycle(nodes, edges):
    """
    Gera um grafo com nós e arestas, incluindo um ciclo negativo.
    
    :param nodes: Número de nós no grafo.
    :param edges: Número total de arestas no grafo.
    :return: Lista de arestas, onde cada aresta é uma tupla (de, para, peso).
    """
    graph = []
    
    # Gerar arestas aleatórias com pesos
    for _ in range(edges):
        from_node = random.randint(1, nodes)
        to_node = random.randint(1, nodes)
        while to_node == from_node:  # Evitar laços
            to_node = random.randint(1, nodes)
        weight = random.randint(-10, 20)  # Pesos aleatórios, incluindo negativos
        graph.append((from_node, to_node, weight))
    
    # Adicionar ciclo negativo
    cycle_size = 3  # Tamanho do ciclo
    cycle_nodes = random.sample(range(1, nodes + 1), cycle_size)  # Selecionar nós do ciclo
    negative_weight_sum = random.randint(-10, 10)  # Soma dos pesos negativos

    for i in range(cycle_size):
        from_node = cycle_nodes[i]
        to_node = cycle_nodes[(i + 1) % cycle_size]  # Nó seguinte (com wrap-around)
        weight = random.randint(-10, 10) if i != cycle_size - 1 else negative_weight_sum
        graph.append((from_node, to_node, weight))
        negative_weight_sum -= weight  # Ajustar a soma para o último peso

    return graph


def main():
    nodes = random.randint(100, 200)  # Número de nós
    edges = random.randint(100, 7000)  # Número de

    graph = generate_graph_with_negative_cycle(nodes, edges)

    # Escreve o grafo num arquivo
    with open("negative.mtx", "w") as file:
        file.write(f"{nodes} {edges}\n")
        for u, v, w in graph:
            file.write(f"{u} {v} {w}\n")


if __name__ == "__main__":
    main()

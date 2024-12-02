import networkx as nx

def bellman_ford_distances(graph, source):
    """
    Calcula as distâncias mínimas a partir de um vértice usando o algoritmo de Bellman-Ford.

    :param graph: Um grafo dirigido e ponderado representado como um objeto NetworkX.
    :param source: O vértice de origem para calcular as distâncias mínimas.
    :return: Um dicionário contendo as distâncias mínimas ou uma mensagem de erro.
    """
    try:
        # Calcula as distâncias mínimas usando Bellman-Ford
        distances = nx.single_source_bellman_ford_path_length(graph, source)
        return distances
    except nx.NetworkXUnbounded:
        return {"error": "O grafo contém ciclos negativos acessíveis a partir da origem."}

def read_graph_from_file(filename):
    """
    Lê um grafo a partir de um arquivo no formato:
    n m
    u v w
    onde n é o número de nós, m é o número de arestas, e cada linha seguinte representa uma aresta de u para v com peso w.

    :param filename: O nome do arquivo contendo o grafo.
    :return: Um objeto NetworkX DiGraph.
    """
    with open(filename, 'r') as file:
        # Lê o número de nós e arestas
        n, m = map(int, file.readline().strip().split())
        
        # Cria o grafo
        graph = nx.DiGraph()
        
        # Lê as arestas
        for _ in range(m):
            u, v, w = map(int, file.readline().strip().split())
            graph.add_edge(u, v, weight=w)
            graph.add_edge(v, u, weight=w)  # Adiciona a aresta de volta para grafos não direcionados
    
    return graph

# Lê os arquivos na pasta examples e escreve o gabarito na pasta solutions
import os

for file in os.listdir("examples"):
    graph = read_graph_from_file(f"examples/{file}")
    source_node = 1
    result = bellman_ford_distances(graph, source_node)

    if "error" in result:
        print(result["error"])

        with open(f"solutions/{file}", "w") as file:
            file.write("Ciclo negativo detectado!")
    else:
        with open(f"solutions/{file}", "w") as file:
            for node in sorted(result.keys()):
                file.write(f"{node}:{result[node]} ")


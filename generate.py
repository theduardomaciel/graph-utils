import random

edge_chance = 0.5

def generate_graph(n, max_weight):
    edges = []
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            if random.random() < edge_chance:
                weight = random.randint(1, max_weight)
                edges.append((u, v, weight))
    return n, len(edges), edges

def print_graph(n, m, edges):
    print(n, m)
    for u, v, weight in edges:
        print(u, v, weight)

def write_graph(filename, n, m, edges):
    with open(filename, 'w') as file:
        file.write(f"{n} {m}\n")
        for u, v, weight in edges:
            file.write(f"{u} {v} {weight}\n")

# Exemplo de uso
for i in range(20, 24):
    filename = f"examples/example{i}.mtx"

    n = random.randint(50, 250)
    max_weight = random.randint(1, 50)

    vertices, edges_count, edges_list = generate_graph(n, max_weight)
    write_graph(filename, vertices, edges_count, edges_list)
    print(f"Arquivo {filename} gerado com sucesso.")
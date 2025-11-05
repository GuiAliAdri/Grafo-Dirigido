import numpy as np

# Aqui esta a parte de definicao dos grafos
nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
idx = {v: i for i, v in enumerate(nodes)}

# Array das bordas
edges = {
    "A": ["B", "C", "D"],
    "B": ["C", "E"],
    "C": ["A"],
    "D": ["C", "E", "F"],
    "E": ["F", "G"],
    "F": ["G"],
    "G": ["E", "H", "I"],
    "H": ["I"],
    "I": ["J"],
    "J": ["G"],
}
n = len(nodes)


# Funcao que retorna os dados base do grafo
def get_graph_data():
    return nodes, idx, edges, n


# Funcao que monta a matriz de transicao P
def build_transion_matriz():
    P = np.zeros((n, n), dtype=float)

    for src, i in enumerate(nodes):
        outs = edges.get(i, [])

        if len(outs) == 0:
            P[:, i] = 1.0 / n
        else:
            prob = 1.0 / len(outs)
            for dst in outs:
                j = idx[dst]
                P[j, i] = prob
    return P

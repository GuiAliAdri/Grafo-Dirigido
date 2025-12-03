import numpy as np

# Aqui esta a parte de definicao dos grafos
nodes = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10"]
idx = {v: i for i, v in enumerate(nodes)}

# Array das bordas
edges = {
    "P1": ["P2", "P3", "P4"],
    "P2": ["P3", "P5"],
    "P3": ["P1"],
    "P4": ["P3", "P5", "P6"],
    "P5": ["P6", "P7"],
    "P6": ["P7"],
    "P7": ["P5", "P8", "P9"],
    "P8": ["P9"],
    "P9": ["P10"],
    "P10": ["P7"],
}
n = len(nodes)


# Funcao que retorna os dados base do grafo
def get_graph_data():
    return nodes, idx, edges, n


# Funcao que monta a matriz de transicao P
def build_transion_matrix(nodes, idx, edges, n):
    P = np.zeros((n, n), dtype=float)

    for src_index, src_name in enumerate(nodes):
        outs = edges.get(src_name, [])

        if len(outs) == 0:
            P[:, src_index] = 1.0 / n
        else:
            prob = 1.0 / len(outs)
            for dst_name in outs:
                dst_index = idx[dst_name]
                P[dst_index, src_index] = prob
    return P

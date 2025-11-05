from time import sleep

# Importa todas as funções modulares
from modules.graph import build_transion_matrix, get_graph_data
from modules.pagerank import apply_damping, power_interation
from modules.utils import draw_graph, export_csv, get_ranking, print_ranking


def main():
    print("================= INICIANDO PROGRAMA =================")
    # Funcao Principal
    # Preparacao dos dados
    nodes, idx, edges, n = get_graph_data()
    alpha = 0.85  # Google Matriz Factor

    print(f"Total de nós (n): {n}")
    print(f"Fator de damping (alpha): {alpha}")
    sleep(0.5)
    # Monta a matriz de transiçao P
    print("\n# 2) Montando Matriz de Transição P...")
    sleep(1)
    P = build_transion_matrix(nodes, idx, edges, n)
    print("Matriz P:\n", P)
    sleep(1)

    print("\n# 3) Aplicando Damping (Google Matriz G)...")
    sleep(1)
    G = apply_damping(P, alpha, n)
    print("Matriz G:\n", G)
    sleep(1)

    print("\n# 4) PageRank por interação de potência...")
    pagerank_vector = power_interation(G, n)

    # Ranking
    ranking = get_ranking(nodes, pagerank_vector)
    print_ranking(ranking)

    # Arquivo CSV
    export_csv(ranking, filename="ranking.csv")

    # Grafico
    draw_graph(nodes, edges, pagerank_vector, filename="grafo_pagerank.png")
    print("================= FIM DO PROFGRAMA =================")


if __name__ == "__main__":
    main()

import csv
import networkx as nx
import matplotlib.pyplot as pl
import os

output_dir = 'output'

def ensure_output_dir():
    #Verifica se a pasta de saída existe, caso não existe, ela é criada
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Diretório de saída '{output_dir}/' criado.")


def get_ranking(nodes, pagerank_vector):
    #Cria a lista de ranking e ordena
    ranking = sorted(zip(nodes, pagerank_vector), key=lambda t: t[1], reverse=True)
    return ranking

def print_ranking(ranking):
    #Imprime o ranking no console
    print('\n# 5) Ranking')
    print("Ranking ('score' alto -> baixo):")
    for k, (name, score) in enumerate(ranking, 1):
        print(f"k={k:2d}. {name}: {score:.6f}")

def export_csv(ranking, filename="ranking.csv"):
    ensure_output_dir()
    filepath = os.path.join(output_dir, filename)

    print(f'\n# 6) Exporta CSV para {filepath}')
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["pagina", "pagerank"])
        for name, score in ranking:
            writer.writerow([name, f"{score:.12f}"])
    print('Exportação CSV concluída')

def draw_graph(nodes, edges, pagerank_vector, filename='grafo_pagerank.png'):
    #Gera e salva arquivo visual do grafo com o networkx dentro da pasta de saida
    ensure_output_dir()

    filepath = os.path.join(output_dir, filename)
    print(f'\n# 7) Gráfico visual com NetworkX para {filepath}')

    gx = nx.DiGraph()
    gx.add_nodes_from(nodes)

    #Adiciona as arestas
    for src, outs in edges.items():
        for dst in outs:
            gx.add_edge(src, dst)
    
    scores = dict(zip(nodes, pagerank_vector))
    size_draw = [6000 * scores[v] for v in gx.nodes()]

    pos = nx.spring_layout(gx, seed=42)
    pl.figure(figsize=(10, 7))

    try:
        #Desenha os nós
        nx.draw_networkx_nodes(gx, pos, node_size=size_draw, node_color="#3498db", alpha=0.9)
        #Desenha as arestas
        nx.draw_networkx_edges(gx, pos, arrows=True, arrowstyle='->', arrowsize=20, edge_color="gray", min_target_margin=5)
        #Desenha os rotulos
        nx.draw_networkx_labels(gx, pos, font_size=10)

        pl.axis('off')
        pl.title("PageRank do Grafo Dirigido")
        pl.tight_layout()
        pl.savefig(filename, dpi=220)
        pl.close()
        print('Gráfico gerado com sucesso')
    except Exception as e:
        print(f'Erro ao gerar gráfico {e}')
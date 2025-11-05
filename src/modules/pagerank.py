import numpy as np


# Funcao que
def apply_damping(P, alpha, n):
    # Matriz E: onde todos os elementos são 1/n
    E = np.ones((n, n)) / n
    G = alpha * P + (1 - alpha) * E
    return G


def power_interation(G, n, tol=1e-12, maxit=10000):
    # Calcula o pagerank usando o metodo de interacao de potencia
    x = np.ones(n) / n  # chute inicial (vetor de probabilidade uniforme)

    for k in range(maxit):
        x_net = G @ x

        # condicao de parada
        if np.linalg.norm(x_net - x, 1) < tol:
            x = x_net
            break
        x = x_net
    x = x / np.sum(x)
    return x

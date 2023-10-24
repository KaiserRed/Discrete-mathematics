import math
import networkx as nx
import matplotlib.pyplot as plt

def Input_Graph (Matrix_of_Adjacency, n):
    graph = nx.DiGraph ()
    for i in range (n):
        for j in range (n):
            if (Matrix_of_Adjacency[i][j] > 0):
                graph.add_nodes_from([i, j])
                graph.add_edge(i, j)
    return graph

def Print_Graph (graph: nx.DiGraph):
    labels = dict()
    for node in graph.nodes:
        labels[node] = node + 1
    pos = nx.spring_layout(graph)
    nx.draw (graph, pos, with_labels=True, labels=labels)
    nx.draw(graph, pos)
    plt.show()

def Enter_Matrix (Matrix_of_Adjacency, n, g ,gr):
    k = 0
    for i in range(n):
        Matrix_of_Adjacency.append(list(map(int, input().split())))
        mat = Matrix_of_Adjacency[i]
        for j in range(n):
            if mat[j] == 1:
                g[k].append(j)
                gr[j].append(k)
        k += 1


def Algorithm (n, g, gr):
    tout = []
    visited = [False for i in range(n)]
    for i in range(n):
        if not visited[i]:
            dfs1(i, visited, g, tout)

    visited = [False for i in range(n)]
    tout = tout[::-1]
    for v in tout:
        scc = []  # strongly connected compoents
        if not visited[v]:
            dfs2(v, scc, visited, gr)
            scc.reverse()
            for j in range(len(scc)):
                scc[j]+=1
            print(scc)

def dfs1(v, visited, g, tout):
    visited[v] = True
    for u in g[v]:
        if not visited[u]:
            dfs1(u, visited, g, tout)
    tout.append(v)

def dfs2(v, scc, visited, gr):
    visited[v] = True
    scc.append(v)
    for u in gr[v]:
        if not visited[u]:
            dfs2(u,scc, visited, gr)

def main ():
    print ("Введите количество вершин графа:", end="")
    n = int (input ())
    g = [[] for i in range(n)]
    gr = [[] for i in range(n)]
    Matrix_of_Adjacency = []
    print ("Введите матрицу достижимости:")
    Enter_Matrix (Matrix_of_Adjacency, n, g, gr)
    print ("Компоненты сильной связности:")
    Algorithm(n, g, gr)
    graph = Input_Graph(Matrix_of_Adjacency, n)
    Print_Graph(graph)
    print ()

if __name__ == "__main__":
    main()
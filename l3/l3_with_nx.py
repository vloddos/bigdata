import re
import networkx as nx

with open(r'C:\Users\User\Desktop\univer\bigdata\lab3\graph_small.txt') as f:
    l = {int(i[0]): tuple(map(int, i[1:])) for i in (re.findall(r'\d+', i) for i in f.readlines())}

g = nx.Graph()
g.add_nodes_from(l)
g.add_edges_from((i, j) for i in l for j in l[i])
print(nx.number_connected_components(g))

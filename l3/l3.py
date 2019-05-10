import re
import networkx as nx
import matplotlib.pyplot as pp

with open(r'C:\Users\User\Desktop\univer\bigdata\lab3\graph_small.txt') as f:
    # l={int(i[0]):tuple(map(int,i[1:])) for i in (re.findall(r'\d+',i) for i in f.readlines())}#i?
    l = {int(i[0]): tuple(map(int, i[1:])) for i in (re.findall(r'\d+', j) for j in f.readlines())}  # generator vs list

v = {*l} | {*sum(l.values(), ())}
v2i = dict(enumerate(v))
i2v = {v2i[i]: i for i in v2i}
n = len(v)
m = [[False] * n for i in range(n)]

for i in l:
    for j in l[i]:
        m[i2v[i]][i2v[j]] = m[i2v[j]][i2v[i]] = True

used = [False] * n
c = []


def dfs(v, c):
    for u in range(n):
        if m[v][u] and not used[u]:
            used[u] = True
            c = dfs(u, c)
    c += [v]
    return c


for i in range(n):
    if not used[i]:
        used[i] = True
        c += [dfs(i, [])]

print('components')
for i, j in enumerate(c):
    print(f'{i}:{j}')

print(f'total:{len(c)}')

for i in c:
    f = pp.figure()
    g = nx.Graph()
    g.add_edges_from((v2i[j], v2i[k]) for j in i for k in i if m[j][k])  # repeat edges?
    nx.draw(g, with_labels=True)
    f.show()

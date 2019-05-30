import re
from collections import defaultdict

with open(r'C:\Users\User\Desktop\univer\bigdata\lab3\graph_small.txt') as f:
    l = defaultdict(list, ((int(i[0]), tuple(map(int, i[1:]))) for i in (re.findall(r'\d+', i) for i in f.readlines())))

for i in [*l]:
    for j in l[i]:
        if type(l[j]) == list:
            l[j].append(i)

used = set()


def dfs(v, c):
    used.add(v)
    for u in l[v]:
        if u not in used:
            dfs(u, c)
    c.append(v)
    return c


print(len([dfs(i, []) for i in l if i not in used]))

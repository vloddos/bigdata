from collections import Counter


c=Counter()
with open('/home/vloddos/Рабочий стол/db2.txt') as f:
    for i in f:
        c[i.lower().strip()]+=1
print(' '.join(i[0] for i in c.most_common(12)))

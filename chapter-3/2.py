import os
import sys 
a = str(sys.argv[1]) 
b = os.listdir(a)
k = []
c = []
f = 0
o = []
z = []
l = 0
for num in b:
    k.append(num.split('.'))
for j in k:
    if len(j) > 1 :
        c.append(j)
for d in c:
    f = 0
    c[1:]
    for e in c:
        if  d[1] == e[1]:
            f = f+1
        if f > 0:
            o.append((e[1],f))
for g in o:
    l = g[1]
    for w in o:
        if w[1] > l:
            l = w[1]
    z.append[(g[0],l)]
print z

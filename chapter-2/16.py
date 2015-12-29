def extsort(a):
    temp=[]
    for f in a:
        temp.append(f.split('.'))
        #print temp
    temp.sort(key= lambda x: x[1:])
    a=[]
    for k in temp:
        a.append(".".join(k))
    return a
print extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])

def dups(a):
    r = []
    i = 0
    for num in a:
        f = 0
        i = i+1
        for u in range(i,len(a)):
            if num == u:
                f = 1
        if f==1:
            r.append(num)
    return r
print dups([1,2,1,3,2,5])

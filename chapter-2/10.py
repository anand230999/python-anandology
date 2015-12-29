def unique(a):
    r = []
    for num in a:
       f = 0
       for u in r:
            if num == u:
                f = 1
       if f == 0:
           r.append(num)
    return r
print unique([1,2,1,3,2,5])


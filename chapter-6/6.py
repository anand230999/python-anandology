def treemap(fun,a,r = None):
    if r is None:
        r = []
    for x in range(len(a)):
        if isinstance(a[x],list):
            treemap(fun,a[x],r)
        else:
           r.append(fun(a[x]))
    return r
print treemap(lambda x: x*x,[1, 2, [3, 4, [5]]])

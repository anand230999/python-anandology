def even(x): return x%2 == 0

def filterr(a,b):
    return [x for x in b if a(x)== True]
print filterr(even, range(10))

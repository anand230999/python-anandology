def square(x): return x*x
def mapp(a,b):
    return [ a(x)for x in b]
print mapp(square, range(5))

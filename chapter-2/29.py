def Nonee(b):
    k = []   
    for y in range(b):
        k.append(None)
    return k

def array(a,b):
    return [[Nonee(b)] * a]

a = array(2, 3)
a[0][0] = 5
print a

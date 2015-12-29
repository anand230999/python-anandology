def product1(a):
    r = 1
    for num in a:
        r = r*num 
    return r 
def factorial(a):
    f = 1;
    for num in range(a,0,-1):
        f = f*num
    return f
print factorial(5)

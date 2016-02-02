def mulr(a,n):
    if n==1:
        return a
    else:
        return a+mulr(a,n-1)
print mulr(25,3)

def cumulative_product(a):
    r=[]
    i=0
    prev=1
    for num in a:
        r.insert(i,(num*prev))
        prev = r[i]
        i = i+1
    return r
print cumulative_product([1,2,3,4])


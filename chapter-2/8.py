def cumulative_sum(a):
    r=[]
    i=0
    prev=0
    for num in a:
        r.insert(i,(num+prev))
        prev = r[i]
        i = i+1
    return r
print cumulative_sum([1,2,3,4])

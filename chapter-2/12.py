def group(a, s):
    out = []
    i = s
    k = 0
    while a != []: 
        temp =[]
        if len(a) < s:
            for o in range(0,len(a),1):
                temp.append(a[0])
        else:

            for o in range(0,s,1):
                temp.append(a[o])
        a=a[s:]
        out.append(temp)
    return out
print group([1,2,3,4,5,6,7,8,9],4)

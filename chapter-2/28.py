def enumerates(a):
    return [(x,a[x]) for x in range(0,len(a),1)]
for index, value in enumerate(["a", "b", "c"]):
    print index, value

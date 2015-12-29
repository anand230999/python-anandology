def unique1(a,key):
    r = []
    for num in a:
       f = 0
       for u in r:
            if num == u:
                f = 1
       if f == 0:
	r.append(num)
    print r
    r.sort(key)
    return r
print unique1(["python", "java", "Python", "Java"], key=lambda s: s.lower())


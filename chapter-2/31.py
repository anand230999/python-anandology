def parse_csv(a,b,c):
    n = len(open(a).readlines())
    f = open(a)
    return [ 1 if (open(a).readline().split(' ')) == '#'  else f.readline().split('!')for y in range(n) ]
print parse_csv('a.csv','!','#')

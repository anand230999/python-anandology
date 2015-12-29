def parse_csv(a):
    n = len(open(a).readlines())
    f = open(a)
    return [1 if y<0 else f.readline().split(',')for y in range(n) ]
print parse_csv('a.csv')
#print generate('a.csv',3)

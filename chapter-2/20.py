import sys
a = str(sys.argv[1])
b = str(sys.argv[2])
f = open(a)
n = len(f.readlines())
f.close()
f = open(a)
for num in range(0,n-1,1):
    g = []
    g.append(f.readline().split())
    #print g
    for o in g:
        for i in o:
            #print i
            if i == b or i == b+'.':
                print " ".join(o)
        


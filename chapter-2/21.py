import sys
a = str(sys.argv[1])
b = int(sys.argv[2])
f = open(a)
l=b
n = len(open(a).readlines())
for num in range(0,n,1):
   k = ''
   k = f.readline()
   if len(k) <= b:
        print k
   else:
        for d in range(b,0,-1):
            if k[d] == ' ':
                break
       # print d
        print k[:d]
        print k[d+1:]
        

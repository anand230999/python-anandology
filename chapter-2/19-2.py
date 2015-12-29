import sys
a = str(sys.argv[1])
f = open(a)
b = len(f.readlines()) 
n = b- 10
f.close()
f = open(a)
for num in range(0,n,1):
    f.readline()
for k in range(n,b,1):
    print f.readline()

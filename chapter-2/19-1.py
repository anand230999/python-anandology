import sys
a = str(sys.argv[1])
f = open(a)
for num in range(0,10,1):
     print f.readline()

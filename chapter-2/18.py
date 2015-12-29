f = open('anand.txt')
g=f.readlines()
print g
f.close()
f = open('anand.txt','w')
print len(g)
for num in range((len(g)-1),-1,-1):
    f.writelines([g[num]])
f.close()

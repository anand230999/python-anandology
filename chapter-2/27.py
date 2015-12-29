def triplets(a):
    b = [(x,y,z) for x in range(0,a,1) for y in range(0,a,1) for z in range(0,a,1) if x+y == z and x!=0 and y!=0 and z!=0 and x != y and y!=x ]
    print b 
print triplets(5)

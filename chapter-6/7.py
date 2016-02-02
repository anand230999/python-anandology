import sys
import os
parent = sys.argv[1]
def ditree(parent,tab=0):
    d = os.listdir(parent)
    for x in d:
        if os.path.isdir(parent+"/"+x):
            ditree(parent+"/"+x,tab=tab+1)
            print "|--"+x+"/"
        else:
            if x==d[-1]:
                print "|"+" "*tab+"`--"+x
            else:
                print "|"+" "*tab+"|--"+x 
print ditree(parent)

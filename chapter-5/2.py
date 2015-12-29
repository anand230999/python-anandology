def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def length(lines):
    return (line for line in lines if len(line)>40)

def printlines(lines):
    for line in lines:
        print line

import sys
filenames = []
for num in range(1,len(sys.argv),1):
   filenames.append(str(sys.argv[num]))
  
lines = readfiles(filenames)
lines = length(lines)
printlines(lines)

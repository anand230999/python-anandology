import os
import sys
import time
a = str(sys.argv[1])
l = os.listdir(a)
for num in l:
    print num,'\t ',os.stat(a+'/'+num).st_size,'\t',time.ctime(os.stat(a+'/'+num).st_mtime)

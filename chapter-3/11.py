import sys
import zipfile
a = sys.argv[1]
z = zipfile.ZipFile(a,'w')

for num in range(2,len(sys.argv),1):
    print sys.argv[num]
    z.write(sys.argv[num])
z.close()

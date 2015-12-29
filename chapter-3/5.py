import urllib
import sys
a = str(sys.argv[1])
response = urllib.urlopen(a)
html = response.read()
print 'saving',a,'as',a.split('/')[-1]
f = open (a.split('/')[-1],'w')
f.write(html)

def fun(a):
   if a == []:
      return
   if type(a[0]) != list:
      if len(a) == 1:
         print "\t"*len(a[0].split('/')),"/--",a[0].split("/")[-1]
      else:
         print "\t"*len(a[0].split('/')),"|--",a[0].split("/")[-1]
      return fun(a[1:])
   else:
       return fun(a[0])
import sys
import os
d = str(sys.argv[1])
a = os.walk(d)
f = []
for filenames in os.walk(d):
   f.extend(filenames)
   #break
   fun(filenames)

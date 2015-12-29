def make_slug(a):
   import re
   o = re.findall(r'\w+',a)
   return ('-').join(o)
print make_slug(" --hello-  world--")
       

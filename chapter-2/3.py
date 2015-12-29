def sum1(a):
     if type(a[0]) == str:
         r =""
     else:
         r = 0
     for  num in a:
        r= r+ num
     return r

   
print sum1(["hello","world"])

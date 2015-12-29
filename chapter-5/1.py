class reverse_iter:
   def __init__(self,l):
      self.i = len(l)-1
      self.l = l 
   def __iter__(self):
      return self
   def next(self):
      if self.i >= 0:
         i = self.l[self.i]
         self.i -=1
         return i
      else:
        raise StopIteration()

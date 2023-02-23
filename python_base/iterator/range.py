print(range(3))
print(dir(range(3)))

'''
['__bool__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
  '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', 
  '__hash__', '__init__', '__init_subclass__', '__iter__',
  '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__',
  '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__str__',
  '__subclasshook__', 'count', 'index', 'start', 'step', 'stop']
'''

# iter_object = [1, 2, 3].__iter__()
# iter_object.__next__()


class Range :
    def __init__(self, stop):
        self.current = 0
        self.stop = stop
    def __iter__(self) :
        return self
    def __next__(self) :
        if self.current < self.stop :
                self.res = self.current
                self.current += 1
        else :
            raise StopIteration
        return self.res
        
        

for i in Range(3) :
    print(i)
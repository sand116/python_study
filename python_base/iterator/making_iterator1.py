class Iterator :
    def __init__(self, stop) :
        self.current = 0
        self.stop = stop
    def __iter__(self) : #받는 인자가 없는 경우 ()를 호출하지 않고 그냥 CLASS이름.__iter__
        return self
    def __next__(self) :
        if self.current < self.stop :
            r = self.current
            self.current += 1
            return r
        else :
            raise StopIteration
for i in Iterator(3) :
    print(i)
    print(Iterator.__iter__)
        
        
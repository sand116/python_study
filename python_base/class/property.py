# getter, setter, @property

# Ex 1

class SampleA:
    def __init__(self):
        self.x = 0 # public
        self__y = 0 # private
    
    # getter
    @property
    def y(self):
        print('Called get method.')
        return self.__y
    
    @y.setter 
    def y(self, value) :
        print('Called set method.')
        self.__y = value
        
    @y.deleter
    def y(self) :
        del self.__y

a = SampleA()

a.x = 1
a.y = 2 # set method 출력

print(f'Ex 1 > x: {a.x}')
print(f'Ex 1 > y: {a.y}') # get method 출력

# deleter
del a.y

print(f'Ex 1 > {dir(a)}') # get method 출력


# 제약 조건 추가 
# Ex 2


class SampleB:
    def __init__(self):
        self.x = 0 # public
        self__y = 0 # private
    
    # getter
    @property
    def y(self):
        print('Called get method.')
        return self.__y
    
    @y.setter 
    def y(self, value) :
        print('Called set method.')
        if value < 0:
            raise ValueError('0 보다 큰 값을 입력하세요.')
        self.__y = value
        
    @y.deleter
    def y(self) :
        del self.__y
        
b = SampleB()

b.x = 1
b.y = -10

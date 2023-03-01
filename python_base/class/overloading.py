# 기본적으로 overloading이 불가

# Ex 1
# 동일 이름 메소드 사용 예제

class SampleB() :
    def add(self, datatype, *args):
        if datatype == 'int' :
            return sum(args)
        if datatype == 'str' :
            return ''.join([x for x in args])
        

b = SampleB()

# 숫자 연산
print(f'Ex2 > ', b.add('int', 5, 6))
print(f'Ex2 > ', b.add('str', 'hi', 'python'))


from multipledispatch import dispatch

class SampleC :
    @dispatch(int, int)
    def product(x, y):
        return x * y
    @dispatch(int, int, int )
    def product(x, y, z):
        return x * y * z
    @dispatch(float, float, float )
    def product(x, y, z):
        return x * y * z
    
c = SampleC()
print(f'Ex2 > ', c.product(5, 6))
print(f'Ex2 > ', c.product(5, 6, 7))
print(f'Ex2 > ', c.product(5.0, 6.0, 7.0))
      
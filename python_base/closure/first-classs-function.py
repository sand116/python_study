# 파이썬 함수 특징

# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능 


# 함수 객체

def factorial(n):
    ''' Factorial Function -> n : int '''
    if n == 1:
        return 1
    else :
        return n*factorial(n-1)
    
class A :
    pass

print(factorial(5))

print(factorial.__doc__)

print(type(factorial)," vs ",type(A))

print(set(sorted(dir(factorial))) - set((sorted(dir(A)))))

print(factorial.__name__)
print(factorial.__code__)

# 변수로 할당 가능하며 참조에 의한 할당으로 같은 함수 객체를 가리킴

var_func = factorial

print(var_func.__doc__)
print(var_func.__name__)
print(var_func.__code__)

print(var_func(10))



# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수

# map, filter, reduce
print(list(map(var_func,range(1, 11))))

# print(list(map(factorial,range(1, 11))))

print([var_func(i) for i in range(1, 6) if i%2])
print(list(map(var_func, filter(lambda x: x%2, range(1, 6)))))

# reduce

from functools import reduce
from operator import add

print(sum(range(1, 11)))
print(reduce(add,range(1, 11)))

# 익명함수(lambda)
# 가급적 주석 작성
# 가급적 함수 작성하고 일반 함수 형태로 리팩토링 권장

print(reduce(lambda x,y : x*y , range(1,4)))

# callable : 호출 연산자() 즉, 메소드 형태로 호출 가능한지 확인 가능

print(callable(str), callable(list), callable(A), callable(3.14)) # 3.14() 불가


# partial 사용법 : 인수 고정하여 함수를 변수에 할당 -> 콜백 함수에 사용
from operator import mul 
from functools import partial

print(mul(10, 10))

# 인수 한쪽 고정하고 싶은 경우

five = partial(mul, 5) # 5 * ?

print(five(10))
print(five(100))

# 고정 추가
six = partial(five, 6)
print(six())
#print(six(10))


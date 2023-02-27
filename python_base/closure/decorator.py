# 데코레이터 


# 장점 
# 1. 중복 제거, 코드 간결, 공통 함수 작성 가능
# 2. 로깅, 프레임워크, 유효성 체크 -> 공통 기능 정의 가능
# 3. 여러가지 함수를 조합해서 사용 용이

# 단점
# 1. 가독성 감소?
# 2. 특정 기능에 한정된 함수는 단일 함수로 작성하는 것이 유리
# 3. 디버깅 불편

# 데코레이터 실습 

# 만약에 여러 코드에서 함수의 시작시간과 종료 시간을 구한다고 가정했을 때 해당 코드를 함수마다 넣게 되면 비효율적일 수 있다.
# 해당 함수를 받아, 함수의 시작과 종료 시간을 구해주는 함수를 따로 만들어 재사용하면 편리하지 않을까?

import time

# 데코레이터 함수 생성
def perf_clock(func):

    # wrapper함수로서, 외부 함수 인자로 넘어온 함수를 가질 수 있음
    # func 함수가 어떤 인자를 가질 수 알 수 없기 때문에 항상 *args, **kargs형태로 작성해야함
    def perf_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()

        # 인자로 받아온 함수 실행 
        result = func(*args)
        
        # 함수 종료 시간
        et = time.perf_counter() - st
        
        # 실행 함수 명
        name = func.__name__
        
        # 함수 매개변수
        arg_str =', '.join(repr(arg) for arg in args)
       
       # 결과 출력
        print('[%0.5fs] %s(%s) -> %r'%(et, name, arg_str, result))

        return result

    return perf_clocked


# 인자로 제공할 함수 
def time_func(seconds) :
    time.sleep(seconds)
    
def sum_func(*numbers) :
    return sum(numbers) 


# 데코레이터 기능 미사용시 클로저의 바깥 함수를 실행해서 인자함수를 전달하고, 내부 함수(wrapper 함수) 객체를 받아옴
# 이때 내부함수는 인자로 전달한 함수를 free variable 형태로 인식, 즉 계속 기억하고 있음

non_deco1 = perf_clock(time_func)
non_deco2 = perf_clock(sum_func)



print(non_deco1, non_deco1.__code__.co_freevars)
print(non_deco2, non_deco2.__code__.co_freevars)

print('-'*40, 'Called Non Decorator -> time_func ')
print()

non_deco1(1.5)

print('-'*40, 'Called Non Decorator -> sum_func ')
print()
non_deco2(100, 200, 300, 400, 500)

# 데코레이터 방식으로 사용
@perf_clock
def time_func2(seconds) :
    time.sleep(seconds)
    
@perf_clock
def sum_func2(*numbers) :
    return sum(numbers)

print('-'*40, 'Called Decorator -> time_func ')
print()
time_func2(1.5)

print('-'*40, 'Called Decorator -> sum_func ')
print()
sum_func2(100, 200, 300, 400, 500)

# 즉, 데코레이터는 내가 작성한 함수에 추가 기능(함수의 수행시간을 구하는 등)을 덧붙이는 경우 유용함
# 내가 작성한 함수를 데코레이터 함수에 인자로 전달해, 데코레이터 내 wrapper함수에 의해 수행되는 방식으로 사용


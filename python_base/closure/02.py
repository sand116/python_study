# 클로저 함수 : 함수를 반환하는 경우 반환된 함수를 클로저라 함

# ex 1)
def calc1():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b    # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
    return mul_add          # mul_add 함수를 반환 * 함수 반환시 ()붙이지 않음
 
c = calc1() # c에 저장된 함수가 클로저 mul_add
print(c(1), c(2), c(3), c(4), c(5))


# 함수를 둘러싼 환경(지역 변수, 코드 등)을 계속 유지하다가, 함수를 호출할 때 다시 꺼내서 사용하는 함수를 클로저(closure)
# ex2) 
def calc2():
    a = 3
    b = 5
    return lambda x: a * x + b    # 람다 표현식을 반환
 
c = calc2()
print(c(1), c(2), c(3), c(4), c(5))


# 클로저 함수의 지역변수 변경하기 

def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        print(f'{x}, total  변경 전 : {total}')
        total = total + a * x + b
        print(f'{x}, total  변경 후 : {total}')
    return mul_add

# calc()함수가 mul_add 리턴을 통해 종료되었음에도 불구하고 mul_add는 calc함수의 지역변수들을 사용할 수 있다.
# total  값이 변경된 상태로 유지되고 있음을 알 수 있음 
c = calc()
c(1)
c(2)
c(3)
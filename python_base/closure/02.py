# 클로저 함수의 지역변수 변경하기 
def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(total)
    return mul_add
# calc()함수가 mul_add 리턴을 통해 종료되었음에도 불구하고 mul_add는 calc함수의 지역변수들을 사용할 수 있음
c = calc()
c(1)
c(2)
c(3)
# 전역 scope 에 선언된 변수는 지역에서 읽을 수 있으나 쓸 수는 없음
# 읽고 쓰기 위해서는 global 선언 필요

'''
전역변수는 주로 변하지 않는 고정 값에 사용
지역변수 사용 이유 : 지역변수는 함수 내에 로직 해결에 국한되는 것이 좋으며 함수 호출 해제시 소멸하기 때문에
전역변수를 지역 내에서 수정되는 것을 권장하지 않음


'''
c = 40

def foobar() :
    global c 
    c = 20
    print(c)

foobar()
print(c)

# 지역변수 안에 하위 지역변수가 있는 경우 상위 함수의 지역변수를 읽을 수 있으나 쓸 수없음
# 읽고 쓰기 위해서는 nonlocal로 선언 필요

def outer() :
    e = 70
    def inner() :
        nonlocal e 
        e += 10
        print('EX5 >', e)
        
    return inner


in_test = outer() # closure

in_test()
in_test()
in_test()
in_test()


# locals() 함수로 지역에 있는 객체들을 출력

def func(var) :
    x = 10
    def printer() :
        print('Printer Func Inner')
    print('Func Inner', locals())
    

func('Hi')



# globals() 로 전역에 있는 객체 출력

print(globals())
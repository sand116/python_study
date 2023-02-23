
'''
파이썬 변수는 네임스페이스에 저장된다.
locals()를 쓰면 현재 네임스페이스를 딕셔너리 형태로 출력할 수 있다
'''
x = 10

print(locals())

print("*"*100)

# 전역범위에서 출력하면 전역네임스페이스를 가져옴
# 함수 내에서 출력하면 함수 내의 locals()만 가져옴 

# 안쪽함수는 바깥함수에 변수에 접근할 수 있지만 바깥함수를 변경하지는 못한다. 같은 이름의 변수를 안쪽 함수 지역 내에 새로 생성한다.

# nonlocal

def A1():
    x = 10        # A의 지역 변수 x 
    def wrapper():
        nonlocal x    # 현재 함수의 바깥쪽에 있는 지역 변수 사용한다는 의미
        x = 20        # A의 지역 변수 x에 20 할당
        print(x)      # A의 지역 변수 x 출력
    return wrapper

def A2():
    x = 10        # A의 지역 변수 x 
    def wrapper():
        nonlocal x    # 현재 함수의 바깥쪽에 있는 지역 변수 사용한다는 의미
        x = 20        # A의 지역 변수 x에 20 할당
        return x      # A의 지역 변수 x 반환

    return wrapper()

def A3(x):
    def wrapper():
        x.append(20)
        print(x)    
    return wrapper

# A1 -> wrapper 함수 반환
b1 = A1()
print(b1)

# A2 -> wrapper 함수 호출한 후  wrapper함수의 리턴 값 반환
b2 = A2()
print(b2)

#

list_ = [] 
b3 = A3(list_)
print(b3)


b3()
b3()
b3()
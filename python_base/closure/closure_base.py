# 클로저 기초
# 외부에서 호출된 함수의 변수 값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근 가능

# 왜 클로저를 사용하는가?
# 기존에 만들어진 함수나 모듈 등을 수정하지 않고 wrapper 함수를 이용해서 자기 입맛에 맞게 조정할 수 있기때문에 사용

# 파이썬 변수 범위

# Ex 1

def func_v1(a):
    print(a)
    #print(b) b is undefined
    
func_v1(10)
b=20

# Ex 2

b=30

def func_v2(a):
    print(a)
    print(b)
    
func_v2(10)

# Ex 3

c = 30

def func_v3(a):
    global c
    print(a)
    print(c)
    c = 40

print('>>', c)
func_v3(10)
print('>>>', c)


def func_v4(list) :  # list = list_  -> 참조에 의한 할당으로 주소값을 복사하는 개념 (얉은 복사), 동일한 객체 참조
    list[0] = 100

list_ = [1,2,3]
print(list_)

func_v4(list_)
print(list_)


# Closure(클로저) 사용하는 이유 

# 서버 프로그래밍 -> 동시성(Concurrency) 제어 
# : 같은 메모리 공간에 여러 자원이 접근하여 교착상태(Dead Lock)에 빠질 수 있으므로 안정된 오픈소스를 사용함 ex) 톰캣
# : 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 ex) Erlang


# 클로저는 함수가 종료되어도 상태를 기억할 수 있음, 리턴할 때 함수를 리턴하여 변수에 할당하면 함수의 상태를 저장하여 계속적으로 사용 가능
# 공유하되 변경되지 않는(Immutable, Read Only) 자료구조를 적극적으로 사용할 수 있어 함수형 프로그래밍과 연결됨
# 결론 : 클로저는 불변 자료구조 및 atom, STM -> 멀티스레드(Coroutine) 프로그래밍에 강점 





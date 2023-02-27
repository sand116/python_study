# 클래스 vs 클로저

# 클래스 이용하여 결과를 누적하는 경우 

class Averager():
    def __init__(self):
        self._series = []

    # 함수처럼 호출 가능하게 해주는 매직 메서드
    def __call__(self, v):
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series,len(self._series)))
        return sum(self._series)/len(self._series)

# 인스턴스 생성
averager_cls = Averager()

# 누적, 함수처럼 호출
print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(50))

#closure 사용
def closure_averager():
    # Free variable
    # closure 영역
    series = []
    def averager(v):
        series.append(v)
        print('inner >> {} / {}'.format(series,len(series)))
        return sum(series)/len(series)
    return averager

# 함수 객체 할당
avg_closure = closure_averager()
print(avg_closure)# 함수 리턴

#함수를 호출할 때마다 자유 변수에 접근해서 새로운 값을 누적 
print(avg_closure(10)) 
print(avg_closure(20)) 
print(avg_closure(30)) 
print(avg_closure(40)) 
print(avg_closure(50)) 



def closure_count():
    # free variable
    i = 0
    def count():
        nonlocal i
        i +=1
        return i
    return count
                       
 
c = closure_count()
for i in range(10):
    print(c(), end=' ')
    

# function inspection
print()
print(avg_closure.__code__)
print(dir(avg_closure.__code__))
print(avg_closure.__code__.co_freevars[0])
print(avg_closure.__closure__)
print(dir(avg_closure.__closure__))

# free variable 출력 
print(avg_closure.__closure__[0].cell_contents)


# 클로저 기초
# 외부에서 호출된 함수의 변수 값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근 가능

# 왜 클로저를 사용하는가?
# 기존에 만들어진 함수나 모듈 등을 수정하지 않고 wrapper 함수를 이용해서 자기 입맛에 맞게 조정할 수 있기때문에 사용
# 서버 프로그래밍 -> 동시성(Concurrency) 제어 
# : 같은 메모리 공간에 여러 자원이 접근하여 교착상태(Dead Lock)에 빠질 수 있으므로 안정된 오픈소스를 사용함 ex) 톰캣
# : 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 ex) Erlang


# 클로저는 함수가 종료되어도 상태를 기억할 수 있음, 리턴할 때 함수를 리턴하여 변수에 할당하면 함수의 상태를 저장하여 계속적으로 사용 가능
# 공유하되 변경되지 않는(Immutable, Read Only) 자료구조를 적극적으로 사용할 수 있어 함수형 프로그래밍과 연결됨
# 결론 : 클로저는 불변 자료구조 및 atom, STM -> 멀티스레드(Coroutine) 프로그래밍에 강점 









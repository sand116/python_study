# 클래스 vs 클로저

# 클래스 이용하여 결과를 누적하는 경우 

class Averager():
    def __init__(self):
        self._series = []

    # 함수처럼 호출 가능하게 함  
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

def closure_ex1():
    # Free variable
    # closure 영역
    series = []
    def averager(v):
        series.append(v)
        print('inner >> {} / {}'.format(series,len(series)))
        return sum(series)/len(series)
    return averager

# 함수 객체 할당
avg_closure1 = closure_ex1()
print(avg_closure1) # 함수 리턴

#함수를 호출할 때마다 자유 변수에 접근해서 새로운 값을 누적 
print(avg_closure1(10)) 
print(avg_closure1(20)) 
print(avg_closure1(30)) 
print(avg_closure1(40)) 
print(avg_closure1(50)) 



def closure_ex2():
    # free variable
    i = 0
    def count():
        nonlocal i
        i +=1
        return i
    return count
                       
 
c = closure_ex2()
for i in range(10):
    print(c(), end=' ')
    

# function inspection

print()
print(dir(avg_closure1))

print()
print(dir(avg_closure1.__code__))
print(avg_closure1.__code__.co_freevars)

print(dir(avg_closure1.__closure__))

# free variable 출력 
print(avg_closure1.__closure__[0].cell_contents)


# 잘못된 클로저 사용 

def closure_ex3():
    # Free variable
    cnt = 0
    total = 0  
    def averager(v):
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure3 = closure_ex3()
#print(avg_closure3(10)) #예외 발생


def closure_ex4():
    # Free variable
    cnt = 0
    total = 0  
    def averager(v):
        # 지역변수가 아니라 자유변수임을 표시함
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    return averager

avg_closure4 = closure_ex4()
print(avg_closure4(10))
print(avg_closure4(20))
print(avg_closure4(30))
# 코루틴 : 단일(싱글) 스레드, 스택을 기반으로 동작하는 비동기 작업
# 쓰레드 : os 관리, cpu 코어에서 실시간, 시분할 비동기 작업 -> 멀티쓰레드

# 코루틴 제어, 상태, 양방향 전송

# 서브루틴 : 메인루틴 호출 -> 서브루틴에서 수행(흐름제어)
# 코루틴 : 루틴 실행 후 중지 -> 동시성 프로그래밍
# 코루틴 : 쓰레드에 비해 오버헤드 감소 
# 쓰레드 : 싱글 스레드 -> 멀티 스레드 -> 복잡 -> 공유하는 자원 -> 교착 상태 발생 가능성, 컨텍스트 스위칭 비용 발생, 자원 소비 가능성 증가


# 코루틴 ex1

def coroutine1():
    print('>>> coroutine started.')
    i = yield
    print('>>> coroutine received : {}'.format(i))
    
# main routine
# 제네레이터 선언

cr1 = coroutine1()
print(cr1, type(cr1))

# yield  지점까지 서브루틴 수행
# next(cr1)

# 기본 전달 값 None
# next(cr1)

# 값 전송
# cr1.send(100)


# coroutine ex2
# gen_created : 처음 대기 상태
# gen_suspended : yield 대기 상태
# gen_closed : 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine started. : {}'.format(x))
    y = yield x
    print('>>> coroutine received. : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received. : {}'.format(z))
    

cr3 = coroutine2(10)

from inspect import getgeneratorstate

# 코루틴 실행 - 첫 yield 실행 후 값 반환
print(getgeneratorstate(cr3))
print(next(cr3))

# next 실행 후 y 값을 받기위한 대기상태 돌입
print(getgeneratorstate(cr3))

# 100 전송하고 다음 yield에서 값 받아옴
print(cr3.send(100))

# 200 전송하고 다음 yield에서 값을 받아오고 싶으나 다음 yield가 없어 stopIteration 돌입
#print(cr3.send(200))

    
# python 3.5부터 def -> async, yield -> await으로 변경하여 사용 가능

# coroutine Ex3
# StopIteration 자동 처리 (3.5 -> await으로 자동 처리)

# 중첩 코루틴 처리

def generator1() :
    for x in 'AB' :
        yield x
    for y in range(1,4) :
        yield y
        

# generator로 iterator 객체 반환
t1 = generator1()
# ㅣ
print(list(t1))


def generator2() :
    yield from 'AB'
    yield from range(1,4)
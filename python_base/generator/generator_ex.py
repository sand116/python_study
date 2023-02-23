# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 코루틴 : 단일 프로그램 안에서 여러 일을 쉽게 해결
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도

# Generator Ex1


def number_generator1():
    x = [1, 2, 3]
    for i in x:
        yield i # yeild 1,2,3 
 
for i in number_generator1():
    print(i)
    
    
def number_generator2():
    x = [1, 2, 3]
    yield from x    # 리스트에 들어있는 요소를 한 개씩 바깥으로 전달
 
for i in number_generator2():
    print(i)

# return을  yield로 대체 :  값을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보

def generator_ex1() :
    print('Start')
    yield ' A point ' # 네이버에서 크롤링
    
    print('Continue')
    yield ' B point ' # 구글에서 크롤링
    
    print('End')
    # yield 'End'
    
#temp = iter(generator_ex1())

#print(next(temp))
#print(next(temp))
#print(next(temp))


# for문은 예외처리 내부적으로 함
for v in generator_ex1() :
    #print(v)
    pass

# generator Ex2

temp2 = [x*3 for x in generator_ex1()]
temp3 = (x*3 for x in generator_ex1())

print(temp2)


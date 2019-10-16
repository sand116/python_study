# 제네레이터 - 이터레이터를 생성해주는 함수(iterator를 상속받음) : 함수 안에 yeild라는 키워드만 사용하면 그 함수는 이터레이터가 됨
# return을  yield로 대체 :  값을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보

    
    
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
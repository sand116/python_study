a = 3 #전역변수는 변경되지 않고 다른 함수나 지역에서 변경되지 않는 값으로 설정
def change() :
    a = 4 #변경되지 않음
change()
print('a',a) #전역변수에서 설정한 것과 함수내에서 설정한 값이 다름 

b = 3
b = 4
print('b',b)

c=3 

def change2(c) :
    print('c',c,id(c)) #매개변수로 넘겨주는 순간에는 같은 id 를 가지지만 ,
    # c = 4 라고 추가하는 순간 이때 c는 함수지역에서 새롭게 할당한 참조변수이다
    c=4
    print('c',c,id(c))
    
change2(c)
print('c',c,id(c)) 

d=3 
def change3() :
    global d #이는 전역변수에서 사용한 d임을 선언했기때문에 d=4를 하여도, 새로운 지역변수로 할당하지 않는다
    d = 4
    print('d',d,id(d))
change3()
print('d',d,id(d))
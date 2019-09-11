# 기존에 만들어진 함수나 모듈 등을 수정하지 않고 wrapper 함수를 이용해서 자기 입맛에 맞게 조정할 수 있기때문에 사용

def func1(num) :
    num = 10 
x=10
print(x)
func1(x) # num = x  -> 단순 복사 :  이므로 num 이 변해도 바뀌지가 않음 -> 지역 변수인 num에 새 변수가 할당되는 것
print(x)


def func2(list) :
    list[0] = 100

list_ = [1,2,3]
print(list_)
func2(list_) # list = list_ -> 단순 복사여도 바뀜 - 동일한 객체 참조 
print(list_)
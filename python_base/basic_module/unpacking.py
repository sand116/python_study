#언패킹
def print_numbers(a,b,c) :
    print(a)
    print(b)
    print(c)
    

x = [10, 20, 30]
print_numbers(*x)


#위치 인수를 사용하는 가변 인수 함수 만들기
# 함수 인자에 *가 들어가는 경우 
def get_max_score(*args) :
    # args -> 튜플 
    return max(args)
    
korean, english, mathematics, science = 100, 86, 81, 91
max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)
 
max_score = get_max_score(english, science)
print('높은 점수:', max_score)

#------------------------------------------
def personal_info1(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)
    
personal_info1(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})
# * -> 딕셔너리의 key 넘겨줌
# ** -> 딕셔너리 value 넘겨줌




#키워드 인수를 사용하는 가변 인수 함수 만들기
# 함수인자에 **가 들어가는 경우 

def personal_info2(**kwargs):
    #kwargs -> {'name': '홍길동'}
    print(kwargs)
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')
#1
personal_info2(name='홍길동')

#2
x = {'name': '홍길동'}
personal_info2(**x)
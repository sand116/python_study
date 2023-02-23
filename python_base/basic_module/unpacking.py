#언패킹

# 튜플 언패킹

def print_numbers(a,b,c) :
    print(a)
    print(b)
    print(c)
    

x = [10, 20, 30]
print_numbers(*x)


#위치 인수를 사용하는 가변 인수 함수 만들기
# 함수 인자에 *가 들어가는 경우 arg로 받는 모든 인자를 튜플 형태로 묶음, 따라서 몇개의 인자를 제공하더라도 상관이 없음
def get_max_score(*args) :
    # args -> 튜플 
    return max(args)
    
korean, english, mathematics, science = 100, 86, 81, 91

# 인자 개수 상관 없음 
max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)
max_score = get_max_score(english, science)
print('높은 점수:', max_score)


# 튜플 언패킹 후 전달 
subjects = (100, 86, 81, 91)
max_score = get_max_score(*subjects)
print('높은점수:', max_score)

#------------------------------------------

# 딕셔너리 언패킹

def personal_info1(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info1(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})

# * -> 딕셔너리의 key 넘겨줌
# ** -> 딕셔너리 value 넘겨줌




#키워드 인수를 사용하는 가변 인수 함수 만들기
# 함수인자에 **가 들어가는 경우, key=value~ 형태로 제공되는 모든 인자를 딕셔너리로 묶음, 몇개의 인자를 받더라도 상관이 없음

def personal_info2(**kwargs):
    print(kwargs)
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')

#1 인자개수 상관 없음
personal_info2(name='홍길동', age=23, adress='용산구 이촌동')

#2 딕셔너리 언패킹 후 전달
x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}


# error 발생 personal_info2(*x)
# 언패킹하여 전달하면, kwargs 함수는 다시 패킹하여 딕셔너리 형태로 받음
personal_info2(**x)
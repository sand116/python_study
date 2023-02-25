# 객체의 복사 종료 :  Copy, Shallow Copy, Dee copy

# 가변 : list, set, dict

'''
단순복제

call by refernce

a 는 리스트 객체의 주소를 바라보는 변수, 그런뒤 a 를 b 에 할당해 주었습니다. 
그러면 b 는 a 와 같은 객체의 주소를 바라보게 됩니다.

'''
a = [1, 2, 3, 4]
b = a     

b[2] = 100   # b의 item 변경

print(id(b), id(a))   
print(a)    # [1, 2, 100, 4], a의 item도 수정됨!!

# 'a 와 b 가 동일한 객체를 참조하기 때문  - 리스트 객체의 주소


a = 10
b = a #  같은 객체 참조
print(b)    # 10 출력
b = "abc" # 새 객체 할당
print(b)    # abc 출력
print(a)    # 10 출력

'''
위의 경우처럼 복사된 참조 변수를 수정했을때, 처음에 할당한 참조 변수의 값 역시
똑같이 수정되는 것은 리스트와 같은 변경가능(mutable) 객체일 때만 해당한다는 것입니다. 
변경 가능 객체는 list, dict, set

숫자나 문자열과 같은 불변의(immutable) 객체일때는 위의 경우가 해당되지 않습니다.
이때, 참조변수를 수정한다는 것은 같은 주소의 객체 값(value)이 바뀌는 것이 아니라
그 변수에 새로운 객체가 할당되는 것
변경 불가능한 객체는 int, str, tuple, float, bool
'''
  
  
'''
shallow copy 

단순 복제와 얕은 복사의 차이점은 복합객체(리스트)는 별도로 생성하지만
그 안에 들어가는 내용은 원래와 같은 객체 객체라는 점

'''

import copy

c = [1, 2,3, [4, 5, 6]]

#  내부 객체가 immutable 객체의 경우

d = copy.copy(c)    # shallow copy 발생

print(id(c), id(d))  
d[0] = 100

print(d)    # [100, [1, 2, 3]] 출력,
print(c)    # [1, [1, 2, 3]] 출력, shallow copy 가 발생해 복사된 리스트는 별도의 객체이므로 item을 수정하면 복사본만 수정된다.

# 내부 객체가 mutable한 경우

d[-1].append(7)    # 리스트의 두번째 item(내부리스트)에 4를 추가
print(c)    # [1, [1, 2, 3, 4]] 출력
print(d)    # [1, [1, 2, 3, 4]] 출력, a가 c와 똑같이 수정된 이유는 리스트의 item 내부의 객체는 동일한 객체이므로 mutable한 리스트를 수정할때는 둘다 값이 변경됨


# 해시 테이블 : 적은 리소스로 많은 데이터를 효율적으로 관리
# key에 value를 저장하는 구조로 파이썬 dict : 해시 테이블 
# 키 값의 연산 결과(해시값)에 따라 직접 접근이 가능한 구조
# key 값을 해싱 함수 -> 해시 주소 - key에 대한 value 참조
# Dict -> Key 중복 허용X, Set -> 중복 허용 X, 


# dict 구조
# print(__builtins__.__dict__)

# hash 값 확인
t1 = (10,20,(30,40,50))
t2 = (10,20,[30,40,50])

# hash함수를 사용할 수 있으려면 객체가 불변형이어야함.
print(hash(t1))
#print(hash(t2)) - 리스트가 가변형이므로 예외 발생

# Dict Setdefault  예제

source =( 
          ('k1','val1'),
          ('k1','val2'),
          ('k2','val3'),
          ('k2','val4'),
          ('k2','val5')       
        )

new_dict1={}
new_dict2={}

# 증복 없음
print(dict(source))

# No use Setdefault

# key는 랜덤하게 리턴, 순서 존재 x
for k,v in source :
    if k in new_dict1:
        new_dict1[k].append(v)
    else :
        new_dict1[k]=[v]
print(new_dict1)

# Use Setdefault
for k, v in source:
    new_dict2.setdefault(k,[]).append(v)

print(new_dict2)

# dict.get('키')
# 키 값이 없어도 에러를 뱉지않고 None 을 뱉음. if문에 유용하게 사용

# error
#if new_dict1['k3'] :
if new_dict1.get('k3') :
    print("있음")
else : print("없음")  

# immutable Dict
from types import MappingProxyType

# 수정 가능- 수정 가능하므로 hash(d) 예외발생 
d = {'key1' : 'value1'}

# 수정 불가 
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen,id(d_frozen))


d['key2']='value2'
#d_frozen['key2']='value2' 불가능









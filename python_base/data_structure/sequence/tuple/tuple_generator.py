# generator 생성
import array

# array : numpy와 같은 수치 연산이나 하나의 자료형을 사용하는 경우
# generator : 한 번에 한 개의 항목을 생성하며, 메모리를 유지하지 않음

chars = '!@##$$%%%^^^&&&*'

list_ng = [ord(s) for s in chars]
tuple_g = (ord(s) for s in chars)
# 정수형 :'I'
array_g = array.array('I',(ord(s) for s in chars))

print(type(list_ng))

print(type(tuple_g))
print(next(tuple_g))
print(next(tuple_g))

print(type(array_g))
print(array_g)
print(array_g.tolist())


# 제네레이터 예제
print(('%s' %c+str(n) for c in ['a','b','c','d'] for n in range(1,21)))

# 출력 : <generator object <genexpr> at 0x0000017285037CF0>

for s in ('%s' %c + str(n) for c in ['a','b','c','d'] for n in range(1,21)) :
    print(s)
    

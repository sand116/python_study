#unpacking


#b, a = a, b

print(divmod(100,9))
print(divmod(*(100,9)))
print(*divmod(100,9))

x, y, *rest = range(10)
print(x, y, rest)

x, y, *rest = range(2)
print(x, y, rest)


# mutable vs immutable

l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l*2
m = m*2

print(l, id(l))
print(m, id(m))

l *=2
m *=2


print(l, id(l))
print(m, id(m))
# tuple은 계속 새로운 id를 할당받음
# list는 연산자에 따라 id가 변경되기도 하고 변경되지 않기도 함 


# sort vs sorted

# sorted : 정렬 후 새로운 객체 반환
# sort : 정렬 후 객체 직접 변경, 반환값 존재 x

f_list = ['orange','apple','banana','coconut','papaya','cherry']

print('sorted - ',sorted(f_list,key=len, reverse=True))
print('sorted - ',sorted(f_list,key=lambda x: x[-1], reverse=True))

print('sort - ',f_list.sort(key=len, reverse=True), f_list)
print('sort - ',f_list.sort(key=lambda x:x[-1], reverse=True), f_list)



# list vs array 적합한 사용법 설명

#리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
#숫자 기반 : 배열(리스트와 거의 호환)
# Set - 중복 허용하지 않는 집합으로 변경 가능 

s1={'apple','orange','bananna','kiwi','orange'}
s2=set(['apple','orange','bananna','kiwi','orange'])
s3={3}
s4=set()

s5=frozenset({'apple','orange','bananna','kiwi','orange'})

s1.add('Melon')
# s5.add('Melon')


# 선언 최적화

# 바이트코드 -> 파이썬 인터프리터 실행

from dis import dis

print('------------')
print(dis('{10}'))


print('------------')
print(dis('set([10])'))


# 지능형 집합


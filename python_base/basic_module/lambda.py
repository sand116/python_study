'''

lambda 장점 : 익명, 힙 영역에서 사용 즉시 소멸, pythonic
일반함수 : 재사용성 위해 메모리에 저장
시퀀스형 전처리에 reduce, map, filter 주로 사용

'''

cul = lambda a, b, c : a*b+c

print('ex : ',cul(10, 15, 20))
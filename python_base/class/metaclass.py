'''
Meta Class

1. Class of class
2. Type
3. Meta Class
4. Custom Meta Class

why? meta class?
1. class를 만드는 역할 -> 의도하는 방향으로 class를 생성하도록 함
2. 프레임워크 작성 시 필수
3. 동적 생성 (type), 커스텀 생성(type) 함수
4. 커스텀 클래스 -> 검증 클래스 등
5. 엄격한 class 사용 요구 ex)메소드 오버라이드 요구, 즉 구현 레벨에서 요구를 할 수 있음

 
'''

# EX 1 
# type 예제
# type 이란 class를 만드는 class를 의미한다.
class SampleA(): # class == object
    pass

# obj1 -> sampleA 객체(인스턴스)
obj1 = SampleA()
print('Ex 1 > ', obj1.__class__)
print('Ex 1 > ', SampleA.__class__)

print('Ex 1 > ', type(obj1))
print('Ex 1 > ', type(obj1) is obj1.__class__)

# class의 class, 즉 meta class는 type class 를 의미
print('Ex 1 > ', obj1.__class__.__class__)


# type()으로 동적 클래스 생성하기
# Names(아름), Bases(상속), Dict(속성, 메소드 (즉, namespace))
s1 = type('SampleB', (),{})
print('Ex 1 > ', s1.__class__)
print('Ex 1 > ', type(s1))
print('Ex 1 > ', type(s1) is s1.__class__)
print('Ex 1 > ', s1.__base__)
print('Ex 1 > ', s1.__dict__)





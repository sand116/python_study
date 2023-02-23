# Iterator, generator 
# iterable한(반복가능한) 객체를 생성 


# 파이썬 반복 가능한 타입
# collections, text file, list, Dict, Set, Tuple, unpacking, *args.. : iterable

# for문으로 반복가능한 이유 -> 내부적으로 iter(x) 함수 호출하여 이터레이터 객체 생성
t = 'ABCD'

print(dir(t))

for c in t :
    print(c)

# __iter__ method를 가지는 객체로, iter()를 호출하여 이터레이터 객체를 생성하게 되면 반복 가능한 객체가 된다.
w = iter(t)
print(dir(w))

# while
w = iter(t)
print(next(w))
print(next(w))
print(next(w))
print(next(w))


while True:
    try :
        print(next(w))
    except StopIteration:
        break
    
# 반복형인지 확인하는 방법
from collections import abc

from pyparsing import Word

print(dir(t))
print(hasattr(t,'__iter__'))

# iterable 상속받았는지 확인
print(isinstance(t, abc.Iterable))
      
print()
print()

# iterator 객체는 내부적으로 __next__ method를 가지기 때문에 반복 가능함
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')
        
    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration')
        self._idx +=1
        return word
    
    def __repr__(self) :
        return 'WordSplit(%s)'%(self._text)
        
wi = WordSplitter('Do today what you could do tomorrow')

print(wi)
print(next(wi))
print(next(wi))

#print(next(wi))


print()
print()



# Generator  패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가, 증가 후 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2. 단위 실행 가능한 코루틴 구현과 연동
# 3. 작은 메모리 조각 사용

# generator란? 

'''

iterator 객체를 생성해주는 함수를 의미한다.
일반적으로 __iter__ 메서드와 __next__메서드를 이용하여 iterator 객체를 생성하나,
함수 안에 yield를 가지는 경우, 해당 함수를 호출하면 generator 객체(여기서는 iterator 객체)가 생성된다.

generator로 생성된 iterator객체도 동일하게 __iter__, __next__ 메서드를 내부적으로 가지며
__next__를 호출하면 함수 안의 yield까지의 코드를 실행시켜 값을 발생 시킨다.

또한, raise로 직접 StopIteration 예외를 발생시키지 않아도 함수의 끝까지 도달하면 자동으로 에러를 발생시킨다.

'''

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')
    
    # __iter__ 메서드 안에 yield를 사용하여, iter() 호출 시 generator객체(정확히는 generator로 생성된 iterator객체) 생성하도록 함
    def __iter__(self):
        # for문에서 yield를 실행
        for word in self._text:
            yield word

    def __repr__(self) :
        return 'WordSplitGenerator(%s)'%(self._text)
        
    
wg = WordSplitGenerator('Do today what you could do tomorrow')

wt = iter(wg)
print(wt, dir(wt))


print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))

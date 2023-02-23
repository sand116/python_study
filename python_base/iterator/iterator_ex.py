# 병행성(Concurrency)
# 이터레이터, 제네레이터
# Iterator, Generator

# 파이썬 반복 가능한 타입
# for, collections, text file, List, Dict, Set, Tuple, unpacking, *args

# 반복 가능한 이유? -> iter(x) 함수 호출
t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# for 반복
# for c in t:
#     print(c)


# while 반복

# iter method를 통해 반복 가능한 객체 호출
# iter로 생성된 객체는 __next__  method 를 가짐

w = iter(t)
print(dir(w))



while True:
    try:
        print(next(w))
    except StopIteration:
        break

print()

from collections import abc

# 반복형 확인
print(hasattr(t, '__iter__'))
print(isinstance(t, abc.Iterable))

print()
print()

# next 사용
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')
    
    def __next__(self):
        # print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')
        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


wi = WordSplitter('Do today what you could do tomorrow')

print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))

print()
print()
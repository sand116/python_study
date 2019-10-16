# 양쪽방향에서 요소를 추가하거나 제거할 수 있는 자료구조를 deque라고 함
import collections
import sys


N = int (sys.stdin.readline())
q = collections.deque([ i for i in range(1,N+1) ])
while (q.__len__() > 1) :
    q.popleft()
    q.rotate(-1)

print(q.pop())
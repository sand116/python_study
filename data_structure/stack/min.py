# 스택 시간복잡도 O(1)으로 최소값 구하기
# O(1) 의 시간복잡도를 가진다는 것은 hash, dictionary 처럼 변수에 직접 접근한다는 의미
# 변수 mins와 min을 추가하여 최소값에 바로 접근 할 수 있도록 한다.
'''

스택은 모든 요소들을 Pop하기 이전에는 그 값들을 엑세스할 수 없다는 단점이 있다. 기껏해야 스택 맨 위에 있는 요소(Top)만을 Peek()를 통해 알 수 있는 정도이다.

따라서 최소값을 갖는 요소를 구하기 위해서는 스택에 요소를 추가할 때, 최소값에 대한 정보를 함께 저장해야 한다. 예를 들어, 매번 요소가 추가될 때, 기존 최소값과
 추가되는 요소 값을 비교하여 추가 요소가 더 작으면 현재 요소까지의 최소값은 새로 추가되는 요소값이 된다. 따라서 스택에 요소 값을 저장할 때, 요소값과 함께 그 요
 소까지의 최소값을 함께 저장하면 Min() 메서드 는 O(1) 의 Time Complexity를 갖게 된다. 
'''
import unittest
class Stack():
    def __init__(self):
        self.items = [] # 새로 받은 것들을 넣는 stack
        self.mins = [] # 가장 최신의 min 말고 직전 시점까지  최솟값이 현재 무엇인지 저장하는 stack
        self.min = None #최솟값은 지정됨 - 지금까지 stack에 쌓인 것중 최솟값을 항상 리턴

    def push(self, item):
        self.items.append(item)
        if self.min != None :
            self.mins.append(self.min)
        if self.min is None or self.min > item:
            self.min = item
    # 7 6 5 8 9 
    # 7 6 5 5 5
    # 5 
    def pop(self):
        self.items.pop()
        self.min = self.mins.pop() # min이 빠지고 나서 그 다음으로 큰 값을 min  으로 변경함

    def get_min(self):
        return self.min
    # 체크 코드 
    
    def peak(self):
        return self.items[-1]


class Test(unittest.TestCase) :
    def test(self) :
        stack = Stack()
        stack.push(5)
        stack.push(3)
        stack.push(2)
        stack.push(7)
        self.assertEqual(2,stack.get_min())
        stack.pop()
        stack.pop()
        self.assertEqual(3,stack.get_min())
        
        
        
if __name__ == '__main__':
    unittest.main()
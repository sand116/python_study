# 스택을 set으로 구현하기
# 스택 공간이 꽉 찰 경우 이를 스택 리스트로 보내기 

import unittest

class Stack :
    def __init__(self) :
        self.max = 3
        self.items = []
    def push(self,item) :  
        self.items.append(item) 
    def pop(self) :
        return self.items.pop()
    def peek(self) :
        return self.items[len(self.items)-1]
    def is_empty(self) :
        return self.items == [] 
    # self.items == [] 가 참이면 True 반환 거짓이면 False 반환
    
class StackList : 
    def __init__(self) :
        self.stackList = []
        self.stackMax = 3
        self.stackList.append(Stack())
        # 처음 객체 만들때 stack 만들어줌
    def push(self,item) :
        st = self.getLastStack() 
        # 마지막 stack
        if len(st.items) == self.stackMax :
            newStack = Stack()
            newStack.push(item)
            self.stackList.append(newStack)
        else :
            st.push(item)
    def pop(self) :
        st = self.getLastStack()
        if st.is_empty() :
            self.stackList.pop()
            st = self.getLastStack()
            st.pop()
        else : 
            st.pop()
    def getLastStack(self) :
        return self.stackList[len(self.stackList)-1]
    
    def printStack(self) :
        result = []
        for st in self.stackList :
            for item in st.items:
                result.append(item)
        return result

class Test(unittest.TestCase) :
    def test(self) :
        stacks = StackList()
        stacks.push(5)
        stacks.push(3)
        stacks.push(2)
        stacks.push(7)
        self.assertEqual([5,3,2,7],stacks.printStack())
        stacks.pop()
        stacks.pop()
        self.assertEqual([5,3],stacks.printStack())
        
        
        
if __name__ == '__main__':
    unittest.main()
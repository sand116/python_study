import sys
class Stack :
    def __init__(self) :
        self.items = []
    def push(self,item) :  
        self.items.append(item)
    def pop(self) :
        if self.items == [] :
            return -1
        else :
            return self.items.pop()
    def empty(self) :
        return int(self.items == [])
    def size(self) :
        return len(self.items)
    def top(self) :
        if self.items == [] :
            return -1
        else :
            return self.items[-1]

N = int(input())
stack = Stack()
for i in range(N) :
    order = sys.stdin.readline().rstrip().split()
    if order[0] == "push" :
        stack.push(order[1])
    elif order[0] == "pop" :
        print(stack.pop())
    elif order[0] == "empty" :
        print(stack.empty())      
    elif order[0] == "size" :
        print(stack.size())
    elif order[0] == "top" :
        print(stack.top())

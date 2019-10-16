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
        return self.items == []
    
    def size(self) :
        return len(self.items)
    
    def top(self) :
        if self.items == [] :
            return -1
        else :
            return self.items[-1]

def check( list ) :
    stack = Stack()
    for i in list :
        if i == "(" :
            stack.push(i)
        elif i == ")" :
            if stack.pop() == -1 :
                return "NO"
    if stack.empty() == True :
        return "YES"
    else : return "NO"
        
    

N = int(input())
result = []
for i in range(N) :
    ps = list(input())
    result.append(check(ps))
    
for i in result :
    print(i)
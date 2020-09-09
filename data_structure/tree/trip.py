# 12 5 10 9 8 2 1 순으로 입력을 받고 트리에 insert 한다. 하나의 트리 안에 넣음을 기준으로 한다
# 구현 기능 - insert, delete, merge, kth, countlessthan 
import random

class node() :
    def __init__ (self, value) :
        self.value = value
        self.priority = random.random()
        self.size = 1 # 해당 노드를 기준으로 한 서브트리의 사이즈 
        self.left = None
        self.right = None

class Trip() :
    def __init__(self) :
        self.root = None
        
    def insert(self, new) :
        if self.root == None :
            self.root == new
            return
        else :
            self.insert_by_value(self.root, new)
            
    def insert_by_value(self, root, new) :
        if root.priority > new.priority :
            if root.value > new.value :
                root.left = self.insert_by_value(root.left, new)
                root.size += root.left.size      
            else :
                root.right = self.insert_by_value(root.right, new)
                root.size += root.right.size
            return root 
        else : 
            left, right = self.split(root.left, new)
            new.left = left
            new += left.size
            new.right = right
            new += right.size
            return new
                        
    def split(self, root, new) :
        if root == None :
            return None, None
        elif root.value < new.value :
            left, right = self.split(root.right,new)
            root.right = left
            return root, right
        
        elif root.value > new.value :
            left, right = self.split(root.left, new)
            root.left = right
            return left, root
        
    def merge(self, root1, root2) :
        if root1 == None :
            return root2
        elif root2 == None :
            return root1
         
        if root1.priority > root2.priority :
            if root1.value < root2.value :
                root1.right = self.merge(root1.right, root2)
            else :
                root1.left = self.merge(root1.left, root2)
            return root1
        else : 
            if root2.value < root1.value :
                root2.right = self.merge(root1,root2.right) 
            else :
                root2.left = self.merge(root1, root2.left)
            return root2 
        
    def delete(self, root, node) :
        if root.value == node.value :
            del root 
            return self.merge(root.left, root.right)
            
        elif root.value < node.value :
            root.right = self.delete(root.right,node)
        else :
            root.left = self.delete(root.left, node)
        
        return root 
            
        
            
        
        
        
N = int(input())
tree = Trip()
for i in range(N) :
    new_node = node(int(input()))
    tree.insert(new_node)
# insert 함수에서 
# 지배 당하는지 확인하는 함수 
# 지배 하는지 확인하는 함수 


class TreeNode() :
    def __init__(self,x,y) :
        self.x = x
        self.y = y
        self.left = self.right = None
        
class BinaryTree() :
    def __init__(self) :
        self.root = None
    def insert :
    
cnt = 0

def is_dominate(pre_node, new_node ) :

    # 지배 당하는지 확인
    if new_node.x < pre_node.x and new_node.y < pre_node.y :
        return 
    else :
        if new_node.x < pre_node.x :
            is_dominate(pre_node.left, new_node)
            
        
        
N = int(input())
tree = BinaryTree()

for i in range(N) :
    x,y = map(int, input().split())
    new = TreeNode(x, y)
    is_dominate(tree.root,new )
class TreeNode :
    def __init__(self, value) :
        self.children = []
        self.value = value
longest = 0 

def height(root) :
    if root.children == None :
        return 0
    
    chidren_heights = []
    for i in root.children :
        children_heights.append(height(root.children))
        
       
def ischild(a, b) : # 직접적인가 아닌가
    for node in b.children :
        if a == node.children :
            return False
    
      
def get_tree(root) :
    tree_node = Node(root)
    for i in array :
        if ischild(i,tree_node) :
            tree_node.children.append(get_tree(i))
    return tree_node
        


N =int(input())
array = []
for i in range(N) :
    array.append(list(map(int,input().split())))
array.sort(key = lambda node_size : node_size[2],reverse = 1)
get_tree(array[0])

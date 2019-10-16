# bst
# search 시간복잡도 o(h) h = tree의 높이
# insert o(h)
# delete - 3가지 케이스 : 자식노드가없는 경우, 자식노드가 1개인 경우, 자식노드가 2개인 경우 o(h)
# node - left /right
class BinarySearchTree :
    class Node :
        def __init__(self,data, left=None, right=None) :
            self.data = data
            self.left = left
            self.right = right
    def __init__(self) :
        self.root = None
    def is_empty(self) :
        return self.root == None
    def bst_search(self,data) :
        if self.is_empty() :
            return None
        else :
            return self.__find(self.root,data)
    def __find(self, node, data) :
        if data == node.data :
            return node
        elif node.left != None and data < node.data :
            self.__find(node.left,data)
        elif node.right != None and data > node.data :
            self.__find(node.right,data)
        else :
            return None

    def bst_insert(self, new_data) :
        if self.is_empty() :
            self.root = self.Node(new_data)
        else :
            self.__bst_insert_by_value(self.root, new_data)
    def __bst_insert_by_value(self, compare_node, new_data) :
        if new_data < compare_node.data :
            if compare_node.left != None:
                self.__bst_insert_by_value(new_data, compare_node.left)
            else:
                compare_node.left = self.Node(new_data)
        else:
            if compare_node.right != None:
                self.__bst_insert_by_value(new_data, compare_node.right)
            else:
                compare_node.right = self.Node(new_data)
                
    def bst_delete(self, data) :
        p, cur, relation = self.__delete_find(data)
        if relation == None :
            print("찾는 결과가 없습니다")
        else :
            if cur.left == None and cur.right == None : #자식노드 없는경우
                if relation == 0 :
                    p.right = None
                else : p.left = None
            elif  cur.left == None :
                if relation == 0 :
                    p.right = cur.right
                else : p.left = cur.right
            elif  cur.right == None :
                if relation == 0 :
                    p.right = cur.left
                else : p.left = cur.left
            else : 
                successor , succesor_p, relation = self.successor(cur) #cur보다 큰 값을 가진다 가정
                cur.data = successor.data
                if relation == 0 :
                    succesor_p.right = successor.right
                elif relation == 1 :
                    succesor_p.left = successor.right
    def successor(self,cur) :
        p = cur # 현재의 오른쪽 노드들 중 가장 왼쪽 노드 찾기
        successor = cur.right
        relation = 0
        while successor.left != None :
            relation = 1
            p = successor
            successor = successor.left
        return successor, p, relation
                 

    def __delete_find(self, data) : #부모와 현재 노드 찾기
        p = self.root
        cur = self.root
        relation = 0 #0이면 right , 1이면 left
        
        if cur.left == None and cur.right == None :
            if cur.data == data :
                return p, cur, relation
            else :
                return None, None, None 
        while (cur.left != None or cur.right != None) :
            if data == cur.data :
                return p, cur, relation
            elif cur.left != None and data < cur.data :
                p = cur
                cur = cur.left
                relation = 1
            elif cur.right != None and data > cur.data :
                p = cur
                cur = cur.right
                relation = 0
            else :
                return None, None, None
    
        
            
            
        # 자식노드 없는경우 -> 자기를 연결하는 부모 노드와 연결을 끊으면됨
        # 하나인경우  -> 자신의 자식 노드와 부모노드를 연결
        # 두개인 경우 -> 자기와 가장 근접한 노드와 부모노드를 연결 
        
    
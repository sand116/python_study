'''
size(self) : 연결 리스트의 크기(항목 수)
is_empty(self) : 연결 리스트의 항목이 없는지(empty)의 여부
search(self, target) : 탐색, 순차탐색을 하므로 수행시간은 O(N)
insert_front(self, item) : 새 노드를 처음에 삽입, O(1)
insert_after(self, item, p) : p가 가리키는 노드 다음에 새 노드를 삽입, O(1)
delete_front(self) : 처음의 노드 삭제, O(1)
print_list(self)

'''
class EmptyError(Exception) :
    def __init__(self,message) :
        print(message)
    

class LinkedList :
    class Node :
        def __init__(self, value, next = None) :
            self.value = value 
            self.next = next 
                       
    def __init__ (self) :
        #참조자
        self.head = None
        self.size = 0
        
    def is_empty(self) :
        return self.size == 0
    
    
    #  노드 앞으로 삽입
    def front_insert(self, value) :
        if self.is_empty() :
            self.head = self.Node(value)
        else :
            self.head = self.Node(value, self.head)

        self.size += 1
    
    # 특정 노드 뒤에 새롭게 삽입 & 맨 뒤에 삽입
    def after_insert(self,value, before) :
        new_node = self.Node(value,before.next)
        before.next = new_node
        self.size += 1
    
    
    def front_delete(self) :
        if self.is_empty():  # empty인 경우 에러 처리
            raise EmptyError('Underflow')
        self.head = self.head.next
        self.size -= 1    
            
    def after_delete(self, p) :
        if self.is_empty():  # empty인 경우 에러 처리
            raise EmptyError('Underflow')
        t = p.next
        p.next = t.next
        self.size -= 1
    
    def print_list(self) :
        if self.is_empty() :
            raise EmptyError('Underflow')            
        t = self.head
        while( t != None) :
            print(t.value, end=" ")
            t = t.next
        print('\n')
            




if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.front_insert(3)
    linked_list.front_insert(4)
    linked_list.front_insert(5)
    linked_list.front_insert(6)
    linked_list.after_insert(7,linked_list.head)
    linked_list.print_list()
    linked_list.front_delete()
    linked_list.front_delete()
    linked_list.after_delete(linked_list.head)
    linked_list.print_list()

    
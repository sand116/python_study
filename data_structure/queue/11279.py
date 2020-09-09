import sys
class Heap :
    def __init__(self) :
        self.heap_list = []
    
    def heap_insert(self, num) :
            self.heap_list.append(num)
            index = len(self.heap_list) - 1 
            while (index >= 1) :
                parent = index//2
                if self.heap_list[parent] >= self.heap_list[index]:
                    break
                self.heap_list[parent], self.heap_list[index] = self.heap_list[index],self.heap_list[parent]
                index = parent
    def heap_delete(self) :
        if self.heap_list == [] :
            return 0
        else :
            self.heap_list[0],self.heap_list[len(self.heap_list)-1] = self.heap_list[len(self.heap_list)-1], self.heap_list[0]
            max_value = self.heap_list.pop()
            self.heapify(0)
            return max_value
    def heapify(self,node_index) :
        self.length = len(self.heap_list)
        left = node_index*2+1
        right = node_index*2+2
        if left > self.length-1 and right > self.length -1 :
            return
        elif left <= self.length-1 :
            if self.heap_list[left] > self.heap_list[node_index] :
                self.heap_list[left], self.heap_list[node_index] =  self.heap_list[node_index], self.heap_list[left]
                self.heapify(left) 
        elif right <= self.length-1 :
            if self.heap_list[right] > self.heap_list[node_index] :
                self.heap_list[right], self.heap_list[node_index] =  self.heap_list[node_index], self.heap_list[right]                
                self.heapify(right)

N = int(sys.stdin.readline())
heap = Heap()
answer_list =[]
#N = 100000 1 log2 log3 log 4 
for _ in range(N) :
    num = int(sys.stdin.readline())
    if num == 0 :
        print(heap.heap_delete()) # log2N
    elif num > 0 :
        heap.heap_insert(num) #log2N -> 높이 
    

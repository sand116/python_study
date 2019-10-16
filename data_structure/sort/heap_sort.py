# heap : n/2 => 마지막노드의 부모노드의 index, 즉 2/n부터 1번 노드까지 순서대로 노드를 방문함 : 시간복잡도 o(n)
# heapify - o(log2n) o(트리높이)

def heap_sort(heap_list) :
    heap_list = build_max_heap(unsorted).copy()
    print(heap_list)
    for i in range(len(heap_list)-1,0,-1) :     
        heap_list[0], heap_list[i] = heap_list[i], heap_list[0]
        max_heapify(heap_list,0,i)

    return heap_list
        
    
def build_max_heap(heap_list) :
    n = len(heap_list)
    for i in range(n//2 , -1, -1):
        max_heapify(heap_list, i, len(heap_list))
    return heap_list
def max_heapify(heap_list, index, heap_size) :
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    
    if  left_index < heap_size and heap_list[index] < heap_list[left_index] :
        heap_list[index], heap_list[left_index] = heap_list[left_index], heap_list[index]               
        max_heapify(heap_list,left_index,heap_size)
        
    if right_index < heap_size and heap_list[index] < heap_list[right_index] :
        heap_list[index], heap_list[right_index] = heap_list[right_index], heap_list[index]
        max_heapify(heap_list,right_index,heap_size)      
    else :
        return 
        
    
    
    
unsorted = [ int(i) for i in input().split()]
i = 0
print( heap_sort(unsorted))
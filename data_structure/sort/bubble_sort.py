def bubble_sort (num_list) :
    for i in range(len(num_list)) :
        for j in range((len(num_list)-1)-i) :
            if num_list[j+1] < num_list[j] : 
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list 
                           
         
    
heap_list = [ int(_) for _ in input().split()]
print(bubble_sort(num_list))



# 바로 옆에 있는 것과 비교 - 큰 것을 맨 뒤로 보내주고 맨 뒤의 연산을 할 필요가 없음
# 시간복잡도 o(n*n) 매번 교체해주기 연산을 해주기 때문에 선택정렬보다 시간복잡도 높다고 할 수 있음
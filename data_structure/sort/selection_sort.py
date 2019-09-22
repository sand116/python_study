# 가장 작은 것을 앞으로 보낸다.
def selection_sort (num_list) :
    for i in range(len(num_list)-1) :
        min = 9999
        for j in range(i,len(num_list)) :
            if min > num_list[j] :
                min = num_list[j]
                index = j   
        num_list[i], num_list[index] = num_list[index], num_list[i]
    return num_list 
                           
            
    

num_list = [ int(_) for _ in input().split()]
print(selection_sort(num_list))

# n(n+1)/2 => o(n*n) 정렬해야할 것이 10000개라면 10000번 해야함
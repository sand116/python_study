def insert_sort (num_list) :
    for i in range(1,len(num_list)) :
        while(i) :
            if num_list[i-1] >= num_list[i] : 
                num_list[i-1], num_list[i] = num_list[i], num_list[i-1]
            else :
                break
            i = i-1
    return num_list 
                           
         
    

num_list = [ int(_) for _ in input().split()]
print(insert_sort(num_list))

# 시간 복잡도
'''
o(n^2)
'''
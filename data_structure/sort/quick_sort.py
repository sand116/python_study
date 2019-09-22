# 분할 정복 알고리즘
# quick sort 재귀로 구현하기 
def quick_sort (num_list,left,right) :
    if left >= right : # 원소가 1개인 경우
        return 
    else :
        pivot = num_list[left]
        i = left +1
        j = right
    #뒤에서부터 pivot 보다 작은 값을 탐색 , 앞에서부터 pivot 보다 큰 값을 탐색, 있으면 swap
    # right -i >0 이라는 것은 작은 값은 인덱스가 큰 값의 인덱스보다 작은 경우 엇갈렸음을 의미함 
        while j >= i  :  
            if num_list[j] < pivot and num_list[i] > pivot :
                # left 값이 pivot 보다 큰 값이 있고 right가 pviot보다 작은 값이 있을 때 이 값들을 swap하고 탐색을 계속 한다 
                num_list[j], num_list[i] = num_list[i], num_list[j]
                i = i + 1
                j = j - 1
            elif num_list[j] < pivot and num_list[i] < pivot :
                i = i + 1
            else :
                j = j -1 
        print("j :",j,"i: ",i,"list[j] : %d"%num_list[j])
        # left 값이 pivot보다 큰 값이 계속 없는 경우 j값은 작은 경우가 있을 때 -> pivot 전환
        num_list[0],num_list[j] = num_list[j], num_list[0] # 피벗 전환  
        quick_sort (num_list,left,j-1) #왼쪽 
        quick_sort (num_list,j,right) #오른쪽 
        return 


    

num_list = [ int(_) for _ in input().split()]
quick_sort(num_list,0,len(num_list)-1)
print(num_list) # 1 3 2 4
# 분할 정복 알고리즘
# quick sort 재귀로 구현하기 
#뒤에서부터 pivot 보다 작은 값을 탐색 , 앞에서부터 pivot 보다 큰 값을 탐색, 있으면 swap
# right -i >0 이라는 것은 작은 값은 인덱스가 큰 값의 인덱스보다 작은 경우 엇갈렸음을 의미함
# left 값이 pivot 보다 큰 값이 있고 right가 pviot보다 작은 값이 있을 때 이 값들을 swap하고 탐색을 계속 한다 


def quick_sort(myList):
    if myList == []:
        return []
    else:
        pivot = myList[0]
        lesser = quick_sort([x for x in myList[1:] if x < pivot])
        greater = quick_sort([x for x in myList[1:] if x >= pivot])
        myList = lesser + [pivot] + greater
        return myList


num_list = [ int(_) for _ in input().split()]
print (quick_sort(num_list))   
# 시간복잡도 = o(logN *N)  - 재귀를 이용한 stack의 깊이가 log N  증명  N(데이터개수)/2^k = 1이 되는 k를 찾아야함 이때 k는 log N
# 최악의 경우 o(N*N)

    
# def quick_sort (num_list,left,right) :
#     if left >= right :
#         return 
#     pivot = num_list[left]
#     i = left 
#     j = right

#     while i <= j  :  
#         while pivot <= num_list[j] and j > left :
#             j = j - 1            
#         while num_list[i] <= pivot and i < right :
#             i = i + 1
#         if i>j : 
#             num_list[left],num_list[j] = num_list[j], num_list[left]
#         else :
#             num_list[i],num_list[j] = num_list[j], num_list[i]
#     quick_sort (num_list,left,j-1) 
#     quick_sort (num_list,j,right) 


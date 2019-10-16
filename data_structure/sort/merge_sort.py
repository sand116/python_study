'''
merge sort 
- divide conquer 분할 정복법을 사용하는 정렬 알고리즘

분할 : 해결하고자 하는 문제를 작은 크기의 '동일한' 문제들로 분할
정복 : 각각의 작은 문제를 순환적으로 해결
합병 : 작은 문제의 해를 합하여( merge ) 원래 문제에 대한 해를 구함

순환식 T(n) = 2T(n/2) +n  => o(nlog2n)
'''    
def merge(left,right) :
    result = []
    i, j = 0, 0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    if i == len(left)  :
        result = result + right[j:]
    elif j == len(right)  :
        result = result + left[i:]
    return result

def merge_sort(list) :
    if len(list) <=1 :
        return list
    mid = len(list)//2
    left_list = merge_sort(list[:mid]) 
    right_list = merge_sort(list[mid:])
    return merge(left_list,right_list)

    
    
string = input().split()
print(merge_sort(string))
# 정렬된 스트링을 리턴하고싶음 
'''
분할 정복 알고리즘
분할 : 배열이 일정 조건이 만족되도록 두 부분으로 나눈다
정복 : 각 부분을 순환적으로 정렬한다.
합병 : NOTHING TO DO 
quick sort 재귀로 구현하기
''' 

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

'''
 퀵소트 알고리즘 
 - 최악의 경우 o(n^2), 평균 시간 복잡도는 o(nlong2n)
 - 최악의 경우가 o(nlog2n)의 시간 복잡도를 가지는 정렬 알고리즘
    -> 합병정렬
    -> 힙 정렬
 - 데이터가 배열이 아닌 연결리스트에 저장되어 있다면? 
    -> 이를 정렬하는 것도  o(n^2)이 최선 - insert sort 
 
 - 최악의 경우 시간 복잡도 계산 : 이미 데이터가 정렬되어있는 경우
 T(n) =T(0) + T(n-1) + o(n) (n - 1 번의 비교연산을 의미)
      =T(n-1) + o(n)
      =T(0) + T(n-2) + o(n-1) + o(n)
      =o(1) + .. + o (n)
      = 1+ ... + n-1
      = o(n^2)
- 최상의 경우 : 항상 절반으로 분할되는 경우
 T(n) = 2T(n/2) + o(n) = o (nlog2n)
 - 항상 적어도 1/9 이상이 되도록 분할된다면 ?
  depth = (9/10)^k * n  
o(log10/9n*n)
 - 평균 시간 복잡도 A(n) = O(nlog2n)
 '''
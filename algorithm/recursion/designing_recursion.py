'''
base case 존재 -> 순환되지 않고 종료되는 case가 있어야 함
모든 case는 결국 base case로 수렴해야 한다.
'''

'''
 1. 암시적 매개변수를 명시적 매개변수로 바뀌어라
 
 recursion에서 프로그래밍을 할때는, 시작점이 0이다와 같은 가설로 설정한
 암시적 변수보다, 매개변수로 시작점을 정확하게 전달하는 등
 명시적으로 변수를 설정해주는 것이 좋다. 
'''
# 예제 1 순차 탐색
def search ( data, begin, end, target) :
    if begin > end :
        return -1
    elif target == data[begin] :
        return begin
    else :
        return search(data, begin + 1, end, target)
# begin - 시작점을 명시적으로 설정해놓음 -> 데이터 구간을 정확하게 표현하기 위해서

# 예제 2 최댓값 찾기 
import math

def find_max (data, begin, end) :
    if begin == end :
        return data[begin]
    else :
        return math.max(data[begin], find_max(data, begin+1, end))
    


# 예제 3 이진 검색 - binary search
# 데이터가 크기 순으로 정렬된 경우를 가정함


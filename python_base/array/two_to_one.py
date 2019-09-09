

#2차원 리스트를 1차원 리스트로 만들기
# 1. sum 함수 
print( sum([1,2,3]) ) 

print( sum([[1,2],[2,3],[3,4]],[]) ) # concatenate list

# 2. list comprehension 이용
[element for array in my_list for element in array]

# 3. reduce 이용
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))


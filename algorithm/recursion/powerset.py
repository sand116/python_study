# 멱집합으로 파이썬 코드 공부하기


# 비트 연산자 이용




# 재귀 이용 
def recursion(list1,list2, result):
    if len(list2) <= 1:q 
    result.append(list1)
    for i,x in enumerate(list2) :
        recursion(list1 + [x], list2[i+1:], result )
        
def combination(list) :
    result = []
    recursion([],list,result)
    return result[1:]
    




# generator 이용
# def powerset(nums) :
#     if len(nums) == 1 :
#         yield []
#     else : 
#         for item in powerset(nums[1:]) :
#             yield [nums[0]] + item  
#             yield item 

if __name__ == "__main__":
    nums = [int(i) for i in input().split()]
    print(combination(nums))
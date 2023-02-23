# map (함수, iterable args) ->함수를 적용해줌
# 시퀀스형 객체는 모두 가능

# ex 1
def map_practice(tupleNumber) :
    return tupleNumber**2

print(list(map(map_practice,(1,3,5))))
print(list(map(lambda x : x**2,(1,3,5))))


# ex 2

def also_square(nums) :
    def double(x) :
        return x ** 2
    
    return map(double, nums)
    
print(list(also_square((1,3,5))))



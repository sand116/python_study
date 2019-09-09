# map (함수, iterable args) ->함수를 적용해줌

def map_practice(tupleNumber) :
    return tupleNumber*2

print(list(map(map_practice,(1,3,5))))
print(list(map(lambda x : x*2,(1,3,5))))

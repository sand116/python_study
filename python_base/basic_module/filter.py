def positive(numberList) :
    return numberList > 0

# filter(함수, iterable args) - 리턴 값이 참인 것만 묶어서 돌려줌
print(list(filter(positive,[3,2,1])))

# 람다 사용 lambda 인자 : return값 - 리스트 내에서도 사용 가능
print(list(filter(lambda x: x>0,[1,-3,2,0])))


def also_positive(num_list) :
    def positive(num) :
        return num>0
    return filter(positive, num_list)

print(list(also_positive([-1,2,3,4])))
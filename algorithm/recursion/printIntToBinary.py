def intToBinary(num_list,n) :
    if n<2 :
        num_list.append(n)
        return 0
    intToBinary(num_list,n//2)
    num_list.append(n%2)


n = int(input())
num_list = []
intToBinary(num_list,n)
print(num_list)
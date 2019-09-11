def length(str_list) :
    if str_list == [] :
        return 0
    else :
        del str_list[0]
    return 1 + length(str_list)

str_list = [1,2,3]
print(length(str_list))
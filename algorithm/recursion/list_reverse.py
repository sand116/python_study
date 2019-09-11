
def reverse(reverse_list, str_list) :
    if len(str_list) == 1 :
        reverse_list.append(str_list[0])
        return 0
    else :
        reverse(reverse_list,str_list[1:])
        reverse_list.append(str_list[0])

       

str_list = [1,2,3,4,5]
reverse_list = []
reverse(reverse_list,str_list)
print(reverse_list)

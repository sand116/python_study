
def permutation(num_list,selection_list,result):
    copy_list=num_list.copy()
    if len(num_list) == 1 :
        selection_list.append(num_list[0])
        result.append(selection_list)
    else :
        for i,j in enumerate(num_list) : #반복할 때는 변형하지 않기
            copy_list[0], copy_list[i] = copy_list[i], copy_list[0] # 바꿀때는 바꾸기
            permutation(copy_list[1:], selection_list+[j], result)
        
    
num_list = [1,2,3,4,5,6]
selection_list = []
result = []
permutation(num_list,selection_list,result)
print(result)
print(len(result))
        
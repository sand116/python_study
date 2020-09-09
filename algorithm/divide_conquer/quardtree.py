def reverse_tree () :
    if compress_list[length] != 'x' :
        length += 1
        return [compress_list[length-1]]
    length +=1
    later1, later2, pre1, pre2 = [], [], [], []
    later1 += reverse_tree()
    later2 += reverse_tree()
    pre1 += reverse_tree()
    pre2 += reverse_tree()
    
    ret = ["x"] + pre1+ pre2 + later1 + later2
    return ret 
        
    
compress_list = list(input())
length = 0
print(reverse_tree())
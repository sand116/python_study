chars='%^&*()#@!!$%^'
code_list1=[]

for s in chars :
    code_list1.append(ord(s))
    
print(code_list1)


#comprehending Lists

code_list2 = [ord(s) for s in chars]
print(code_list2)


# Comprehending List + Map, Filter

code_list3 = [ord(s) for s in chars if ord(s)>40]
code_list4 = list(filter(lambda x : x>40, map(ord,chars)))


print(code_list3)
print(code_list4)

print([chr(s) for s  in code_list1])
print([chr(s) for s  in code_list2])
print([chr(s) for s  in code_list3])
print([chr(s) for s  in code_list4])

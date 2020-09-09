def stack(str_line) :
    check = []
    for i in str_line :
        if i == "(" or i == "[" :
            check.append(i)
            continue   
        if i == ")" :
            if check == [] :
                return "no"
            j = check.pop()
            if j != "(" :
                return "no"
        elif i == "]" :
            if check == [] :
                return "no"
            j = check.pop()
            if j != "[" :
                return "no"
    if check == [] :
        return "yes"
    else :
        return "no"
    
            
while(True) :
    str_line = input()
    if str_line == '.' :
        break
    print(stack(str_line))
    
    
        
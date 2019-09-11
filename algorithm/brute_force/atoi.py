string = "1234"
sum = 0;
string_list = [ int(i) for i in string]
for idx,num in enumerate(string_list) :
    sum += num*(10**(len(string_list)-(idx+1)))
print(sum)
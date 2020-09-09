def recur(a, b) :
    if b == 0 :
        return 1
    if b == 1 :
        return a
    if b%2 == 1 :
        return recur(a, b-1)*a
    num = recur(a, b//2)
    return (num*num)%c
a, b, c = map(int, input().split()) 

print (recur(a,b)%c)
'''
a, b, c = map(int, input().split())
print(pow(a, b, c))
'''
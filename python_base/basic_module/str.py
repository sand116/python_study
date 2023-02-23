# 전체 문자열 길이 ^ 중간정렬 / < 왼쪽정렬 >오른쪽 정렬

s = 12345
n = 30 
print("{0:^{1}}".format(s, n))

#f-string 이용
print(f'{s:<{n}}')




#문자열 '리스트' 요소들 -> 문자열로 합치고싶을때
# ''.join(list)

k = [5,4]
def ch(a) :
    a.append(3)
    res = id(a)
    return res


print(ch(k), id(k))

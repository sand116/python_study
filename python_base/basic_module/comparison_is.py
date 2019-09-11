# Python의 비교문에는 '=='(equal), '!='(not equal) 외에도 'not'과 'is' 가 있음
# ==, !=는 값 자체를 비교하고, is, is not은 객체(object)를 비교

a=6
print(id(a)) #객체의 reference 출력 
print(id(6))
print(a is 6)

a=7
print(id(a))
print(a is 7)


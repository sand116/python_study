
# Generator Ex3 (중요함수)

# filterfalse, accumulate, chain, product, groupby...

import itertools

gen1 = itertools.count(1,2.5)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
# ... 무한

# # 조건

# gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1,2.5))

# for v in gen2 :
#     print(v)
#     pass

# gen3 = itertools.filterfalse(lambda n : n < 3, [1,2,3,4,5])

# for v in gen3:
#     print(v)
    
# 누적합계
gen4 = itertools.accumulate([x for x in range(1,101)])
print(list(gen4))

# 연결1

gen5 = itertools.chain('ABCDE', range(1,11,2))
print(list(gen5))

# 연결2

gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6))

# 개별

gen7 = itertools.product('ABCDE')
print(list(gen7))

# 연산(경우의 수)
gen8 = itertools.product('ABCDE', repeat=2)
print(list(gen8))

gen9 = itertools.product('ABCDE', repeat=3)
print(list(gen9))

# 그룹화
gen9 = itertools.groupby('AAABBCCCDDEEE')
#print(list(gen9))

for chr, group in gen9:
    print(chr,' : ', list(group))

# 조합

gen10 = itertools.combinations('ABCDEFG', 3)
print(list(gen10))

gen11 = itertools.combinations_with_replacement('ABCDEFG', 3)
print(list(gen11))
from functools import *
import operator

listOfElems = ['1','3',['2','3','1'],'4']

# 1. count1
def count1(x, L) : 
    return reduce(lambda sum, elem : sum + (1 if elem == x else 0),L,0)

# 2. count2
def count2(x,L):
    return reduce(lambda sum, elem: sum + (count2(x,elem) if isinstance(elem, list) else ( 1 if elem == x else 0) ), L, 0)



print(count1('1', listOfElems))
print(count2('1', listOfElems))


# 3. reverse


lists = [ 1 ,2 ,3 , [5,[6,7]], 8, [9, 0, 1 ,4 ]]


def reverse(L) :
    return reduce(lambda x, y:  [y]+x ,L, [])


# 4. twist

def twist(L) :

   return reduce(lambda x, y:  ([twist(y)] if isinstance(y, list) else [y])+x ,L, [])

a = [1,2,3,4,5]

print(reverse(listOfElems))
print(twist(lists))


# 5. sort 
def insert(L, x):
    for i, value in enumerate(L):
        if value > x:
            return L[:i] + [x] + L[i:]
    return L + [x]

def insertion_sort(L) :
   return reduce( lambda sorted, x : insert(sorted,x), L, [] )

print(insertion_sort([3,2,4,3]))



# permutations 


def permutations(L):
    if len(L) == 1:
        return [[L[0]]]
    else:
        return reduce(lambda result, p: result +  [ p[:i] + [L[0]] + p[i:] for i in range(0, len(p) + 1)], permutations( L[1:]), [])
    

print(permutations(['a','b','c']))


# powerset

def powerset(L):
    return reduce(lambda result, x: result + [subset + [x] for subset in result],
                  L, [[]])
    
print(powerset(['a','b','c']))

def perm(n, i):
    if i == len(n) - 1:
        print(f' i = {i}' )
        print(n)
    else:
        for j in range(i, len(n)):
            print(f' i = {i} ,j = {j}' )
            n[i], n[j] = n[j], n[i] # 단순 복사여서 값이 바뀔 것임,, - i,j swap 
            print('재귀전--------------------------')
            perm(n, i + 1)
            print('재귀후--------------------------')
            print(f' i = {i} ,j = {j}' )
            
            n[i], n[j] = n[j], n[i]  # swap back, for the next loop
            print('for문 끝--------------------------')



if __name__ == "__main__":
    perm([1, 2, 3], 0)
        
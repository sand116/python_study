# 함수 인자에 리스트(튜플) 앞에 *를 붙이면 언패킹(unpacking)이 됨

# 가변인수 만들 때 사용
def print_numbers(*args):
    print(args)
    for arg in args:
        print(arg)
        
print_numbers(3,[1,2,4,5],'k')
        
'''
첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 
둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 
1,000,000보다 작거나 같은 정수이다.
'''
class MyError(Exception):
    def __init__(self, msg='init_error_msg'):
        self.msg = msg
    def __str__(self):
        return self.msg


class Input :
    cnt = 0
    def input_cnt(self) :    
        self.cnt=int(input())
        if self.cnt>1000000 or self.cnt<1 : 
            raise MyError("올바른 범위가 아닙니다")
        return self.cnt 

    def input_list(self) :
        output=input().split()
        output_list = list(map(lambda x : int(x), output))
        for i in output_list :
            if i < -1000000 or i > 10000000 :
                raise MyError("올바른 범위가 아닙니다")
        if len(output) != self.cnt :
            raise MyError("개수가 틀렸습니다")
        return output_list
    
input_object = Input()        
cnt = input_object.input_cnt()
output = input_object.input_list()
print(f'{max(output)} {min(output)}')




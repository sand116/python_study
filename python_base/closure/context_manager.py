'''
Context Manager
__enter__, __exit__, exception

원하는 타이밍에 정확하게 리소스를 할당 및 제공, 반환하는 역할
with 문에 사용 가능
'''

# ex1

file = open('./testfile1.txt', 'w')
try:
    file.write('context manager test1\n contextlib test1')
finally:
    file.close()
    
    
# ex2

with open('./testfile2.txt', 'w') as f:
    f.write('context manager test2\n contextlib test2')
    

    
# ex3 class 형태로 구현

class MyFileWriter():
    def __init__(self, file_name, method):
        print('MyFileWriter started : __init__')
        self.file_obj = open(file_name, method)
        
    def __enter__(self):
        print('MyFileWriter started : __enter__')
        return self.file_obj
    
    def __exit__(self, exc_type, value, trace_back) :
        print('MyFileWriter started : __exit__')
        if exc_type :
            print(f'Logging exception {(exc_type, value, trace_back)}')
        self.file_obj.close()

with MyFileWriter('./testfile3.txt', 'w') as f :
    # as f 에서 __enter__ 실행
    f.write('context manager test3\n contextlib test3')
    # with 문이 끝나면 __exit__ 실행





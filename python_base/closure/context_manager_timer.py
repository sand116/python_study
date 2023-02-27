'''
Measure execution(타이머) 제작
'''

import time

class ExecuteTimer(object):
    def __init__(self, msg):
        self._msg = msg
    
    def __enter__(self):
        self._start = time.monotonic()
        return self._start
     
    def __exit__(self, exc_type, value, trace_back) :
        print('MyFileWriter started : __exit__')
        # 에러 발생 시 
        if exc_type :
            print(f'Logging exception {(exc_type, value, trace_back)}')
        else :
            print(f'{self._msg} : {time.monotonic() - self._start}')

        return True
    
with ExecuteTimer('start job!') as v:
    #__enter__에서 return한 값
    print(f'Recieved start monotonic : {v}')
    # 실행할 코드
    for i in range(10000000) :
        pass
    raise Exception('Raise exception!') # 강제로 예외 발생


# decorator 사용

from contextlib import contextmanager

@contextmanager
def executeTimerDc(msg) :
    start = time.monotonic()
    # 예외처리
    try: #__enter__
        yield start
    except BaseException as e:
        print(f'Logging exception: {msg} : {e}')
        raise
    else: #__exit__
        print(f'{time.monotonic() - start}')

with executeTimerDc('start job!') as v:
    #__enter__에서 return한 값
    print(f'Recieved start monotonic2 : {v}')
    # 실행할 코드
    for i in range(10000000) :
        pass
    raise ValueError('decorator error') # 강제로 예외 발생

  
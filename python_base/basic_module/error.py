    


# if - else : 코드 실행 전 예외 상황을 미리 검사, 오류 발생 확률 높을 때 (50%?)
# try 문 : 예외상황을 미리 검사하지 않음, 오류 발생 확률 적을 때 


a = ['1' ,'2', 'a', '3']


try:
    '''
    예외가 발생할 수 있는 코드 블록
    '''
    for i in a:
        print(int(i))
except: #예외종류 지정
    '''
    예외 발생 시 해당 예외 종류에 해당하는 경우 실행할 코드 블록 
    '''
    print("error")
    # error 가 발생하는 경우, error를 raise하지 않으면 빠져나와 아래 코드 실행됨
else : #try의 본문을 다 실행할때까지 예외가 발생되지 않은 경우 에 실행
    pass
finally : # try이든 except이든 어떤 상황에서라도 실행되어야하는 코드
    print("surely show up")    
    
print("pass")    

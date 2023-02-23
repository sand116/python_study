# Chapter06-05
# Futures 동시성
# 비동기 작업 실행
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> (File)Network I/O 관련 작업 -> 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상

# futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.Futures
# 1. 멀티스레딩/멀티프로세싱 API 통일 -> 매우 사용하기 쉬움
# 2. 실행중이 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념

# 2가지 패턴 실습
# concurrent.futures map
# concurrent.futures wait, as_completed

# GIL : 두 개 이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스 하는 경우 -> 문제점을 방지하기 위해
#       GIL 실행 , 리소스 전체에 락이 걸린다. -> Context Switch(문맥 교환)

# GIL : 멀티프로세싱 사용, CPython

import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed

# 다양한 예외 사항이 있을 것 - 몇개의 job은 실패하거나 혹은 작업마다 소요시간이 다 다른 등, 따라서 각 작업의 결과를 각각 받아올 수 있어야함
WORK_LIST = [10000, 100000, 1000000, 10000000]


# 동시성 합계 계산 메인 함수
# 누적 합계 함수(제레네이터)
def sum_generator(n):
    return sum(n for n in range(1, n+1))

# wait
# as_completed
def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))
    
    # 시작 시간
    start_tm = time.time()
    # Futures (스케줄링 리스트)
    futures_list = []

    # 결과 건수
    # ProcessPoolExecutor
    with ThreadPoolExecutor() as excutor:
        for work in WORK_LIST:
            # future 반환( 미래의 할 일 반환)
            future = excutor.submit(sum_generator, work)
            # 스케쥴링
            futures_list.append(future)
            # 스케쥴링 확인
            print('Scheduled for {} : {}'.format(work, future))
            # print()
        
        # wait 결과 출력 (timeout될 때까지 성공한 작업)
        # result = wait(futures_list, timeout=7)
        # # 성공된 작업들
        # print('Completed Tasks : ' + str(result.done))
        # # 실패한 작업들
        # print('Pending ones after waiting for 7seconds : ' + str(result.not_done))
  
        # # 결과 값 출력
        # print([future.result() for future in result.done])
        
        # as_completed 결과 출력, 끝나는 것 부터 출력
        for future in as_completed(futures_list, timeout=7):
            # 가장 적게 걸리는 작업부터 수행
            result = future.result()
            # 수행 완료 된 작업들
            done = future.done()
            # 타임아웃을 벗어나 수행되지 않은 작업들 
            cancelled = future.cancelled
            
            # future 결과 확인
            print('Future Result : {}, Done : {}'.format(result, done))
            print('Future Cancelled : {}'.format(cancelled))
        
        
            
    # 종료 시간
    end_tm = time.time() - start_tm
    # 출력 포멧
    msg = '\n Time : {:.2f}s'
    # 최종 결과 출력
    print(msg.format(end_tm))



# 실행
if __name__ == '__main__':
    main()







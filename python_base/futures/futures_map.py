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
from concurrent import futures

WORK_LIST = [100000, 1000000, 10000000, 100000000]

def sum_generator(n) :
    return sum(n for n in range(1,n+1))

def main() :    
    # Worker count
    worker = min(10, len(WORK_LIST))
    
    # 시작 시간
    start_tm = time.time()

    # 결과 건수
    # 멀티 쓰레드 혹은 멀티 프로세스로 수행
    # ProccessPoolExecutor
    with futures.ThreadPoolExecutor() as executor:
        result = executor.map(sum_generator, WORK_LIST)
    # 반환되는 객체는 제네레이터 객체
    
    # 종료 시간
    end_tm = time.time() - start_tm

    msg = f'\n Result -> {list(result)} Time : {end_tm:.2f}s'
    print(msg)
# 실행
if __name__ =='__main__' :
    main()

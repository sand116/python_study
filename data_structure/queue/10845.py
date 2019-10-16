from queue import  Queue
import sys


N = int(sys.stdin.readline())
queue = Queue(N)
for _ in range(N) :
    order = sys.stdin.readline().split()
    if order[0] == "push" :
        queue.put_nowait(order[1])
    elif order[0] == "pop" :
        try :
            pop_item = queue.get_nowait()
            print(pop_item)
        except :
            print(-1)
    elif order[0] == "size" :
        print(queue._qsize())
    elif order[0] == "empty" :
        if queue.empty() :
            print(1)
        else : print(0) 
    elif order[0] == "front" :
        try :
            print(queue.queue[0])
        except :
            print(-1)
        
    elif order[0] == "back" :
        try :
            print(queue.queue[-1])
        except :
            print(-1)
    else :
        pass
    
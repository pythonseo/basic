import time
import sys

def timecount(fu):
    def counttime():
        fu()
        t=time.process_time()
        print(t)
    return counttime

@timecount

def test():
    print('hello')
    time.sleep(1)
    
test()

def fibnq(n):
    a,b,count=0,1,0
    while count <n:
        yield a
        a,b=b,a+b
        count +=1
f=fibnq(10)

while True:
    try:
        print(next(f),end="")
    except StopIteration:
        sys.exit()
        

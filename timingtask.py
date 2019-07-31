import time
from threading import Timer

def task():
    print('now is {}'.format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))#以打印当前时间作为目标任务

while True:
    x = time.strftime('%S', time.localtime())#获取当前时间秒数作为参考标准
    print(x)
    if x=='00' or x=='30':#如果满足条件则执行目标任务，并延迟目标时间执行
        task()
        time.sleep(30)
    else:#如果不满足条件则不执行目标任务，并按秒延迟使程序具备达成目标条件的能力
        time.sleep(1)



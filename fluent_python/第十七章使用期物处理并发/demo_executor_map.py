from time import sleep,strftime
from concurrent import futures

def display(*args):
    print(strftime('[%H:%M%S]'),end=' ')
    print(*args)

def loiter(n):
    msg= '{}loiter{}:doing nothing for {}s'
    display(msg.format('\t'*n,n,n))
    sleep(n)
    msg = '{}loiter{}:done'
    display(msg.format('\t'*n,n))
    return n*10


def main():
    display('script starting')
    exectutor = futures.ThreadPoolExecutor(max_workers=3)
    results = exectutor.map(loiter,range(5)) # 把5个任务提交给exector（因为只有三个线程，所以只有三个任务会立即开始：loiter(0),loiter(1),loiter(2)）
    #这是非阻塞调用
    display('results:',results) # result 是一个生成器
    display('waiting for individual result')
    for i, result in enumerate(results):
        display('result{}:{}'.format(i,result))

if __name__ == "__main__":
    main()
"""
[10:3057] script starting
[10:3057] loiter0:doing nothing for 0s
[10:3057] loiter0:done
[10:3057] 	loiter1:doing nothing for 1s
[10:3057] 		loiter2:doing nothing for 2s
[10:3057] results: <generator object Executor.map.<locals>.result_iterator at 0x000001F872757CA8>
[10:3057] waiting for individual result
[10:3057] result0:0
[10:3057] 			loiter3:doing nothing for 3s
[10:3058] 	loiter1:done
[10:3058] 				loiter4:doing nothing for 4s
[10:3058] result1:10
[10:3059] 		loiter2:done
[10:3059] result2:20
[10:3100] 			loiter3:done
[10:3100] result3:30
[10:3102] 				loiter4:done
[10:3102] result4:40
"""


"""
executor.submit 和futures.as_completedb
比exectuor.map更灵活,因为submit方法能处理不同的可调用对象和参数，而exeutor.map只能处理参数不同的同一个调用
对象，此外。传给futures.as_completed函数的期物集合可以来之多个executor实例，
"""
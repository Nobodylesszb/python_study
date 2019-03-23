"""
fork函数被调用后会返回两次，pid为0的代表子进程，其他返回子进程的id号表示父进程。
getpid和getppid函数可以获取本进程和父进程的id号
"""

import os
pid = os.fork() # 创建一个子进程
if pid == 0:
    print('这是子进程')
    print(os.getpid(),os.getppid())
else:
    print('这是父进程')
    print(os.getpid())
os.wait() # 等待子进程结束释放资源
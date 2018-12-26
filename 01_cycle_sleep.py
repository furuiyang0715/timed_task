"""
定时任务的第一种实现：
在死循环中 使用线程睡眠函数 sleep()
"""
import datetime
import time


def timeTask():
    """
    每隔10s打印当前时间
    :return:
    """
    while True:
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(10)


if __name__ == "__main__":
    timeTask()

"""
如果定时任务timedTask()之后还有其他操作 我们使用死循环+阻塞线程
会使timedTask()一直占用CPU资源，导致后续操作无法执行 
"""


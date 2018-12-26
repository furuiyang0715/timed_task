"""
非阻塞式 启动一个新线程来执行定时任务
"""
import datetime
import time

from threading import Timer


def task():
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def timedTask(task):
    """
    每隔 10 s打印当前时间
    :return:
    """
    Timer(10, task, ()).start()


if __name__ == "__main__":
    timedTask(task)
    # 非阻塞式 可以执行其他任务
    while True:
        print(time.time())
        time.sleep(5)


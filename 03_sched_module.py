"""
第三种方式是调用标准库中的sched模块
sched是事件调度器，它通过scheduler类来调度事件
从而达到执行定时任务的效果
"""
import datetime
import sched
import time


def timedTask(task):
    """
    每隔 10 s打印当前时间
    :return:
    """
    # 初始化 sched 模块的 scheduler 类
    schedule = sched.scheduler(time.time, time.sleep)
    # 增加调度任务
    schedule.enter(1, 1, task)
    # 运行任务
    schedule.run()


def task():
    print("我是一个定时任务......", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    timedTask(task)

"""

1）首先构造一个sched.scheduler类
它接受两个参数：timefunc 和 delayfunc。timefunc 应该返回一个数字，代表当前时间，delayfunc 函数接受一个参数，用于暂停运行的时间单元。
一般使用默认参数就行，即传入这两个参数 time.time 和 time.sleep.当然，你也可以自己实现时间暂停的函数。
2）添加调度任务
scheduler 提供了两个添加调度任务的函数:

enter(delay, priority, action, argument=(), kwargs={})

该函数可以延迟一定时间执行任务。delay 表示延迟多长时间执行任务，单位是秒。priority为优先级，越小优先级越大。两个任务指定相同的延迟时间，优先级大的任务会向被执行。action 即需要执行的函数，argument 和 kwargs 分别是函数的位置和关键字参数。

scheduler.enterabs(time, priority, action, argument=(), kwargs={})

添加一项任务，但这个任务会在 time 这时刻执行。因此，time 是绝对时间.其他参数用法与 enter() 中的参数用法是一致。
3）把任务运行起来
调用 scheduler.run()函数

scheduler 中的每个调度任务只会工作一次，不会无限循环被调用。如果想重复执行同一任务， 需要重复添加调度任务即可。

"""


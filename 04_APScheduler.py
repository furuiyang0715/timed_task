import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler

"""
APScheduler 是一个可以循环执行定时任务的库
"""

"""
APScheduler的全称是Advanced Python Scheduler。它是一个轻量级的 Python 定时任务调度框架。
APScheduler 支持三种调度任务：固定时间间隔，固定时间点（日期），Linux 下的 Crontab 命令。
同时，它还支持异步执行、后台执行调度任务。

"""

# 使用步骤
# 1 新建一个schedulers（调度器）
# 2 添加一个调度任务（job stores)
# 3 运行调度任务


def timedTask():
    print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])


if __name__ == "__main__":
    # 创建后台执行的schedulers
    scheduler = BackgroundScheduler()
    # 添加调度任务
    # 调度方法为 timedTask 触发器选择 interval（间隔性） 间隔时间长为2s
    scheduler.add_job(timedTask, "interval", seconds=2)
    # 启动调度任务
    scheduler.start()

    while True:
        print(time.time())
        time.sleep(5)


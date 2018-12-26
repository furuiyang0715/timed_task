"""
通过scheduler.get_jobs()能够获取当前调度器中的所有job的列表
"""
import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler


def job_func(text):
    print(text)


scheduler = BackgroundScheduler()
scheduler.add_job(job_func, "interval", seconds=2, args=["hahaha"])
scheduler.add_job(job_func, "interval", seconds=1, args=["xixixi"])
scheduler.start()
print("---------", scheduler.get_jobs())

while True:
    time.sleep(10)
    # 关闭 job
    # 默认情况下调度器会等待所有正在运行的作业完成之后关闭所有的调度器和作业存储
    # 如果不想等待 可以把 wait 选项设置为 False
    # scheduler.shutdown()
    try:
        scheduler.shutdown(wait=False)
    except Exception as e:
        print(e)


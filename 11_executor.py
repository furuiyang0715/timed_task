ssPoolExecutor 和 ThreadPoolExecutor
"""
from pymongo import MongoClient
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


def my_job():
    print("hello world")


# 基本配置信息
host = "127.0.0.1"
port = 27017
client = MongoClient(host, port)

# 任务存储对象
jobstores = {
    'mongo': MongoDBJobStore(collection='job', database='test', client=client),
    'default': MemoryJobStore()
}

# 执行器对象
executors = {
    'default': ThreadPoolExecutor(10),
    'processpool': ProcessPoolExecutor(3)
}

# job 实例
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
scheduler.add_job(my_job, 'interval', seconds=5)

try:
    scheduler.start()
except SystemExit:
    client.close()

# https://zhuanlan.zhihu.com/p/46948464

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



from datetime import datetime
from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler

"""
date 是最基本的一种调度，作业任务只会执行一次。它表示特定的时间点触发。
"""

def job_func(text):
    print(text)

scheduler = BackgroundScheduler()
scheduler.add_job(job_func, "date", run_date=date(2018, 12, 26), args=["我被执行啦"])
scheduler.add_job(job_func, "date", run_date=datetime(2018, 12, 25, 17, 0, 0), args=["我被执行啦2"])
scheduler.add_job(job_func, "date", run_date='2018-12-25 17:01:00', args=["我被执行啦3"])
while True:
    try:
        scheduler.start()
    except:
        print("already running......")


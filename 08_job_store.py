import datetime
from apscheduler.scheduler.background import BackgroundScheduler


@scheduler.scheduled_job(job_func, "interval", minutes=2)
def job_func(text):
    print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])


scheduler = BackgroundScheduler()
scheduler.start()

"""
第二种添加任务的方式的例子
这两种办法的区别是：第一种方法返回一个 apscheduler.job.Job 的实例，可以用来改变或者移除job
第二种办法只适用于应用运行期间不会改变的 job
"""


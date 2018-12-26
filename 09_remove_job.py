"""
移除job也有两种办法
(1)remove_job()
(2)job.remove()
"""
import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler

def job_func():
    print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])


scheduler = BackgroundScheduler()

# remove_job() 是根据job的id来移除所以要在job创构建的时候指定一个id
# scheduler.add_job(job_func, "interval", minutes=0.01, id="job_one")
# scheduler.start()
# # 5s 后移除该job
# time.sleep(5)
# scheduler.remove_job("job_one")

# job.remove() 则是对job执行remove方法即可
job = scheduler.add_job(job_func, "interval", minutes=0.01, id="job_two")
# print(job)
# print(type(job))
scheduler.start()
# 5s 后移除该job
time.sleep(5)
job.remove()


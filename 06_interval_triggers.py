
m datetime import datetime
from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler


def job_func(text):
    print(text)

scheduler = BackgroundScheduler()
# 每隔两分钟执行一次 job_func 方法
scheduler.add_job(job_func, "interval", minutes=0.05, args=["hhhhh"])
# 在起止时间之间每隔两分钟执行一次 job_func 方法
scheduler.add_job(job_func, "interval", minutes=0.1, start_date="2018-12-25 18:05:00",
                  end_date="2018-12-25 18:20:00", args=["yyyyy"])
while True:
    try:
        scheduler.start()
    except:
        pass


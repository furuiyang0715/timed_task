nux crontab格式兼容。它是功能最强大的触发器。
"""

import datetime
from apscheduler.scheduler.background import BackgroundScheduler


def job_func(text):
    print("当前时间：", datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])


scheduler = BackgroundScheduler()
# 在每年 1-3 7-9 月份的每个星期一、二中的 00:00 02:00 和 03:00 执行 job_func 任务
scheduler.add_job(job_func, "cron", month="1-3,7-9", day="0, tue", hour="0-3")
scheduler.start()


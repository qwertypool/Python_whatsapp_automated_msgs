from datetime import datetime
import chat
from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()

# Schedule job_function to be called every one minute
sched.add_job(chat.msg, 'interval',Hours=24)

sched.start()
Get next executions from crone expression
```python
import croniter
import datetime

now = datetime.datetime.now()
sched = '0 10 * * WED'
cron = croniter.croniter(sched, now)

for i in range(5):
    nextdate = cron.get_next(datetime.datetime)
    print(nextdate)
```
### Connection to Azure EventHub 

Here we are using the time offset.

```python
from datetime import datetime as dt , timedelta

startTime = (dt.now() + timedelta(days=-1)).strftime("%Y-%m-%dT%H:%M:%S.%fZ")

startingEventPosition = {
  "offset": None,
  "seqNo": -1,
  "enqueuedTime": startTime,
  "isInclusive": True
}

ehConf['eventhubs.connectionString'] = sc._jvm.org.apache.spark.eventhubs.EventHubsUtils.encrypt(connectionString)

eventhub = spark\
  .readStream\
  .format("eventhubs")\
  .options(**ehConf)\
  .option("eventhubs.consumerGroup", "$Default")\
  .option("eventhubs.startingPosition",  json.dumps(startingEventPosition))\
  .load()\
  .selectExpr("*","cast(body as string) payload")

```

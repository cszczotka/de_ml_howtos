
By default, the vacuum retains data for up to 7 days. We can set the retention period to zero hours, effectively removing data older than zero hours

```sql
%sql
SET spark.databricks.delta.retentionDurationCheck.enabled = false;
VACUUM DELTA_DEMO.file1 RETAIN 0 HOURS
```
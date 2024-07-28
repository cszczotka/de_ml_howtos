### How to replace some value in data frame column

This is case where is payload column we want to replace some string 'undefined' by 'null'

```python
eventhub = eventhub.withColumn("payload", F.regexp_replace("payload", "undefined", "null")) 
```
### How to replace some value in data frame column

This is case where is payload column we want to replace some string 'undefined' by 'null'

```python
eventhub = eventhub.withColumn("payload", F.regexp_replace("payload", "undefined", "null")) 
```

### How to create single column dataframe

```python

df = spark.createDataFrame([1,2,3,-1], IntegerType()).toDF("col1")
df2 = = spark.createDataFrame(["a","b","c"], StringType()).toDF("col1")
```
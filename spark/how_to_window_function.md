### How to create window spec 

```python
    win_spec  = Window.partitionBy(["col1", "col2", "col3"]).orderBy(sf.desc("col4"))
    df = df.withColumn("row_number", row_number().over(win_spec)).where(sf.col("row_number") == 1).select(*keep)
```
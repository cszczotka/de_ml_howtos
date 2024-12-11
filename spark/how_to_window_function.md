### How to create window spec 

```python
    win_spec  = Window.partitionBy(["col1", "col2", "col3"]).orderBy(sf.desc("col4"))
    df = df.withColumn("row_number", row_number().over(win_spec)).where(sf.col("row_number") == 1).select(*keep)
```


### Windows spec

```python
from pyspark.sql import functions as F
from pyspark.sql import Window

dfw=spark.createDataFrame([("abc",1,100),("abc",2,200),("abc",3,300),("abc",4,200),("abc",5,100)],"name string,id int,price int")
display(dfw)

```

```python
dfw.withColumn("max",F.max("price").over(Window.partitionBy("name").orderBy("id").rowsBetween(Window.unboundedPreceding, Window.currentRow))).show()
```


```python
dfw.withColumn("max",F.max("price").over(Window.partitionBy("name").orderBy("id").rowsBetween(Window.unboundedPreceding,Window.unboundedFollowing))).show()
```

The window it's looking downwards in all values for a max instead of limiting it to the current row

```python
dfw.withColumn("max",F.max("price").over(Window.partitionBy("name").orderBy("id").rowsBetween(Window.currentRow,Window.unboundedFollowing))).show()
```

### row_number vs rank vs dense_rank

```sql
%sql
 SELECT a,
        b,
        row_number() OVER(PARTITION BY a ORDER BY b) as row_number,
        dense_rank() OVER(PARTITION BY a ORDER BY b) dense_rank,
        rank() OVER(PARTITION BY a ORDER BY b) as rank
    FROM VALUES ('A1', 2), ('A1', 1), ('A2', 3), ('A1', 1), ('A1', 1) tab(a, b)

```